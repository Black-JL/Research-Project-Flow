---
title: Commands Cheatsheet
layout: default
parent: Reference
nav_order: 1
---

# Commands Cheatsheet

Quick reference for every command available in the Research Project Flow template.

---

## Project commands

These commands work inside any project built from the template.

### `/status`

Scans the project and reports its current state.

```
> /status
```

**Shows:** pipeline steps and last run dates, uncommitted changes, Dropbox conflicts, stale logs, scratch files.

**When to use:** Start of every session. The AI runs this automatically when you launch Claude Code in a project with `CLAUDE.md`.

---

### `/run`

Executes a pipeline step with logging and validation.

```
> /run                    # prompts for which step
> /run 05_merge           # runs a specific step
> /run --all              # runs the full pipeline
> /run --from 05          # runs from step 05 forward
```

**What it does:**

1. Validates the script exists
2. Executes it via `run_all.sh`
3. Captures the log to `output/logs/`
4. Reads the log and reports results

---

### `/check`

Full integrity audit of the project.

```
> /check
```

**Verifies:**

- Every script in the pipeline table exists and has a valid header
- Script inputs/outputs match the pipeline table in the README
- `params.do` values match the README Parameters table
- Referenced data files exist
- Manuscript `\input` references point to existing files
- Table/figure map matches actual output files

---

### `/add-step`

Scaffolds a new pipeline step end-to-end.

```
> /add-step
```

**Prompts for:** step number, language (Stata/R/Python), description, inputs, outputs.

**Creates:**

- The script file with a structured header
- An entry in the README pipeline table
- A registration in `00_run.do`
- A registration in `run_all.sh`

---

### `/handoff`

Writes a session summary for future reference or co-author communication.

```
> /handoff
```

**Produces:** a markdown file in `session_logs/` with:

- Files created or modified
- Outputs regenerated
- Open questions or next steps
- Git status at time of handoff

---

### `/git`

Stages, commits, and pushes all changes.

```
> /git
```

**What it does:**

1. Stages all tracked and new files
2. Writes a descriptive commit message based on changes
3. Commits
4. Pushes to the remote

No confirmation prompt — it runs immediately. Use when your project is in a clean, working state.

---

## Terminal commands

These are standard terminal commands you will use alongside Claude Code.

| Command | Purpose |
|:--------|:--------|
| `claude` | Launch Claude Code in the current directory |
| `cd ~/Dropbox/my-project` | Navigate to your project |
| `git status` | Check for uncommitted changes |
| `git log --oneline -10` | View recent commits |
| `./run_all.sh "script_name"` | Run a pipeline step directly |
| `./run_all.sh --all` | Run the full pipeline directly |

---

## Keyboard shortcuts in Claude Code

| Shortcut | Action |
|:---------|:-------|
| `Enter` | Send message |
| `Esc` | Cancel current operation |
| `Ctrl+C` | Exit Claude Code |
| `Up arrow` | Scroll through message history |
