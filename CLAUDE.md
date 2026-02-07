# AI Agent Instructions

**Project root:** `/Users/jaredblack/Library/CloudStorage/Dropbox/Research-Project-Flow`

## Before Any Action

1. Confirm you are working in the correct directory.
2. Read `pipeline.md` before modifying any script or running any pipeline step.
3. Check `parameters.md` before using any hardcoded values.

## Folder Permissions

- **Read-only:** `data/raw/`, `legacy/`
- **Write allowed:** `data/processed/`, `output/`, `scratch/`, `session_logs/`
- **Write with caution:** `scripts/`, `manuscript/` (update `pipeline.md` and `table_figure_map.md` when changing these)

## Pipeline Reference

Always read `pipeline.md` before modifying any script. Every script's inputs, outputs, and dependencies are documented there.

## Parameters Reference

Check `parameters.md` for all critical research parameters. Never hardcode values that appear in `parameters.md` — use `params.do` instead.

## MCP Workflow

See `run_all.sh` for script execution. All executions must be logged to `output/logs/`, auditable, and pipeline-aware.

## Session Logging

After each working session, update `session_logs/` with a summary of work done, files modified, and next steps.

## Writing Standard

All prose follows McCloskey's *Economical Writing* principles: active verbs, concrete language, plain words, ruthless deletion. When reviewing manuscript text, flag violations by principle number.

## Guardrails

### Tier 1 — Always (before any action):
- Confirm correct working directory
- Confirm correct target files
- Read `pipeline.md` before modifying scripts
- Check `parameters.md` before using hardcoded values
- Never assume which file version is active — ask if ambiguous
- Never present uncertain results with confidence — flag uncertainty
- Never push to a remote repo without confirming the target

### Tier 2 — Structural changes (break the glass):
Any action that moves/renames/deletes files in `scripts/`, `data/`, or `output/`, or changes output paths, globals, pipeline steps, or manuscript references triggers:
1. Identify what breaks (read `pipeline.md` and `table_figure_map.md`)
2. Show the full impact
3. Propose the complete fix
4. Get explicit confirmation
