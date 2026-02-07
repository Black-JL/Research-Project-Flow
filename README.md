# Research Project Flow

A reusable template for empirical research projects. Built for economists and social scientists using Stata, R, Python, LaTeX, Zotero, Dropbox, and AI-assisted workflows.

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

| Command | Purpose |
|---------|---------|
| `/run` | Run a pipeline step with validation |
| `/check` | Full project integrity and manuscript audit |
| `/status` | Project status dashboard |
| `/handoff` | Co-author or future-session summary |
| `/add-step` | Scaffold a new pipeline step end-to-end |
| `/git` | Stage, commit, and push all changes to GitHub |

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

All prose follows McCloskey's *Economical Writing* principles:

1. **Active verbs.** "Prices increased" not "an increase in prices occurred."
2. **Concrete.** "Machines and workers" not "capital and labor inputs."
3. **Plain.** "Use" not "utilize."
4. **Delete ruthlessly.** Cut "very," "basically," "actually."
5. **One word, one meaning.** Pick a term and keep it.
6. **End strong.** The last word carries emphasis.
7. **No boilerplate.** Never open with "This paper discusses..."
8. **Tables and graphs are writing.** Same rules apply.

For AEA-specific formatting, see `manuscript/aea_style_guide.md`.

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
- McCloskey — *Economical Writing* (2nd ed., 2000)
