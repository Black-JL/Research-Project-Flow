---
title: Your First Session
layout: default
parent: The Flow
nav_order: 2
---

# Your First Session

You have the tools installed. You have the template cloned. You are staring at a terminal. Now what?

This chapter walks through what actually happens when you launch an AI coding tool in your project for the first time — and how to use it to rescue a stalled project.

## The first 30 minutes

Open your terminal. Navigate to your project folder. Type `claude` (or `gemini`, or `codex`) and press Enter.

Here is what happens:

```
$ cd ~/Dropbox/my-project
$ claude

> Claude Code is reading your project...
> Found CLAUDE.md. Loading project instructions.
```

The AI reads your `CLAUDE.md` and silently runs `/status` to orient itself. If everything is clean, it says nothing. If something needs attention — uncommitted changes, missing files, stale logs — it tells you.

Now you are in a conversation. The AI can see your files. You can see your files. Everything it does happens in the folder in front of you.

**Your first message should be simple.** Try:

```
> Look at my project and tell me what you see. What's here,
> what's missing, and what needs attention?
```

The AI will scan your folder structure, read your scripts, check your README, and give you a status report. It might say: "You have 6 scripts in `scripts/` but none of them are registered in the pipeline table. Your `data/raw/` folder has 3 CSV files but no README documenting their source."

That is your starting point. You now know what the AI sees, and you can start giving it tasks.

**A few things to try in your first session:**

- *"Read `scripts/05_merge.do` and explain what it does."* — Test whether the AI understands your code.
- *"Create a README for `data/raw/` documenting the three CSV files in there."* — Low-risk, high-value. You can see exactly what it writes.
- *"Run `/check` and show me everything that's inconsistent."* — Let the AI audit the project so you can see where the gaps are.

Do not try to rebuild your entire pipeline in the first session. Get comfortable with the conversation. Watch how the AI reads files, proposes changes, and asks for confirmation. Build trust gradually.

## Rescuing a messy project

This is the core use case. You have a folder — maybe several folders — with scattered scripts, old data files, half-finished analysis, and a manuscript that references outputs you cannot reproduce. Here is how to turn that into an organized project.

### Step 1: Drop everything into the template

Clone the template (or download the zip). Copy your existing files into it:

- Data files → `data/raw/`
- Scripts → `scripts/` (keep their original names for now)
- Output files → `output/figures/`, `output/tables/`, or `output/results/`
- Manuscript → `manuscript/`
- Everything else → `scratch/`

Do not worry about getting it perfect. The point is to get everything into the structure so the AI can see it.

### Step 2: Tell the AI what you have

```
> I just dropped my existing project files into this template.
> Here's what I have:
> - 6 Stata do-files in scripts/. They were written at different
>   times and I'm not sure of the correct run order.
> - 3 CSV files in data/raw/ from CDC WONDER.
> - A half-finished manuscript in manuscript/.
> - Some old figures in output/figures/ that may or may not match
>   the current code.
>
> Please read through the scripts, figure out the dependency
> order, and tell me what you find.
```

The AI will read every script, trace what each one reads and writes, and map the dependencies. It will come back with something like: "Here is the order I think these run in, based on inputs and outputs. Script 03 reads a file that script 01 produces. Script 06 references a variable that doesn't exist in any upstream data — this may be a bug or a missing step."

### Step 3: Let the AI build the pipeline

Once you agree on the order:

```
> That looks right. Please:
> 1. Rename the scripts to follow the numbering convention
>    (01, 05, 10, etc.)
> 2. Add structured headers to each one
> 3. Register them in the README pipeline table
> 4. Set them up in 00_run.do and run_all.sh
```

The AI does the mechanical work. You review the result. In one session, your scattered folder becomes a documented, reproducible pipeline.

### Step 4: Test it

```
> /run --all
```

Run the full pipeline. The AI reads the logs and reports what succeeded and what failed. Fix the failures. Run again. Repeat until everything is clean.

This process — drop, describe, organize, test — can take a single long session or a few shorter ones depending on how messy the project is. The point is that you supply the knowledge of what each piece does, and the AI handles the reorganization.

## How to talk to the AI

If you have only used AI through a chat interface, you are probably used to writing vague prompts and getting vague answers. That does not work here. The AI is operating on your actual files, and it needs specificity.

### Be explicit about inputs and outputs

**Bad:** "Write a script to clean the data."

**Good:** "Write a Stata do-file that reads `data/raw/cdc_wonder_2015_2022.csv`, keeps only county FIPS, year, and death count columns, drops rows where the Notes column contains 'Unreliable', and saves to `data/processed/cdc_clean.dta`."

The second prompt gives the AI everything it needs to write working code on the first try. The first prompt forces it to guess — and it will guess wrong.

### Name your files

The AI can see your file system, but it helps to be explicit. Instead of "merge the datasets," say "merge `data/processed/cdc_clean.dta` with `data/processed/acs_demographics.dta` on county FIPS code." This eliminates ambiguity and prevents the AI from merging the wrong files.

### State what you do NOT want changed

This matters more than you think. If you ask the AI to "clean up this script," it may rewrite your estimation logic along with the formatting. Be specific:

```
> Edit scripts/20_estimate.do. Tighten the formatting and add
> a proper header. Do NOT change any estimation commands, variable
> definitions, or sample restrictions.
```

### Give context about your research

The AI does not know your field. If you say "run a diff-in-diff," it will write generic code. If you say "run a difference-in-differences where treatment is city-level decriminalization, the treatment date varies by city, and we need to account for staggered adoption using Callaway and Sant'Anna (2021)," it will write much better code — and you will still need to verify it.

### Three prompts, from worst to best

1. *"Analyze the data"* — The AI has no idea what you want. It will produce something generic and probably wrong.

2. *"Run a regression of death_rate on treatment with county and year fixed effects"* — Better. The AI can write this. But it might pick the wrong command, the wrong standard errors, or the wrong sample.

3. *"Write a Stata do-file that estimates a two-way fixed effects regression: `reghdfe death_rate treatment, absorb(county year) cluster(state)`. Use the analysis file at `data/processed/analysis_panel.dta`. Save the estimates to `output/results/main_fe.ster` and produce a formatted table to `output/tables/main_results.tex` using `esttab`."* — The AI can execute this exactly. You still check the output, but you are far less likely to get something wrong.

The pattern is always the same: tell the AI what goes in, what comes out, and what the constraints are.
