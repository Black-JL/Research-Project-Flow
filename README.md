# Research Project Flow

A reusable template for empirical research projects. Built for economists and social scientists using Stata, R, Python, LaTeX, Zotero, Dropbox, and AI-assisted workflows.

**Guide:** [black-jl.github.io/Research-Project-Flow](https://black-jl.github.io/Research-Project-Flow) — full documentation, setup instructions, and workflow guide.

**Origin:** Distilled from the Psychedelic Decriminalization & Psychosis project (2024-2026), validated against Gentzkow & Shapiro, TIER Protocol 4.0, AEA Data Editor guidelines, World Bank DIME Analytics, and the skhiggins/Julian Reif Stata guides.

---

## Guiding Principles

1. **Every file has one home.** Outputs in `output/`, data in `data/`, scripts in `scripts/`. No duplicates.
2. **Data-processing scripts write to `data/processed/`. Analysis scripts write to `output/`.** No script writes to both.
3. **Absolute paths in one place only.** Machine-specific paths appear in `00_run.do`. Everything else uses globals.
4. **One command reproduces everything.** `run_all.sh` executes the full pipeline.
5. **Fail loudly.** Log everything. When something breaks, the log says where and why.
6. **Structure enforces discipline.** If a file doesn't have an obvious home, the structure needs updating.

---

## Folder Structure

```
project-name/
├── README.md                  ← This file (project overview, pipeline, replication)
├── CLAUDE.md                  ← AI agent instructions
├── run_all.sh                 ← Master execution script (Stata + R + Python)
├── .gitignore
│
├── data/
│   ├── raw/                   ← Untouched data as first obtained. NEVER modify.
│   │   └── README.md          ← Source, date, access instructions, DUA terms
│   └── processed/             ← Created by scripts. Documented in pipeline below.
│
├── scripts/
│   ├── 00_run.do              ← Master do-file: sets globals, runs all steps
│   ├── params.do              ← Treatment dates, sample restrictions, outcome codes
│   └── programs/              ← Reusable ado files, helper functions
│
├── output/
│   ├── logs/                  ← Execution logs
│   ├── figures/               ← Plots, maps (manuscript pulls from here)
│   ├── tables/                ← LaTeX .tex fragments (manuscript \input from here)
│   └── results/               ← Stored estimation results (.ster, .rds, .pkl)
│
├── manuscript/
│   ├── manuscript.tex         ← Active manuscript
│   ├── references.bib         ← Auto-exported from Zotero. Do not hand-edit.
│   ├── aea_style_guide.md     ← AEA formatting and style reference
│   └── submission/            ← Camera-ready versions, cover letters
│
├── scratch/                   ← Throwaway debugging. Nothing here is committed.
│
└── .claude/
    ├── settings.json
    └── commands/              ← AI agent commands
```

**Key conventions:**
- **Data naming:** `{project}_{description}_{version}.{ext}` — e.g., `psychosis_treatment_v2.dta`. New versions rather than overwrites.
- **Script numbering:** Leave gaps (01, 05, 10...) for inserted steps. Use letter suffixes (10a, 10b) for variants.
- **Script headers:** Every script must include a structured header documenting Purpose, Inputs, Outputs, and Dependencies. The AI parses these directly.
- **Temporary files:** Prefix with `_`. Anything starting with `_` is disposable.

---

## Data Availability Statement

<!-- Per AEA requirements. Describe data sources, access, restrictions. -->

---

## Dataset List

| Data file | Source | Provided | Notes |
|-----------|--------|----------|-------|
<!-- | data/raw/xxx.csv | [Source] | Yes/No | [Access instructions if No] | -->

---

## Computational Requirements

- **Stata** (version XX, MP/SE)
- **R** (version X.X)
- **Python** (version X.X)
- **LaTeX** (for manuscript compilation)
- **Zotero** with Better BibTeX (for citation management)
- **Packages:** <!-- list Stata/R/Python packages -->
- **Expected runtime:** <!-- X minutes/hours -->
- **Last run on:** <!-- OS, machine description -->

---

## Parameters

All critical research parameters. Every value here must match `scripts/params.do`.

| Parameter | Value | Source |
|-----------|-------|--------|
<!-- | Treatment date, City | YYYY-MM-DD | [Citation] | -->
<!-- | Sample restriction | [Value] | [Rationale] | -->
<!-- | Outcome definition | [Definition] | [Citation] | -->

---

## Description of Programs

Pipeline step order, file dependencies, and I/O map. Update this table every time a script is added or modified.

| Step | Script | Input | Output | Notes |
|------|--------|-------|--------|-------|
<!-- | 01 | scripts/01_import.do | data/raw/xxx.csv | data/processed/xxx_clean.dta | Drops missing IDs | -->
<!-- | 05 | scripts/05_merge.do | data/processed/xxx_clean.dta | data/processed/xxx_merged.dta | Merges with... | -->

---

## Instructions to Replicators

1. Set your machine path in `scripts/00_run.do`.
2. Run `./run_all.sh --all` to execute the full pipeline.
3. Compile `manuscript/manuscript.tex` to produce the paper.

---

## List of Tables and Figures

| Manuscript ref | Output file | Source script |
|---------------|-------------|---------------|
<!-- | Figure 1 | output/figures/fig1_xxx.pdf | scripts/10_treatment.do | -->
<!-- | Table 1 | output/tables/tab1_xxx.tex | scripts/15_balance.R | -->

---

## Available Commands

### Project commands (this repo only)

| Command | Purpose | Usage |
|---------|---------|-------|
| `/status` | Project status dashboard | Just type `/status`. Shows pipeline steps, last run dates, Dropbox conflicts, scratch work. |
| `/run` | Run a pipeline step with validation | `/run` (prompts for step), `/run --all` (full pipeline), `/run --from 05` (from step 05 forward). |
| `/check` | Full project integrity and manuscript audit | Just type `/check`. Verifies scripts, data files, params, and manuscript references all match. |
| `/review` | Adversarial review of an estimation/sample change | Just type `/review` after changing specification logic. Diffs old vs. new, grades each identification dimension PASSED/WARNING/BLOCKER, escalates blockers. |
| `/write` | Draft or revise prose that is clear and sounds like you | Also runs on its own when you ask for prose ("write up Table 3"). Outline of claims first, then a draft, a cold read by a fresh AI reader, and checks. Paste your edits back to teach it your voice. |
| `/lit-search` | Search OpenAlex, Semantic Scholar, and Crossref directly | Also runs on its own when you ask for papers. Nearest-neighbour and duplication check, debate map, gap saturation, similar papers, DOI verification. |
| `/add-step` | Scaffold a new pipeline step end-to-end | Just type `/add-step`. Prompts for step number, language, inputs, outputs. Creates script, updates README and run_all.sh. |
| `/handoff` | Co-author or future-session summary | Just type `/handoff`. Summarizes recent changes, outputs regenerated, open questions. Writes to `session_logs/`. |

### Global commands (available in any project)

| Command | Purpose | Usage |
|---------|---------|-------|
| `/git` | Stage, commit, and push all changes | Just type `/git`. No confirmation needed — stages everything, writes a commit message, commits, and pushes. |
| `/handoff` | Summarize recent work for a collaborator | Just type `/handoff`. Summarizes last 7 days of git activity, modified files, and TODOs. |

> **Note:** In this repo, `/handoff` uses the project-specific version (checks pipeline status, writes to `session_logs/`). The global version is a simpler git-based summary used in other projects.

---

## Collaboration

### Co-Author Instructions
1. The active manuscript is `manuscript.tex`. Do not edit any other `.tex` file.
2. Add comments as `% COAUTHOR: [comment]` so they can be found with search.
3. To add a citation: add to Zotero (preferred) or to `.bib` with `% MANUAL ENTRY` prefix.
4. Do not rename, move, or delete figure/table files. Flag issues as comments.

### Zotero Setup
1. Install [Better BibTeX for Zotero](https://retorque.re/zotero-better-bibtex/).
2. Create a project collection. Export with "Keep Updated" to `manuscript/references.bib`.
3. Set auto-export to "On Change."

### Dropbox + Git
- Project lives in Dropbox. Git is secondary (version control, backup).
- Exclude `.git/` from Dropbox sync: `xattr -w com.dropbox.ignored 1 .git` (macOS).
- Co-author Dropbox edits = merges to main. Commit on their behalf.

---

## Writing Standard

AI-drafted prose fails in four separate ways: it is unclear, it is jargony, the ideas get lost in the language, and it doesn't sound like the author. The `write` skill (`.claude/skills/write/SKILL.md`) handles all four. It runs whenever you ask for prose. Four layers, each with a distinct job:

### 1. Structure: outline first, then PEER paragraphs

Before any prose, the skill writes one topic sentence per paragraph. Each is a **claim**, not a topic, and you approve the list. **Skip test:** the topic sentences alone should make the argument. Each paragraph then makes one point, built as **P**oint, **E**vidence, **E**xplain, **R**epeat/link (from David Stuckler; see `.claude/skills/write/references/peer.md`).

### 2. Voice: yours

How the prose *sounds* comes from a personal voice skill: your own writing samples, a profile of your voice, and a ledger of every edit you make to AI drafts. It lives in `~/.claude/skills/`, outside this repo, because it contains your writing. Setup takes about 15 minutes: `.claude/skills/write/references/voice-setup.md`.

**Style modes** are optional and chosen per piece. A mode borrows another writer's *moves* for clarity and urgency, never their arguments. For example, a Weitzman mode sets facts side by side instead of using adjectives, states exactly where a claim stops, and uses understatement.

### 3. Guidelines: McCloskey and Orwell

These are rules for what to cut, not voices to imitate. Full text is in `.claude/skills/write/references/`:

- **McCloskey, *Economical Writing*** (`mccloskey.md`): active verbs, concrete and plain words, delete ruthlessly, one word one meaning, end strong, no boilerplate, and tables and graphs are writing too.
- **Orwell, "Politics and the English Language"** (`orwell.md`): the six rules, and the four habits to hunt for (dying metaphors, verbal false limbs, pretentious diction, meaningless words). "Let the meaning choose the word, and not the other way about."

### 4. Formatting: AEA

For typesetting, tables, figures, citations, and submission requirements, see `manuscript/aea_style_guide.md`.

### Checks built into the `write` skill

- **Cold read:** a fresh AI reader with no project context summarizes each paragraph. If its summary doesn't match the outline, the text is unclear.
- **Jargon leak:** catches variable names, script and spec labels, and undefined acronyms that crept into prose.
- **Meaning drift:** after any edit, looks for synonym swaps, dropped qualifiers, changed verb strength, and widened outcomes.
- **AI tells:** em dashes, "not just X but Y", reflexive triplets, summary last sentences, and words like "crucial", "landscape", and "delve".

### How they interact

The outline decides *what* to say, the voice decides *how it sounds*, the guidelines decide *what to cut*, and AEA decides *how it looks on the page*.

---

## Setup Checklist

1. Create the folder structure above.
2. Fill in this README with project-specific details.
3. Write `scripts/00_run.do` with collaborator machine paths and sentinel file check.
4. Write `scripts/params.do` with all critical parameters. Verify against primary sources.
5. Set up Zotero and auto-export to `manuscript/references.bib`.
6. Configure `CLAUDE.md` with your project root path.
7. Set up `.gitignore` and Git. Exclude `.git/` from Dropbox.
8. Push to a private GitHub repo as backup.

---

## References

- [Gentzkow & Shapiro — Code and Data for the Social Sciences](https://web.stanford.edu/~gentzkow/research/CodeAndData.pdf)
- [TIER Protocol 4.0](https://www.projecttier.org/tier-protocol/protocol-4-0/)
- [AEA Data Editor — Template README](https://aeadataeditor.github.io/posts/2020-12-08-template-readme)
- [World Bank DIME — Stata Coding Practices](https://dimewiki.worldbank.org/Stata_Coding_Practices)
- [Julian Reif — Stata Coding Guide](https://julianreif.com/guide/)
- [skhiggins — Stata Guide](https://github.com/skhiggins/Stata_guide)
- [Better BibTeX — Auto-Export](https://retorque.re/zotero-better-bibtex/exporting/auto/)
- [Scott Cunningham — MixtapeTools (Referee 2 audit protocol)](https://github.com/scunning1975/MixtapeTools)
- [Scott Cunningham — Claude Code for Empirical Research](https://causalinf.substack.com/p/claude-code-part-12-how-i-use-claude)
- McCloskey — *Economical Writing* (2nd ed., 2000)
- Weitzman, "Fat-Tailed Uncertainty in the Economics of Catastrophic Climate Change" (*Review of Environmental Economics and Policy*, 2011): an example of style moves for clarity and urgency (an optional style mode)
- Orwell, "Politics and the English Language" (*Horizon*, 1946): [text at the Orwell Foundation](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/)
- Stuckler, PEER paragraph system: [video](https://www.youtube.com/watch?v=gFv47hloKN8)

---

## License

This template — the scaffolding, scripts, instruction files, and documentation — is released under the [MIT License](LICENSE). You are free to use, modify, and adapt it for your own research projects, including commercial work, with attribution preserved.

The license covers the template only. When you build a project on top of it, your own research data, analysis code, and manuscript remain yours to license (or restrict) as you see fit — and any restricted-use data you load is governed by its own Data Use Agreement, not this license.
