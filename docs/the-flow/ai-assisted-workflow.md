---
title: The AI-Assisted Workflow
layout: default
parent: The Flow
nav_order: 2
---

# The AI-Assisted Workflow

This chapter shows how a research session works in practice. Not theory — the actual sequence of actions when you sit down to work.

## Starting a session

Open Terminal, navigate to your project folder, and launch Claude Code:

```bash
cd ~/Dropbox/my-project
claude
```

The AI reads your `CLAUDE.md` file and runs `/status` automatically. It scans the project and reports anything that needs attention: stale logs, Dropbox conflicts, uncommitted changes. If everything is clean, it stays quiet.

You talk to the AI by typing in the terminal. It responds, reads files, writes code, and executes commands — all within your project directory.

## The core loop

Every research task follows the same pattern:

1. **You describe what you need.** Plain English. "Write a script that merges the treatment and control datasets on county FIPS codes." Be specific about inputs and outputs.

2. **The AI proposes a plan.** It reads your existing scripts, checks the pipeline table, and tells you what it intends to create or modify. If the change affects the project's structure (new scripts, new file paths), it asks for approval before proceeding.

3. **The AI writes the code.** It follows your project conventions: script headers, naming patterns, parameter references. It creates the script, updates the README pipeline table, and registers the step in `00_run.do` and `run_all.sh`.

4. **You run the script.** Either directly or through the AI:

    ```
    /run 05_merge
    ```

5. **The AI reads the log.** It checks for errors, warnings, and unexpected output. It reports what it finds.

6. **You review and iterate.** If the output is wrong, you describe the problem. The AI fixes the code and you run again.

## Example session

Here is what an actual session looks like. You type the lines after `>`. Everything else is the AI responding.

```
> I need to import the raw CDC WONDER data and clean it. The file
> is data/raw/cdc_wonder_2015_2022.txt. It's tab-delimited with
> a header row. I want to keep county FIPS, year, and death count.
> Drop any rows with "Unreliable" in the notes column.
```

The AI reads the raw file to understand its format. It writes `scripts/01_import_cdc.do` with a proper header, the import logic, and a save to `data/processed/cdc_clean.dta`. It updates the README pipeline table, adds the step to `00_run.do`, and registers it in `run_all.sh`.

```
> /run 01_import_cdc
```

The script runs. The AI reads the log and reports: "Imported 15,847 rows. Dropped 312 with 'Unreliable' flag. Saved 15,535 observations to `data/processed/cdc_clean.dta`."

You check the numbers. They make sense. You move on.

## Commands

The template includes built-in commands that handle common tasks:

| Command | What it does |
|:--------|:-------------|
| `/status` | Scans the project. Reports pipeline state, last run dates, conflicts, uncommitted work. |
| `/run` | Runs a pipeline step. Validates the script exists and logs the output. |
| `/run --all` | Runs the full pipeline from start to finish. |
| `/check` | Full integrity audit. Verifies scripts, data, params, and manuscript references all match. |
| `/add-step` | Scaffolds a new pipeline step. Creates the script, updates README, `00_run.do`, and `run_all.sh`. |
| `/git` | Stages, commits, and pushes all changes to GitHub. |
| `/handoff` | Writes a session summary to `session_logs/`. Useful when ending a work session or handing off to a co-author. |

## Working with data

{: .warning }
> **`data/raw/` is sacred** — Never modify raw data. The AI knows this rule (it's in `CLAUDE.md`). If you ask it to edit a file in `data/raw/`, it will refuse and explain why.

The typical data workflow:

1. Place raw data in `data/raw/` with a README documenting its source and access date.
2. Write import/cleaning scripts that read from `data/raw/` and save to `data/processed/`.
3. Write analysis scripts that read from `data/processed/` and save results to `output/`.

Each script has a structured header that documents its purpose, inputs, outputs, and dependencies. The AI writes these headers and reads them before modifying any script.

## Working with parameters

Research parameters — treatment dates, sample restrictions, outcome definitions — live in `scripts/params.do`. They also appear in the README's Parameters table. The two must match.

When you need to change a parameter:

```
> Change the sample start year from 2015 to 2016. Update params.do
> and the README.
```

The AI modifies both files and verifies consistency.

## Ending a session

When you are done working:

```
> /handoff
```

This writes a summary of what changed during the session: files modified, outputs regenerated, open questions. The summary is saved to `session_logs/` and is useful for:

- Picking up where you left off in a future session
- Briefing a co-author on recent changes
- Maintaining a record of project evolution

Then save your work:

```
> /git
```

This stages, commits, and pushes to GitHub.
