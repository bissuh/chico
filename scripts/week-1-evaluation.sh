#!/bin/zsh
# One-shot evaluation runner for the C-007 newsletter ship (Save 9 Hours a Week).
# Fires once on Sunday 2026-05-03 at 14:30 BRT via launchd, then self-disables.
#
# Why a one-shot: this evaluates week-1 signal of the first major TBP newsletter.
# After running, it removes its own plist so it never fires again.
#
# Usage (manual override, mostly for testing):
#   ./week-1-evaluation.sh

set -euo pipefail

WORKSPACE="/Users/bissuh/Documents/TBP/chico"
LOG_DIR="$WORKSPACE/logs"
PLIST_LABEL="com.tbp.chico.week-1-evaluation"
PLIST_PATH="$HOME/Library/LaunchAgents/${PLIST_LABEL}.plist"
EXPECTED_DATE="2026-05-03"
TODAY="$(date +%Y-%m-%d)"
RUN_STARTED="$(date -Iseconds)"
LOG_FILE="$LOG_DIR/week-1-evaluation-${TODAY}.log"

mkdir -p "$LOG_DIR"
cd "$WORKSPACE"

# Self-protection: only run on the expected date. launchd's StartCalendarInterval
# with Month+Day will fire every year on that date, so this guards against
# accidental future runs.
if [[ "$TODAY" != "$EXPECTED_DATE" ]]; then
    echo "[$RUN_STARTED] week-1-evaluation: skipping, today=$TODAY expected=$EXPECTED_DATE" >> "$LOG_FILE"
    exit 0
fi

# NVM installs claude under ~/.nvm/versions/node/<ver>/bin, which is only on
# PATH after ~/.zshrc runs. Source defensively (same pattern as consolidate-memory.sh).
[[ -f "$HOME/.zprofile" ]] && source "$HOME/.zprofile" 2>/dev/null || true
[[ -f "$HOME/.zshrc" ]]   && source "$HOME/.zshrc"   2>/dev/null || true

if ! command -v claude >/dev/null 2>&1; then
    echo "[$RUN_STARTED] ERROR: claude not found on PATH after sourcing shell config" >> "$LOG_FILE"
    exit 1
fi

echo "[$RUN_STARTED] week-1-evaluation: starting  claude=$(command -v claude)" >> "$LOG_FILE"

PROMPT="You are Chico, AI co-founder of The Billion Person (TBP). The first major newsletter shipped Monday 2026-04-27, titled 'Save 9 Hours a Week: The 10 AI Automations Real Operators Are Already Using'. Today is Sunday 2026-05-03 — the day before the next Monday newsletter. Your job: evaluate week-1 signal and prep edition 2.

Run-started timestamp (use verbatim where needed): ${RUN_STARTED}

## Boot ritual (read all of these before doing anything else)
1. SOUL.md, IDENTITY.md, CLAUDE.md, SPEC.md
2. memory/core.md, memory/bissuh.md, memory/division-of-labor.md, memory/permissions.md, memory/playbook.md
3. /Users/bissuh/.claude/projects/-Users-bissuh-Documents-TBP-chico/memory/MEMORY.md plus the relevant project memories: project_deli_owner_anchor_character.md, project_palinha_chico_recurring_section.md, project_palinha_2_parked_content.md, feedback_no_shorts_only_full_tutorials.md
4. sessions/2026-04-26-12-00-newsletter-ship.md (the C-007 ship session)
5. outbox/newsletter-10-automations-v3.md (what shipped)

## Part 1 — Beehiiv stats on C-007
Use scripts/beehiiv.sh (the read-only beehiiv API wrapper, see skills/beehiiv-api/SKILL.md). Find the post titled 'Save 9 Hours a Week: The 10 AI Automations Real Operators Are Already Using' sent 2026-04-27. Capture: open rate, click rate, total clicks per outbound link, reply count, unsubscribe count. Compare to TBP's prior baseline if available.

Save to outbox/c-007-week-1-stats.md as status: review-needed.

## Part 2 — Reply triage
The beehiiv API can list incoming replies via the /posts/{id}/responses endpoint or similar. If it does not expose replies through scripts/beehiiv.sh, log that gap in outbox/c-007-reply-pack.md, mark Part 2 incomplete, and note 'Bissuh provides reply data manually'.

If you do get replies: group by which of the 10 automations each reader picked. Identify (a) most-picked, (b) most-confused, (c) most-enthusiastic. Draft 3-5 templated reply variants Bissuh can adapt-and-send fast.

Save to outbox/c-007-reply-pack.md as status: review-needed.

## Part 3 — Palinha #2 draft
Use the parked content from memory project_palinha_2_parked_content.md as the base (system-sellers vs ritual-shippers angle). Tighten to 120-150 words. Drop straight into content — no meta-intro section, that was a first-edition-only convention. Sign off '— Chico' per IDENTITY.md.

Save to outbox/palinha-2-draft.md as status: review-needed.

## Part 4 — Edition 2 proposal
Based on Part 1 and Part 2 signals, recommend ONE direction for the 2026-05-04 newsletter:
(a) Deep-dive on the most-picked automation from week 1 (give people the rest of what they need to actually finish it)
(b) Volume 2 — 10 NEW automations using the same methodology (same SEO-validated, transcript-deep-dived approach)
(c) Shift angle — operator teardown of someone who shipped one of the v1 automations (could be a real reader if replies surfaced one)

Make a clear recommendation with reasoning. Save to outbox/edition-2-proposal.md as status: review-needed.

## Hard rules
- Yellow tier on EVERYTHING. Do not publish anything. All four artifacts go to outbox/ as 'status: review-needed' for Bissuh's edit pass.
- Do NOT auto-edit operating canon: CLAUDE.md, SPEC.md, SOUL.md, IDENTITY.md, memory/permissions.md, memory/division-of-labor.md, memory/core.md, memory/playbook.md.
- Append to or create sessions/2026-05-03-14-30-week-1-evaluation.md with what you did, decisions made, and any rule candidates surfaced.
- Quiet on success: write the files and stop, no summary to stdout. Loud on failure with clear blocker.
- If you discover the beehiiv API doesn't expose replies, that is NOT a failure — log it and proceed to Parts 3 and 4."

claude -p "$PROMPT" --permission-mode acceptEdits >> "$LOG_FILE" 2>&1 || {
    EXIT_CODE=$?
    echo "[$(date -Iseconds)] week-1-evaluation: claude exited $EXIT_CODE" >> "$LOG_FILE"
    # Still self-disable even on failure — we don't want a broken job firing again next year
    if [[ -f "$PLIST_PATH" ]]; then
        launchctl unload "$PLIST_PATH" 2>/dev/null || true
        rm -f "$PLIST_PATH"
        echo "[$(date -Iseconds)] week-1-evaluation: self-disabled (plist removed)" >> "$LOG_FILE"
    fi
    exit $EXIT_CODE
}

echo "[$(date -Iseconds)] week-1-evaluation: finished" >> "$LOG_FILE"

# Self-disable: unload the plist and remove it so it never fires again.
if [[ -f "$PLIST_PATH" ]]; then
    launchctl unload "$PLIST_PATH" 2>/dev/null || true
    rm -f "$PLIST_PATH"
    echo "[$(date -Iseconds)] week-1-evaluation: self-disabled (plist removed from ~/Library/LaunchAgents/)" >> "$LOG_FILE"
fi
