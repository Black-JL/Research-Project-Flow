# AI Agent Instructions

Project root: . (repository root)

## Session Start
At the start of every session:
1. Run /status silently to orient yourself.
2. Read the most recent file in `session_logs/` to understand what happened in the last session.
3. Check `TODO.md` (or the task list) for pending work.
4. Check `output/logs/` for the most recent execution log — confirm whether the last run succeeded or failed.
5. Tell the user what you found: current state, what completed since last session, pending items, blockers.

When a co-author opens with "where are we at?", "what's left?", "status?", or similar — this is your cue to run the full session-start protocol above. Don't wait to be asked for specifics; proactively walk them through the project state.

## Rules

### Raw Data Protection — ABSOLUTE
- `data/raw/` is **UNTOUCHABLE**. The ONLY permitted operation is reading.
- **NEVER** run `rm`, `erase`, `del`, `shell rm`, `!rm`, `unlink`, `save ... , replace`, or any write/delete/move/rename command targeting `data/raw/` or any path listed in the project's Protected Raw Data Inventory (see `data/raw/README.md`).
- If the project uses data on an external drive or restricted-access location, those files inherit the same absolute protection. The only permitted operation is `use` (read).
- If a script errors while raw data is loaded, do NOT attempt to "clean up" or "fix" the data file — just stop.
- **Why:** Raw data may be irreplaceable (restricted-use agreements, months-long procurement). Destroying it ends the project.

### DUA Compliance
- **Data Use Agreement (DUA) awareness:** If the project uses restricted-use data (HCUP, CMS, etc.), encounter-level or patient-level data must NEVER be saved to cloud-synced folders (Box, Dropbox, Google Drive). Only aggregated data may live in cloud storage. When writing any `save` command, verify the destination is DUA-compliant. If unsure, ask the user before saving.
- Read script headers before modifying any script (they document inputs/outputs/dependencies).
- Check `scripts/params.do` before using hardcoded values. Values must match the README Parameters table.
- **Break the glass.** If your action changes any of the following, STOP and warn the user before proceeding: the project's I/O graph (which scripts exist, what they read, what they write, what paths are used), the pipeline order in `00_run.do` or `run_all.sh`, research parameters in `params.do`, or the AI's own instructions in `CLAUDE.md`. Tell the user exactly what you plan to change and what it will affect downstream. Use language like: "This changes the pipeline — everything downstream of this step will be affected. Are you sure?" Do not proceed until the user confirms. For everything else, just do it.
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
- **Prevent sleep on long-running scripts:** When launching Stata, R, or Python in batch mode, attach `caffeinate -s -w <PID>` to the process so the Mac stays awake until the script finishes. Example: after launching Stata, run `caffeinate -s -w $(pgrep -f "stata-mp" | head -1) &`

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

Three layers govern all prose. See the full Writing Standard in README.md.

**Voice (Weitzman):** Let the structure of the problem make the argument. Make ignorance dangerous — show that what is unknown is where the stakes live. Name the mechanism that makes the evidence base misleading. Write to a decision-maker, not a spectator. Never say "this is important"; set up the logic so the reader arrives there.

**Clarity (McCloskey):** Active verbs, concrete language, plain words. Delete ruthlessly. End strong. No boilerplate.

**Formatting (AEA):** Follow `manuscript/aea_style_guide.md` for all typesetting, tables, figures, and citation decisions.

When in doubt: Weitzman decides *what* to say, McCloskey decides *how* to say it, AEA decides *how it looks on the page*.
