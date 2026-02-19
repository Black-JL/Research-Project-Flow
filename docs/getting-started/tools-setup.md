---
title: Tools & Setup
layout: default
parent: Getting Started
nav_order: 2
---

# Tools & Setup

This chapter walks you through every installation step. Follow it in order. By the end, you will have a working environment ready for AI-assisted research.

{: .note }
> **Platform** — Instructions below are written for macOS. Windows equivalents are noted where they differ. If you are on Windows, start with Step 1 — installing WSL gives you a Linux environment where the remaining commands work the same way.

## Two paths

There are two ways to get started. Both end in the same place — a project folder on your machine with Claude Code running inside it.

**Path A: With GitHub.** You clone the template from GitHub, and your project stays synced to a remote repository. You get version control, backup, and the ability to undo any mistake. This is the recommended path, and the rest of this guide assumes it. But it is not the only path.

**Path B: Without GitHub.** You download the template as a zip file, unzip it, and drop your files into the folder structure. Then you open Claude Code in that folder and start working. No Git, no GitHub account, no command line beyond what Claude Code itself provides. The AI reads your `CLAUDE.md`, understands the project structure, and works with you exactly the same way. You lose version control and remote backup, but the core workflow — AI-assisted coding, pipeline management, documentation — works identically.

Choose your path and follow the steps below. Steps marked *(GitHub only)* can be skipped if you are taking Path B.

## Overview

| Tool | Purpose | Required |
|:-----|:--------|:---------|
| SuperWhisper | Voice-to-text dictation (offline) | Recommended |
| Homebrew | Package manager (macOS) | Yes (macOS) |
| Git | Version control | GitHub only |
| GitHub account | Remote repository hosting | GitHub only |
| GitHub CLI (`gh`) | Terminal interface to GitHub | GitHub only |
| Node.js | Runtime for Claude Code | Yes |
| Claude Code | AI command-line assistant | Yes |
| Stata / R / Python | Statistical software | At least one |
| Zotero + Better BibTeX | Citation management | Recommended |
| Dropbox | File sync and backup | Recommended |
| VS Code or text editor | Viewing and editing files | Recommended |

---

## Step 0: Set up voice input with SuperWhisper

Before installing anything technical, set up the tool that will change how you interact with your computer. [SuperWhisper](https://superwhisper.com/) is a voice-to-text app for macOS that runs entirely on your machine. No cloud. No subscription for the core functionality. No data leaving your computer. It uses OpenAI's Whisper model compiled to run locally on Apple Silicon.

Why this matters: in this workflow, you talk to Claude Code constantly — describing what you need, explaining your data, asking questions. Typing all of that is slow. With SuperWhisper, you put your cursor wherever you want text to appear (the Terminal, a text editor, a manuscript file), press a hotkey, speak, and the transcribed text appears right there when you finish. No copy-pasting from a separate app. No online transcription service.

*Windows: SuperWhisper is macOS-only. [Whisper.cpp](https://github.com/ggerganov/whisper.cpp) offers similar offline voice-to-text and runs on Windows. The concept is the same — local transcription, no cloud — but setup requires more manual configuration.*

### Install and configure

1. Download [SuperWhisper](https://superwhisper.com/) from the website or the [Mac App Store](https://apps.apple.com/us/app/superwhisper/id6471464415).

2. Open SuperWhisper and go to its settings. Set it to **offline mode** — select one of the local Whisper models. The "Large" model gives the best accuracy; "Standard" is a good balance of speed and quality. Avoid the cloud models. The whole point is that this runs on your hardware with zero internet dependency.

3. The default hotkey is <kbd>⌥</kbd> + <kbd>Space</kbd> (Option + Space). You can change this in SuperWhisper's settings to whatever feels natural.

### How to use it

The workflow is simple:

1. Click where you want text to go — the Terminal, a text file, an email, anything.
2. Press <kbd>⌥</kbd> + <kbd>Space</kbd> (or your chosen hotkey). SuperWhisper starts listening.
3. Speak naturally. Say what you want to type.
4. Press the hotkey again (or let it auto-stop after a pause). SuperWhisper transcribes your speech and pastes the text wherever your cursor is blinking.

That's it. No intermediate steps. No browser tab. No waiting for a server. The transcription runs on your Mac's neural engine and the text appears in place.

{: .tip }
> **Where this shines** — When you are working in Claude Code and need to describe a complex data task — "merge the treatment dataset with the county demographics file on FIPS codes, keep only counties with population above 50,000, and flag any counties that appear in the treatment group before the policy date" — just say it. SuperWhisper transcribes it directly into the Terminal where Claude Code reads it. Faster than typing, and you tend to explain things more completely when speaking than when typing.

{: .note }
> **Hardware** — Offline models perform best on Apple Silicon Macs (M1 and later). If you are on an Intel Mac, the offline models will be slow — you can still use SuperWhisper's cloud mode, but you lose the offline advantage.

---

## Step 1: Install Homebrew (macOS)

Homebrew is a package manager for macOS. It installs software from the command line. Open **Terminal** (search for "Terminal" in Spotlight) and paste:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the prompts. When it finishes, close and reopen Terminal, then verify:

```bash
brew --version
```

You should see a version number. If you get "command not found," follow the instructions Homebrew printed about adding it to your PATH.

{: .note }
> **Windows users** — Install [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install), then install Homebrew inside WSL. Once WSL and Homebrew are set up, every `brew install` command in the remaining steps works identically. Claude Code requires a Unix-like environment — WSL provides this on Windows.

---

## Step 2: Install Git *(GitHub only)*

Skip this step if you are taking Path B (no GitHub).

```bash
brew install git
```

Verify:

```bash
git --version
```

Configure your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## Step 3: Create a GitHub account *(GitHub only)*

Skip this step if you are taking Path B (no GitHub).

Go to [github.com](https://github.com) and create an account if you don't have one.

Install the GitHub CLI, which lets you interact with GitHub from the terminal:

```bash
brew install gh
gh auth login
```

Follow the prompts to authenticate. Choose HTTPS and log in through your browser when prompted.

---

## Step 4: Install Node.js

Claude Code runs on Node.js. Install it:

```bash
brew install node
```

Verify:

```bash
node --version
```

You need version 18 or higher.

---

## Step 5: Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

Verify:

```bash
claude --version
```

Now authenticate. Run:

```bash
claude
```

The first time you launch Claude Code, it will walk you through authentication. You need an [Anthropic account](https://console.anthropic.com/) with API access or a Claude Pro/Team subscription.

{: .important }
> **API costs** — Claude Code uses the Anthropic API. Each session consumes tokens. A typical research session costs a few dollars. Monitor your usage at [console.anthropic.com](https://console.anthropic.com/).

---

## Step 6: Get the project template

**Path A (GitHub):**

```bash
gh repo create my-project --template Black-JL/Research-Project-Flow --private --clone
cd my-project
```

This creates a private copy of the template on your GitHub account and clones it to your machine.

**Path B (no GitHub):**

1. Go to [github.com/Black-JL/Research-Project-Flow](https://github.com/Black-JL/Research-Project-Flow).
2. Click the green **Code** button → **Download ZIP**.
3. Unzip it wherever you keep your research projects.
4. Rename the folder to your project name.

Either way, you now have the full folder structure on your machine. Open Terminal, navigate to the folder, and launch Claude Code:

```bash
cd /path/to/my-project
claude
```

The AI reads your `CLAUDE.md`, orients itself, and is ready to work. The workflow from here is identical regardless of which path you chose.

---

## Step 7: Install your statistical software

Install whichever you use:

**Stata:** Download from your institutional license portal. Ensure the `stata` command works from the terminal. On macOS, you may need to add it to your PATH:

```bash
# Add to your ~/.zshrc:
export PATH="/Applications/Stata/StataMP.app/Contents/MacOS:$PATH"
```

*Windows: Stata installs normally. To use it from WSL, call the Windows executable directly or add its path to your WSL environment.*

**R:**

```bash
brew install r
```

*Windows: download from [r-project.org](https://www.r-project.org/), or install inside WSL with `brew install r`.*

**Python:**

```bash
brew install python
```

*Windows: download from [python.org](https://www.python.org/), or install inside WSL with `brew install python`.*

---

## Step 8: Install Zotero and Better BibTeX *(optional)*

1. Download [Zotero](https://www.zotero.org/download/) and install it.
2. Install the [Better BibTeX plugin](https://retorque.re/zotero-better-bibtex/installation/).
3. In Zotero, create a collection for your project.
4. Right-click the collection → Export → Format: Better BibTeX → Check "Keep updated" → Save to `manuscript/references.bib` in your project folder.

This keeps your bibliography in sync automatically. Add a source in Zotero, and it appears in your `.bib` file.

---

## Step 9: Set up Dropbox *(optional)*

If you use Dropbox for file sync:

1. Place your project folder inside Dropbox.
2. If you are using Git (Path A), exclude the `.git` directory from Dropbox sync to avoid conflicts:

```bash
xattr -w com.dropbox.ignored 1 /path/to/your/project/.git
```

*Windows: in Dropbox desktop settings, add the `.git` folder to "Files not to sync," or use `Set-Content -Path '.git\.dropbox.ignore' -Value ''` in PowerShell.*

This lets you use Dropbox for file backup and sharing with co-authors while Git handles version control separately. If you are on Path B (no GitHub), Dropbox becomes your primary backup — consider it strongly recommended.

---

## Verify everything

Run these commands and confirm each returns a version number or success message:

```bash
node --version
claude --version
```

If you are on Path A (GitHub), also verify:

```bash
git --version
gh --version
```

If any command fails, revisit the corresponding step above. Once everything works, move on to [Project Structure]({% link the-flow/project-structure.md %}) to set up your first project.
