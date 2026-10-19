---
name: lit-search
description: Search the peer-reviewed literature directly through OpenAlex (~250M works), Semantic Scholar, and Crossref, with no third-party server in between. Use when the user asks to find papers, "what's been done on X", find the nearest-neighbour or closest paper, run a duplication or novelty check, map the debate or foundational papers on a topic, check whether a gap is closing, find papers similar to one they've read, look up a paper by DOI, or verify that a citation/DOI is real. Also use before writing any literature-review prose, so every cited claim traces to a real paper.
---

# Literature search

All calls go through one script: `python3 -I <this skill's folder>/lit.py <command> …`. It uses only the standard library and needs no install. Run it with Bash.

| Need | Command |
|---|---|
| Find papers on a question | `lit.py search "keywords" [--from 2015] [--to 2025] [--n 10] [--strict]` |
| Closest existing papers (duplication / novelty check) | `lit.py neighbors "keywords" [--strict] [--n 15]` |
| The foundations of a debate (what recent work keeps citing) | `lit.py debate "keywords" [--years 5]` |
| Is the gap closing? Enough studies for a review? | `lit.py saturation "keywords" [--from 2000]` |
| More like a paper already read | `lit.py similar DOI [DOI …]` |
| Full record: abstract, TLDR, citations per year | `lit.py paper DOI` |
| Is this citation real? | `lit.py verify DOI` or `lit.py verify --title "…"` |

Add `--dois` to print bare DOIs (for Zotero import) or `--json` for raw data.

## How to run a search well

1. **Translate the question into 2–4 short keyword queries.** OpenAlex ranks short keyword queries far better than full sentences. For "Does psychedelic decriminalization raise psychosis ED visits?" run `psilocybin decriminalization`, `psychedelic decriminalization psychosis`, and `hallucinogen emergency department`.
2. **Run each query twice:** once default (broad relevance) and once with `--strict` (every word must be in the title or abstract, sorted by citations). Strict finds the established core. Default finds adjacent work. A very small strict count is itself evidence for a gap; report it.
3. **Biomedical or clinical questions:** also use the PubMed connector (`mcp__pubmed__*`), if it's connected. Use PubMed for clinical precision and OpenAlex and Semantic Scholar for breadth across economics, policy, and health services.
4. **Merge and deduplicate** across queries. Lead with the papers that more than one query, or both sources, returned.

## Rules

- **Results are leads, not findings.** Say what a paper found only if you've read its abstract (`lit.py paper`) or full text. Never infer a finding from a title. If a claim rests on the abstract alone, say so.
- **The researcher judges.** For a duplication or gap check, give the nearest neighbours and what each one covers (population, setting, design, outcome). Then lay out what would make the gap real or fail, and leave the call to the researcher.
- **Verify before citing.** Every DOI that goes into a manuscript, slide, or reference list gets checked with `lit.py verify DOI`, and the title, authors, and year must match the citation. This follows the global DOI-integrity rule; never write a DOI from memory.
- **Zotero:** when the user wants papers saved, use the Zotero MCP (`zotero_add_by_doi`) with DOIs from `--dois`. In a project that uses the `zotero-refs` skill, follow that pipeline. Ask before adding more than a handful of papers.
- **Semantic Scholar rate limits:** without a key, Semantic Scholar shares one pool with every anonymous user, so it often answers HTTP 429. The script then warns and returns OpenAlex results only. Tell the user when that happens, so they know the results are one-source.

## Keys (optional, free, raise rate limits)

Read from the environment or from `~/.config/lit-search/keys.env` (keep that file private, `chmod 600`):

```
OPENALEX_API_KEY=...   # free: openalex.org → sign in → Settings → API key (10 → 30 requests/sec)
S2_API_KEY=...         # free: request at https://www.semanticscholar.org/product/api (dedicated 1 request/sec, no shared-pool 429s)
LIT_MAILTO=...         # optional contact email sent to the APIs; only set if the user chooses to
```

Never put the user's email address or keys anywhere without their say-so.
