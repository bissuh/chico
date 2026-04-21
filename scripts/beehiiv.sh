#!/usr/bin/env bash
#
# beehiiv.sh — thin wrapper around beehiiv v2 REST API.
# Loads BEEHIIV_API_KEY and BEEHIIV_PUB_ID from .env at repo root.
# Output is raw JSON by default. Pipe to jq or python for formatting.
#
# Usage:
#   ./scripts/beehiiv.sh <subcommand> [args]
#
# Subcommands:
#   stats                   publication-level stats (subs, opens, clicks, total sent)
#   publication             full publication details
#   posts [limit]           list recent posts (default limit 10), newest first
#   post <post_id>          full detail + stats for one post
#   subscribers [limit]     list recent subscribers (default 10), newest first
#   sub <subscription_id>   detail on one subscriber
#   segments                list segments
#   segment <segment_id>    detail on one segment
#   automations             list automations
#   raw <path> [query]      hit any endpoint, e.g. `raw /publications/$PUB/posts "limit=5"`
#
# All subcommands hit GET. Write operations are intentionally not wrapped here —
# any POST/PATCH/DELETE must be explicit and reviewed, never shell-automated.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ENV_FILE="$REPO_ROOT/.env"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "error: $ENV_FILE not found. Copy .env.example and fill in." >&2
  exit 1
fi

# shellcheck disable=SC1090
source "$ENV_FILE"

: "${BEEHIIV_API_KEY:?BEEHIIV_API_KEY missing from .env}"
: "${BEEHIIV_PUB_ID:?BEEHIIV_PUB_ID missing from .env}"

API_BASE="https://api.beehiiv.com/v2"
PUB_PATH="/publications/$BEEHIIV_PUB_ID"

call() {
  local path="$1"
  local query="${2:-}"
  local url="$API_BASE$path"
  if [[ -n "$query" ]]; then
    url="$url?$query"
  fi
  curl -sS -H "Authorization: Bearer $BEEHIIV_API_KEY" "$url"
}

cmd="${1:-}"
shift || true

case "$cmd" in
  stats)
    call "$PUB_PATH" "expand=stats"
    ;;
  publication)
    call "$PUB_PATH"
    ;;
  posts)
    limit="${1:-10}"
    call "$PUB_PATH/posts" "limit=$limit&order_by=publish_date&direction=desc&expand[]=stats"
    ;;
  post)
    post_id="${1:?post_id required}"
    call "$PUB_PATH/posts/$post_id" "expand[]=stats&expand[]=free_web_content&expand[]=free_email_content"
    ;;
  subscribers)
    limit="${1:-10}"
    call "$PUB_PATH/subscriptions" "limit=$limit&order_by=created&direction=desc&expand[]=stats&expand[]=custom_fields&expand[]=referrals"
    ;;
  sub)
    sub_id="${1:?subscription_id required}"
    call "$PUB_PATH/subscriptions/$sub_id" "expand[]=stats&expand[]=custom_fields&expand[]=referrals"
    ;;
  segments)
    call "$PUB_PATH/segments" "limit=25"
    ;;
  segment)
    segment_id="${1:?segment_id required}"
    call "$PUB_PATH/segments/$segment_id"
    ;;
  automations)
    call "$PUB_PATH/automations" "limit=25"
    ;;
  raw)
    path="${1:?path required, e.g. /publications/\$PUB/posts}"
    query="${2:-}"
    call "$path" "$query"
    ;;
  ""|help|-h|--help)
    sed -n '3,28p' "$0"
    ;;
  *)
    echo "unknown subcommand: $cmd" >&2
    sed -n '3,28p' "$0" >&2
    exit 1
    ;;
esac
