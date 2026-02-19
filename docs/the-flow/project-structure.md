---
title: Project Structure
layout: default
parent: The Flow
nav_order: 1
---

# Project Structure

<img src="{{ site.baseurl }}/assets/images/real_scenario_1.png" alt="Project setup illustration" class="page-illustration">

## Clone the template

Open Terminal, navigate to where you want the project, and clone:

```bash
gh repo create my-project --template Black-JL/Research-Project-Flow --private --clone
cd my-project
```

This creates a private repo on your GitHub account with the full template structure. You now have a project folder that looks like this:

```
my-project/
├── README.md                  ← Project overview, pipeline, replication
├── CLAUDE.md                  ← AI agent instructions
├── run_all.sh                 ← Master execution script
├── .gitignore
│
├── data/
│   ├── raw/                   ← Untouched source data. NEVER modify.
│   │   └── README.md          ← Source, date, access instructions
│   └── processed/             ← Created by scripts
│
├── scripts/
│   ├── 00_run.do              ← Master do-file: globals and pipeline
│   ├── params.do              ← Research parameters
│   └── programs/              ← Reusable helper functions
│
├── output/
│   ├── logs/                  ← Execution logs
│   ├── figures/               ← Plots and maps
│   ├── tables/                ← LaTeX table fragments
│   └── results/               ← Stored estimation results
│
├── manuscript/
│   ├── manuscript.tex         ← Active manuscript
│   ├── references.bib         ← Auto-exported from Zotero
│   └── aea_style_guide.md     ← Formatting reference
│
└── scratch/                   ← Throwaway work. Not committed.
```

## Why this structure

Six principles govern the layout:

1. **Every file has one home.** Outputs in `output/`, data in `data/`, scripts in `scripts/`. No duplicates, no ambiguity.
2. **Data scripts write to `data/processed/`. Analysis scripts write to `output/`.** No script crosses this boundary.
3. **Absolute paths live in one place.** Machine-specific paths go in `00_run.do`. Everything else uses globals defined there.
4. **One command reproduces everything.** `run_all.sh` executes the full pipeline from raw data to final output.
5. **Fail loudly.** Every script logs its execution. When something breaks, the log shows where and why.
6. **Structure enforces discipline.** If a file doesn't have an obvious home, the structure needs updating — not the file.

These are not arbitrary conventions. They come from Gentzkow & Shapiro, the TIER Protocol, and the AEA Data Editor's requirements. Following them means your project is replication-ready from day one.

## Key files

### `README.md`

The project README is the single source of truth. It contains:

- The pipeline table (every script, its inputs, its outputs)
- The parameters table (every hardcoded research value and its source)
- The table/figure map (which script produces which output)
- Replication instructions

When the AI adds a script or modifies an output, it updates the README automatically. You should verify these updates are correct.

### `CLAUDE.md`

This file tells the AI how to behave in your project. It specifies:

- The project root path
- Rules (e.g., `data/raw/` is read-only)
- Key file locations
- How to execute scripts
- Writing standards

The AI reads this file at the start of every session. It is the contract between you and the AI. Edit it when you want to change the AI's behavior. If you are starting a project without the template, you can create a fresh `CLAUDE.md` by typing `/init` in Claude Code.

{: .note }
> **Other tools have their own equivalents.** Codex uses `AGENTS.md`. Gemini CLI uses `GEMINI.md`. The content is the same idea — project instructions the AI reads at startup. If you use multiple tools on the same project, create the appropriate file for each. The template ships with `CLAUDE.md`; adapt it for your tool of choice.

### `scripts/00_run.do`

The master do-file. It defines path globals for every collaborator's machine and calls each pipeline step in order. When you or the AI add a new script, it gets registered here.

### `scripts/params.do`

All hardcoded research parameters — treatment dates, sample restrictions, outcome definitions. Centralizing them here means a parameter change propagates everywhere automatically. The values must match the Parameters table in the README.

### `run_all.sh`

The shell script that executes the pipeline. It calls Stata, R, and Python scripts in sequence, captures logs, and reports success or failure. Run a single step:

```bash
./run_all.sh "01_import"
```

Run everything:

```bash
./run_all.sh --all
```

## First steps after cloning

1. **Set your machine path** in `scripts/00_run.do`. Replace the placeholder path with your actual project directory.

2. **Edit the README.** Replace placeholder content with your project details: data sources, computational requirements, parameters.

3. **Configure CLAUDE.md.** Update the project root path. Review the rules and adjust if needed.

4. **Set up `.gitignore`.** The template includes sensible defaults. Add any large data files or sensitive content.

5. **If using Dropbox:** Move the project folder into Dropbox and exclude `.git`:

```bash
xattr -w com.dropbox.ignored 1 .git
```

6. **Launch Claude Code** and start your first session:

```bash
claude
```

The AI will read your `CLAUDE.md`, orient itself, and tell you if anything needs attention. You're ready to work.
