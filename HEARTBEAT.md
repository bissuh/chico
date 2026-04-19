# HEARTBEAT.md — the 30-minute loop

The heartbeat is operational hygiene, not thinking. It runs every 30 minutes via launchd, does a small, predictable set of things, and exits.

It is deliberately boring. If the heartbeat starts trying to be smart, it will drift into low-value work that clogs logs and creates surprise commits. Keep it dumb.

## What the heartbeat does

On every tick:

1. **Commit tracked changes to git.** Stages everything not excluded by `.gitignore` via `git add -A`. This covers edits, deletions, and new files in operating-canon paths (SOUL.md, IDENTITY.md, CLAUDE.md, SPEC.md, BOOT.md, TOOLS.md, HEARTBEAT.md, SUBAGENT-POLICY.md, README.md, scripts/**, skills/**, knowledge-base/README.md). The `.gitignore` is the gate — if a file should stay local, gitignore it. USER.md, memory/, inbox/, outbox/, sessions/, logs/ are all local-only.
2. **Update `memory/heartbeat-state.json`** with `last_heartbeat_at` (ISO-8601).
3. **Exit.**

That is the whole job.

## What the heartbeat does NOT do

- Does not read `memory/` / `inbox/` / `outbox/` / `sessions/` beyond what git needs.
- Does not run the consolidate-memory skill (that's a separate 02:00 job).
- Does not propose rule candidates, draft content, or touch anything subscriber-facing.
- Does not push to a remote (no remote is configured yet; adding one is Red-tier).
- Does not invoke `claude -p`. The heartbeat is pure shell. No LLM calls. Cheap, fast, silent.

The heartbeat is not "mini consolidation." It is git commit + timestamp. That is on purpose.

## The daily and weekly rhythms live elsewhere

This file is named HEARTBEAT.md because SPEC §4 and §8 called for a heartbeat file, but the actual rhythm is three-tiered:

- **30 min** — heartbeat (this file). Git commit, timestamp, exit. `scripts/heartbeat.sh` via `com.tbp.chico.heartbeat` launchd job.
- **Daily 02:00** — consolidation. Reads yesterday's sessions, compresses to memory, proposes rule candidates. `scripts/consolidate-memory.sh` via `com.tbp.chico.consolidate-memory` launchd job. Already installed as of 2026-04-19.
- **Weekly Sunday** — review. Scoreboards, experiment results, next week's plan. `skills/weekly-review/` — not yet built.

## What a good heartbeat commit message looks like

```
chore(heartbeat): 2026-04-19 15:30 checkpoint
```

Conventional Commits format. `chore(heartbeat)` scope. Timestamp in the message body is the tick time. Nothing more.

If git has nothing to commit (no tracked changes), the script exits without touching anything. Empty commits clutter history.

## Failure modes

- **Git commit fails** (e.g., hook rejected): log the failure, do not retry, exit non-zero so launchd surfaces it in `.err`. Bissuh investigates at his next session.
- **heartbeat-state.json is missing or malformed**: create it fresh.
- **Working directory is mid-change** (Bissuh is editing a file right now): the commit may pick up an incomplete state. Acceptable — the next heartbeat will capture the completed state, and git history is the recovery path.
- **Lock file or concurrent claude session writing to workspace**: git does not care; it commits whatever is on disk at the moment it runs. If this becomes a problem, add a lockfile check in a later version. Not in v0.1.

## When to run the heartbeat manually

- After a heavy editing session, to checkpoint the work immediately rather than wait up to 30 min.
- Before shutting the laptop, so the latest state is captured.
- When debugging git state.

Manual invocation:
```sh
./scripts/heartbeat.sh
```

## Installing the heartbeat job

The plist is at `scripts/launchd/com.tbp.chico.heartbeat.plist`. Install the same way as the consolidation job (see `scripts/README.md`):

```sh
cp scripts/launchd/com.tbp.chico.heartbeat.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.tbp.chico.heartbeat.plist
launchctl list | grep tbp.chico
```

As with the consolidation plist, loading is Red-tier — Bissuh runs the install command, not Chico.

## Graduation

The heartbeat is v0.1. It may grow to include:
- Remote push (once a remote is configured)
- A dashboard update (once `canvas/` exists)
- A check-in that prints a one-line status if any scheduled job has been failing

None of that in v0.1. Prove the 30-min commit is reliable first.
