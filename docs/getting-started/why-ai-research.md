---
title: Why AI-Assisted Research
layout: default
parent: Getting Started
nav_order: 1
---

# Why AI-Assisted Research

![Data analysis illustration]({{ site.baseurl }}/assets/images/header_3.png)

## The problem

Empirical research requires managing a staggering number of moving pieces: raw data, cleaning scripts, analysis code, output files, manuscripts, citations, and the documentation that ties them together. Most researchers handle this by hand. Files accumulate. Naming conventions drift. Documentation lags behind reality. By the time a paper is under review, the project folder is a maze that only the original author can navigate — and sometimes not even them.

The tools exist to solve this. Version control, reproducible pipelines, structured folder layouts — these practices are well-documented. Gentzkow and Shapiro wrote the definitive guide in 2014. The TIER Protocol formalized it. The AEA Data Editor enforces it. But adoption remains low, because the overhead of maintaining these systems falls entirely on the researcher.

## What changes with AI

AI does not replace the researcher's judgment. It replaces the overhead. Specifically:

**Structure maintenance.** An AI agent that reads your `CLAUDE.md` file knows your project layout, your naming conventions, and your pipeline order. When you add a new script, it updates the README, the master do-file, and the execution script automatically. The structure stays current because the AI maintains it.

**Script writing.** You describe what a script should do — its inputs, outputs, and purpose. The AI writes the code, following your existing conventions. You review and approve. The tedious translation from "I need a script that merges these files on county FIPS codes" to actual working code takes minutes instead of hours.

**Documentation.** Every script header, every pipeline table entry, every data dictionary update — the AI handles these as part of the workflow. Documentation is no longer a separate task you defer. It happens as you work.

**Error checking.** The AI reads your logs after every run. It flags warnings, identifies failures, and suggests fixes. You catch problems immediately instead of discovering them three weeks later.

## What does not change

- **You** decide the research question.
- **You** choose the identification strategy.
- **You** evaluate whether results make economic sense.
- **You** write the arguments that hold a paper together.

The AI is fast at mechanical tasks and unreliable at judgment calls. A good workflow exploits the first property and guards against the second.

### Where to trust it and where not to

For **data cleaning, organization, and visualization**, the AI is consistently strong. Importing, reshaping, merging, labeling, charting — this is where the workflow saves the most time.

For **estimation code**, the AI often gets things wrong. Not just the logic — the syntax. A `reghdfe` command with the wrong absorb structure, a `felm` call with misspecified clusters. You need to understand your statistical software well enough to catch these errors. If you hand estimation off to the AI without careful review, you accelerate bad code. Learn to write code, not just read it.

For **writing**, the AI can tighten prose and enforce style rules, but the actual argument — the interpretation, the contribution, the narrative — must be yours. Be completely hands-on for estimation and writing, even if you give the AI wide latitude over everything else.

## The cost of not adopting

If you organize your project poorly, no AI can fix it. If you organize it well, AI makes every subsequent step faster. The Research Project Flow template gives you the organization. This guide shows you how to use AI within it.

The researchers who adopt these tools now will have a compounding advantage: every project they complete makes the next one faster, because the template improves and the habits stick.
