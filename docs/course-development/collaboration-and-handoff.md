---
title: Collaboration & Handoff
layout: default
parent: Course Development Flow
nav_order: 4
---

# Collaboration & Handoff

Course development often involves multiple instructors working asynchronously — different people, different machines, different schedules. The handoff system is what keeps this from falling apart.

## The handoff log

A handoff file (e.g., `HANDOFF.md`) is an append-only running log at the root of the repository. Every time someone finishes a work session, a new entry gets added with:

- What was done (files created, slides built, decisions made)
- What decisions need input from others
- What's still open (FIXMEs, incomplete work, next steps)

Nobody edits or deletes previous entries — you only add to the end. This means any collaborator can be out of the loop for a week, read the handoff log, and know exactly what changed, what needs their attention, and what's still unfinished.

**Before starting work:**
> *"Read the handoff log and summarize what's new."*

**When you're done:**
> *"Update the handoff notes with what we did today."*

## Status tracking

A status table in the repository's README provides a quick-glance view of every lesson or deliverable:

| Status | Meaning |
|--------|---------|
| **Done** | Complete, reviewed, ready to use |
| **Template only** | Structure exists, content needed |
| **Not started** | No work done yet |

The AI updates this table as work progresses, so any collaborator can see the current state without reading through the full handoff log.

## Collaborators who don't use AI tools

The handoff system works regardless of how each collaborator works. Instructors who prefer traditional tools can contribute content in any format, use the `resources/` folder to share materials, and read the handoff log to stay current. The file structure and collaboration protocol are tool-agnostic.

## Parallel agents for batch work

When you have repetitive, independent tasks — building slides for multiple lessons, processing several source materials, creating handouts for different classes — the AI can spin up additional agents that work in parallel, each following the same template and conventions. Each agent gets its own context window, so there's no interference between them.

> *"Create slides for lessons 10, 14, and 17 in parallel, using the same template and the source materials in each lesson's resources/ folder."*

This is where the workflow scales. Batch work that would take hours sequentially can run simultaneously.

## Common mistakes

A few things to watch for:

- **Don't assign multiple complex tasks in a single prompt.** One major task per prompt, iterated to completion.
- **Be explicit about what should NOT change.** If you want the AI to add a slide without modifying existing ones, say so.
- **Don't trust summaries without checking the actual output.** Always open the PDF and look at the slides.
- **Don't let sessions run too long** without resetting context or writing a handoff entry. Quality degrades as the context window fills up.
- **Use voice-to-text** (e.g., SuperWhisper on macOS) for giving instructions. It's dramatically faster than typing for nuanced or complex prompts.
