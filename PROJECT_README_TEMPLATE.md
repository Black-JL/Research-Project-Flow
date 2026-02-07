# [Project Name]

**Canonical location:** `/Users/jaredblack/Library/CloudStorage/Dropbox/Research-Project-Flow`

## Overview

[Brief description of the research project, research question, and approach.]

## Data Availability Statement

[Describe data sources, access requirements, and any restrictions. Follow AEA Template README format.]

## Software Requirements

- **Stata** (version XX or later)
- **R** (version X.X or later)
- **LaTeX** (for manuscript compilation)
- **Zotero** with Better BibTeX (for citation management)

## Replication Instructions

1. Clone this repository or sync via Dropbox.
2. Open `scripts/00_run.do` and set your machine path.
3. Run `./run_all.sh --all` to execute the full pipeline.
4. Compile `manuscript/manuscript.tex` to produce the paper.

## Available Commands

| Command | What it does |
|---------|-------------|
| `/run-step` | Run a pipeline step with input/output validation |
| `/validate` | Check pipeline integrity — missing files, misplaced scripts, parameter drift |
| `/audit` | Audit manuscript figures/tables against source scripts and `table_figure_map.md` |
| `/status` | Show project status — last runs, recent logs, pipeline progress |
| `/log` | Update today's session log |
| `/handoff` | Prepare a plain-language co-author summary |

## Project Structure

See `pipeline.md` for the step-by-step execution order and file dependencies.
See `parameters.md` for all critical research parameters.
See `table_figure_map.md` for the mapping between manuscript outputs and source scripts.
