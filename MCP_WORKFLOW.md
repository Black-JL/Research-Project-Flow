# MCP + AI Coding Tool Workflow

This document explains how this project uses AI coding tools (Claude Code, Gemini CLI, Codex, etc.) with MCP (Model Context Protocol) for AI-assisted script execution. For a quick overview, see the main [README.md](README.md).

---

## What is MCP?

MCP (Model Context Protocol) is an open protocol that allows AI assistants to interact with external tools and services in a controlled, auditable way.

In this project, MCP enables the AI to:

1. **Execute scripts** (Stata, R, Python) via the command line
2. **Read and parse log files** to diagnose errors
3. **Iteratively debug** failing scripts
4. **Document changes** in human-readable session logs

Think of it as giving the AI "hands" to run your statistical software and "eyes" to read the results — but with strict guardrails on what it can and cannot do.

---

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                     AI Coding Tool (e.g. Claude Code)           │
│  - Reads scripts and understands syntax                        │
│  - Plans execution strategy                                     │
│  - Diagnoses errors from logs                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     MCP / Bash Interface                        │
│  Command: ./run_all.sh "script_name.do"                        │
│  - Detects file type (.do → Stata, .R → R, .py → Python)      │
│  - Executes in batch mode (no GUI)                             │
│  - Captures exit codes (0 = success, nonzero = failure)        │
│  - Writes timestamped logs to output/logs/                     │
│  - Opens log for review when complete                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Statistical Software                          │
│  Stata, R, or Python                                           │
│  - Runs scripts                                                │
│  - Writes text logs                                            │
│  - Returns exit codes                                          │
└─────────────────────────────────────────────────────────────────┘
```

### Execution Flow

1. You request the AI run an analysis or fix an error
2. The AI reads the relevant script(s) to understand them
3. The AI executes via `./run_all.sh "script_name.do"`
4. The software runs in batch mode, writing output to a log file
5. The AI reads the log file to check for success or errors
6. If errors: the AI diagnoses, edits the script, re-runs
7. All changes documented in session logs

---

## Why MCP Guardrails Matter

You might ask: why not just let an AI directly control your statistical software however it wants? The MCP architecture provides critical guardrails that make AI-assisted research **safe, reproducible, and auditable**.

### The Problem with Unconstrained AI Access

An AI with unrestricted access to your statistical software could:
- Silently modify estimation code without documentation
- Overwrite source data files
- Delete files to "clean up" without asking
- Run commands interactively with no log trail
- Make changes that look correct but subtly alter results
- Lose track of what it changed across a long session

For academic research, this is unacceptable. You need to be able to explain and defend every analytical decision to reviewers, co-authors, and yourself.

### How MCP Provides Guardrails

| Risk | MCP Guardrail |
|------|---------------|
| **Silent changes** | All file edits are logged in session notes; the AI must document what it changed and why |
| **Data destruction** | `data/raw/` is READ-ONLY; the AI cannot modify original data |
| **Untraceable execution** | Scripts run in batch mode writing complete logs to `output/logs/`; every command and its output is recorded |
| **Hidden state** | No interactive sessions; everything runs from documented scripts |
| **Scope creep** | `CLAUDE.md` explicitly prohibits changing statistical logic without permission |
| **Lost work** | Failed run logs are preserved, not deleted; you can always see what went wrong |
| **Unverifiable results** | Exit codes provide programmatic success/failure detection; the AI cannot claim success if the software errored |

### The Audit Trail

Every MCP-mediated session produces:

1. **Session logs** (`session_logs/YYYY-MM-DD_*.md`) — Human-readable narrative of what the AI attempted, what worked, what failed, and what changed

2. **Execution logs** (`output/logs/*.log`) — Complete output including every command executed and its results

3. **Git-trackable changes** — All edits happen to files in the project folder, visible in version control

This means a co-author (or reviewer, or future-you) can:
- See exactly what the AI did on any given date
- Verify that the software actually produced the reported results
- Understand why changes were made
- Revert anything problematic
- Reproduce the entire analysis independently

### Research Integrity

The MCP workflow treats AI assistance like a research assistant who must:
- Keep a lab notebook (session logs)
- Never touch the original data (read-only sources)
- Document every procedure (execution logs)
- Get permission before changing methods (operating instructions)

This is not about distrusting AI — it is about maintaining the same standards of transparency and reproducibility you would expect from any collaborator.

---

## Operating Instructions

These instructions govern how the AI operates on this project. They are enforced in `CLAUDE.md`.

### ALWAYS DO

1. **Run scripts through `run_all.sh`** — Never call Stata, R, or Python directly.
2. **Read the log after every run** — Diagnose issues from logs, not from guessing.
3. **Update session logs** — Every working session must create or update a dated file in `session_logs/`.
4. **Document before modifying** — Read and understand a script before editing it.
5. **Preserve statistical logic** — Only make structural changes (paths, logging, headers) unless explicitly asked to modify estimation code.

### NEVER DO

1. **Never modify `data/raw/`** — Raw data is read-only. If the data is restricted-use, do not read it without explicit permission.
2. **Never run scripts outside `run_all.sh`** — All execution goes through the wrapper so logs are captured.
3. **Never make silent changes** — Every modification must be documented in session logs.
4. **Never delete logs** — Failed run logs are kept for diagnosis.
5. **Never change statistical/identification logic** without explicit permission.

---

## Watching Scripts in Real-Time

Because scripts run in batch mode, there is no GUI window to watch. The template includes `watch_logs.sh` to monitor output in real-time.

### Usage

```bash
./watch_logs.sh                    # Watch all logs in output/logs/
./watch_logs.sh --latest           # Watch the most recently modified log
./watch_logs.sh output/logs/step9.log  # Watch a specific log file
```

This opens a new terminal window that continuously reads ("tails") the log files as they are written. You see every command and result as the software processes them.

### Manual Alternative

Open a terminal and run:

```bash
tail -f output/logs/*.log
```

Leave this terminal open while working. You will see all output scroll by as scripts run.

---

## For Co-Authors

If you see changes in the codebase that you do not understand:

1. Check `session_logs/` for the relevant date
2. The session log explains what the AI did and why
3. Check `output/logs/` for the actual execution output
4. All changes are in tracked files — use `git diff` to see what changed

If you have concerns about any AI-assisted changes, the audit trail makes it straightforward to review, understand, or revert them.
