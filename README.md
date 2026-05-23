# Chico

AI co-founder of The Billion Person.

## What this folder is

Chico's operating system. Everything Chico needs to work on TBP lives here. This folder is the source of truth for Chico's identity, memory, permissions, and output.

This repo is **public and open source**. If you're here looking for ideas, the short version is: one human co-founder (Bissuh) plus one AI co-founder (Chico, running on Claude Code) building a newsletter business together, in the open. The point is the co-work, not the automation.

## What Chico can do

Skills are Chico's capabilities. Each one is earned — built, tested, made repeatable. The list grows as the co-work deepens.

### Skills you can clone and use

Every skill is a self-contained workflow built and tested on TBP before it ships here. Drop a folder into your own Claude Code `skills/` directory and invoke it by name. Everything's in one place on purpose, so you can grab the whole toolkit at once.

- **`ghostshelf`** — build and run a faceless (no-face) content page that sells a small digital product, end to end: pick the niche, make the product, batch the slides, wire the funnel, run the weekly loop. Honest odds baked in.
- **`micromagnet-craft`** — design, score, or extract a micromagnet: a 2-minute tool that solves one tiny problem and trades for a newsletter opt-in.
- **`story-craft`** — write or fix any persuasive piece with the 5-line framework (Mirror, Friction, Realization, Shift, Invitation).
- **`name-craft`** — name a company, product, feature, or lead magnet using David Placek's Lexicon method, with domain availability checks.
- **`anti-ai-linguo`** — voice-check a draft and strip the AI tells (long-form, short-form, and video modes).
- **`beehiiv-api`** — read a beehiiv publication's state: subscribers, opens, clicks, top posts, segments, automations.
- **`youtube-api`** — read a YouTube channel's state and research competitors via the YouTube Data API.
- **`consolidate-memory`** — roll session logs into durable daily memory and propose new rules.

The build tooling behind our own faceless launch is here too: the Remotion slide + reel renderer in `remotion/`, the operating playbook in `playbooks/faceless-gallery-engine.md`, and the run-it-yourself command in `.claude/commands/produce-week.md`.

Hard rules + how skills get added: `skills/README.md`. New skills land when a workflow has shipped cleanly at least twice, or when it's infrastructure that unlocks others.

## Folder map

```
chico/
  SOUL.md                The reason. Read first.
  IDENTITY.md            Who Chico is as a character. Read second.
  CLAUDE.md              Operating rules. Read third.
  SPEC.md                Project blueprint + roadmap + current status.
  backlog.md             Build / create / automate / experiment queue.
  HEARTBEAT.md           How the scheduled heartbeat works.
  SUBAGENT-POLICY.md     Rules for spawning subagents.
  TOOLS.md               Tool inventory and usage conventions.
  README.md              This file.
  .env.example           Template for local secrets. Copy to .env (gitignored).
  memory/                Persistent memory across sessions (gitignored)
    core.md              Mission, vision, three scoreboards
    bissuh.md            Who Bissuh is, how he works, his voice
    division-of-labor.md Who owns what
    permissions.md       Green / Yellow / Red tier system
    playbook.md          Growth playbook (living doc)
  knowledge-base/        Sources Chico studies (teardowns, tactics)
    README.md            How to use it, priority sources
    matt-mcgarry/        Newsletter growth frameworks (MAGIC, WEAC, ADAPT, ...)
  skills/                Repeatable workflows Chico can invoke
    README.md            Hard rules, starter queue, what's built
    ghostshelf/          Build + run a faceless page that sells a digital product
    micromagnet-craft/   Design/extract a 2-minute opt-in tool
    story-craft/         5-line persuasion framework
    name-craft/          Naming via Placek's Lexicon method + domain checks
    anti-ai-linguo/      Voice-check + strip AI tells
    beehiiv-api/         Read-only access to a beehiiv publication
    youtube-api/         Read-only access to YouTube Data API v3
    consolidate-memory/  Nightly memory compression + rule candidates
  playbooks/             Replicable growth playbooks
    youtube-shorts-cta-machine.md   Faceless YouTube Shorts growth pipeline
    faceless-gallery-engine.md      TBP's no-face IG/TikTok content engine
  remotion/              Slide + reel renderer (React/Remotion) for the gallery engine
  .claude/commands/      Slash commands, incl. produce-week (run the weekly content machine)
  scripts/               Shell wrappers called by skills or schedulers
    beehiiv.sh           beehiiv API wrapper (see skills/beehiiv-api)
    youtube.sh           YouTube Data API wrapper (see skills/youtube-api)
    heartbeat.sh         30-min heartbeat tick
    consolidate-memory.sh Invokes the consolidate-memory skill
    launchd/             macOS launchd plists for scheduled jobs
  sessions/              Daily work logs (gitignored)
    README.md
  inbox/                 Bissuh drops tasks/ideas here (gitignored)
    README.md
  outbox/                Finished drafts waiting for review (gitignored)
    README.md
  logs/                  Runtime logs (gitignored)
```

**What's private** (gitignored): `memory/`, `inbox/`, `outbox/`, `sessions/`, `logs/`, `USER.md`, `.env`, `.env.*` (except `.env.example`). These hold work logs, drafts in progress, secrets, and personal notes. If you're forking, the README files inside each of these directories explain what's expected to live there.

## Getting started (for Chico, at the start of a session)

1. Read `SOUL.md` (the reason)
2. Read `IDENTITY.md` (who you are)
3. Read `CLAUDE.md` (the method)
4. Read `SPEC.md` (the blueprint, roadmap, current status)
5. Read `backlog.md` (what's queued, what's in-progress, what's blocked)
6. Read all `memory/*.md` files
7. Check `inbox/` for new items
8. Check the last few `sessions/` entries for context
9. Start a new session file for today: `sessions/YYYY-MM-DD-HH-MM-<topic>.md`
10. Work

## Getting started (for Bissuh, dropping work)

- Drop tasks / ideas / links into `inbox/inbox.md` (or separate files, either works)
- Review drafts in `outbox/` — flip `status:` to `approved` when good
- Read `sessions/` any time you want to see what Chico's been doing
- Update `memory/*.md` directly if something has changed (division of labor, permissions, etc.)
- Add items to `backlog.md` if you want them on the queue

## Local setup (for anyone forking this repo)

1. Clone the repo
2. Copy `.env.example` to `.env` and fill in your own values
3. `.env.example` covers the two API-backed skills currently built (`beehiiv-api` and `youtube-api`). If you don't use one of those platforms, skip that section or delete the skill.
4. The `memory/`, `inbox/`, `outbox/`, `sessions/`, `logs/` folders are gitignored. You'll need to create them locally and drop the expected README files from the source.

## Rules for this folder

- Do not delete session files. They are the audit trail.
- Do not let memory files drift. Update them when facts change.
- Do not add skills before they're earned. See `skills/README.md`.
- Do not let outbox drafts pile up. Ship, archive, or drop.
- Secrets live in `.env` (gitignored). Never commit real keys. `.env.example` is the template.
- Anything Yellow or Red per `memory/permissions.md` stays drafts-in-outbox until Bissuh approves.

## Related

- TBP Writing Manual: `/Users/bissuh/Documents/TBP/TBP-WRITING-MANUAL.md`
- Newsletter format guide: `/Users/bissuh/Documents/TBP/newsletter-format-guide.md`
- Existing TBP content: `/Users/bissuh/Documents/TBP/Articles/`
