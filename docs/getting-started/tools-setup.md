---
title: Tools & Setup
layout: default
parent: Getting Started
nav_order: 2
---

# Tools & Setup

{: .note }
> Instructions are written for macOS with Windows/Linux notes where they differ.

{: .tip }
> **Feeling overwhelmed?** This guide covers a lot. You do not need to absorb it all before you start. Follow the first few steps below to get an AI coding tool running on your machine. Once it is working, copy the URL for this website and paste it into your AI tool: *"Read this guide and help me set up my project."* It will walk you through the rest.

## Two paths

**Path A: With GitHub.** Clone the template, get version control and backup. Recommended, and the rest of this guide assumes it.

**Path B: Without GitHub.** Download the template as a zip, unzip it, drop your files in, open an AI coding tool in that folder. No Git required. The core workflow is identical.

---

## Step 1: Set up an AI coding tool

You need a terminal-based AI coding assistant — Claude Code, Gemini CLI, OpenAI Codex, or similar. Any of them will work with this template.

For setup instructions covering prerequisites, installation, and authentication on **Mac, Windows, and Linux**, follow the guide at:

> **[ai-in-the-terminal](https://github.com/Black-JL/ai-in-the-terminal)** — Start with the [prerequisites](https://github.com/Black-JL/ai-in-the-terminal/blob/main/docs/01-prerequisites.md) and [quickstart](https://github.com/Black-JL/ai-in-the-terminal/blob/main/docs/02-quickstart.md), then follow the page for whichever tool you choose ([Claude Code](https://github.com/Black-JL/ai-in-the-terminal/blob/main/docs/04-claude-code.md), [Gemini CLI](https://github.com/Black-JL/ai-in-the-terminal/blob/main/docs/03-gemini-cli.md), [Codex](https://github.com/Black-JL/ai-in-the-terminal/blob/main/docs/05-codex.md), etc.).

*Based on [NetworkChuck's](https://github.com/theNetworkChuck/ai-in-the-terminal) companion guide to the "AI in the Terminal" video.*

### A note on costs

This is an AI-heavy workflow. If you are working on a real research project — reading data files, writing scripts, editing manuscripts — you will consume tokens quickly. Be realistic about that upfront.

**At minimum, you need a paid subscription.** Claude Code works with a Claude Pro account ($20/month), which gives you a set number of tokens per hour, per day, and per month. The free tier will not get you through a working session.

**I recommend going further**, at least for the first month. If you are trying to get a stalled project unstuck, treat the higher-tier subscription (Claude Max at $100/month, or equivalent for your tool) as part of the cost of getting your research moving again. Dive in, spend a few weeks working intensively, and then assess whether the ongoing cost is worth it. For most researchers, the answer is obvious after one real session — but you need to be all-in enough to reach that point.

You can monitor your token usage at [console.anthropic.com](https://console.anthropic.com/). If you hit your limit mid-session, the tool pauses until your tokens refresh — no surprise charges. This is not a tool you can evaluate on the free tier. Budget accordingly.

If you get stuck during setup, you can use any AI you already have access to (ChatGPT, Claude.ai, Gemini) to help troubleshoot.

---

## Step 2: Set up Git and GitHub *(Path A only)*

Skip this if you are taking Path B (no GitHub).

The [prerequisites guide](https://github.com/Black-JL/ai-in-the-terminal/blob/main/docs/01-prerequisites.md) above covers Git installation. Once Git is installed, create a [GitHub account](https://github.com) if you don't have one, then install the GitHub CLI:

```bash
brew install gh        # macOS/Linux
gh auth login
```

---

## Step 3: Get the project template

**Path A (GitHub):**

```bash
gh repo create my-project --template Black-JL/Research-Project-Flow --private --clone
cd my-project
```

**Path B (no GitHub):**

1. Go to [github.com/Black-JL/Research-Project-Flow](https://github.com/Black-JL/Research-Project-Flow).
2. Click the green **Code** button → **Download ZIP**.
3. Unzip it wherever you keep your research projects. Rename the folder to your project name.

Either way, you now have the full folder structure. Open your terminal, navigate to the folder, and launch your AI tool:

```bash
cd /path/to/my-project
claude                   # or gemini, codex, etc.
```

The AI reads your `CLAUDE.md`, orients itself, and is ready to work.

---

## Step 4: Install your statistical software

Install whichever your field uses:

- **Stata:** Download from your institutional license portal. On macOS, add it to your PATH: `export PATH="/Applications/Stata/StataMP.app/Contents/MacOS:$PATH"` in `~/.zshrc`.
- **R:** `brew install r` *(Windows: [r-project.org](https://www.r-project.org/))*
- **Python:** `brew install python` *(Windows: [python.org](https://www.python.org/))*

---

## Step 5: Optional tools

**SuperWhisper (voice-to-text).** [SuperWhisper](https://superwhisper.com/) runs offline on your Mac and transcribes speech to text wherever your cursor is. Set it to offline mode, press <kbd>⌥</kbd> + <kbd>Space</kbd>, talk, and the text appears. No typing, no cloud, no subscription. Lets you speak instructions to Claude Code instead of typing them. *(macOS only; Windows alternative: [Whisper.cpp](https://github.com/ggerganov/whisper.cpp))*

**Zotero + Better BibTeX (citation management).** Install [Zotero](https://www.zotero.org/download/) and the [Better BibTeX plugin](https://retorque.re/zotero-better-bibtex/installation/). Create a project collection, export with "Keep updated" to `manuscript/references.bib`. Your bibliography stays in sync automatically.

**Dropbox (file sync).** Place your project folder in Dropbox for backup and co-author sharing. If using Git, exclude `.git` from Dropbox sync: `xattr -w com.dropbox.ignored 1 .git` *(macOS)*. If you are on Path B with no GitHub, Dropbox becomes your primary backup — consider it strongly recommended.

---

## Verify

```bash
claude --version         # or your chosen AI tool
```

If you are on Path A, also verify:

```bash
git --version
gh --version
```

Once everything works, move on to [Project Structure]({% link the-flow/project-structure.md %}).
