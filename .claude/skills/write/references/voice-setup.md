# Setting up your own voice skill (about 15 minutes)

The `write` skill makes prose clear. To make it sound like **you**, it needs a personal voice skill. Keep that skill **outside** this repo, because it contains your own writing and this template is public.

## 1. Create the folder

```
~/.claude/skills/<yourname>-voice/
├── SKILL.md        # name, description, load order (copy the structure below)
├── profile.md      # what your voice does, with quotes from your samples
├── ledger.md       # your corrections of Claude's drafts (starts empty)
└── samples/        # 2–4 pieces you wrote yourself
```

## 2. Pick samples carefully

- **Written by you alone, with no AI help.** Anything drafted after about 2023 may contain AI prose you edited rather than wrote. Earlier drafts are often truer to your voice than final versions.
- **At least two registers**, e.g. a personal essay and an academic draft (an intro or discussion section).
- 1,000–3,000 words each is plenty.

## 3. Write the profile from the samples, not from memory

Ask Claude: "Read my samples and list 8–12 concrete features of my voice, each with a quoted example, and a 'not me' list." Then **correct the list yourself**. A profile you haven't checked is just a guess.

## 4. Optional: style modes

If you admire a writer's *style* (not their arguments), add `<writer>-style.md` with their specific moves, each with a verbatim quote from their text. In the voice skill, make it a **mode** you choose for a given piece, not a default.

## 5. Point your project at it

In the project's `CLAUDE.md`, under Writing: `Voice skill: <yourname>-voice`.

## 6. Let the ledger do the work

Every time you edit a Claude draft, hand the edited version back ("here's my edit"). The `write` skill logs each change to `ledger.md`. After ten entries it proposes profile updates. The ledger is how the voice gets learned over time.
