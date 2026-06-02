---
name: cta-machine
description: Build and run an AI-assisted YouTube Shorts growth machine end to end. Invoke when someone wants to grow a YouTube channel or drive subscribers to a destination (newsletter, app, lead magnet, product) by stitching a single branded CTA outro onto the front-hooks of already-viral Shorts, then scheduling them on autopilot. Walks the user through brand setup, building the CTA in Remotion, scraping source hooks, stitching, uploading, scheduling via Postiz, and the weekly operating loop, with the shadow-ban and Content-ID warnings baked in.
---

# CTA Machine

A complete blueprint for an AI-assisted YouTube Shorts growth machine. Drop this folder into a fresh Claude Code project and the assistant has everything needed to ship a posting pipeline for a new channel or product.

Built and open-sourced by The Billion Person. We run this exact machine on our own channel. The method is public on purpose. The one thing that is *not* in this folder is our own numbers (our CTA URL, our conversion rate, what actually worked for us). The method transfers; the results are ours to report. If you want the running teardown with real numbers, that lives in the newsletter at the destination this very machine points to.

Adapted from the Mau Baron / Ernesto Lopez "Prayer Lock" pattern: one CTA stitched onto thousands of viral hook clips, ~100k YouTube subscribers in 8 months, total cost in their telling under $50.

## What this builds

A pipeline that:

1. Renders one polished ~6-second branded CTA video using Remotion (animated text over backgrounds, with audio).
2. Scrapes top-performing YouTube Shorts from chosen creator channels (sorted by all-time view count).
3. Stitches the first 3 seconds of each scraped short onto the front of the CTA, producing ~9-second hybrid videos.
4. Uploads each finished short to Postiz cloud storage.
5. Schedules each upload to YouTube via the Postiz REST API on a 4/day, 6-hour-spaced cadence.
6. Tracks every video's lifecycle (downloaded -> stitched -> uploaded -> scheduled) in a persistent ledger so nothing repeats.

End state after week 1: ~28 viral-hook + branded-CTA shorts published to a YouTube channel, all pointing at one CTA URL.

## Why it works (in one paragraph)

The hook isn't yours. The hook is the first 3 seconds of someone else's already-viral short. YouTube's algorithm rewards retention and completion, both of which spike when a viewer is grabbed by content their friends already shared. The CTA is the only branding: the same identical outro on every video. Some viewers click through. Subscribers compound. It doesn't read as spam because the CTA is well-made (animated, branded, audio-paired) and sends viewers to something legitimately useful: a free newsletter, app, course, or product page.

## When to use this

Good fit:
- You have a single destination people can subscribe to (newsletter, app, lead magnet, paid product).
- You have a YouTube channel (existing or new) for the brand.
- You're OK with content that mixes other creators' hooks with your own outro.
- You can spend ~3-5 hours of human time per week on creative review and occasional manual posts.

Bad fit:
- Your audience is allergic to growth-hacking optics (some B2B enterprise plays).
- You don't have one clear URL to send people to.
- You're not OK with YouTube Content ID claims. The trending audio you bake into the CTA is owned by labels. Content ID detects it and routes any ad revenue to the rights holder. Your videos stay up; you just don't earn YouTube ad revenue. Fine if your model is "drive subscribers to a destination."

## What you'll need (≈$10 + a subscription you may already have)

1. **A domain** for your destination (~$10/year). Cloudflare Registrar sells at cost, no upsells.
2. **GitHub** (free) for your repo.
3. **A YouTube channel** for the brand. Profile pic, banner, and a description with the CTA URL.
4. **Postiz** (postiz.com cloud, or self-host from github.com/gitroomhq/postiz-app). Connect your YouTube account in Postiz settings. This handles scheduling.
5. **Claude Code** (claude.ai) for the assistant running this skill.
6. **A YouTube Data API key** (free, 10,000 units/day) from console.cloud.google.com after enabling "YouTube Data API v3."

Then in Postiz: Settings -> Developers -> Public API -> generate your API key.

## Stack and install

```bash
npm install -g @anthropic-ai/claude-code     # if you don't have it
npm install -g postiz                         # Postiz CLI (uploads)
brew install ffmpeg yt-dlp                     # video processing (or your OS equivalent)
pip3 install requests python-dotenv            # python deps for the scripts
```

## Setup

1. Copy this whole `cta-machine/` folder into your project (or clone the repo).
2. `cp .env.example .env` and fill in your keys (see `.env.example` for where each comes from).
3. Create the working folders the scripts expect (they auto-create on first run, but for clarity):
   ```
   assets/
   assets/source_hooks/      # scraped source shorts, per channel
   assets/finished/          # stitched outputs, per channel
   assets/cta.mp4            # your rendered CTA (built in Step 1)
   ```
4. Add to `.gitignore`: `.env`, `node_modules/`, `assets/`, `remotion/out/`, `remotion/public/bg*.png`.

By default the scripts use the current working directory as the project root. To run them from elsewhere, set `CTA_WORKDIR` to your project's absolute path.

## Step 0: Lock the brand (do this before any code)

Walk the user through these. Nothing renders well until these are decided.

| Item | What the user provides |
|---|---|
| Product name | Their brand name |
| Destination URL | The single URL, e.g. `yourdomain.com` |
| Brand color (hex) | Their accent color |
| Headline 1 (alarm) | Short imperative, attention-grab. e.g. "STOP SCROLLING." |
| Headline 2 (action) | Short imperative, what to do instead. e.g. "START BUILDING." |
| Subhead | One sentence: who it's for + proof. Keep it under ~50 chars. |
| Post title | Same on every video. Often "Hook \| yourdomain.com" |
| Post description | 2-3 lines, includes the URL |
| Post tags | 5-8 tags |
| Source channels | 2-4 YouTube handles whose audience overlaps with your customer |
| Background images | 3 images, 9:16, dominant tone = your brand color (or skip; the CTA falls back to a brand-color gradient) |

Put title/description/tags into `.env` as `CTA_POST_TITLE`, `CTA_POST_DESCRIPTION`, `CTA_POST_TAGS`.

## Step 1: Build the CTA video (Remotion)

The CTA is THE brand. Spend time here. It's the only part viewers will associate with you.

```bash
cd remotion
npm install
npm run dev        # opens Remotion Studio to preview + tweak copy live
```

Edit the copy in `remotion/src/Root.tsx` (or pass `--props` with a JSON file). The component (`remotion/src/CtaVideo.tsx`) is brand-neutral and parametrized: `headline1`, `headline2`, `subhead`, `url`, `brandColor`, and three optional backgrounds. It is three scenes with crossfades:

1. **Alarm.** Headline 1 springs in.
2. **Checklist.** Headline 1 shrinks and gets a clean CSS strike-through while headline 2 rises confidently below. The "checking off a list" feel.
3. **Offer.** Subhead enters, then the URL scales in as a hero with a subtle pulse.

A persistent URL pill rides the top of scenes 1-2, then hands off to the hero URL. Grain + vignette over the whole thing. Backgrounds get a Ken Burns push and a brand-color multiply so they stay on-palette even if the art drifts.

Render:
```bash
cd remotion
npm run render      # writes out/cta.mp4
cp out/cta.mp4 ../assets/cta.mp4
```

**Test it on a phone screen before shipping.** What's readable on a desktop preview can be mush at 320px in someone's feed.

### Backgrounds

Drop `bg1.png`, `bg2.png`, `bg3.png` into `remotion/public/` (see that folder's README). Tell a 3-act arc: trapped -> working -> free. The structural rule beats any art style: each image needs ample negative space where text lands, and a dominant tone matching your brand color. No images? It still renders on a brand-color gradient. Ship that, add art later.

## Step 2: Bake trending audio onto the CTA

A silent CTA dies in the feed. Find a trending sound, borrow its audio:

1. TikTok Creative Center -> Trends -> Sounds. Pick a trending sound, open a top video using it, copy the URL.
2. `yt-dlp -f mp4 "https://www.tiktok.com/@user/video/123" -o trending.mp4`
3. `./scripts/bake_audio.sh trending.mp4 assets/cta.mp4 cta.mp4`  (overwrites the silent CTA with the audio version)

This triggers Content ID claims. That's expected and fine (see "When to use this").

## Step 3: Scrape source hooks

```bash
./scripts/scrape_shorts.py https://www.youtube.com/@SomeCreator 25
./scripts/scrape_shorts.py @AnotherCreator 25
```

Pulls top shorts by all-time view count, filters to <=90s (true Shorts), downloads to `assets/source_hooks/{slug}/`, writes a `manifest.json`. Re-running skips files already on disk. Cost: ~100 API units per channel.

## Step 4: Stitch

```bash
./scripts/stitch_hooks.py some_creator        # uses assets/cta.mp4, 3s hook
```

Trims the first 3s of each source short, concatenates your CTA, normalizes to 1080×1920, writes `assets/finished/{slug}/{video_id}.mp4`. Skips IDs already finished.

## Step 5: Upload to Postiz

```bash
set -a && source .env && set +a
./scripts/upload_finished.py                   # all channels, or pass a slug
```

Uploads each finished short via the Postiz CLI, records the hosted URL in `assets/postiz_uploads.json` (the ledger). Never re-uploads.

## Step 6: Schedule

Always preview first:
```bash
set -a && source .env && set +a
./scripts/schedule_via_postiz.py --dry-run --count 28 --start now
```

Then go live. For week 1, use draft mode (you confirm + publish each from the YouTube app within minutes of its slot, which dodges the automated-upload filter):
```bash
./scripts/schedule_via_postiz.py --count 28 --start 2026-01-10T01:00:00Z --type draft
```

After 7 clean days, switch to auto-publish:
```bash
./scripts/schedule_via_postiz.py --count 50 --start 2026-01-17T01:00:00Z --type schedule
```

It sorts unscheduled uploads by source view count, spaces them every `--interval` hours, posts with the identical title/description/tags from `.env`, and writes `scheduled_at_utc` back to the ledger so nothing double-posts.

## Weekly operating loop

- **Plan (Sun/Mon):** Check Postiz sent last week's posts. Open YouTube Studio, note top performers and any sudden average-view drop (a shadow-ban tell).
- **Refill (Mon/Tue):** Re-run `scrape_shorts.py` per channel with a higher count (next tier of hits) -> `stitch_hooks.py` -> `upload_finished.py` -> `schedule_via_postiz.py --dry-run` -> go live for the next 28-50 slots.
- **Daily:** Skim the feed and comments once. Reply to anything real. Flag any short pulling 5x the average; capture what was different.
- **Monthly:** Audit which source channels convert best. Add/drop channels. Refresh the CTA audio with a new trending sound. Consider a second CTA variant to A/B.

## Cadence and warnings

**4 posts/day, 6 hours apart** is the proven cadence. Rotate slots across global time zones; tune with YouTube Analytics -> Audience -> "When your viewers are on YouTube."

**Shadow-ban.** YouTube's automated-upload filter can hide your shorts from discovery if you trip it. Two mitigations: (1) draft mode + manual publish for week 1; (2) even in steady state, occasionally upload one manually with a different hook/audio to vary the pattern.

**Content ID is normal.** Covered above. Videos stay up; ad revenue goes to the artist. This machine is for subscribers, not ad rev.

**Channel quality decays without curation.** After ~100 videos, audit your top 10 and bottom 10 by retention. Drop hook styles that lose viewers in the first 3 seconds. Add channels that match your top performers.

## Anti-patterns (do NOT)

- Don't filter source hooks for thesis-fit. Pick by view count. The CTA does the audience filtering.
- Don't optimize the CTA before posting 50+ videos. Ship, measure, iterate.
- Don't vary the title/description per video. Sameness is the brand signal.
- Don't burst more than 4-6/day in week 1. The filter punishes bursts.
- Don't "improve" a source hook by editing it. Use the first 3 seconds raw.
- Don't ship the CTA without testing it on a phone.
- Always `--dry-run` before any batch schedule. 50 wrong posts is harder to undo than 0 right ones.

## Operational notes

- `set -a && source .env && set +a` before the Postiz CLI. It does not auto-load `.env`.
- The Postiz REST API returns a list of post objects, not a single object. The scheduler already handles that.
- YouTube's `videoDuration=short` means "<4 minutes," not "<60s." The scraper filters to <=90s afterward.
- A laptop that sleeps silently stops cron jobs. For unattended runs, prevent sleep (or use a always-on machine).
- Clean intermediate files at the end of every pass: old CTA renders, extracted audio, temp frames. Keep the latest deliverable + regenerable sources.
