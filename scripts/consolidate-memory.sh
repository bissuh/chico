#!/bin/zsh
# Nightly consolidation. Invokes Chico via `claude -p` to run the
# consolidate-memory skill against a target date (default: yesterday).
#
# Usage:
#   ./consolidate-memory.sh              # consolidates yesterday
#   ./consolidate-memory.sh 2026-04-15   # consolidates the given date

set -euo pipefail

WORKSPACE="/Users/bissuh/Documents/TBP/chico"
LOG_DIR="$WORKSPACE/logs"
TARGET_DATE="${1:-$(date -v-1d +%Y-%m-%d)}"
RUN_STARTED="$(date -Iseconds)"
LOG_FILE="$LOG_DIR/consolidate-$(date +%Y-%m-%d).log"

mkdir -p "$LOG_DIR"
cd "$WORKSPACE"

# NVM installs claude under ~/.nvm/versions/node/<ver>/bin, which is only on
# PATH after ~/.zshrc runs. launchd's login shell does not always source it,
# so source defensively. Silent failure is OK; the next check catches missing
# claude.
[[ -f "$HOME/.zprofile" ]] && source "$HOME/.zprofile" 2>/dev/null || true
[[ -f "$HOME/.zshrc" ]]   && source "$HOME/.zshrc"   2>/dev/null || true

if ! command -v claude >/dev/null 2>&1; then
    echo "[$RUN_STARTED] ERROR: claude not found on PATH after sourcing shell config" >> "$LOG_FILE"
    exit 1
fi

echo "[$RUN_STARTED] consolidate-memory: target=$TARGET_DATE  claude=$(command -v claude)" >> "$LOG_FILE"

PROMPT="You are Chico. Start-of-session ritual: read SOUL.md, IDENTITY.md, CLAUDE.md, SPEC.md, then memory/core.md + memory/bissuh.md + memory/division-of-labor.md + memory/permissions.md + memory/playbook.md. Then run the consolidate-memory skill per skills/consolidate-memory/SKILL.md. Target date: $TARGET_DATE. Run timestamp (use verbatim as last_consolidation_at in heartbeat-state.json, do not guess): $RUN_STARTED. Follow the skill's procedure exactly. Do not skip deduplication against existing docs or prior rule-candidate files. Do not edit operating canon. Write only to memory/$TARGET_DATE.md, inbox/rule-candidates-$TARGET_DATE.md (only if there are candidates), and memory/heartbeat-state.json. Exit quietly on success: write the files and stop, no summary to stdout. If blocked at any step, report what blocked you and stop."

claude -p "$PROMPT" --permission-mode acceptEdits >> "$LOG_FILE" 2>&1 || {
    EXIT_CODE=$?
    echo "[$(date -Iseconds)] consolidate-memory: claude exited $EXIT_CODE" >> "$LOG_FILE"
    exit $EXIT_CODE
}

echo "[$(date -Iseconds)] consolidate-memory: finished target=$TARGET_DATE" >> "$LOG_FILE"
