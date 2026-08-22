# Chico

A portable, open-source specialist you install into any project. The crew a one person project cannot otherwise afford: product judgment, design, engineering, marketing, and distribution.

## What this is

Two layers:

- **turma** (`turma/`) is the craft. An open-source Claude Code plugin: skills, a specialist agent, and commands that install into any project. It reads one file, `brand.md`, and adapts to that project's voice, audience, and goal. Clone it, drop it into your own Claude Code project, and you have a crew. It started as growth craft and widened on 2026-08-22 to cover whatever a project needs, so today's shipped skills are still growth heavy.
- **Chico** is the operator. A character, named after Chico Bento (the underestimated farm kid who ends up right), who wields turma, runs the work, watches the numbers, and writes what worked back into the craft so it compounds.

The plugin is the body of knowledge. Chico is the practitioner. This repo is both: turma to use, and Chico's operating canon (`SOUL.md`, `IDENTITY.md`, `CLAUDE.md`, `SPEC.md`) if you want to see how the operator is wired.

## Use turma in your project

Development mode, no install:
```
claude --plugin-dir /path/to/chico/turma
```
Or install via the local marketplace:
```
/plugin marketplace add /path/to/chico
/plugin install turma@chico-marketplace
```
Then either:
- **Summon the operator:** `/turma:chico` reads your project's `brand.md` and starts working it in character.
- **Call a single specialist:** `turma:story-craft`, `turma:name-craft`, `turma:power-law`, and the rest.

First step in any project: copy `turma/templates/brand.template.md` to `growth/brand.md` and fill it in. Every skill reads it.

## What turma ships

**Skills** (`turma/skills/`, invoked as `turma:<name>`):
- `story-craft`: persuasion via the 5-line framework
- `name-craft`: naming via Placek's Lexicon method, with domain checks
- `micromagnet-craft`: 2-minute opt-in tools
- `anti-ai-linguo`: the final voice pass, strips AI tells and dashes
- `power-law`: treat content and growth as a power law, run the barbell
- `ghostshelf`: build and run a faceless page that sells a digital product
- `cta-machine`: an AI-assisted YouTube Shorts growth machine
- `beehiiv-connector`, `youtube-connector`: read-only data pulls

**Operator + entry points:**
- `agents/chico`: the portable Chico persona
- `/turma:chico`: summon him into a project

## Folder map

```
chico/
  SOUL.md              The reason. Chico's mission.
  IDENTITY.md          Who Chico is (the character).
  CLAUDE.md            How Chico operates.
  SPEC.md              The blueprint, roadmap, and status.
  README.md            This file.
  turma/               THE CRAFT (the open-source plugin)
    .claude-plugin/plugin.json
    skills/            the specialists
    agents/chico.md    the portable operator
    commands/          entry points (/turma:chico, ...)
    templates/         the brand.md + learnings.md contracts
    examples/          a filled (fictional) brand.md
  .claude-plugin/marketplace.json   makes turma installable
  RUNTIME.md           Layer 2 (autonomous runtime) design, not activated
  backlog.md           what is queued
  memory/              private: mission, permissions, roster   (gitignored)
  clients/             private: per-project brand.md + learnings (gitignored)
  playbooks/           private: per-project channel playbooks  (gitignored)
  knowledge-base/      private: raw research and teardowns     (gitignored)
  standards/           PUBLIC: the rubrics Chico grades against
  inbox/ outbox/ sessions/   private working dirs              (gitignored)
```

## Public vs private

The craft is public on purpose. Business data never is. A filled `brand.md`, real `learnings.md`, API keys, and client names stay gitignored (`clients/`, `**/growth/brand.md`, `**/*.local.md`, `memory/`, `.env*`). The public canon and turma name no project. Only a generalized, sanitized technique ever crosses from a client's work back into turma.

## Getting started

**If you're Chico, at the start of a session:** read `SOUL.md`, `IDENTITY.md`, `CLAUDE.md`, `SPEC.md`, then `memory/*`. Know which project you're growing, read its `brand.md`, then work.

**If you're a builder cloning turma:** point Claude Code at `turma/` with `--plugin-dir`, drop a filled `brand.md` in your project, and run `/turma:chico`.
