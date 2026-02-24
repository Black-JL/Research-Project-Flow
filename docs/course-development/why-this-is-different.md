---
title: Why This Is Different
layout: default
parent: Course Development
nav_order: 1
---

# Why This Is Different

The copy-paste-between-windows workflow — paste content into a chatbot, get a response, paste it somewhere else, lose track of versions — breaks down for course development the same way it breaks down for research. Context drifts. File structure drifts. The thread breaks.

The terminal-based workflow replaces that with something more reliable. Three things make it fundamentally different:

## A. Context engineering, not prompt engineering

Your files, your folder structure, your instructions — all of it lives on your computer, not in a chatbot's memory. The AI reads files directly from the filesystem and writes output back into the same structure. When a session ends, everything is right there.

Because terminal-based AI tools use the API rather than a persistent chat interface, memory between sessions is zero — by design. The AI only knows what you've written down in files. No cross-contamination from old projects, no hallucinated context from previous conversations. You control exactly what it knows.

## B. Enforced file structure

You define a folder layout once, and the AI enforces it on every operation. Files go where they're supposed to go, every time.

## C. You stay at a higher level of thinking

The mechanical work — formatting, compiling, organizing files, fixing layout errors — gets handled for you. What you spend your time on is: *What do students need to learn? How do I get from where I am to there?*

{: .tip }
> The division of labor is simple: you supply the teaching decisions — what to cover, in what order, with what emphasis. The AI handles structure, formatting, file organization, and mechanical execution.

## Once you have a template, it's all content

This is the real payoff. Create slide and document templates you like, put them in the repository, and tell the AI to use them. From that point forward, you work on *content* — what to teach, what sources support it, what's the narrative arc — and the AI handles the rest. There is very little iterative work making slides look right.
