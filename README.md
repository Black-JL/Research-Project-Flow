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

Three layers, each with a distinct job:

### Voice: Weitzman

The default voice for all prose is modeled on Martin Weitzman's late-career writing. Weitzman's power came from letting the structure of the problem make the argument. Five principles:

1. **Make ignorance dangerous.** State what is unknown, then show that the unknown region is exactly where the largest consequences live. The absence of evidence is not safety — it is a feature of how the evidence was generated.
2. **Let structure make the argument.** Never say "this is important." Set up the logical structure so the reader arrives at importance on their own. Describe the decision problem precisely; the conclusion follows.
3. **Use the nulls as setup.** When most results are null, that is not a weakness — it is the center of the distribution. The finding is in the tail. The nulls breed false confidence; the tail is where the stakes live.
4. **Name the mechanism that makes the evidence misleading.** Do not say "prior research has limitations." Identify the specific feature of the evidence-generating process that produces the blind spot — screening criteria, sample selection, institutional design. A named mechanism is harder to dismiss than a vague caveat.
5. **Write to a decision-maker, not a spectator.** Frame the contribution as: here is what you now know, here is what you still do not, and you will have to decide anyway. The reader should feel the weight of what they are deciding after finishing the paper.

### Clarity: McCloskey

All prose follows McCloskey's *Economical Writing* principles:

1. **Active verbs.** "Prices increased" not "an increase in prices occurred."
2. **Concrete.** "Machines and workers" not "capital and labor inputs."
3. **Plain.** "Use" not "utilize."
4. **Delete ruthlessly.** Cut "very," "basically," "actually."
5. **One word, one meaning.** Pick a term and keep it.
6. **End strong.** The last word carries emphasis.
7. **No boilerplate.** Never open with "This paper discusses..."
8. **Tables and graphs are writing.** Same rules apply.

### Formatting: AEA

For typesetting, tables, figures, citations, and submission requirements, see `manuscript/aea_style_guide.md`.

### How They Interact

Weitzman sets the *force* — the argument's architecture, what is foregrounded, what the reader is left to conclude. McCloskey sets the *surface* — every sentence is active, concrete, and short. AEA sets the *container* — margins, fonts, table rules, citation style. When in doubt: Weitzman decides *what* to say, McCloskey decides *how* to say it, AEA decides *how it looks on the page*.

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
- Weitzman — "On Modeling and Interpreting the Economics of Catastrophic Climate Change" (*Review of Economics and Statistics*, 2009) — model for argument structure and making ignorance dangerous

---

## License

This template — the scaffolding, scripts, instruction files, and documentation — is released under the [MIT License](LICENSE). You are free to use, modify, and adapt it for your own research projects, including commercial work, with attribution preserved.

The license covers the template only. When you build a project on top of it, your own research data, analysis code, and manuscript remain yours to license (or restrict) as you see fit — and any restricted-use data you load is governed by its own Data Use Agreement, not this license.
