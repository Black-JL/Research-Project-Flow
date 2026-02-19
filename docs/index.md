---
title: Welcome
layout: home
nav_order: 1
---

# The AI-Assisted Research Flow
{: .fs-8 }

A practical guide for empirical researchers.
{: .fs-5 .fw-300 }

By Dr. Jared L. Black
{: .fs-4 .fw-300 }

[Download as PDF](guide.pdf){: .btn .btn-primary .mr-2 }

---

## Is this you?

You have a research project sitting in a folder somewhere on your computer. Maybe several. You started it a while ago — could be months, could be years — and life moved on. The project didn't.

The code lives in scattered files. Some of it you wrote yourself. Some you borrowed from someone else's analysis and adapted to your data. You put it together in pieces, at different times, under different assumptions, and it worked well enough to produce some results. But now those pieces are spread across folders like papers on a messy office floor. You know the work is in there. You just can't face the idea of sorting through it.

Your output is in a similar state. Maybe you have a LaTeX document, or a Word file, or some Markdown. There are figures and tables embedded in it — but they are old versions. The updated ones sit in another folder, waiting to be swapped in. The code that produced those figures may or may not be streamlined. It may be in a different directory entirely. You are not sure you could run it again and get the same results.

Your data preparation steps live in one place, grounded in one set of assumptions. Your estimation results and exhibits were created later, possibly under different assumptions, and you cannot completely trace them back. The pipeline — if you can call it that — has gaps. Dependencies are unclear. The idea of picking this project back up and bringing it to a publishable state feels overwhelming.

**If this sounds familiar, this guide is for you.**

## What this does

By learning the approach described here, you can do what I did: take a stalled project — disorganized, daunting, collecting dust — and revive it. Organize the code. Rebuild the pipeline. Map every table and figure back to the script and data that produced it. Update your manuscript. Get the project to a state where one command reproduces everything from raw data to final output.

You do this with an AI that works directly in your project files. Not a chatbot you paste code into. A command-line tool that reads your scripts, understands your folder structure, writes new code that follows your conventions, and maintains the documentation as you go. You make the research decisions. It handles the scaffolding.

The whole process may take a few dedicated sessions. And once the project is organized and the paper is done, you can put it down and move on to the next one — knowing that if you ever need to come back, everything is in order.

## What you will learn

1. **Set up your machine** — install the tools, configure the environment, get Claude Code running.
2. **Understand the project structure** — a folder layout that enforces discipline and makes AI collaboration possible.
3. **Work the flow** — how a research session actually works when AI handles the scaffolding and you handle the thinking.
4. **Write with AI** — use AI assistance for manuscripts without losing your voice or your standards.

## Why this workflow and not a chatbot

One of the most important things to understand upfront: **everything stays on your computer, in your files, in your format.**

When you paste code into ChatGPT or upload files to a web interface, your work lives in someone else's context window. You do not know exactly where it is. You cannot easily undo what was done. If the session ends or the tool changes, your work may be gone.

This workflow is different. The AI operates directly in your project folder — the same folder you see in Finder or File Explorer. Every script it writes is a file on your hard drive. Every change it makes is visible in your file system. If you are using Git, every change is tracked and reversible. Nothing is hidden from you. Nothing takes place outside of your control.

If the AI writes a bad script, you delete the file. If it makes a change you do not like, you revert it with one Git command. If you decide to stop using AI entirely, you still have a perfectly organized project folder with all your code, data, and documentation exactly where you left it.

That is the point. The AI is a tool that works in your space, on your terms, producing artifacts that belong to you.

## The template

Everything in this guide maps to a concrete, reusable project template: [Research-Project-Flow](https://github.com/Black-JL/Research-Project-Flow). You can clone it, fill in your details, and start working. The guide explains what each piece does and why.

No command-line experience required. No AI experience required. Just a willingness to follow instructions and learn as you go.

## Acknowledgments

This guide builds on the work of several people:

- [Scott Cunningham](https://github.com/scunning1975) (*Causal Inference: The Mixtape*) — the [Referee 2 audit protocol](https://github.com/scunning1975/MixtapeTools) and the idea that you cannot grade your own homework. His [MixtapeTools](https://github.com/scunning1975/MixtapeTools) project pioneered many of the practices described here for using AI in empirical research.
- [Matthew Gentzkow and Jesse Shapiro](https://web.stanford.edu/~gentzkow/research/CodeAndData.pdf) — *Code and Data for the Social Sciences*, the foundational reference for reproducible project organization.
- [Deirdre McCloskey](https://www.deirdremccloskey.com/docs/pdf/Article_86.pdf) — *Economical Writing*, the source of the writing standards enforced throughout the template.
- [NetworkChuck](https://github.com/theNetworkChuck/ai-in-the-terminal) — the setup guide and video that this project's installation instructions are based on.

{: .tip }
> **Reading this guide** — Work through the Getting Started chapters to set up your machine. Read The Flow chapters when you start your first project. Keep the Reference section open as a cheatsheet.
