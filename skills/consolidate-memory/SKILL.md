---
name: consolidate-memory
description: Nightly job. Reads today's session logs, compresses them into a dated memory file, and proposes rule candidates for Bissuh to review. Runs at 2am via launchd. Also invocable manually at the end of a heavy day.
---

# consolidate-memory

The insatiability engine. Without this skill, every morning Chico wakes up forgetting yesterday. With it, Chico compounds.

Two jobs, one run:

1. **Compress** today's sessions into a durable, compact memory entry. (Green, autonomous.)
2. **Propose** rule candidates where patterns in the sessions suggest a new rule, playbook tactic, or identity sharpening. (Yellow. Bissuh approves before anything is ported into CLAUDE.md, SPEC.md, IDENTITY.md, or the playbook.)

## When to run

- **Primary trigger**: daily at 02:00 local time via launchd. Plist is a separate deliverable (Phase 0 remaining).
- **Manual trigger**: end of any day Chico feels was dense enough to warrant it, or when Bissuh asks.
- **Do not** run more than once for the same calendar date. Re-running overwrites. If you need to re-run, delete the existing `memory/YYYY-MM-DD.md` first and note why in the new file.
- **If no sessions exist for the target date**: write a one-line dormant-day entry in the daily memory file and exit. No rule candidates from nothing.

## Inputs

- `sessions/YYYY-MM-DD*.md` — glob all session files for the target date. Naming convention is currently ambiguous between `sessions/README.md` (one-per-day) and `SPEC.md` §4 (many-per-day with HH-MM-topic). Glob `YYYY-MM-DD*.md` handles both; flag the conflict on first run until locked.
- `memory/*.md` — to check for duplicates before proposing rule candidates.
- `CLAUDE.md`, `SPEC.md`, `SOUL.md`, `IDENTITY.md`, `memory/playbook.md` — to check whether a "candidate" is already written somewhere. Do not propose what is already locked.
- `inbox/rule-candidates-*.md` from prior runs — so you can see what's been proposed before and whether it was approved, rejected, or still pending. Do not re-propose a rejected candidate.
- Target date: passed explicitly by the invoker. The scheduled run (`scripts/consolidate-memory.sh`, fired by launchd at 02:00) passes *yesterday's* date because 2am is already the next calendar day. Manual runs pass whatever date Bissuh specifies. If no date is passed at all, default to the most recent YYYY-MM-DD for which session files exist.

## Outputs

1. `memory/YYYY-MM-DD.md` — the consolidated daily memory. Autonomous write.
2. `inbox/rule-candidates-YYYY-MM-DD.md` — only if there is at least one candidate. Max 5 per run. Autonomous write. Bissuh reviews.
3. `memory/heartbeat-state.json` — update `last_consolidation_at` field. Create the file if it does not exist yet.

Nothing else. This skill never edits `CLAUDE.md`, `SPEC.md`, `SOUL.md`, `IDENTITY.md`, `memory/permissions.md`, `memory/division-of-labor.md`, `memory/core.md`, or `memory/playbook.md`. Those are Yellow or Red. Proposals go to `inbox/`, not into the source docs.

## Procedure

1. **Resolve target date.** Default today. If invoked with a date argument (YYYY-MM-DD), use that.
2. **Glob session files.** `sessions/<date>*.md`. If zero matches, write dormant-day entry and stop.
3. **Read every matched session in full.** Do not skim.
4. **Extract structured facts from each session:**
   - Work shipped (with tier tag).
   - Decisions locked.
   - Outstanding items and blockers.
   - Explicit "Rule candidates" section content (if the session used the format).
   - Patterns: things that happened twice or are worth remembering even if not locked as rules.
5. **Deduplicate against existing memory.** If a "rule candidate" pulled from a session is already codified in CLAUDE.md / SPEC.md / IDENTITY.md / playbook.md, drop it. Do not propose rules that already exist.
6. **Deduplicate against prior proposals.** Scan `inbox/rule-candidates-*.md` from the last 14 days. If a candidate is already open for review, do not duplicate. If a candidate was rejected (marked with ❌), do not re-propose unless new evidence appears (cite the new evidence explicitly).
7. **Write `memory/YYYY-MM-DD.md`** using the daily memory template below. Keep it under 2KB. If you are tempted to write more, compress harder.
8. **Write `inbox/rule-candidates-YYYY-MM-DD.md`** using the rule candidate template below. Max 5 candidates per run. If there are more than 5 plausible candidates, pick the 5 with the strongest evidence and note in the file that others were held for next run.
9. **Update `memory/heartbeat-state.json`** with `last_consolidation_at` and `last_consolidation_sessions_count`. For `last_consolidation_at`, use the ISO-8601 timestamp passed verbatim by the invoker (the shell script captures real run time at script start). Do not guess a clock value from inside the subprocess — you do not reliably know the real time.
10. **Write one line to today's session file** (or create one if this is running headless) noting that consolidation ran, with a link to both output files.

## Daily memory file format

```markdown
# Memory — YYYY-MM-DD

## Work shipped
- [Green|Yellow|Red] <one-line description> → <path to output or commit>

## Decisions locked
- <decision> — <why>

## Patterns noticed (not yet rules)
- <observation>

## Outstanding
- <open item> — <waiting on what/who>

## Rule candidates surfaced
- <count> proposed → see inbox/rule-candidates-YYYY-MM-DD.md (or: none)

## Source sessions
- <list of session filenames>
```

Dormant-day version:

```markdown
# Memory — YYYY-MM-DD

Dormant day. No sessions logged.
```

## Rule candidate file format

```markdown
# Rule candidates — YYYY-MM-DD

<intro line: how many, how to approve, deadline if any>

## Candidate 1
**Rule**: <exact wording, as Chico would write it if adopted>
**Applies to**: <CLAUDE.md §X | SPEC.md §X | IDENTITY.md | memory/playbook.md | new file>
**Evidence**: <session file(s) and dates where this pattern appeared; cite specifics, not generalities>
**Tier to adopt**: <Green | Yellow | Red — what permission tier this rule lives under once adopted>
**Confidence**: <low | medium | high>
**Chico's note**: <one sentence on why this matters or what it unlocks>

<repeat for up to 5 candidates>

## How to approve
- ✅ next to the candidate number means adopt. On next run, I will port it into the target doc and remove from this file.
- ❌ next to the candidate number means reject. I will not re-propose without new evidence.
- No mark means still pending. It carries over.

## Held for next run
<if more than 5 plausible candidates existed, list the held ones by one-line summary only>
```

## Hard constraints

- **Exit quietly on success.** Write the output files and stop. Do not print a summary to stdout. The operational log in `logs/` should be the script's own start/finish lines plus any subprocess errors, not a recap of what was written (the files themselves are the recap). If blocked at any step, print what blocked you and stop immediately — loud on failure, silent on success.
- **Never auto-edit the operating canon.** CLAUDE.md, SPEC.md, SOUL.md, IDENTITY.md, memory/permissions.md, memory/division-of-labor.md, memory/core.md, memory/playbook.md. Proposals only.
- **Never propose more than 5 candidates per run.** The inbox should stay readable in 60 seconds. If you are generating more, you are probably pattern-matching noise.
- **Never propose a generic rule.** "Always be direct" is not a rule, it is a platitude. A rule names a specific situation and a specific behavior.
- **Never propose a rule from a single session without at least one prior instance of the pattern.** One data point is a story, not a pattern. Exception: if a session contains an explicit Bissuh directive ("from now on, do X"), that is immediately proposable with confidence: high.
- **Never re-propose a rejected candidate.** Check `inbox/rule-candidates-*.md` history. Rejected means rejected, unless new evidence appears, in which case cite it.
- **Never skip deduplication against existing docs.** Proposing a rule that is already in CLAUDE.md is wasted inbox.

## Failure modes and how to handle

- **No sessions for the target date.** Write dormant-day entry. Do not invent content.
- **Session file is unreadable or malformed.** Log the failure in the daily memory file under a "Consolidation issues" section. Continue with what you can read. Do not silently drop a session.
- **More than 5 strong candidates.** Pick top 5 by evidence strength, list the rest under "Held for next run" with one-line summaries, no full proposal.
- **Same rule proposed in multiple sessions.** Merge into one candidate. Evidence section cites all sessions.
- **heartbeat-state.json missing or malformed.** Create a fresh one. Do not crash the run.
- **Target date is in the future.** Refuse. Log why.

## What success looks like

After 30 days of running, Bissuh should be able to read through the 30 daily memory files and reconstruct what Chico did, decided, and learned without opening a single session file. The rule candidates should have a healthy approve/reject ratio (too many approves means Chico is proposing only obvious rules; too many rejects means Chico is pattern-matching noise). The playbook, CLAUDE.md, and IDENTITY.md should have measurably evolved from v0.1 based on what actually happened, not what we guessed at the start.

## Graduation criteria (Yellow → Green, or v0.1 → v0.2)

This skill stays at its current scope until:
- It has shipped 14 clean runs.
- At least 5 rule candidates have been approved and ported cleanly.
- Bissuh has not had to hand-correct the daily memory file more than twice.

On graduation, candidate expansions (only after trust is earned):
- Also auto-update `memory/playbook.md` when a candidate is approved (saving Bissuh the port step).
- Also propose edits to specific CLAUDE.md sections as diffs, not just prose rules.
- Roll up into a weekly review artifact every Sunday.

None of that happens in v0.1.
