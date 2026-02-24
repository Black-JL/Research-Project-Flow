---
title: The Instruction File
layout: default
parent: Course Development Flow
nav_order: 2
---

# The Instruction File

Just as the research workflow uses `CLAUDE.md` to store project conventions, the course development workflow uses the same mechanism to store teaching conventions. The instruction file is the most important file in a course repository.

## What it contains

The AI reads this file at the start of every session and uses it to shape every response. A course instruction file typically includes:

- **Course schedule and instructor assignments** — who teaches what, on which days
- **Folder structure conventions** — where files go, how they're named
- **Slide design standards** — layout patterns, color schemes, font hierarchies
- **Speaker note requirements** — teaching scripts, timing tags, real-world examples
- **Technical rules** — overflow prevention, compilation settings, diagram conventions

## Why it matters

You don't re-explain conventions each session. The AI reads the file and follows it. If you want to change behavior — say, a different color scheme or a different speaker note format — you change the instruction file and every future session picks up the new rules.

## Sub-instructions

The instruction file can reference specialized sub-documents that only activate in context. Mention slides in your prompt, and the AI reads the detailed slide creation guide. Mention research, and it follows research conventions. This keeps the main file focused while giving the AI deep domain knowledge when it needs it.

{: .note }
> The instruction file is what makes this workflow reproducible across instructors. Any collaborator can launch the AI tool, and it follows the same rules because it reads the same file. The consistency comes from the file, not from the person driving.
