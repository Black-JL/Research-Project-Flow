# AI Agent Instructions

Project root: . (repository root)

## Session Start
At the start of every session, run /status silently to orient yourself. Tell the user what you found only if something needs attention.

## Rules
- `data/raw/` is READ-ONLY. Never modify. Never read files in `data/raw/` unless the user explicitly confirms it is safe to do so (the data may be restricted-use or individually identifiable).
- Read script headers before modifying any script (they document inputs/outputs/dependencies).
- Check `scripts/params.do` before using hardcoded values. Values must match the README Parameters table.
- If your action changes the project's I/O graph (which scripts exist, what they read, what they write, what paths are used), show the user what you plan to change and what it affects before doing it. For everything else, just do it.
- Never present uncertain results with confidence. Flag uncertainty.

## Key Files
- `scripts/00_run.do` — Master script. All path globals defined here.
- `scripts/params.do` — Research parameters. Must match README Parameters table.
- `run_all.sh` — Shell executor for pipeline steps. All script execution goes through this.
- `watch_logs.sh` — Opens a terminal to tail log files in real-time.
- `pipeline.md` — Master pipeline document: step order, file dependencies, manuscript figure manifest.
- `MCP_WORKFLOW.md` — Detailed documentation of the MCP execution workflow and guardrails.
- `README.md` — Pipeline overview, table/figure map, parameters, data documentation.
- `manuscript/aea_style_guide.md` — AEA formatting rules. Read before editing the manuscript.

## Execution — MCP Workflow

Use `./run_all.sh "<script_name>"` for ALL script execution. This is mandatory.

The script automatically:
1. Runs the script in batch mode (Stata, R, or Python — detected by file extension)
2. Saves the log to `output/logs/` with a timestamp
3. Opens the log for review when complete

**ALWAYS:**
- Run scripts through `run_all.sh`, never by calling Stata/R/Python directly
- Read the log after every run — check for errors, warnings, unexpected output
- Report what the log shows to the user

**NEVER:**
- Leave log files in `scripts/` (they belong in `output/logs/`)
- Skip reading the log after execution
- Assume a script succeeded without checking the log

### Pipeline tracing

Before modifying any script, trace its dependencies in both directions:
- **Upstream:** What data files does this script read? What scripts created those files?
- **Downstream:** What files does this script produce? What scripts or manuscript sections consume them?

Check the pipeline table in the README to verify the chain. If your change affects upstream or downstream dependencies, tell the user before proceeding.

## Session Logging

At the end of each session (or when asked for `/handoff`), write a session log to `session_logs/`:
- **File naming:** `YYYY-MM-DD_<brief-topic>.md`
- **One log per day** — append if a log already exists for today
- **Required sections:** Summary, Tasks Completed, Files Created/Modified, Commands Run, Errors/Blockers, Pending Steps

## Writing
Active verbs, concrete language, plain words. See Writing Standard in README.
When editing the manuscript, follow `manuscript/aea_style_guide.md` for all formatting decisions.
