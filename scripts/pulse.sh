#!/bin/bash
# pulse.sh — pull the full TBP audience board in one shot.
# Run at the start of every work session. Prints a dated snapshot of every channel.
# Sources curl-able feeds: beehiiv (REST), Search Console (impersonated SA), YouTube Data API, Postiz.
# Site traffic still comes from the beehiiv MCP (get_website_analytics) — not in the public REST API.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1
set -a; source .env 2>/dev/null; set +a

DATE=$(date +%Y-%m-%d)
SA="chico-reader@backstage-bot.iam.gserviceaccount.com"
say(){ printf '%s\n' "$*"; }

say "===================== TBP PULSE  $DATE ====================="

say ""; say "## NEWSLETTER (beehiiv)"
curl -s -m 20 -H "Authorization: Bearer ${BEEHIIV_API_KEY:-}" \
  "https://api.beehiiv.com/v2/publications/${BEEHIIV_PUB_ID:-}?expand[]=stats" \
  | jq -r '.data.stats as $s | "  active_subs: \($s.active_subscriptions // "?")   open: \($s.average_open_rate // "?")   click: \($s.average_click_rate // "?")"' 2>/dev/null \
  || say "  (beehiiv REST unavailable — use MCP get_publication_stats)"

say ""; say "## SEO / SEARCH CONSOLE (last 28d)"
TOK=$(gcloud auth print-access-token --impersonate-service-account="$SA" --scopes=https://www.googleapis.com/auth/webmasters.readonly 2>/dev/null)
if [ -n "$TOK" ]; then
  END=$(date -v-2d +%Y-%m-%d 2>/dev/null || date -d '2 days ago' +%Y-%m-%d)
  START=$(date -v-30d +%Y-%m-%d 2>/dev/null || date -d '30 days ago' +%Y-%m-%d)
  curl -s -m 25 -H "Authorization: Bearer $TOK" -H "Content-Type: application/json" \
    "https://www.googleapis.com/webmasters/v3/sites/sc-domain%3Athebillionperson.com/searchAnalytics/query" \
    -d "{\"startDate\":\"$START\",\"endDate\":\"$END\"}" \
    | jq -r '.rows[0] as $r | "  impressions: \($r.impressions // 0)   clicks: \($r.clicks // 0)   ctr: \((((($r.ctr // 0)*1000)|round)/10))%   avg_pos: \(((($r.position // 0)*10)|round)/10)"' 2>/dev/null \
    || say "  (GSC query failed)"
else say "  (impersonation token failed — check the chico-reader SA)"; fi

say ""; say "## YOUTUBE (channel, lifetime)"
curl -s -m 20 "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=${YOUTUBE_CHANNEL_ID:-}&key=${YOUTUBE_API_KEY:-}" \
  | jq -r '.items[0].statistics as $s | "  subs: \($s.subscriberCount)   total_views: \($s.viewCount)   videos: \($s.videoCount)"' 2>/dev/null \
  || say "  (YT Data API failed)"

say ""; say "## SOCIAL (Postiz, latest values)"
pz(){ curl -s -m 20 -H "Authorization: ${POSTIZ_API_KEY:-}" "https://api.postiz.com/public/v1/analytics/$2?date=30" \
   | jq -rc --arg L "$1" '"  \($L): " + ([.[] | "\(.label)=\(.data[-1].total)"] | join("  "))' 2>/dev/null || say "  $1: (failed)"; }
pz "INSTAGRAM" "cmpisrqck03e2qm0yc8qzt72e"
pz "TIKTOK"    "cmpiuhmut03mcqm0ykb99rjow"
pz "YOUTUBE"   "cmoyuys5108jxl70yk63ihmco"

say ""; say "=========================================================="
say "Next: append the deltas to memory/metrics-log.md and pull site traffic via beehiiv MCP."
