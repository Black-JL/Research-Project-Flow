---
title: FAQ
layout: default
parent: Reference
nav_order: 2
---

# FAQ

<img src="{{ site.baseurl }}/assets/images/real_scenario_4.png" alt="Manuscript and notes illustration" class="page-illustration">

## Getting started

### Do I need to know how to code?

Not to get started. The AI writes code based on your descriptions. You need to understand what a script should do — what data goes in, what results come out — but you do not need to write it from scratch.

That said, **learning to write code is worth the effort** — not just reading it. The more you understand the syntax and logic of your statistical software, the better you can evaluate what the AI produces. This matters most where it matters most: estimation. See the next question.

### Where is the AI good and where is it not?

Be honest with yourself about this. The AI is not equally reliable across all parts of the research workflow.

**Where it excels:**

- **Data cleaning and organization.** Importing, reshaping, merging, labeling — the AI does this very well. Not perfect, but consistently strong. This is the bread and butter of the workflow.
- **Visualization.** Charts, graphs, maps. The AI writes clean plotting code and iterates quickly on formatting. Post-estimation, once you know what the output means, the AI is a great tool for turning results into publication-quality figures.
- **Project scaffolding.** Folder structure, script headers, documentation, pipeline management — everything this template automates.

**Where you must be hands-on:**

- **Estimation code.** The AI often gets this wrong. Not just the logic — the *syntax*. A `reghdfe` command with the wrong absorb structure, a `felm` call with misspecified clusters, a `linearmodels` panel estimator with the wrong entity effects. You need to understand the software you are using well enough to catch these errors. If you hand estimation off to the AI without careful review, you risk accelerating bad code. This is where learning to write code pays off.
- **Writing.** The AI is good at telling you what it thinks results mean, and it can tighten prose and enforce style rules. But in my experience, the actual argument — the interpretation, the contribution, the narrative that holds a paper together — needs to come from you. No AI I have used writes well enough to produce publishable academic prose without heavy revision. I recommend being hands-on for the writing that matters.

This workflow is designed for **resurrecting stalled projects** — organizing them, rebuilding the pipeline, getting the scaffolding right. It is not a replacement for critical thinking, and your mileage may vary.

### Which statistical software should I use?

The template supports Stata, R, and Python. Use whatever your field and co-authors expect. Most economics departments use Stata. The template handles mixed-language pipelines, so you can use R for data visualization and Stata for estimation in the same project.

### How much does this cost?

This is an AI-heavy workflow. You will use tokens quickly when the AI reads data files, writes scripts, edits manuscripts, and runs your pipeline. Be realistic about that upfront.

**At minimum, you need a paid subscription.** Claude Code works with a Claude Pro account ($20/month), which comes with a set number of tokens per hour, per day, and per month. The free tier will not get you through a working session. Other tools (Gemini CLI, Codex) have their own subscription tiers — check their pricing.

**I recommend starting with a higher tier.** If you are trying to get a stalled project unstuck, treat the higher-tier subscription (Claude Max at $100/month, or equivalent) as part of the cost of getting your research moving. Dive in, work intensively for a few weeks, then decide whether the ongoing cost is worth it. For me, the value was obvious after one real session — but I had to invest enough to reach that point.

You can monitor your token usage at [console.anthropic.com](https://console.anthropic.com/) to see how quickly you burn through your allocation. If you hit your limit mid-session, the tool pauses until your tokens refresh — you do not get surprise charges.

### Can I use this with ChatGPT or other AI tools?

The template ships with `CLAUDE.md` and slash commands designed for Claude Code. Other terminal-based AI tools (Gemini CLI, Codex) work with this template too — they read and write files directly in your project the same way. Chat-based tools like ChatGPT operate differently and cannot interact with your file system.

### What about auto-accept / "YOLO" mode?

All three tools have a mode that auto-approves every action without asking you first:

| Tool | Command |
|:-----|:--------|
| Claude Code | `claude --dangerously-skip-permissions` |
| Codex | `codex --yolo` |
| Gemini CLI | `gemini --yolo` |

**I do not recommend this**, especially for anything involving estimation code. In auto-accept mode, the AI may decide it needs to do extensive web research and disappear down a rabbit hole for a long time. It may wander into other folders on your machine and write itself helper scripts you did not ask for. It may modify files outside your project. You lose the ability to review each action before it happens — which is the whole point of the guardrails in this workflow.

If you do use it, you can confine the AI to specific folders:

- **Claude Code:** Set `permissions.deny` rules in `.claude/settings.json` (e.g., `"Edit(data/raw/**)"` to block raw data edits), or use `--disallowedTools` to block specific tool categories.
- **Codex:** Use `--sandbox workspace-write` to restrict writes to your project directory.
- **Gemini CLI:** Use `--sandbox` for OS-level isolation, or `--allowed-tools` to restrict which tools auto-approve.

These commands exist. Use them as you see fit. But for the parts of the workflow that matter most — estimation and writing — stay hands-on.

---

## Working with the template

### How do I add a co-author?

1. Share the Dropbox folder with them.
2. Add their machine path to `scripts/00_run.do`.
3. Point them to the Co-Author Instructions section in the README.

They do not need Claude Code to contribute. They edit files in Dropbox, and you commit the changes to Git on their behalf.

### What if the AI modifies something it shouldn't?

The `CLAUDE.md` file includes rules that prevent the AI from modifying raw data or making unauthorized structural changes. If the AI proposes something you do not want, say no. It will adjust.

If the AI does make an unwanted change, Git makes it trivial to undo:

```bash
git diff              # see what changed
git checkout -- path/to/file   # revert a specific file
```

### How do I handle sensitive or restricted data?

- Never commit sensitive data to Git. Add the file paths to `.gitignore`.
- Document access instructions in `data/raw/README.md`.
- Use the Data Availability Statement in your README to describe restrictions.
- The AI operates locally on your machine — it does not upload your data anywhere.

### What if the pipeline breaks?

Run `/check` to identify the problem. The AI will report which scripts, data files, or references are inconsistent. Common issues:

- A script references a file that was renamed → update the script or rename back
- `params.do` and README disagree → reconcile the values
- A log shows an error → read the log, fix the script, re-run

---

## Git and GitHub

### I have never used Git. Is that a problem?

No. The `/git` command handles staging, committing, and pushing. You do not need to learn Git commands to use the template. But understanding what Git does — tracking changes, enabling undo, syncing with GitHub — will help you appreciate why the template uses it.

### Can I use a private repository?

Yes. When you clone the template, use `--private`:

```bash
gh repo create my-project --template Black-JL/Research-Project-Flow --private --clone
```

Your code and data descriptions stay private. Only people you explicitly invite can see the repo.

### What goes on GitHub vs. Dropbox?

- **GitHub:** Code, scripts, documentation, manuscript source, configuration files. Everything text-based and version-controlled.
- **Dropbox:** Large data files, binary outputs, anything too big for Git. Dropbox provides the backup and sharing layer.

The `.gitignore` file controls what Git tracks. Large data files should be excluded from Git and shared via Dropbox.

---

## Common mistakes

### Things I wish I had known

These are patterns that tripped me up, and that I have seen others run into. Learn from them before you repeat them.

**Giving the AI too many tasks at once.** "Reorganize all my scripts, rebuild the pipeline, update the README, and fix the estimation code" will produce mediocre results across the board. One task per request. Let it finish, review the output, then move on.

**Letting sessions run too long.** After an hour or two of active work, the AI's context window is full. It starts forgetting what it did earlier, contradicting itself, or getting slower. Run `/handoff`, close the session, and start fresh. A clean session with a good handoff note is more productive than a marathon session that degrades.

**Trusting the log summary instead of the log.** When the AI says "the script ran successfully and produced 15,000 observations," read the actual log. The AI is usually right, but "usually" is not good enough for research. The log is in `output/logs/`. Read it.

**Not stating what should stay the same.** When you ask the AI to edit a script, it may "improve" things you did not ask it to touch. Always say what should not change: "Edit the formatting. Do not change any estimation commands or sample restrictions."

**Skipping the first `/check`.** Before you start real work in a session, run `/check`. It takes a few seconds and tells you whether the pipeline is consistent. Finding out that something is broken *after* you have been building on top of it for an hour is painful.

**Using AI for the parts that require judgment.** Data cleaning and visualization? Let the AI drive. Estimation code and manuscript writing? You drive. In my experience, the AI works best for the mechanical parts of research. The intellectual parts are where your judgment matters most. See [Where is the AI good and where is it not?](#where-is-the-ai-good-and-where-is-it-not) above.

---

## Working with co-authors

### My co-author does not use AI. Is that a problem?

No. This is the normal case. Most co-authors will not use AI coding tools, and they do not need to.

Your co-author sees the same project folder you do — scripts, data, output, manuscript. Every file is a normal file in a normal folder. Nothing about the project depends on AI to function. If your co-author wants to open `scripts/10_balance.R` and edit it by hand, they can. If they want to run the pipeline themselves, `./run_all.sh --all` works without any AI tool installed.

The question your co-author will have is: *"How do I know what the AI changed?"*

The answer is in three places:

1. **Session logs** (`session_logs/`). Every working session produces a dated log that says what the AI did and why. Your co-author reads these the same way they would read your lab notebook.

2. **Git history.** Every commit has a message describing the changes. `git log --oneline` shows the history. `git diff` shows exactly what changed in any file.

3. **The code itself.** Every script has a structured header documenting its purpose, inputs, outputs, and dependencies. The code is readable, conventional, and follows the same patterns whether you or the AI wrote it.

If your co-author is skeptical — and healthy skepticism is appropriate — point them to the session logs and the git history. The audit trail is the whole point of this workflow. You can explain and defend every change because every change is documented.

### How do I bring this up with a co-author?

Be direct: *"I've been using an AI coding tool to organize the project and write data cleaning scripts. Every change is tracked in version control and documented in session logs. The estimation code and the writing are mine. Here's the session log from the last working session if you want to see what it did."*

The audit trail is there for exactly this conversation. Anyone who wants to verify what the AI did can read the session logs, check the git history, and inspect the code. That is the point of the workflow.

---

## Troubleshooting

### Claude Code says "command not found"

Your PATH is not set up correctly. Check that Node.js and Claude Code are installed:

```bash
node --version
which claude
```

If `claude` is not found, reinstall:

```bash
npm install -g @anthropic-ai/claude-code
```

### The AI seems confused about my project

It probably has not read `CLAUDE.md`. Make sure the file exists in your project root and contains the correct project path. Launch Claude Code from the project directory:

```bash
cd ~/Dropbox/my-project
claude
```

### Scripts run in Terminal but not through `run_all.sh`

Check that `run_all.sh` is executable:

```bash
chmod +x run_all.sh
```

Also verify that the statistical software is accessible from the command line. Stata in particular may need a PATH addition (see [Tools & Setup]({% link getting-started/tools-setup.md %})).
