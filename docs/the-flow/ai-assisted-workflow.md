---
title: The AI-Assisted Workflow
layout: default
parent: The Flow
nav_order: 3
---

# The AI-Assisted Workflow

<img src="{{ site.baseurl }}/assets/images/real_scenario_5.png" alt="Pipeline execution illustration" class="page-illustration">

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

## How the AI runs your scripts

When you tell the AI to run a Stata do-file, an R script, or a Python script, it does not fire the command blindly. The template includes `run_all.sh`, a shell script that wraps every execution with structured logging and feedback.

Here is what happens when the AI runs a script:

1. You say "run Step 3" (or use the `/run` command).
2. The AI calls `./run_all.sh "Step_3_setup.do"`.
3. `run_all.sh` detects the file type (`.do` → Stata, `.R` → R, `.py` → Python) and launches the appropriate tool in batch mode.
4. All output is captured to a timestamped log in `output/logs/`.
5. The log opens automatically so you can see what happened.
6. The AI reads the same log, checks for errors and warnings, and reports what it finds.

You see the tool running. The AI sees the same output you do. This is how it can tell you "row 4,312 has a missing FIPS code" instead of just "the script ran."

### What this looks like with Stata

The `run_all.sh` script creates a wrapper do-file that sets up proper logging, runs your script, and saves the log to `output/logs/`. When the run completes, the log opens in your default text editor. If you are working in VS Code with the terminal on the left, you can watch the log appear in a new tab while the AI reads it and reports results in the terminal beside it.

The `CLAUDE.md` file enforces this workflow. The AI is instructed to always run scripts through `run_all.sh`, always read the log afterward, and never assume success without checking. If a script fails, the AI reads the error from the log and proposes a fix.

### Pipeline tracing

Before the AI modifies any script, it traces dependencies in both directions:

- **Upstream:** What data does this script read? What created that data?
- **Downstream:** What does this script produce? What consumes it — other scripts, tables, the manuscript?

This prevents the common problem of fixing one script and breaking another. The dependency chain is documented in the README pipeline table, and the AI checks it before making changes.

## The core loop

Every research task follows the same pattern:

1. **You describe what you need.** Plain English. "Write a script that merges the treatment and control datasets on county FIPS codes." Be specific about inputs and outputs.

2. **The AI proposes a plan.** It reads your existing scripts, checks the pipeline table, and tells you what it intends to create or modify. If the change affects the project's structure, the AI is required to stop and warn you before proceeding. See "Break the glass" below.

3. **The AI writes the code.** It follows your project conventions: script headers, naming patterns, parameter references. It creates the script, updates the README pipeline table, and registers the step in `00_run.do` and `run_all.sh`.

4. **You run the script.** Either directly or through the AI:

    ```
    /run 05_merge
    ```

5. **The AI reads the log.** It checks for errors, warnings, and unexpected output. It reports what it finds.

6. **You review and iterate.** If the output is wrong, you describe the problem. The AI fixes the code and you run again.

### Break the glass

The `CLAUDE.md` file includes a safety mechanism for high-impact changes. If you ask the AI to do anything that would alter:

- **The pipeline** — adding, removing, or reordering scripts; changing what a script reads or writes
- **Core parameters** — modifying `params.do` or the Parameters table in the README
- **The master scripts** — changing `00_run.do` or `run_all.sh`
- **The AI's own instructions** — editing `CLAUDE.md` itself

...the AI will stop and warn you before doing it. It will tell you exactly what it plans to change and what will be affected downstream. It will not proceed until you confirm.

This exists because pipeline changes cascade. If you rename a data file that three scripts depend on, those scripts will break. If you change a parameter that feeds into your estimation, every table and figure downstream may need to be regenerated. The AI knows this and will flag it.

For routine work — writing a new script, editing prose, fixing a bug, generating a table — the AI just does it. The warning only fires when the change touches something structural.

### Long tasks and sub-agents

Some tasks — rebuilding an entire pipeline, reorganizing a messy project, processing a dozen scripts — take longer than a single conversation. AI tools have a finite context window, and a sprawling session can lose focus.

When you have a large task, you can ask the AI to break it into pieces and spawn separate agents for each one. For example: *"I need to clean and standardize all six raw data files. Spin up an agent for each one."* The AI will launch parallel sub-tasks that work independently and report back. You stay in the main session, reviewing results as they come in.

This is not something you need to learn the mechanics of right now — the tools handle the details. Just know the capability exists. When a task feels too big for one session, tell the AI to decompose it.

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
| `/init` | Initializes a new `CLAUDE.md` in the current directory. Use for non-template projects. |
| `/status` | Scans the project. Reports pipeline state, last run dates, conflicts, uncommitted work. |
| `/run` | Runs a pipeline step. Validates the script exists and logs the output. |
| `/run --all` | Runs the full pipeline from start to finish. |
| `/check` | Full integrity audit. Verifies scripts, data, params, and manuscript references all match. |
| `/add-step` | Scaffolds a new pipeline step. Creates the script, updates README, `00_run.do`, and `run_all.sh`. |
| `/git` | Stages, commits, and pushes all changes to GitHub. |
| `/handoff` | Writes a session summary to `session_logs/`. Useful when ending a work session or handing off to a co-author. |

## Working with data

### Protect your raw data from the AI

{: .important }
> **If you have proprietary, restricted-use, or individually identifiable data, the AI should never see it.**

This matters more than anything else in this guide. If your data is covered by a data use agreement (DUA), HIPAA, or any other access restriction, you must do your data cleaning, de-identification, and aggregation **before** the AI has access to any of it. That means:

1. **Write your data cleaning and collapsing code offline.** The AI can help you write the code — describe what you need, let it draft the script — but you run that code yourself, outside of the AI session, on your own machine. Do not give the AI a path to read the raw files.

2. **Only give the AI access to aggregated or de-identified data.** Once your data is collapsed to the level where it is safe — no individual records, no identifiers, within the bounds of your DUA — then you can let the AI read it, work with it, and help you analyze it.

3. **Consider physical separation.** One approach: keep your raw disaggregated data on an external drive. Do not even have the drive plugged in while working with the AI. This makes it impossible for the AI to access raw data, even accidentally.

The template's `data/raw/` folder is marked read-only in `CLAUDE.md`, and the AI is instructed never to modify it. But "read-only" still means the AI can read the files if they are on a connected drive. For truly sensitive data, physical separation is the safest approach.

{: .warning }
> **`data/raw/` is sacred** — Never modify raw data. The AI knows this rule (it's in `CLAUDE.md`). If you ask it to edit a file in `data/raw/`, it will refuse and explain why.

### The typical data workflow

1. Place raw data in `data/raw/` with a README documenting its source and access date.
2. Write import/cleaning scripts that read from `data/raw/` and save to `data/processed/`. If your raw data is restricted, **run these scripts yourself offline** — not through the AI.
3. Once your processed data is safe for the AI to see, write analysis scripts that read from `data/processed/` and save results to `output/`. The AI can run these.

Each script has a structured header that documents its purpose, inputs, outputs, and dependencies. The AI writes these headers and reads them before modifying any script.

## Working with parameters

Research parameters — treatment dates, sample restrictions, outcome definitions — live in `scripts/params.do`. They also appear in the README's Parameters table. The two must match.

When you need to change a parameter:

```
> Change the sample start year from 2015 to 2016. Update params.do
> and the README.
```

The AI modifies both files and verifies consistency.

## Git is your undo button

If you have never let software modify your research files before, this is the most important thing to understand: **every change the AI makes is reversible.**

When the AI edits a script, creates a file, or modifies your README, that change exists in your file system — visible, inspectable, and undoable. If you are using Git (Path A), you have a complete history of every change and can undo any of them:

```bash
git diff                       # see what changed
git checkout -- scripts/05_merge.do   # revert one file
git stash                      # undo all uncommitted changes (keeps them saved)
```

This is why the workflow uses `/git` to commit after each working session. Each commit is a snapshot. If something goes wrong three sessions later, you can go back to any previous snapshot.

Even if you are not using Git (Path B), the AI is working on files in your Dropbox folder. Dropbox keeps version history. You can restore any file to a previous version through the Dropbox website.

The point: **you are not handing control to the AI.** You are letting it make changes that you can see, review, and reverse. The worst case is not "the AI destroyed my project." The worst case is "the AI made a change I don't like, and I reverted it." That should take about five seconds.

## Session hygiene

AI sessions degrade over time. The longer a session runs, the more context the AI accumulates, and eventually it starts losing track of earlier decisions, repeating itself, or making mistakes it would not have made at the start. This is a property of how context windows work, and it affects every AI tool.

**Keep sessions focused.** One task per session is ideal. "Reorganize the pipeline" is a session. "Write the estimation code" is a different session. Do not try to do both in one sitting — the quality of the second task will suffer because the AI's context is full of the first.

**Watch for signs the session is going sideways:**
- The AI proposes changes you already discussed and rejected
- It forgets file names or paths it was using earlier
- It starts writing code that contradicts its own earlier output
- Responses get slower or more generic

When you see these signs, wrap up. Run `/handoff` to save the session state, then quit and start fresh. The new session will read `CLAUDE.md` and the session log, and pick up where you left off — but with a clean context window.

**Use `/handoff` liberally.** Even if you are not done for the day, a handoff captures what happened so the next session (or the next day) starts with a clear summary instead of a vague memory. Think of it as saving your game.

**Commit before and after.** Run `/git` at the start of a session (to capture the baseline) and at the end (to capture your work). If a session goes badly, you can revert to the start-of-session commit and try again.

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
