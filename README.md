# Chico

AI co-founder of The Billion Person.

## What this folder is

Chico's operating system. Everything Chico needs to work on TBP lives here. This folder is the source of truth for Chico's identity, memory, permissions, and output.

This repo is **public and open source**. If you're here looking for ideas, the short version is: one human co-founder (Bissuh) plus one AI co-founder (Chico, running on Claude Code) building a newsletter business together, in the open. The point is the co-work, not the automation.

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
    consolidate-memory/  Nightly memory compression + rule candidates
    beehiiv-api/         Read-only access to TBP's beehiiv publication
  scripts/               Shell wrappers called by skills or schedulers
    beehiiv.sh           beehiiv API wrapper (see skills/beehiiv-api)
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
3. The current `.env.example` covers the `beehiiv-api` skill. If you don't use beehiiv, skip that section or delete the skill.
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
