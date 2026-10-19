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

## Rigor & Audit Standards

These standards make every analytical step auditable and stop code from drifting away from the results it produced. Adapted from the Data Analyst Augmentation Framework (DAAF, LGPL-3.0).

### 1. Dual-layer validation — every transformation gets a validation, no exceptions

**Layer 1 — in-script assertions at named checkpoints.** As data moves through a script, assert what must be true, and comment each checkpoint so a reader can find it:
- **CP1 (post-load):** row/column counts, key uniqueness, expected date range.
- **CP2 (post-merge / post-clean):** merge match rates, no unexpected missingness, no duplicate keys introduced.
- **CP3 (post-transform):** derived variables in valid ranges, no rows dropped unintentionally.
- **CP4 (pre-save / pre-estimate):** final N matches the analysis plan; no rows lost since CP3 without an explicit, commented `drop`.

```stata
* --- CP2 (post-merge): every treatment row must find a covariate row ---
merge m:1 fips year using "$processed/acs.dta"
assert _merge == 3 if treat == 1
count
assert r(N) == 412903   // expected analysis N; change only with a logged reason
```
R: `stopifnot(...)`. Python: `assert ...`.

**Detecting a failed checkpoint (Stata).** Stata's `-b` batch mode exits 0 even when a do-file errors with `r(<n>)`, so a failed `assert` cannot be detected from the shell exit code — `run_all.sh` will report success. Always confirm a Stata run by scanning its log in `output/logs/` for `r(` / `--Break--` / your own failure marker, not by trusting the exit status. (R `stopifnot` and Python `assert` do set nonzero exit codes, so the exit code is reliable for those.)

**Layer 2 — adversarial methodology review.** Layer 1 catches code that ran *wrong*. Layer 2 catches code that ran *fine but is methodologically wrong*. Run `/review` before accepting any change to estimation or sample-construction logic.

### 2. Inline Audit Trail (IAT)

Every line that changes which rows or columns enter the analysis carries three comments — what it does, why, and what it assumes. Applies to every sample restriction, merge, collapse/aggregate, and derived analysis variable. A bare `keep if` is a silent identifying assumption; name it.

```stata
* INTENT:    Keep first encounter per patient.
* REASONING: Survival origin is the first observed encounter; later visits are outcomes, not entries.
* ASSUMES:   visit_seq == 1 reliably flags the first encounter (verified at CP1).
keep if visit_seq == 1
```
R/Python: same three tags as `#` comments.

### 3. Immutable execution record — code and its output never drift apart

- **Logs are append-only.** `run_all.sh` writes a timestamped log per run to `output/logs/`. Never delete or overwrite a log, including failed runs — it is the permanent record of what the code did.
- **Don't edit a script that produced a manuscript output — version it.** Once a script has generated a figure/table the manuscript uses, a change to its *specification* creates a new lettered copy (`10_estimate.do` → `10a_estimate.do`), per the script-numbering convention. The old script and its log stay, so any output traces to the exact code that made it.
- **Provenance.** The run that produced an output is the most recent successful log for that script in `output/logs/`. Don't rename outputs out from under their logs.

## Session Logging

At the end of each session (or when asked for `/handoff`), write a session log to `session_logs/`:
- **File naming:** `YYYY-MM-DD_<brief-topic>.md`
- **One log per day** — append if a log already exists for today
- **Required sections:** Summary, Tasks Completed, Files Created/Modified, Commands Run, Errors/Blockers, Pending Steps

## Writing

**All prose goes through the `write` skill** (`.claude/skills/write/`). That covers manuscript paragraphs and sections, abstracts, write-ups of findings, and proposal text. Use it whenever the user asks for prose, even if they don't name it. When the user hands back an edited version of a draft, run the skill's Learn step. See the Writing Standard in README.md.

Voice skill: (set per author, e.g. `jared-voice`; it lives in `~/.claude/skills/`, outside this public repo)

Four layers, each with a distinct job:

- **Structure (outline + PEER):** one claim per paragraph, approved as an outline before drafting. Each paragraph is built as Point, Evidence, Explain, Repeat/link.
- **Voice (the author's voice skill):** how it sounds. The author's samples and edit ledger, not a famous writer's.
- **Guidelines (McCloskey + Orwell):** what to cut and what to replace. Active verbs, concrete and plain words, no boilerplate, no worn phrases. See `.claude/skills/write/references/`.
- **Formatting (AEA):** follow `manuscript/aea_style_guide.md` for typesetting, tables, figures, and citations.

**Style modes** (e.g. Weitzman) are optional and chosen per piece: suggest one, and let the author pick. A style mode borrows a writer's *moves for clarity and urgency*, never their *arguments* or framing.

When in doubt: the outline decides *what* to say, the voice decides *how it sounds*, the guidelines decide *what to cut*, and AEA decides *how it looks on the page*.
