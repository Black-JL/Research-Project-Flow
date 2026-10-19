---
name: write
description: Draft or revise research prose (a paragraph, a section, an abstract, a results write-up) so it is clear to a reader who has not seen the code, and sounds like the author rather than like Claude. Use whenever the user asks to "write up", "draft", "write a paragraph/section about", "turn these findings into prose", "tighten", "edit", or "rewrite" text for a manuscript, report, or proposal. Also use when the user hands back an edited version of a draft Claude wrote, so the edit can be learned from.
---

# Write

Bad AI prose for research is four separate failures. Each has its own cause and its own fix, and this skill applies all four.

| Failure | Cause | Fix |
|---|---|---|
| **Unclear** | Prose gets drafted before the point of each paragraph is decided. | Step 2: a points outline the author approves before any prose is written. |
| **Jargony / over-technical** | The drafting session is full of code, variable names, and spec labels, so the drafter can't see its own jargon (the curse of knowledge). | Step 4: a cold reader with no session context reads the draft. Step 5: a jargon-leak scan. |
| **Concepts lost in the language** | Several points packed into one paragraph; abstract claims with no example; cause and effect pulled apart. | Step 3: one point per paragraph, PEER structure, related ideas kept together. |
| **Doesn't sound like the author** | The model writes in its own default voice. Writing guidelines (McCloskey, Orwell) say what to avoid; they don't supply a voice. | Step 0: load the author's voice skill (profile, samples, edit ledger). Prefer **Edit mode**. Step 7: learn from every edit the author makes. |

**Guidelines vs. voice.** McCloskey (`references/mccloskey.md`), Orwell (`references/orwell.md`), and PEER (`references/peer.md`) are *guidelines*. They apply to everyone, always, and sit underneath the voice. The *voice* belongs to the author and lives in a personal voice skill outside this repo (see `references/voice-setup.md`). A style model such as Weitzman is an optional *mode* the author turns on for a given piece. It covers the model's style moves, never their arguments.

## Modes

- **Edit mode (preferred).** The author supplies rough words: typed notes, a messy paragraph, or a voice memo. Claude tightens and structures them and keeps the author's words. This keeps the voice better than generating from scratch, because the words start out as the author's. A voice memo can be transcribed locally: `mlx_whisper memo.m4a --model mlx-community/whisper-large-v3-turbo --output-format txt`.
- **Draft mode.** Claude writes from findings. Use it when the author has no rough words. Run every step.
- **Learn mode.** The author returns an edited version of a Claude draft. Go straight to Step 7.

When the request is "write a paragraph about X" and the author hasn't given rough words, offer Edit mode once in a single line ("Want to give me two or three rough sentences first? It'll sound more like you."). Then continue with whichever mode they pick. Don't ask twice.

## Step 0 — Load the voice and the rules

1. **Voice skill.** Use the skill named in the project's `CLAUDE.md` (`Voice skill:`). Failing that, use any personal voice skill installed in `~/.claude/skills/` (e.g. `jared-voice`). Follow its load order: profile, edit ledger, samples, and style modes. The ledger holds the author's own corrections of Claude's drafts; where it conflicts with a general rule here, the ledger wins.
2. **Guidelines.** Read `references/mccloskey.md`, `references/orwell.md`, and `references/peer.md` (skim them after the first time in a session).
3. **Project rules.** Read whatever the project's `CLAUDE.md` points to for prose: voice rules, and the formatting guide. These set what is allowed. The voice skill sets how it should sound. In a journal manuscript, project rules win where they conflict.

If there is no voice skill, say so in one line and continue. Point the author to `references/voice-setup.md` for a 15-minute setup.

## Step 1 — Brief

Before writing, you need these four things. Take any you can from the conversation and ask only for what's missing, all in one message:

1. **Job:** what this text has to do (e.g. "convince a referee the null isn't a power problem").
2. **Reader:** who reads it and what they already know. Default: *a smart researcher in an adjacent field who has read the abstract and nothing else, and has never seen the code.*
3. **Claim:** the single sentence the reader should walk away with.
4. **Facts:** every number to be used, each with its source file (table, log, or output). Take numbers from files, never from memory or from earlier in the chat. If a number has no source, mark it `[SOURCE?]` rather than inventing one.
5. **Mode** (if the voice skill defines modes, e.g. Standard vs. Weitzman): suggest one in a single line with a reason, and let the author pick. Skip this if the author has already said which.

## Step 2 — Points outline (gate)

For anything longer than one paragraph, write one topic sentence per paragraph and nothing else:

- Each one is a **claim**, not a topic. "Breached hospitals' revenue did not fall" is a claim. "Revenue effects" is a topic.
- Use plain words: no variable names and no spec numbers.
- **Skip test:** read the topic sentences alone, top to bottom. They should make the whole argument. If they don't, fix the outline. Don't count on prose to fix it later.

Show the outline to the author and **wait for approval** before drafting. A five-line outline takes thirty seconds to fix. A five-paragraph draft built on the wrong outline is wasted. For a single paragraph, state its one point in a line and go ahead.

## Step 3 — Draft

**Paragraph structure: PEER.** **P**oint: the topic sentence, one point only. **E**vidence: the number, the study, the example. **E**xplain: what the evidence means and why it supports the point. **R**epeat/link: a last sentence that closes the point and leads into the next paragraph. If a paragraph needs a second point, it needs a second paragraph.

**Sentences:**
- One idea per sentence. A long sentence is fine if it is easy to read. The problem is a long sentence that carries three ideas.
- Use a concrete actor as the subject: hospitals, patients, states, insurers. Avoid abstractions like "the specification", "the battery", or "the analysis". When project rules forbid "we", the subject should still be a concrete thing, not a nominalization.
- Use verbs and nouns, not adjectives and adverbs. "Reduced", not "had a negative impact on".
- Keep related things together: the cause next to its effect, the timing next to the thing it describes, the qualifier next to the word it qualifies.
- Give each number a meaning. Put the scale or comparison right beside it ("a 2.1% drop, about $4 million for the median hospital").
- Any technical term the reader may not know gets defined in plain words the first time it appears, or gets replaced with plain words.
- One word, one meaning. Pick a term and keep it. Never swap in a synonym for variety.

**Voice:** match the profile and samples on sentence length, rhythm, how claims are made, how sources are named, and how paragraphs end. Where the profile and your instinct disagree, follow the profile.

## Step 4 — Cold read (always, in Draft mode)

Spawn a **fresh subagent** (Agent tool, general-purpose). Give it **only** the draft text and the reader description from Step 1. Don't give it the conversation, the code, or the outline. Ask it to return:

1. The point of each paragraph, in one sentence each, in its own words.
2. Every word or phrase it had to stop on, or that the stated reader wouldn't know.
3. Every sentence it had to read twice.
4. Any claim that reads stronger than the evidence shown next to it.
5. The one sentence it would tell a colleague the text says.

Compare item 1 with the approved outline and item 5 with the Claim from Step 1. **A mismatch means the text is unclear.** Rewrite and run the cold read again (at most twice). The drafting session can't do this check itself, because it already knows what it meant.

## Step 5 — Mechanical checks

Run these on the final text. Use grep for the ones that can be grepped.

- **Jargon leak:** code identifiers (`snake_case`, `camelCase`, file names, `.do`/`.R`/`.py`), script or spec numbers ("spec 3", "model 2b", "CP2"), dataset column names, undefined acronyms, and labels coined during this session.
- **Meaning drift (Edit mode, and any revision of existing text):** list every place the edit (a) swapped a term for a near-synonym ("consumption" → "intake"), (b) dropped a qualifier or scope word ("interventions to reduce X" → "reducing X"), (c) strengthened or weakened a verb ("reduced" → "harmed"), (d) widened or narrowed an outcome ("metabolic outcomes" → "metabolic health"). Undo each one unless the change was intended, and report the intended ones.
- **AI tells:** em dashes; "not just X, but Y" and "it's not X, it's Y"; three-item lists used for rhythm rather than because there are three things; a closing sentence that only restates the paragraph; openers such as "In recent years" or "It is important to note"; stacked hedges ("may potentially"); and the words *crucial, pivotal, landscape, underscore, delve, nuanced, notably, sheds light, plays a role, a growing body of literature, in the realm of*. ("Robust" is fine in its statistical sense.)
- **Skip test** again on the final text.
- **Project rules** (voice rules, AEA formatting): run their checklists.

## Step 6 — Deliver

Give the text first. After it, add at most five short lines:
- what the cold reader misread, and what was changed because of it;
- any term choice or claim strength the author should confirm;
- any `[SOURCE?]` left in the text.

Don't explain the process or praise the draft.

## Step 7 — Learn from the author's edits

Whenever the author hands back an edited version of something Claude drafted, in this session or a later one:

1. Diff Claude's version against the author's version.
2. Append one entry per meaningful change to the edit ledger, in this format:

   ```
   ## YYYY-MM-DD · <project> · <section>
   - Claude: "<original sentence>"
   - Author: "<edited sentence>"
   - Pattern: <one line: what the author did, stated as a rule, e.g. "puts the number before the interpretation">
   ```

   Skip pure typo fixes.
3. Once the ledger has 10 or more new entries since the profile last changed, propose specific additions to `profile.md` in a short list, each with the ledger entries that support it. **Ask before changing the profile.**

The ledger is how the voice gets learned. A profile written once from a few samples is a first guess. The ledger corrects it every time the author edits a draft.
