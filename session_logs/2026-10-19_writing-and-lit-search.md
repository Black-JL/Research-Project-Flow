# 2026-10-19 · Writing system and direct literature search

## Summary
Rebuilt how prose gets written in this template and added direct literature search. Prompted by David Stuckler's videos on Claude for research (connectors, skills as SOPs, PEER paragraphs, how AI edits drift in meaning).

## Tasks Completed
- New `write` skill (`.claude/skills/write/`): claim outline gate, PEER drafting, a cold read by a fresh-context subagent, jargon-leak / meaning-drift / AI-tell checks, and an edit ledger so the author's voice is learned from their own corrections.
- References: `mccloskey.md` (from writing-mentor-framework), `orwell.md` (quotes checked against the Orwell Foundation text), `peer.md`, `voice-setup.md`.
- New `lit-search` skill (`.claude/skills/lit-search/lit.py`): OpenAlex + Semantic Scholar + Crossref, standard library only, no third-party server. Tested on hospital-data-breach and psychedelic-decriminalization topics.
- CLAUDE.md and README Writing Standard: Weitzman reframed from argument rules to an optional, per-piece *style mode*; added a structure layer and the voice-skill pointer.
- Separate commit for earlier uncommitted work (rigor & audit standards, `/review`).

## Files Created/Modified
`.claude/skills/write/**`, `.claude/skills/lit-search/**`, `CLAUDE.md`, `README.md`, `docs/the-flow/writing-with-ai.md`, this log.

## Errors/Blockers
- Semantic Scholar often returns HTTP 429 without an API key (shared anonymous pool). The script falls back to OpenAlex only and warns.

## Pending Steps
- Author voice skills live outside this public repo (`~/.claude/skills/<name>-voice/`).
- Optional free API keys: `~/.config/lit-search/keys.env`.
- `.git/` sits inside Dropbox, which conflicts with the standing rule against repos in synced folders; consider moving the repo.
