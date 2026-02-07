# Research Project Flow

A reusable template for empirical research projects. Built for economists and social scientists using Stata, R, LaTeX, Zotero, Dropbox, and AI-assisted workflows.

**How to use this document:**
- **Starting a new project?** Go to [Setup Checklist](#setup-checklist).
- **Configuring an existing project?** Use the [Folder Structure](#folder-structure) as a reference.
- **Troubleshooting?** See [Appendix A: Lessons Learned](#appendix-a-lessons-learned).

**Origin:** Distilled from the Psychedelic Decriminalization & Psychosis project (2024-2026), validated against Gentzkow & Shapiro, TIER Protocol 4.0, AEA Data Editor guidelines, World Bank DIME Analytics, and the skhiggins/Julian Reif Stata guides. See [Appendix B](#appendix-b-references) for links.

**This document is not:** a Stata coding style guide, a LaTeX tutorial, or a Git manual. It is a project organization framework.

---

## Guiding Principles

1. **Every file has one home.** Outputs in `output/`, data in `data/`, scripts in `scripts/`. No duplicates.
2. **Data-processing scripts write to `data/processed/`. Analysis scripts write to `output/`.** No script writes to both.
3. **Absolute paths in one place only.** Machine-specific paths appear in `00_run.do`. Everything else uses globals (`$data`, `$figures`) set by that file.
4. **One command reproduces everything that can be reproduced.** `run_all.sh` executes the full pipeline. For restricted data, it starts from the first shareable dataset.
5. **The pipeline document is the source of truth.** Every script's inputs, outputs, and dependencies are in `pipeline.md`. Nothing runs without being documented there.
6. **Fail loudly.** Log everything. When something breaks, the log says where and why.
7. **Structure enforces discipline.** If a file doesn't have an obvious home, the structure needs updating — not the file.

---

## Folder Structure

```
project-name/
│
├── README.md                  ← Project overview, replication instructions, available commands
├── CLAUDE.md                  ← AI agent instructions (references pipeline.md)
├── pipeline.md                ← Step order, file dependencies, I/O map
├── parameters.md              ← Single source of truth for critical research parameters
├── table_figure_map.md        ← Maps every manuscript figure/table → source script
├── run_all.sh                 ← Master execution script (Stata + R)
├── .gitignore                 ← Excludes secrets, large data, build artifacts
│
├── context/                   ← Background research (excluded from replication package)
│   ├── literature/            ← Papers, PDFs (linked to Zotero via Better BibTeX)
│   └── notes/                 ← Memos, meeting notes, methodology decisions
│
├── legacy/                    ← Read-only materials from prior/related projects
│   ├── scripts/
│   └── data/
│
├── data/
│   ├── raw/                   ← Untouched data as first obtained. NEVER modify.
│   │   └── README.md          ← Source, date, access instructions, DUA terms
│   └── processed/             ← Created by scripts. Documented in pipeline.md.
│
├── scripts/
│   ├── 00_run.do              ← Master do-file: sets globals, runs all steps
│   ├── params.do              ← Treatment dates, sample restrictions, outcome codes
│   ├── 01_import.do           ← Numbered with gaps (01, 05, 10, 15...)
│   ├── 05_merge.do            ← Use suffixes for variants (10a, 10b)
│   ├── 10_treatment.do
│   ├── 15_balance.R           ← R scripts alongside Stata
│   └── programs/              ← Reusable ado files, helper functions
│
├── scratch/                   ← Throwaway debugging scripts. Nothing here is committed.
│
├── output/                    ← ALL generated outputs. Nothing hand-created.
│   ├── logs/                  ← Execution logs (01_import.log, etc.)
│   ├── figures/               ← Plots, maps (manuscript pulls from here)
│   ├── tables/                ← LaTeX .tex fragments, CSVs (manuscript \input{} from here)
│   └── results/               ← Stored estimation results (.ster, .rds)
│
├── manuscript/                ← LaTeX paper (or name this overleaf/ if using Overleaf sync)
│   ├── manuscript.tex         ← Single active version. Mark with %% ACTIVE MANUSCRIPT header.
│   ├── references.bib         ← Auto-exported from Zotero. Do not hand-edit.
│   └── submission/            ← Camera-ready versions, cover letters (empty until needed)
│
├── session_logs/              ← AI session documentation. One file per day, append within day.
│
└── .claude/
    ├── settings.json          ← Permissions, hooks
    └── commands/              ← Default slash commands (see below)
```

**Key conventions:**
- **Data naming:** `{project}_{description}_{version}.{ext}` — e.g., `psychosis_treatment_v2.dta`. New versions (`_v2`, `_v3`) rather than overwrites. Document changes in `pipeline.md`.
- **Script numbering:** Leave gaps (01, 05, 10...) for inserted steps. Use letter suffixes (10a, 10b) for variants. Decimal (3.5) also acceptable for patches.
- **Temporary files:** Prefix with `_` anywhere in the project. Anything starting with `_` is disposable and belongs in `scratch/`.
- **Binary data formats** (.dta, .rds) embed metadata that doesn't auto-update when scripts change. After correcting a parameter, re-run from the affected step — don't just fix downstream scripts.

---

## Setup Checklist

To start a new project, run through these steps in order:

1. **Create the folder structure** above. Create all directories including `data/raw/`, `data/processed/`, `output/logs/`, `output/figures/`, `output/tables/`, `output/results/`, `scratch/`, `session_logs/`, `.claude/commands/`.

2. **Write `README.md`** with the canonical project location as the first line, a project overview, data availability statement, and software requirements. Follow the [AEA Template README](https://aeadataeditor.github.io/posts/2020-12-08-template-readme) format.

3. **Write `00_run.do`** with collaborator machine paths and a sentinel file check:
   ```stata
   * Detect user and set project root
   if "`c(username)'" == "yourname" {
       global root "/Users/yourname/Dropbox/Project Name"
   }
   * ... add each collaborator ...

   * Verify correct folder
   capture confirm file "$root/pipeline.md"
   if _rc != 0 {
       display as error "Cannot find pipeline.md — wrong folder?"
       exit 601
   }

   * Define globals
   global data      "$root/data"
   global raw       "$root/data/raw"
   global processed "$root/data/processed"
   global scripts   "$root/scripts"
   global output    "$root/output"
   global figures   "$root/output/figures"
   global tables    "$root/output/tables"
   global logs      "$root/output/logs"
   ```

4. **Write `parameters.md`** and `params.do` with all critical research parameters — treatment dates, sample restrictions, outcome definitions. Verify against primary sources. `params.do` is sourced by `00_run.do`; `parameters.md` is the human-readable version with citations to official sources.

5. **Write `pipeline.md`** as a skeleton. Fill in steps as you build:
   ```markdown
   ## Step 01: Import and Clean
   - **Script:** scripts/01_import.do
   - **Input:** data/raw/survey.csv
   - **Output:** data/processed/survey_clean.dta
   - **Notes:** Drops missing IDs. Creates derived variables.
   ```

6. **Set up Zotero** — install [Better BibTeX](https://retorque.re/zotero-better-bibtex/), create a project collection, export with "Keep Updated" checked, save as `manuscript/references.bib`. Set auto-export to "On Change."

7. **Configure `CLAUDE.md`** with pipeline reference, parameters reference, folder permissions, guardrails, and structural protection (see [AI Agent Configuration](#ai-agent-configuration)).

8. **Install default commands** — copy each command from the [Default Commands](#default-commands) section into `.claude/commands/<name>.md`. Add the command table to `README.md`.

9. **Set up `.gitignore` and Git.** Exclude `.git/` from Dropbox: `xattr -w com.dropbox.ignored 1 .git` (macOS). Push to a private GitHub repo as backup.

10. **Send co-authors the 5-point instruction list** from [Co-Author Workflow](#co-author-workflow).

11. **Start working.** As you add scripts, update `pipeline.md`. As you add outputs, update `table_figure_map.md`. As you find papers, add to Zotero. As you work with AI, log sessions.

---

## Script Execution

### `run_all.sh`

Handles both Stata and R. Usage: `./run_all.sh "05_merge.do"` (single step) or `./run_all.sh --all` (full pipeline). Logs go to `output/logs/`, and the log opens for review after execution. See the full template in `run_all.sh` in the project root.

The script should include `run_stata()` and `run_r()` functions that:
1. Create a logging wrapper
2. Execute the script in batch mode
3. Clean up temporary files
4. Open the log for review
5. Return the exit code

### MCP Workflow

Document in `mcp_workflow.md`: path to the Stata/R executable, how to invoke `run_all.sh`, logging conventions, and error handling. When AI assists with running code, every execution must be **logged** (to `output/logs/`), **auditable** (log opens for review), and **pipeline-aware** (AI checks `pipeline.md` first).

---

## AI Agent Configuration

### CLAUDE.md Requirements

Every project's `CLAUDE.md` must include:

1. **Project root path** — prevents "wrong folder" errors
2. **Pipeline reference** — "Read `pipeline.md` before modifying any script"
3. **Parameters reference** — "Check `parameters.md` for all hardcoded values"
4. **Folder permissions** — which folders are read-only, what can be written where
5. **MCP workflow reference** — how to execute scripts
6. **Session logging protocol** — when and how to log
7. **Writing standard** — reference the project [Writing Standard](#writing-standard)

### Guardrails

Two tiers of protection:

**Tier 1 — Always (before any action):**
- Confirm correct working directory
- Confirm correct target files
- Read `pipeline.md` before modifying scripts or running pipeline steps
- Check `parameters.md` before using hardcoded values
- Never assume which file version is active — ask if ambiguous
- Never present uncertain results with confidence — flag uncertainty
- Never push to a remote repo without confirming the target

**Tier 2 — Structural changes only (break the glass):**

Any action that moves/renames/deletes files in `scripts/`, `data/`, or `output/`, changes output paths in scripts, modifies `00_run.do` globals or `params.do`, adds/removes/renumbers pipeline steps, or alters `\graphicspath`/`\input` references in the manuscript triggers the following mandatory sequence:

1. **Identify what breaks.** Read `pipeline.md` and `table_figure_map.md`. List every file, script, and manuscript reference that depends on what is about to change.
2. **Show the full impact.** Present: what you want to change, every downstream dependency that will break, every upstream file that feeds into the changed item.
3. **Propose the complete fix.** All scripts needing path updates, all `pipeline.md` entries to revise, any manuscript references that change, any `table_figure_map.md` updates.
4. **Get explicit confirmation.** Do not proceed until the user approves the full change set.

**What is always safe** (no guardrail needed): editing code logic within a script without changing its I/O, adding text or citations to the manuscript, writing to `session_logs/`, working in `scratch/`, reading any file.

### Default Commands

Copy each block below into `.claude/commands/<name>.md`. These are plain markdown files. Document them in `README.md` so anyone opening the project knows what's available.

| Command | What it does |
|---------|-------------|
| `/run-step` | Run a pipeline step with input/output validation |
| `/validate` | Check pipeline integrity — missing files, misplaced scripts, parameter drift |
| `/audit` | Audit manuscript figures/tables against source scripts and `table_figure_map.md` |
| `/status` | Show project status — last runs, recent logs, pipeline progress |
| `/log` | Update today's session log |
| `/handoff` | Prepare a plain-language co-author summary |

**`/run-step`**
```
Read pipeline.md. The user wants to run a pipeline step. Ask which step if not specified.
Before running: (1) confirm input files exist, (2) confirm output paths are correct,
(3) check parameters.md, (4) identify downstream steps that will need re-running.
Execute using ./run_all.sh "<script_name>". Read the log, summarize results,
update session log.
```

**`/validate`**
```
Run a full integrity check: (1) every script in pipeline.md exists, (2) every input
data file exists, (3) no scripts or logs sitting in data/, (4) output directories exist,
(5) params.do matches parameters.md, (6) manuscript compiles if possible.
Report all issues. Do not fix anything — present findings for user review.
```

**`/audit`**
```
Read table_figure_map.md. For every entry: (1) verify the output file exists,
(2) verify the source script exists, (3) check parameters match parameters.md,
(4) find any manuscript references NOT in table_figure_map.md (undocumented),
(5) find any output files NOT in the manuscript (orphans),
(6) check that key statistics in manuscript text match parameters.md and recent outputs.
Report broken links, stale outputs, undocumented references.
```

**`/status`**
```
Quick project overview: (1) summarize pipeline steps and status from pipeline.md,
(2) check output/logs/ for recent runs with dates, (3) check session_logs/ for last entry,
(4) check scratch/ for active debugging, (5) check for Dropbox conflicted copies.
Present as a clean table: Step | Last Run | Status | Notes.
```

**`/log`**
```
Append to today's session log (session_logs/YYYY-MM-DD_topic.md). Create if needed.
Include: summary, files modified, commands run, errors, next steps.
```

**`/handoff`**
```
Prepare a plain-language co-author summary. Read session_logs/ and git log.
Cover: what changed, what figures/tables were regenerated, what to review,
open questions needing co-author input. Write to session_logs/YYYY-MM-DD_handoff.md.
```

### Session Context Protocol

Start every AI session with a context block to prevent misdirected work:

```
Context: [Project name] at [path]. Active manuscript: [file].
Pipeline status: Steps 1-N done, Step N+1 in progress.
Today's goal: [task]. Constraints: [anything non-obvious].
```

### Human Oversight Rule

AI assistants present incorrect results with false confidence. Always verify numerical claims against log files. After AI batch operations, run `/validate`. Trust AI for speed. Trust yourself for correctness.

---

## Collaboration

### Co-Author Instructions (Send These)

1. **The active manuscript is `[filename].tex`.** Do not edit any other `.tex` file.
2. **Add comments as `% COAUTHOR: [comment]`** so they can be found with search.
3. **To add a citation:** add to Zotero (preferred) or to `.bib` with `% MANUAL ENTRY` prefix.
4. **Do not rename, move, or delete figure/table files.** Flag issues as comments.
5. **The project lives at `[Dropbox path]`.** Do not create copies elsewhere.

### Handling Co-Author Edits

- Check for Dropbox "conflicted copy" files. Resolve and delete.
- If using Git, commit co-author changes: `git commit -m "Apply [Name]'s edits from [date]"`.
- Review `.bib` changes for duplicates.

### Zotero Setup

1. Install [Better BibTeX for Zotero](https://retorque.re/zotero-better-bibtex/).
2. Create a project collection. Export with "Keep Updated" → save as `manuscript/references.bib`.
3. Set auto-export to "On Change" in Better BibTeX preferences.
4. Never hand-edit `references.bib`. Edit in Zotero. Before final submission, copy to `references_final.bib` for proofreading tweaks.

### Dropbox + Git

Dropbox is primary (collaboration). Git is secondary (version control, backup).

1. Project lives in Dropbox.
2. Exclude `.git/` from sync — **macOS:** `xattr -w com.dropbox.ignored 1 .git` | **Windows:** `Set-Content -Path '.git' -Stream 'com.dropbox.ignored' -Value 1`
3. Push to a private GitHub repo as backup.
4. Co-author Dropbox edits = merges to main. Commit on their behalf.

### Manuscript Management

- One active `.tex` file. Header: `%% ACTIVE MANUSCRIPT — last confirmed [date]`.
- Archived versions get: `%% ARCHIVED — see manuscript.tex`.
- Figures pulled via `\graphicspath{{../output/figures/}{./}}` (fallback to local for migration).
- Tables via `\input{../output/tables/main_results.tex}`.
- If using Overleaf, name the folder `overleaf/` instead of `manuscript/`. Same principles apply.

### Writing Standard

All prose in this project — manuscript text, session logs, handoff summaries, co-author memos — follows these principles (after McCloskey, *Economical Writing*):

1. **Use active verbs.** Find the action and express it as a verb, not a noun. "Prices increased" not "an increase in prices occurred." Circle every "is" — if the page looks diseased, rewrite.
2. **Be concrete.** "Machines and workers" not "capital and labor inputs." Readers generalize from examples; they cannot particularize from abstractions.
3. **Be plain.** "Use" not "utilize." "Do" not "implement." Five-dollar words hide five-cent thoughts.
4. **Delete ruthlessly.** Cut "very," "basically," "actually," "absolutely." Most adverbs convey opinion nobody asked for. If a word adds nothing, it subtracts.
5. **One word, one meaning.** Do not call it "the healthcare sector," then "the medical industry," then "health services." Pick a term and keep it.
6. **End strong.** The last word in a sentence carries emphasis. Do not let sentences straggle with qualifications.
7. **No boilerplate.** Never open with "This paper discusses..." Never write a table-of-contents paragraph. Get to the point.
8. **Tables and graphs are writing.** Same rules apply. Use words in headings, not acronyms. Show only what the reader needs.
9. **Read out loud.** If you blush, rewrite.

**For AI agents:** Apply these principles when drafting or revising any prose. When reviewing manuscript text, flag violations by principle number (e.g., "Principle 1: nominalization in paragraph 3").

### Manuscript Audit Checklist

Before sharing or submitting:

- [ ] Compiles from scratch (delete all build artifacts first)
- [ ] All `\includegraphics` resolve to files in `output/figures/`
- [ ] All `\input{...table...}` resolve to files in `output/tables/`
- [ ] All `\cite` commands resolve (no "??" in PDF)
- [ ] Cross-references (`\ref`, `\label`) all resolve
- [ ] Key statistics in text match `parameters.md` and recent output logs
- [ ] `table_figure_map.md` is current
- [ ] Every dataset cited in bibliography
- [ ] Prose follows the [Writing Standard](#writing-standard) — active verbs, no nominalizations, no boilerplate openings
- [ ] Table/figure headings use descriptive words, not acronyms or variable names

### Restricted-Access Data

For DUA-governed data (HCUP, CMS, NCHS, etc.): document terms in `data/raw/DUA_README.md`, never store restricted raw data in cloud sync folders without DUA approval, mark the pipeline boundary where shareable data begins, and include data access instructions in `README.md`.

---

## Appendix A: Lessons Learned

Real mistakes from the project that generated this template:

| Mistake | What Happened | Prevented By |
|---------|--------------|-------------|
| Wrong treatment dates | Santa Cruz coded 20 months wrong. Cascaded through 65+ files. | `parameters.md` / `params.do` |
| Wrong working folder | 2-3 sessions in Box instead of Dropbox. | Sentinel check in `00_run.do` |
| Hardcoded drive paths | 131 scripts used `/Volumes/WD_2Tb/...`. | Globals in `00_run.do` |
| Scattered outputs | Figures in 4 different folders. | Single `output/` folder |
| Missing pipeline step | Gap between Steps 3 and 4 discovered late. | `pipeline.md` |
| Multiple manuscript versions | 3 `.tex` files, unclear which was active. | `%% ACTIVE MANUSCRIPT` header |
| Lost AI context | No session logs. Repeated work. | `session_logs/` |
| Stale embedded labels | DTA labels retained wrong dates after script fix. | Re-run from affected step |
| AI acted on wrong target | Wrong repo, wrong rubric version, wrong folder. | Guardrails + session context |
| AI jumped before reading | Batch path changes without checking pipeline. | Tier 1 guardrails |
| AI reported wrong results | Contradictory findings presented confidently. | Human oversight rule |

---

## Appendix B: References

- **Gentzkow & Shapiro** — [Code and Data for the Social Sciences](https://web.stanford.edu/~gentzkow/research/CodeAndData.pdf)
- **TIER Protocol 4.0** — [Project TIER](https://www.projecttier.org/tier-protocol/protocol-4-0/)
- **AEA Data Editor** — [Preparing Your Files](https://aeadataeditor.github.io/aea-de-guidance/preparing-for-data-deposit) | [Template README](https://aeadataeditor.github.io/posts/2020-12-08-template-readme)
- **World Bank DIME** — [Stata Coding Practices](https://dimewiki.worldbank.org/Stata_Coding_Practices) | [ietoolkit](https://github.com/worldbank/ietoolkit)
- **skhiggins** — [Stata Guide](https://github.com/skhiggins/Stata_guide)
- **Julian Reif** — [Stata Coding Guide](https://julianreif.com/guide/)
- **Luke Stein** — [Stata/LaTeX Workflows](https://lukestein.com/stata-latex-workflows/)
- **Sebastian Tello-Trillo** — [Stata Folder Structure Setup](https://sebastiantellotrillo.com/resources/sebastians-way-of-setting-up-stata-folder-structure)
- **Better BibTeX** — [Auto-Export Docs](https://retorque.re/zotero-better-bibtex/exporting/auto/)
- **McCloskey** — *Economical Writing* (2nd ed., 2000). Principles distilled in [Writing Standard](#writing-standard).
- **Chicago Booth** — [Git When Collaborators Use Dropbox](https://handbook.booth.school/using-git-when-collaborators-use-dropbox)
- **Stata MCP Server** — [DeepEcon.ai](https://deepecon.ai/projects/stata-mcp) | [tmonk/mcp-stata](https://github.com/tmonk/mcp-stata)
