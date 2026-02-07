# AI Agent Instructions

Project root: /Users/jaredblack/Library/CloudStorage/Dropbox/Research-Project-Flow

## Session Start
At the start of every session, run /status silently to orient yourself. Tell the user what you found only if something needs attention.

## Rules
- `data/raw/` is READ-ONLY. Never modify.
- Read script headers before modifying any script (they document inputs/outputs/dependencies).
- Check `scripts/params.do` before using hardcoded values. Values must match the README Parameters table.
- If your action changes the project's I/O graph (which scripts exist, what they read, what they write, what paths are used), show the user what you plan to change and what it affects before doing it. For everything else, just do it.
- Never present uncertain results with confidence. Flag uncertainty.

## Key Files
- `scripts/00_run.do` — Master script. All path globals defined here.
- `scripts/params.do` — Research parameters. Must match README Parameters table.
- `run_all.sh` — Shell executor for pipeline steps.
- `README.md` — Pipeline overview, table/figure map, parameters, data documentation.
- `manuscript/aea_style_guide.md` — AEA formatting rules. Read before editing the manuscript.

## Execution
Run steps via: `./run_all.sh "<script_name>"`
All runs log to `output/logs/`. Read the log after every run.

## Writing
Active verbs, concrete language, plain words. See Writing Standard in README.
When editing the manuscript, follow `manuscript/aea_style_guide.md` for all formatting decisions.
