---
title: FAQ
layout: default
parent: Reference
nav_order: 2
---

# FAQ

![Results and tables illustration]({{ site.baseurl }}/assets/images/header_4.png)

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
- **Writing.** The AI is good at telling you what it thinks results mean, and it can tighten prose and enforce style rules. But the actual argument — the interpretation, the contribution, the narrative that holds a paper together — must be yours. No AI I know of writes well enough to produce publishable academic prose without heavy revision. Be 100% hands-on for the writing that matters.

This workflow is designed for **resurrecting stalled projects** — organizing them, rebuilding the pipeline, getting the scaffolding right. It is not a replacement for critical thinking or for engaging carefully with your estimation and your writing.

### Which statistical software should I use?

The template supports Stata, R, and Python. Use whatever your field and co-authors expect. Most economics departments use Stata. The template handles mixed-language pipelines, so you can use R for data visualization and Stata for estimation in the same project.

### How much does this cost?

This is an AI-heavy workflow. You will use tokens quickly when the AI reads data files, writes scripts, edits manuscripts, and runs your pipeline. Be realistic about that upfront.

**At minimum, you need a paid subscription.** Claude Code works with a Claude Pro account ($20/month), which comes with a set number of tokens per hour, per day, and per month. The free tier will not get you through a working session. Other tools (Gemini CLI, Codex) have their own subscription tiers — check their pricing.

**I recommend starting with a higher tier.** If you are trying to get a stalled project unstuck, treat the higher-tier subscription (Claude Max at $100/month, or equivalent) as part of the cost of getting your research moving. Dive in, work intensively for a few weeks, then decide whether the ongoing cost is worth it. For most researchers, the answer is obvious after one real session — but you need to invest enough to reach that point.

You can monitor your token usage at [console.anthropic.com](https://console.anthropic.com/) to see how quickly you burn through your allocation. If you hit your limit mid-session, the tool pauses until your tokens refresh — you do not get surprise charges.

### Can I use this with ChatGPT or other AI tools?

The template is designed for Claude Code specifically. The `CLAUDE.md` file, the slash commands, and the automated project management all depend on Claude Code's ability to read and write files directly in your project. Other AI tools operate through a chat interface and cannot do this.

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
