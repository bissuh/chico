---
name: youtube-api
description: Query The Billion Person's YouTube channel state + do competitive research on YouTube via the YouTube Data API v3. Read-only public data. Invoke when Bissuh asks about channel growth, video performance, which videos are driving views, competitor research on other AI/creator channels, or when pulling a weekly YouTube snapshot for the Chico Note or a health review.
---

# youtube-api

Direct read access to YouTube Data API v3. Thin wrapper around public data endpoints via `scripts/youtube.sh`.

## When to invoke

- Weekly review — pull channel snapshot, top-performing video, engagement delta
- Any question about YouTube state (subs, views, video-level performance)
- Competitive research (search other creators, study their video strategies)
- Before drafting the Chico Note when a YouTube metric is worth including
- When proposing a YouTube-specific experiment and we need a baseline

## When NOT to invoke

- Private analytics (watch time retention curves, demographics, revenue) — requires OAuth. Tracked in `backlog.md` as B-003. Out of scope for this skill.
- Uploading or editing videos — out of scope, separate skill with approval flow.
- Replying to comments autonomously — Bissuh handles replies per `memory/` voice policy. This skill can READ comments; responses go through outbox for review.

## How to use

Wrapper lives at `scripts/youtube.sh`. Loads `YOUTUBE_API_KEY` and `YOUTUBE_CHANNEL_ID` from `.env`.

### Core commands

```bash
# Channel snapshot (subs, views, video count, branding)
./scripts/youtube.sh channel

# Recent uploads (default 10), newest first
./scripts/youtube.sh uploads 10

# Full detail + stats for one video
./scripts/youtube.sh video <video_id>

# Batch pull stats for up to 50 videos
./scripts/youtube.sh videos <id1,id2,id3>

# Search YouTube (competitive research)
./scripts/youtube.sh search "vibe coding newsletter" 10

# Top comments on a video
./scripts/youtube.sh comments <video_id>

# Escape hatch
./scripts/youtube.sh raw /channels "part=topicDetails&id=$YOUTUBE_CHANNEL_ID"
```

## Quota notes

Default YouTube Data API quota is 10,000 units/day. Costs:
- Read calls (channel, video, playlistItems): 1 unit each
- Search: 100 units each (expensive)

Day-to-day use for TBP reporting is under 50 units. Search should be deliberate, not exploratory.

## Reporting convention

When invoking this skill to answer Bissuh:
1. State the headline number (subs, top video, trend)
2. Compare to last report where possible (previous week, previous month)
3. Flag any metric moving faster or slower than expected
4. Tie back to narrative/health/thesis scoreboard

## Healthy ranges and benchmarks (evolving)

Early-stage YouTube (first 90 days) is about proving signal, not hitting metrics. Track:
- **Shorts views** in first 24h (discovery signal)
- **Long-form like rate** (likes / views, high = strong per-viewer signal)
- **Comment-to-view rate** (community engagement)
- **Subscriber-per-view ratio** (conversion from watcher to fan)

Real benchmarks will emerge from our own 90-day data + competitor study.

## Related

- `skills/beehiiv-api/SKILL.md` — sibling skill, same read-only pattern
- `backlog.md` → B-001 (done, beehiiv) and B-003 (queued, YouTube OAuth for private analytics)
- `knowledge-base/matt-mcgarry/tactics.md` → ADAPT framework covers YouTube as a repurposing target

## Hard rules

Reads only. Never writes. Never uploads. Never comments on Bissuh's behalf.
No scraping, no unofficial endpoints, no circumvention of quota via multiple keys.
Search results may include content we disagree with — report factually, don't filter.
