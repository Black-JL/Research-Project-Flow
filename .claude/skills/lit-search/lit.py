#!/usr/bin/env python3
"""Literature search straight against OpenAlex, Semantic Scholar, and Crossref.

No third-party servers in between. Standard library only.

Usage:
  lit.py search "question" [--from 2015] [--to 2025] [--n 10] [--source both|oa|s2]
  lit.py paper DOI_OR_OPENALEX_ID
  lit.py similar DOI [DOI ...] [--n 10]
  lit.py verify DOI                      # Crossref record for a DOI
  lit.py verify --title "Paper title"    # find the DOI for a title via Crossref
  lit.py neighbors "research question" [--n 15]   # nearest-neighbour set for a duplication check
  lit.py debate "topic" [--years 5] [--n 40]      # shared reference core of recent papers
  lit.py saturation "topic" [--from 2000]          # papers and reviews per year
Add --json to any command for raw JSON. Add --dois to print just the DOIs (for Zotero import).

Optional keys (raise rate limits; both free) are read from the environment or
~/.config/lit-search/keys.env:
  OPENALEX_API_KEY=...   S2_API_KEY=...   LIT_MAILTO=you@example.org
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter

OA = "https://api.openalex.org"
S2 = "https://api.semanticscholar.org"
CR = "https://api.crossref.org"


def load_keys():
    path = os.path.expanduser("~/.config/lit-search/keys.env")
    if os.path.exists(path):
        for line in open(path):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


load_keys()
OA_KEY = os.environ.get("OPENALEX_API_KEY", "")
S2_KEY = os.environ.get("S2_API_KEY", "")
MAILTO = os.environ.get("LIT_MAILTO", "")


def get(url, headers=None, data=None, tries=4):
    h = {"User-Agent": "lit-search/1.0" + (f" (mailto:{MAILTO})" if MAILTO else "")}
    h.update(headers or {})
    body = None
    if data is not None:
        body = json.dumps(data).encode()
        h["Content-Type"] = "application/json"
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=body, headers=h)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(2 ** i + 1)
                continue
            if e.code == 404:
                return None
            raise SystemExit(f"HTTP {e.code} from {url.split('?')[0]}"
                             + (" (rate limited; a free API key fixes this, see SKILL.md)" if e.code == 429 else ""))
        except urllib.error.URLError as e:
            if i < tries - 1:
                time.sleep(2)
                continue
            raise SystemExit(f"Network error: {e.reason}")


def oa(path, **params):
    if OA_KEY:
        params["api_key"] = OA_KEY
    elif MAILTO:
        params["mailto"] = MAILTO
    return get(f"{OA}{path}?{urllib.parse.urlencode(params)}")


def s2(path, data=None, **params):
    """Semantic Scholar call. Never fatal: on failure, warn and return None so OpenAlex results still come back."""
    hdr = {"x-api-key": S2_KEY} if S2_KEY else {}
    q = f"?{urllib.parse.urlencode(params)}" if params else ""
    try:
        return get(f"{S2}{path}{q}", headers=hdr, data=data)
    except SystemExit as e:
        print(f"[warning] Semantic Scholar unavailable ({e}). Results below are OpenAlex only.", file=sys.stderr)
        return None


# ---------- normalising records ----------

def oa_abstract(inv):
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def clean_doi(d):
    if not d:
        return ""
    d = d.strip()
    for p in ("https://doi.org/", "http://doi.org/", "doi:", "DOI:"):
        if d.startswith(p):
            d = d[len(p):]
    return d.lower()


def from_oa(w):
    src = ((w.get("primary_location") or {}).get("source") or {})
    doi = clean_doi(w.get("doi"))
    return {
        "title": w.get("display_name") or w.get("title") or "",
        "year": w.get("publication_year"),
        "authors": [a["author"]["display_name"] for a in w.get("authorships", []) if a.get("author")],
        "venue": src.get("display_name") or "",
        "cited_by": w.get("cited_by_count", 0),
        "doi": doi,
        "openalex": (w.get("id") or "").replace("https://openalex.org/", ""),
        "type": w.get("type"),
        "url": f"https://doi.org/{doi}" if doi else w.get("id", ""),
        "abstract": oa_abstract(w.get("abstract_inverted_index")),
        "source": "OpenAlex",
    }


def from_s2(p):
    ext = p.get("externalIds") or {}
    doi = clean_doi(ext.get("DOI"))
    return {
        "title": p.get("title") or "",
        "year": p.get("year"),
        "authors": [a.get("name", "") for a in p.get("authors") or []],
        "venue": p.get("venue") or "",
        "cited_by": p.get("citationCount") or 0,
        "influential": p.get("influentialCitationCount"),
        "doi": doi,
        "s2": p.get("paperId"),
        "url": f"https://doi.org/{doi}" if doi else (p.get("url") or ""),
        "abstract": p.get("abstract") or "",
        "tldr": (p.get("tldr") or {}).get("text", ""),
        "source": "Semantic Scholar",
    }


S2_FIELDS = "title,year,authors,venue,citationCount,influentialCitationCount,externalIds,url,abstract"


def oa_search(q, n, yfrom=None, yto=None, extra_filter=None, strict=False):
    f = []
    if strict:
        # every word must appear in the title or abstract
        f.append("title_and_abstract.search:" + " AND ".join(w for w in q.replace(",", " ").split()))
    if yfrom:
        f.append(f"from_publication_date:{yfrom}-01-01")
    if yto:
        f.append(f"to_publication_date:{yto}-12-31")
    if extra_filter:
        f.append(extra_filter)
    params = {"per_page": min(n, 200)}
    if strict:
        params["sort"] = "cited_by_count:desc"
    else:
        params["search"] = q
    if f:
        params["filter"] = ",".join(f)
    r = oa("/works", **params) or {}
    return [from_oa(w) for w in r.get("results", [])], r.get("meta", {}).get("count", 0)


def s2_search(q, n, yfrom=None, yto=None):
    params = {"query": q, "limit": min(n, 100), "fields": S2_FIELDS}
    if yfrom or yto:
        params["year"] = f"{yfrom or ''}-{yto or ''}"
    r = s2("/graph/v1/paper/search", **params) or {}
    return [from_s2(p) for p in r.get("data", []) or []]


def merge(lists):
    """Merge result lists; papers found by both sources are marked."""
    out, seen = [], {}
    for lst in lists:
        for rank, p in enumerate(lst):
            key = p["doi"] or p["title"].lower().strip()
            if key in seen:
                o = seen[key]
                o["found_by"] = "both"
                o["rank_sum"] += rank
                for k in ("tldr", "influential", "s2", "openalex"):
                    if p.get(k) and not o.get(k):
                        o[k] = p[k]
                if not o.get("abstract") and p.get("abstract"):
                    o["abstract"] = p["abstract"]
            else:
                p = dict(p, found_by=p["source"], rank_sum=rank + 50)
                seen[key] = p
                out.append(p)
    out.sort(key=lambda p: (p["found_by"] != "both", p["rank_sum"]))
    return out


# ---------- output ----------

def cite(p):
    a = p["authors"]
    au = (a[0].split()[-1] + (" et al." if len(a) > 2 else (f" & {a[1].split()[-1]}" if len(a) == 2 else ""))) if a else "?"
    return f"{au} ({p.get('year') or 'n.d.'})"


def show(papers, args, abstract_chars=300):
    if args.json:
        print(json.dumps(papers, indent=2))
        return
    if args.dois:
        for p in papers:
            if p.get("doi"):
                print(p["doi"])
        return
    for i, p in enumerate(papers, 1):
        line = f"{i}. **{p['title']}**, {cite(p)}"
        if p.get("venue"):
            line += f", *{p['venue']}*"
        line += f". Cited {p.get('cited_by', 0)}"
        if p.get("influential") is not None:
            line += f" ({p['influential']} influential)"
        if p.get("found_by"):
            line += f". [{p['found_by']}]"
        print(line)
        if p.get("url"):
            print(f"   {p['url']}")
        txt = p.get("tldr") or p.get("abstract") or ""
        if txt and abstract_chars:
            print(f"   {txt[:abstract_chars]}{'…' if len(txt) > abstract_chars else ''}")
    if not papers:
        print("(no results)")


# ---------- commands ----------

def cmd_search(a):
    lists = []
    if a.source in ("both", "oa"):
        lists.append(oa_search(a.query, a.n, a.yfrom, a.yto, strict=a.strict)[0])
    if a.source in ("both", "s2"):
        lists.append(s2_search(a.query, a.n, a.yfrom, a.yto))
    show(merge(lists)[: a.n * (2 if a.source == "both" else 1)], a)


def resolve_oa(ident):
    ident = ident.strip()
    if ident.upper().startswith("W"):
        return oa(f"/works/{ident}")
    return oa(f"/works/doi:{clean_doi(ident)}")


def cmd_paper(a):
    w = resolve_oa(a.id)
    s = s2(f"/graph/v1/paper/DOI:{clean_doi(a.id)}", fields=S2_FIELDS + ",tldr") if not a.id.upper().startswith("W") else None
    if not w and not s:
        raise SystemExit("Not found in OpenAlex or Semantic Scholar.")
    p = from_oa(w) if w else from_s2(s)
    if s:
        sp = from_s2(s)
        p["tldr"], p["influential"] = sp.get("tldr"), sp.get("influential")
    if a.json:
        p["counts_by_year"] = (w or {}).get("counts_by_year", [])
        print(json.dumps(p, indent=2))
        return
    show([p], a, abstract_chars=0)
    if p.get("abstract"):
        print(f"\n**Abstract:** {p['abstract']}")
    if p.get("tldr"):
        print(f"\n**TLDR (Semantic Scholar):** {p['tldr']}")
    cby = sorted((w or {}).get("counts_by_year", []), key=lambda c: c["year"])
    if cby:
        print("\n**Citations per year:** " + ", ".join(f"{c['year']}: {c['cited_by_count']}" for c in cby))


def cmd_similar(a):
    ids = [f"DOI:{clean_doi(d)}" for d in a.ids]
    r = s2("/recommendations/v1/papers", data={"positivePaperIds": ids, "negativePaperIds": []},
           limit=a.n, fields=S2_FIELDS) or {}
    recs = [from_s2(p) for p in r.get("recommendedPapers", [])]
    rel = []
    w = resolve_oa(a.ids[0])
    if w and w.get("related_works"):
        ids_oa = "|".join(x.replace("https://openalex.org/", "") for x in w["related_works"][: a.n])
        rel = [from_oa(x) for x in (oa("/works", filter=f"openalex:{ids_oa}", per_page=a.n) or {}).get("results", [])]
    show(merge([recs, rel])[: a.n * 2], a)


def cmd_verify(a):
    if a.title:
        r = get(f"{CR}/works?{urllib.parse.urlencode({'query.bibliographic': a.title, 'rows': 3})}")
        items = (r or {}).get("message", {}).get("items", [])
    else:
        r = get(f"{CR}/works/{urllib.parse.quote(clean_doi(a.doi))}")
        items = [r["message"]] if r else []
    if not items:
        print("NOT FOUND in Crossref. Treat the DOI as unverified.")
        return
    out = []
    for m in items:
        rec = {
            "doi": m.get("DOI"),
            "title": (m.get("title") or [""])[0],
            "authors": [f"{x.get('given', '')} {x.get('family', '')}".strip() for x in m.get("author", [])],
            "journal": (m.get("container-title") or [""])[0],
            "year": ((m.get("issued") or {}).get("date-parts") or [[None]])[0][0],
            "volume": m.get("volume"), "issue": m.get("issue"), "pages": m.get("page"),
            "type": m.get("type"),
        }
        out.append(rec)
    if a.json:
        print(json.dumps(out, indent=2))
        return
    for r in out:
        print(f"- DOI {r['doi']} → **{r['title']}**")
        print(f"  {', '.join(r['authors'][:8])}{' …' if len(r['authors']) > 8 else ''}")
        print(f"  *{r['journal']}* {r['year']}; vol {r['volume']}, issue {r['issue']}, pp {r['pages']} ({r['type']})")
    if a.title:
        print("\nCheck the top match's title and authors against the citation before using its DOI.")


def cmd_neighbors(a):
    oa_r, total = oa_search(a.query, a.n * 2, strict=a.strict)
    s2_r = s2_search(a.query, a.n * 2)
    m = merge([oa_r, s2_r])[: a.n]
    if not (a.json or a.dois):
        print(f"Nearest-neighbour papers for: \"{a.query}\" ({total:,} OpenAlex matches overall)")
        print("Papers found by both sources are listed first. For each one, ask: does it already answer my question,")
        print("in my population, with my design? Whether the gap holds is the researcher's call; these are leads to read.\n")
    show(m, a)


def cmd_debate(a):
    yfrom = time.localtime().tm_year - a.years
    recent, _ = oa_search(a.query, a.n, yfrom=yfrom)
    if not recent:
        print("(no recent papers found)")
        return
    ids = "|".join(p["openalex"] for p in recent if p["openalex"])
    works = (oa("/works", filter=f"openalex:{ids}", per_page=a.n, select="id,referenced_works") or {}).get("results", [])
    c = Counter()
    for w in works:
        for ref in set(w.get("referenced_works") or []):
            c[ref.replace("https://openalex.org/", "")] += 1
    top = [k for k, v in c.most_common(15) if v >= 2]
    anc = []
    if top:
        res = (oa("/works", filter=f"openalex:{'|'.join(top)}", per_page=len(top)) or {}).get("results", [])
        byid = {from_oa(w)["openalex"]: from_oa(w) for w in res}
        anc = [dict(byid[k], shared_by=c[k]) for k in top if k in byid]
    if a.json:
        print(json.dumps({"recent": recent, "shared_references": anc}, indent=2))
        return
    print(f"## Shared reference core: cited by several of the {len(recent)} most relevant papers since {yfrom}\n")
    print("These are the older papers that the recent work keeps citing: the foundations of the debate.\n")
    for p in anc:
        print(f"- cited by **{p['shared_by']}/{len(recent)}**: {p['title']}, {cite(p)}. {p['url']}")
    print(f"\n## The recent papers ({yfrom}–now)\n")
    show(recent[:15], a, abstract_chars=200)


def cmd_saturation(a):
    def counts(extra=None):
        q = a.query.replace(",", " ")
        f = [f"title_and_abstract.search:{q}", f"from_publication_date:{a.yfrom}-01-01"] + ([extra] if extra else [])
        r = oa("/works", filter=",".join(f), group_by="publication_year") or {}
        return {int(g["key"]): g["count"] for g in r.get("group_by", []) if str(g["key"]).isdigit()}
    allc, revc = counts(), counts("type:review")
    rows = sorted(set(allc) | set(revc))
    if a.json:
        print(json.dumps({"all": allc, "reviews": revc}, indent=2))
        return
    print(f"Papers per year matching \"{a.query}\" (OpenAlex, title + abstract match; a rough count, not a precise one):\n")
    print("| Year | Papers | Reviews |\n|---|---|---|")
    for y in rows:
        print(f"| {y} | {allc.get(y, 0):,} | {revc.get(y, 0):,} |")
    print("\nA steep recent rise, especially in reviews, suggests the gap may be closing. Read the newest reviews before claiming one.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--dois", action="store_true")
    sp = ap.add_subparsers(dest="cmd", required=True)

    def common(p):
        p.add_argument("--json", action="store_true", default=argparse.SUPPRESS)
        p.add_argument("--dois", action="store_true", default=argparse.SUPPRESS)
        return p

    p = common(sp.add_parser("search")); p.add_argument("query"); p.add_argument("--from", dest="yfrom", type=int)
    p.add_argument("--to", dest="yto", type=int); p.add_argument("--n", type=int, default=10)
    p.add_argument("--source", choices=["both", "oa", "s2"], default="both")
    p.add_argument("--strict", action="store_true", help="OpenAlex: every word must be in title/abstract")
    p.set_defaults(f=cmd_search)
    p = common(sp.add_parser("paper")); p.add_argument("id"); p.set_defaults(f=cmd_paper)
    p = common(sp.add_parser("similar")); p.add_argument("ids", nargs="+"); p.add_argument("--n", type=int, default=10)
    p.set_defaults(f=cmd_similar)
    p = common(sp.add_parser("verify")); p.add_argument("doi", nargs="?"); p.add_argument("--title")
    p.set_defaults(f=cmd_verify)
    p = common(sp.add_parser("neighbors")); p.add_argument("query"); p.add_argument("--n", type=int, default=15)
    p.add_argument("--strict", action="store_true", help="OpenAlex: every word must be in title/abstract")
    p.set_defaults(f=cmd_neighbors)
    p = common(sp.add_parser("debate")); p.add_argument("query"); p.add_argument("--years", type=int, default=5)
    p.add_argument("--n", type=int, default=40); p.set_defaults(f=cmd_debate)
    p = common(sp.add_parser("saturation")); p.add_argument("query"); p.add_argument("--from", dest="yfrom", type=int, default=2000)
    p.set_defaults(f=cmd_saturation)
    a = ap.parse_args()
    if a.cmd == "verify" and not (a.doi or a.title):
        ap.error("verify needs a DOI or --title")
    a.f(a)


if __name__ == "__main__":
    main()
