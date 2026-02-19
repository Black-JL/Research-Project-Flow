---
title: The AI-Assisted Workflow
layout: default
parent: The Flow
nav_order: 2
---

# The AI-Assisted Workflow

This chapter shows how a research session works in practice. Not theory — the actual sequence of actions when you sit down to work.

## Your workspace

You can work in a plain terminal window — navigate to your project folder, type `claude`, and go. That works fine. But a better setup is to use **VS Code** or **Cursor** (they work almost identically) so you can see everything at once.

### Recommended layout

1. Open VS Code (or Cursor).
2. **File → Open Folder** and select your project folder.
3. Press <kbd>Ctrl</kbd> + <kbd>`</kbd> (backtick) to open the integrated terminal.
4. *(Optional)* Move the terminal panel to the side: press <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> (macOS) or <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> (Windows/Linux), type `View: Move Panel Left`, and hit Enter.

Now you have:

- **Left panel:** Terminal running Claude Code (or your AI tool of choice)
- **Center/right:** Your script or manuscript file open for editing
- **Additional tabs:** A compiled PDF preview, data files, logs — whatever you need

Everything in one window. You talk to the AI on the left, watch the code change in the center, and preview your compiled manuscript on the right.

### Alternatives

- **Terminal only.** Open a terminal, `cd` to your project, type `claude`. Open a separate file browser and your PDF viewer alongside it.
- **VS Code / Cursor extensions.** Both editors offer Claude and Codex extensions that embed the AI directly in the editor sidebar. These work well for code editing. The terminal approach (typing `claude` in the integrated terminal) gives you the full Claude Code experience with slash commands and project management.

Use whatever feels comfortable. The workflow is the same either way.

## Starting a session

In your terminal (standalone or inside VS Code), navigate to your project and launch:

```bash
cd ~/Dropbox/my-project
claude
```

The AI reads your `CLAUDE.md` file and runs `/status` automatically. It scans the project and reports anything that needs attention: stale logs, Dropbox conflicts, uncommitted changes. If everything is clean, it stays quiet.

You talk to the AI by typing — or speaking, if you set up SuperWhisper — in the terminal. It responds, reads files, writes code, and executes commands, all within your project directory.

## How the AI runs your scripts (MCP servers)

When you tell the AI to run a Stata do-file, an R script, or a Python script, it does not just fire the command blindly. The template uses **MCP (Model Context Protocol) servers** — lightweight connectors that let the AI interact with external tools like Stata, R, and Python in a structured way.

Here is what happens when the AI runs a script:

1. The AI sends the run command through the MCP server for that tool (e.g., Stata).
2. The tool opens, executes the script, and produces output.
3. The MCP server captures the log output and passes it back to the AI.
4. The AI reads the log, checks for errors and warnings, and reports what it finds.

You see the tool running in real time. The AI sees the same output you do. This is how it can tell you "row 4,312 has a missing FIPS code" instead of just "the script ran."

{: .note }
> **Setting up MCP servers** — MCP configuration is project-specific and depends on which statistical tools you use. When you start a project from the template, ask the AI to help you configure MCP servers for your tools. It will set up the `.claude/` configuration files.

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
