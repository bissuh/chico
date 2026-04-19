# BOOT.md — session startup ritual

Every session, every time. No skipping, no "I already know this." The ritual is the practice; the practice keeps the voice and the judgment intact.

Order matters. Read top to bottom.

## The ritual

1. **Read `SOUL.md`** — the reason. Re-seat why TBP exists and why Chico exists. Not optional on session 500.
2. **Read `IDENTITY.md`** — who Chico is. Re-seat the character before opening your mouth.
3. **Read `CLAUDE.md`** — the operating manual. The method.
4. **Read `SPEC.md`** — the blueprint and current status. Pay attention to the changelog (§15) and open questions (§13).
5. **Read this file (`BOOT.md`)** — catch any updates to the ritual itself.
6. **Read `USER.md`** — runtime facts about Bissuh (timezone, current context, what he's building right now).
7. **Read `TOOLS.md`** — paths, binaries, accounts, scheduled jobs. Verify nothing is broken if a scheduled run failed recently.
8. **Read all of `memory/`**:
   - `memory/core.md` — mission, scoreboards
   - `memory/bissuh.md` — deep profile
   - `memory/division-of-labor.md` — who owns what
   - `memory/permissions.md` — Green/Yellow/Red tiers
   - `memory/playbook.md` — growth playbook
9. **Read the last 2 dated memory files**: `ls -t memory/20*.md | head -2` — this is what the nightly consolidation wrote about recent work.
10. **Read the last 2–3 session files**: `ls -t sessions/*.md | head -3` — raw, un-consolidated context for the most recent days.
11. **Check `inbox/`**:
    - `cat inbox/inbox.md` if it exists
    - `ls inbox/*.md` for any individual drops
    - `ls inbox/rule-candidates-*.md` — open rule candidates waiting on Bissuh's ✅/❌
12. **Check `outbox/`** for items with `status: review-needed` that Bissuh may have responded to. Look for flipped statuses (`approved`, `changes-requested`).
13. **Check heartbeat state**: `cat memory/heartbeat-state.json` — when did consolidation last run? Are we behind?
14. **Read `SUBAGENT-POLICY.md`** only if planning delegation; otherwise skip.
15. **Start a new session file**: `sessions/YYYY-MM-DD-HH-MM-<topic>.md` using the template in `sessions/README.md`.

## After the ritual: first decisions

Before doing work, ask in order:

1. **Is there anything urgent in the inbox?** Unblockers first.
2. **Are there approved outbox items that need to ship?** Shipping is higher priority than drafting new things.
3. **Are there open rule candidates Bissuh marked ✅?** Port them before the next consolidation run overwrites the inbox.
4. **What does the last session file say I queued for today?** If yes, start there.
5. **If none of the above: what moves a scoreboard today?** (See `memory/core.md`.)

## When the ritual surfaces a conflict

If reading these files reveals contradictions (CLAUDE.md says X, memory says Y, a session log says Z), trust the file highest in the hierarchy and flag the lower one as stale:

1. SOUL.md (the reason — always wins)
2. IDENTITY.md (who Chico is)
3. CLAUDE.md (operating method)
4. SPEC.md (current state of the build)
5. memory/permissions.md + memory/division-of-labor.md (the split)
6. Other memory files
7. Session logs and inbox notes

Drift happens. Catching it at boot is cheaper than fixing it after a mis-shipped post.

## When NOT to do the full ritual

Rarely. Three exceptions:

1. **Scheduled runs** (`consolidate-memory.sh` and similar) already embed a reduced ritual in the prompt. They do not need to re-run this full boot — the scheduled prompts are narrower.
2. **One-shot tool invocations** Bissuh triggers mid-session with an explicit "just do X" — you are already inside a session, the ritual was done at the top of it.
3. **Debugging a broken file** — if CLAUDE.md itself is broken and you are fixing it, obviously read what you're fixing.

Every other case: do the ritual.

## If the ritual takes too long

It should not. Total read volume is under 50KB as of 2026-04-19. If the files grow past what is readable in a minute, that is a signal to split or archive — not to skip.
