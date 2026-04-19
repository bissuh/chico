#!/bin/zsh
# 30-minute heartbeat. Commits any tracked changes to git and updates
# memory/heartbeat-state.json. No LLM calls. No side effects beyond git.
#
# Invoked every 30 minutes by launchd (com.tbp.chico.heartbeat) and
# manually as needed.

set -euo pipefail

WORKSPACE="/Users/bissuh/Documents/TBP/chico"
LOG_DIR="$WORKSPACE/logs"
RUN_STARTED="$(date -Iseconds)"
TICK_HUMAN="$(date +'%Y-%m-%d %H:%M')"
LOG_FILE="$LOG_DIR/heartbeat-$(date +%Y-%m-%d).log"
STATE_FILE="$WORKSPACE/memory/heartbeat-state.json"

mkdir -p "$LOG_DIR"
cd "$WORKSPACE"

# Load shell config so git and related tools are on PATH under launchd.
[[ -f "$HOME/.zprofile" ]] && source "$HOME/.zprofile" 2>/dev/null || true
[[ -f "$HOME/.zshrc" ]]   && source "$HOME/.zshrc"   2>/dev/null || true

if ! command -v git >/dev/null 2>&1; then
    echo "[$RUN_STARTED] ERROR: git not found on PATH" >> "$LOG_FILE"
    exit 1
fi

# Stage everything not excluded by .gitignore. This captures modifications,
# deletions, and new files in operating-canon paths (scripts/, skills/,
# root *.md). The .gitignore is the gate: memory/, inbox/, outbox/, sessions/,
# logs/, and USER.md stay local.
git add -A

if git diff --cached --quiet; then
    # No tracked changes. Silent no-op is correct for a heartbeat.
    :
else
    COMMIT_MSG="chore(heartbeat): $TICK_HUMAN checkpoint"
    if ! git commit -m "$COMMIT_MSG" >> "$LOG_FILE" 2>&1; then
        echo "[$(date -Iseconds)] ERROR: heartbeat commit failed" >> "$LOG_FILE"
        exit 1
    fi
    echo "[$(date -Iseconds)] heartbeat: committed \"$COMMIT_MSG\"" >> "$LOG_FILE"
fi

# Update heartbeat-state.json. Preserve any existing fields (e.g. consolidation
# timestamps) by reading and merging, falling back to a fresh object on parse
# error or missing file.
python3 - "$STATE_FILE" "$RUN_STARTED" <<'PY' 2>>"$LOG_FILE"
import json, os, sys
path, ts = sys.argv[1], sys.argv[2]
state = {}
if os.path.exists(path):
    try:
        with open(path) as f:
            state = json.load(f)
            if not isinstance(state, dict):
                state = {}
    except Exception:
        state = {}
state["last_heartbeat_at"] = ts
with open(path, "w") as f:
    json.dump(state, f, indent=2)
    f.write("\n")
PY
