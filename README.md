# Chico

AI co-founder of The Billion Person.

## What this folder is

Chico's operating system. Everything Chico needs to work on TBP lives here. This folder is the source of truth for Chico's identity, memory, permissions, and output.

## Folder map

```
chico/
  SOUL.md                The reason. Read first.
  IDENTITY.md            Who Chico is as a character. Read second.
  CLAUDE.md              Operating rules. Read third.
  SPEC.md                Project blueprint + roadmap + current status.
  README.md              This file.
  memory/                Persistent memory across sessions
    core.md              Mission, vision, three scoreboards
    bissuh.md            Who Bissuh is, how he works, his voice
    division-of-labor.md Who owns what
    permissions.md       Green / Yellow / Red tier system
    playbook.md          Growth playbook (living doc)
  knowledge-base/        Sources Chico studies (teardowns, tactics)
    README.md            How to use it, priority sources
  skills/                Repeatable workflows (starts empty, earned)
    README.md
  sessions/              Daily work logs, one file per day
    README.md
  inbox/                 Bissuh drops tasks/ideas here
    README.md
  outbox/                Finished drafts waiting for review
    README.md
```

## Getting started (for Chico, at the start of a session)

1. Read `SOUL.md` (the reason)
2. Read `IDENTITY.md` (who you are)
3. Read `CLAUDE.md` (the method)
4. Read `SPEC.md` (the blueprint, roadmap, current status)
5. Read all `memory/*.md` files
6. Check `inbox/` for new items
7. Check the last few `sessions/` entries for context
8. Start a new session file for today: `sessions/YYYY-MM-DD-HH-MM-<topic>.md`
9. Work

## Getting started (for Bissuh, dropping work)

- Drop tasks/ideas/links into `inbox/inbox.md` (or separate files, either works)
- Review drafts in `outbox/` — flip `status:` to `approved` when good
- Read `sessions/` any time you want to see what Chico's been doing
- Update `memory/*.md` directly if something has changed (division of labor, permissions, etc.)

## Rules for this folder

- Do not delete session files. They are the audit trail.
- Do not let memory files drift. Update them when facts change.
- Do not add skills before they're earned.
- Do not let outbox drafts pile up. Ship, archive, or drop.

## Related

- TBP Writing Manual: `/Users/bissuh/Documents/TBP/TBP-WRITING-MANUAL.md`
- Newsletter format guide: `/Users/bissuh/Documents/TBP/newsletter-format-guide.md`
- Existing TBP content: `/Users/bissuh/Documents/TBP/Articles/`
