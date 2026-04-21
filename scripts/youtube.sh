#!/usr/bin/env bash
#
# youtube.sh — thin wrapper around YouTube Data API v3 (public data).
# Loads YOUTUBE_API_KEY and YOUTUBE_CHANNEL_ID from .env at repo root.
# Returns raw JSON by default. Pipe to jq or python for formatting.
#
# Scope: public data only. No OAuth. Can NOT read private analytics
# (watch time retention, audience demographics, revenue). Those need
# a separate OAuth flow, tracked in backlog as B-003.
#
# Usage:
#   ./scripts/youtube.sh <subcommand> [args]
#
# Subcommands:
#   channel                 TBP channel snapshot (subs, views, video count)
#   uploads [limit]         Recent uploads (default 10), newest first
#   video <video_id>        Full detail + stats for one video
#   videos <id,id,id>       Batch stats for up to 50 video IDs, comma-separated
#   search <query> [limit]  Search YouTube (e.g. competitor research), default 10
#   comments <video_id>     Top-level comments on a video (up to 20)
#   raw <path> [query]      Hit any endpoint, e.g. raw /search "q=ai&type=channel"
#
# Quota: each call counts against YouTube Data API daily quota (10K units default).
# Simple reads are 1 unit, search is 100 units. Use search sparingly.

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

: "${YOUTUBE_API_KEY:?YOUTUBE_API_KEY missing from .env}"
: "${YOUTUBE_CHANNEL_ID:?YOUTUBE_CHANNEL_ID missing from .env}"

API_BASE="https://www.googleapis.com/youtube/v3"

call() {
  local path="$1"
  local query="${2:-}"
  local url="$API_BASE$path?key=$YOUTUBE_API_KEY"
  if [[ -n "$query" ]]; then
    url="$url&$query"
  fi
  curl -sS "$url"
}

get_uploads_playlist() {
  call "/channels" "part=contentDetails&id=$YOUTUBE_CHANNEL_ID" \
    | python3 -c "import sys,json; print(json.load(sys.stdin)['items'][0]['contentDetails']['relatedPlaylists']['uploads'])"
}

cmd="${1:-}"
shift || true

case "$cmd" in
  channel)
    call "/channels" "part=snippet,statistics,contentDetails,brandingSettings&id=$YOUTUBE_CHANNEL_ID"
    ;;
  uploads)
    limit="${1:-10}"
    playlist_id=$(get_uploads_playlist)
    call "/playlistItems" "part=snippet,contentDetails&playlistId=$playlist_id&maxResults=$limit"
    ;;
  video)
    video_id="${1:?video_id required}"
    call "/videos" "part=snippet,statistics,contentDetails,topicDetails&id=$video_id"
    ;;
  videos)
    ids="${1:?comma-separated video IDs required}"
    call "/videos" "part=snippet,statistics,contentDetails&id=$ids"
    ;;
  search)
    query="${1:?query required}"
    limit="${2:-10}"
    encoded=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote_plus(sys.argv[1]))" "$query")
    call "/search" "part=snippet&q=$encoded&maxResults=$limit&type=video,channel"
    ;;
  comments)
    video_id="${1:?video_id required}"
    call "/commentThreads" "part=snippet&videoId=$video_id&maxResults=20&order=relevance"
    ;;
  raw)
    path="${1:?path required, e.g. /search}"
    query="${2:-}"
    call "$path" "$query"
    ;;
  ""|help|-h|--help)
    sed -n '3,26p' "$0"
    ;;
  *)
    echo "unknown subcommand: $cmd" >&2
    sed -n '3,26p' "$0" >&2
    exit 1
    ;;
esac
