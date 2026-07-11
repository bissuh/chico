---
name: youtube-connector
description: Query the project's YouTube channel state and do competitive research on YouTube via the YouTube Data API v3. Read-only public data. Reads the channel id and API key from the host project's .env (YOUTUBE_CHANNEL_ID, YOUTUBE_API_KEY) and the scoreboard and voice from brand.md. Invoke when asked about channel growth, video performance, which videos are driving views, competitor research on other channels in the niche, or when pulling a weekly YouTube snapshot for a content draft or a health review.
---

# youtube-connector

Direct read access to YouTube Data API v3. Thin wrapper around public data endpoints via `scripts/youtube.sh`.

**Before you start:** read the host project's `brand.md`. It names the channel, the scoreboard the numbers tie back to, and the voice for any written summary. Confirm the project's `.env` at its root has `YOUTUBE_API_KEY` and `YOUTUBE_CHANNEL_ID`. The connector supplies the reads. `brand.md` and `.env` supply the specifics.

## When to invoke

- Weekly review. Pull channel snapshot, top-performing video, engagement delta.
- Any question about YouTube state (subs, views, video-level performance).
- Competitive research (search other creators in the niche, study their video strategies).
- Before drafting a project content piece (newsletter, video, post) when a YouTube metric is worth including.
- When proposing a YouTube-specific experiment and you need a baseline.

## When NOT to invoke

- Private analytics (watch time retention curves, demographics, revenue). Requires OAuth. Out of scope for this connector, which is public data only.
- Uploading or editing videos. Out of scope. That is a write action behind an approval flow, not this read-only connector.
- Replying to comments autonomously. The owner handles replies per the project's voice policy (`brand.md`). This connector can READ comments; any drafted response goes to review, never posted from here.

## How to use

The wrapper travels with this connector: `scripts/youtube.sh`. Point it at any channel by giving the host project a `.env` at its root with two vars:

```
YOUTUBE_API_KEY=...        # a YouTube Data API v3 key
YOUTUBE_CHANNEL_ID=...     # the project's channel id (also recorded in brand.md)
```

The wrapper loads both from the host project's `.env` and hardcodes nothing. Same wrapper, different `.env`, different channel. Output is raw JSON by default; pipe to `jq` or `python3` to format.

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

# Search YouTube (competitive research in any niche)
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

Day-to-day use for routine reporting is under 50 units. Search should be deliberate, not exploratory.

## Reporting convention

When invoking this connector to answer the owner:
1. State the headline number (subs, top video, trend)
2. Compare to last report where possible (previous week, previous month)
3. Flag any metric moving faster or slower than expected
4. Tie back to the project's scoreboard (`brand.md`, the numbers that matter here)

## Healthy ranges and benchmarks (evolving)

Early-stage YouTube (first 90 days) is about proving signal, not hitting metrics. Track:
- **Shorts views** in first 24h (discovery signal)
- **Long-form like rate** (likes / views, high = strong per-viewer signal)
- **Comment-to-view rate** (community engagement)
- **Subscriber-per-view ratio** (conversion from watcher to fan)

Real benchmarks emerge from the project's own 90-day data plus competitor study.

## Related

- The host project's `brand.md`. Which channel, the scoreboard the numbers tie back to, and the voice for any written summary. Source of truth for specifics.
- `turma:beehiiv-connector`. Sibling connector, same read-only public-data pattern for the newsletter side.
- `turma:cta-machine`. Consumes this channel data to run the YouTube Shorts growth machine.
- `turma:power-law`. Which videos to double down on (the converters) and which to retire.

## Hard rules

- Reads only. Never writes. Never uploads. Never comments on the owner's behalf.
- Public data only. No OAuth. Private analytics (retention curves, demographics, revenue) are out of scope.
- No scraping, no unofficial endpoints, no circumventing quota with multiple keys.
- Reads creds from the host project's `.env` and the channel, scoreboard, and voice from `brand.md`. Never hardcodes a channel or a key.
- Never edits operating canon (`SOUL.md`, `IDENTITY.md`, `CLAUDE.md`, `SPEC.md`, `memory/`).
- Search results may include content you disagree with. Report factually, do not filter.
