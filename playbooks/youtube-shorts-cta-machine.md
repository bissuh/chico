# YouTube Shorts CTA Machine — Replicable Playbook

A complete blueprint for an AI-assisted YouTube Shorts growth machine. Drop this file into a fresh Claude Code project and the assistant has everything needed to ship a posting pipeline for a new channel/product.

Origin: Built for The Billion Person (TBP) on 2026-05-09. Adapted from the Mau Baron / Ernesto Lopez "Prayer Lock" pattern (100k YouTube subscribers in 8 months from one CTA stitched onto thousands of viral hook clips).

---

## What this builds

A pipeline that:

1. Renders one polished 6-second branded CTA video using Remotion (animated text over backgrounds, with audio).
2. Scrapes top-performing YouTube Shorts from chosen creator channels (sorted by all-time view count).
3. Stitches the first 3 seconds of each scraped short onto the front of the CTA → 9-second hybrid videos.
4. Uploads each finished short to Postiz cloud storage.
5. Schedules each upload to YouTube via the Postiz REST API on a 4/day, 6-hour-spaced cadence.
6. Tracks every video's lifecycle (downloaded → stitched → uploaded → scheduled → posted) in a persistent ledger so nothing repeats.

End state after week 1: ~28 viral-hook + branded-CTA shorts published to a YouTube channel automatically, attributed to one CTA URL.

---

## Why it works (in one paragraph)

The hook isn't yours. The hook is the first 3 seconds of someone else's already-viral short. YouTube's algorithm rewards high retention and completion, both of which spike when a viewer is hooked by content their friends already shared. The CTA is the only branding — same identical 6-second outro on every video. Some viewers click through. Subscribers compound. Mau and Ernesto did this with 869 videos and earned the Silver Play Button. Total cost in their telling: under $50.

The reason it doesn't feel like spam: the CTA is well-made (animated, branded, audio-paired) and sends viewers to something legitimately useful (a free newsletter, app, course, or product page).

---

## When to use this playbook

✅ You have a destination people can subscribe to (newsletter, app, lead magnet, paid product).
✅ You have a YouTube channel (existing or new) for the brand.
✅ You're OK with content that mixes other creators' hooks with your own outro.
✅ You can spend ~3-5 hours of human time per week on creative review + occasional manual posts.

❌ You sell something whose audience is allergic to "growth hacking" optics (some B2B enterprise plays).
❌ You don't have a clear, single URL to direct people to.
❌ You're not OK with potential YouTube Content ID claims (the trending audio often triggers monetization claims that go to the song's rights holder — you don't earn YouTube ad revenue, but the videos stay up).

---

## Required accounts (≈$10 + monthly subscription you may already have)

Open six tabs and create accounts in this order:

1. **Cloudflare Registrar** (cloudflare.com/products/registrar) — register your destination domain. ~$10/year for .com. No upsells.
2. **GitHub** (github.com) — free. Hosts your repo + scripts.
3. **YouTube** (youtube.com) — free. Create the channel that will receive the shorts. Add a profile pic, banner, description with the CTA URL.
4. **Postiz** (postiz.com — sign up for cloud, or self-host from github.com/gitroomhq/postiz-app) — handles scheduling. Connect your YouTube account in Postiz settings.
5. **Anthropic Claude Max** (claude.ai/upgrade) — $100/month for Claude Code. You probably already have this if you're reading this.
6. **YouTube Data API key** (console.cloud.google.com → enable YouTube Data API v3 → create API key) — free, 10,000 units/day quota.

Get these, then in Postiz Settings → Developers → Public API, generate your API key.

---

## Stack and install commands

```bash
# Node + Claude Code
brew install node                                    # if not installed
npm install -g @anthropic-ai/claude-code

# Postiz CLI
npm install -g postiz

# Video processing
brew install ffmpeg yt-dlp

# Python deps
pip3 install requests python-dotenv pillow

# Remotion deps land in remotion/ folder via project npm install (see Step 1)
```

---

## Environment variables

Create `.env` at repo root and gitignore it:

```bash
# .env
YOUTUBE_API_KEY=AIzaSy...                    # YouTube Data API v3 key
POSTIZ_API_KEY=pos_...                       # Postiz public API key
POSTIZ_YOUTUBE_INTEGRATION_ID=cmoyu...       # See: curl -i -H "Authorization: $POSTIZ_API_KEY" https://api.postiz.com/public/v1/integrations
```

Add to `.gitignore`:
```
.env
.env.*
!.env.example
node_modules/
remotion/out/
remotion/.cache/
```

---

## Folder structure to create

```
project-root/
├── .env                              # secrets (gitignored)
├── .gitignore
├── playbooks/
│   └── youtube-shorts-cta-machine.md # this file
├── outbox/
│   ├── scripts/
│   │   ├── scrape_shorts.py
│   │   ├── stitch_hooks.py
│   │   ├── upload_finished.py
│   │   ├── schedule_via_postiz.py
│   │   ├── append_cta.sh
│   │   └── bake_audio.sh
│   └── assets/
│       ├── CTAvideo.mp4              # current branded CTA
│       ├── postiz_uploads.json       # ledger
│       ├── source_audio_clips/       # downloaded TikToks for audio extraction
│       ├── source_hooks/             # scraped source shorts per channel
│       │   └── {channel_slug}/
│       │       ├── manifest.json
│       │       └── {video_id}.mp4
│       └── finished/                 # stitched 9-sec outputs
│           └── {channel_slug}/
│               └── {video_id}.mp4
└── remotion/
    ├── package.json
    ├── tsconfig.json
    ├── remotion.config.ts
    ├── public/
    │   ├── bg1.png                   # scene 1 background (Midjourney)
    │   ├── bg2.png                   # scene 2 background
    │   └── bg3.png                   # scene 3 background
    └── src/
        ├── index.ts
        ├── Root.tsx
        └── Composition.tsx
```

---

## Step 0: Brand customization (Claude must confirm with user before starting)

Before writing any code, Claude should ask the user to lock these:

| Item | Example (TBP) | What user provides |
|---|---|---|
| Product name | The Billion Person | Their brand name |
| Destination URL | thebillionperson.com | The single URL |
| Brand color (hex) | #2A7A6D (deep teal) | Their accent color |
| Headline 1 (alarm) | STOP SCROLLING. | Short imperative, attention-grab |
| Headline 2 (action) | START BUILDING. | Short imperative, what they should do instead |
| Subhead (social proof + offer) | Start a business with AI. Join 4,000 people. | One sentence, ≤50 chars |
| YouTube post title | Start a Business with AI \| thebillionperson.com | Same on every video |
| YouTube description | Get the free weekly playbook: thebillionperson.com\n\n4,000+ readers learning how to start AI-powered businesses. | 2-3 lines, includes URL |
| YouTube tags | AI, Entrepreneur, Startup, Side Hustle, Make Money With AI, Business Ideas, Shorts | 5-10 tags |
| Source channels | @AlexHormozi, @MyFirstMillionPod, @ChrisWillx | 2-4 YouTube handles whose audience overlaps |
| Background images | 3 Midjourney prompts, 9:16, brand color accent | See Step 1 for prompts |

---

## Step 1: Build the CTA video (Remotion)

The CTA is THE brand. Spend time making it good. ~6 seconds, 1080×1920 9:16, three scenes:
1. Alarm headline ("STOP SCROLLING.") with background image of distraction
2. Checklist scene — first headline struck through, second headline emerges ("START BUILDING.") with background image of action
3. Offer + URL with background image of resolution/horizon

### Scaffold

```bash
mkdir -p remotion/{src,public,out}
cd remotion
npm init -y
npm install --save remotion @remotion/cli @remotion/google-fonts react react-dom
npm install --save-dev typescript @types/react
```

### `remotion/package.json` (key fields)

```json
{
  "scripts": { "render": "remotion render src/index.ts TBPCta out/cta.mp4" },
  "dependencies": {
    "@remotion/cli": "^4.0.0",
    "@remotion/google-fonts": "^4.0.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "remotion": "^4.0.0"
  },
  "devDependencies": {
    "@types/react": "^18.3.0",
    "typescript": "^5.4.0"
  }
}
```

### `remotion/remotion.config.ts`

```ts
import {Config} from '@remotion/cli/config';
Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
```

### `remotion/src/index.ts`

```ts
import {registerRoot} from 'remotion';
import {RemotionRoot} from './Root';
registerRoot(RemotionRoot);
```

### `remotion/src/Root.tsx`

```tsx
import {Composition} from 'remotion';
import {TBPCta} from './Composition';

export const RemotionRoot: React.FC = () => (
  <Composition
    id="TBPCta"
    component={TBPCta}
    durationInFrames={180}   // 6 seconds at 30fps
    fps={30}
    width={1080}
    height={1920}
    defaultProps={{
      headline1: 'STOP SCROLLING.',
      headline2: 'START BUILDING.',
      subhead: 'Start a business with AI. Join 4,000 people.',
      url: 'thebillionperson.com',
      bg1: 'bg1.png',
      bg2: 'bg2.png',
      bg3: 'bg3.png',
    }}
  />
);
```

### `remotion/src/Composition.tsx`

See full source in chico's `remotion/src/Composition.tsx`. Key design notes:

- 3 scenes with crossfade overlap (8 frames each).
- Scene 1: headline scales in with spring, alarm-style.
- Scene 2: STOP SCROLLING shrinks + native CSS line-through (`text-decoration: line-through` with animated alpha) while START BUILDING enters confidently below — gives "checking off a list" feel.
- Scene 3: subhead enters first (spring from below), URL hero scales in 14 frames later with subtle pulse.
- Backgrounds: full-bleed Midjourney engravings via `<Img>` from `staticFile()`, with Ken Burns scale 1.02 → 1.07 over the scene + slight pan.
- Brand-color multiply overlay (60% opacity) over each background to lock visual canon even if Midjourney drifts.
- Dark center gradient (50% → 0% radial) under text for readability on busy backgrounds.
- Persistent URL caption at top (small pill, fades in by frame 14, fades out as scene 3 hero URL takes over).
- Grain + vignette overlay across the whole video.
- Fonts: Anton (headlines, condensed display) + Playfair Display 900 italic (URL hero) via `@remotion/google-fonts`.

### Background images (Midjourney)

3 images, all 9:16, brand color accent. Tell a 3-act arc: trapped → working → free.

**Prompt 1 (trapped — STOP SCROLLING):**
```
A figure slumped on a worn velvet armchair in a dim 19th-century parlor,
hunched over a small glowing rectangular tablet (anachronistic phone). The
pale [BRAND COLOR HEX] glow of the screen lights only their face, casting
harsh shadows in the empty room around them. Their finger paused mid-scroll,
eyes locked on the device, expression hollow. Outside the window, a city of
golden light they no longer notice. Heavy crosshatching throughout.
Monochromatic engraving with deep [BRAND COLOR HEX] as the only color.
Gustave Doré 19th century style. Vertical 9:16. Figure in lower-center,
device-glow dramatic, leaving the upper third open for text overlay.
--ar 9:16 --v 7
```

**Prompt 2 (action — START BUILDING):**
```
A determined figure with sleeves rolled up, hammering molten metal at an
anvil in a small workshop. Sparks fly upward in a [BRAND COLOR HEX] glow.
Tools and finished works hang on the walls behind him. The figure leans
forward with full body weight into the strike. Heavy crosshatching.
Monochromatic engraving with deep [BRAND COLOR HEX] as the only color.
Gustave Doré 19th century style. 9:16. Figure in lower third, sparks fill
upper area, leaving upper-center open for text overlay.
--ar 9:16 --v 7
```

**Prompt 3 (resolution — URL):**
```
A lone traveler standing at the threshold of a wide open landscape at dawn,
viewed from behind. A stone road stretches forward into rolling hills under
a vast sky. The sun rises ahead, casting [BRAND COLOR HEX] light across the
horizon. Heavy crosshatching. Monochromatic engraving with deep
[BRAND COLOR HEX] as the only color. Gustave Doré 19th century style. 9:16.
Traveler small and distant in the center, strong horizon line, large open
sky above for text overlay.
--ar 9:16 --v 7
```

Replace the Doré-style aesthetic with whatever fits your brand. The structural rule: each image must have ample negative space where text will land, and the dominant color tone must match your brand.

### Render

```bash
cd remotion
npx remotion render src/index.ts TBPCta out/cta.mp4
```

Output: `remotion/out/cta.mp4`. Move/copy to `outbox/assets/CTAvideo.mp4`.

---

## Step 2: Bake trending audio onto the CTA

The CTA needs music. The Mau pattern: download a viral TikTok using a trending sound, extract the audio, overlay onto your silent CTA. Triggers YouTube Content ID monetization claims (artist gets the ad revenue, video stays up — fine if you're not monetizing).

### `outbox/scripts/bake_audio.sh`

```bash
#!/bin/bash
set -euo pipefail
[ "$#" -ne 3 ] && { echo "usage: $0 <source_video.mp4> <cta.mp4> <output_filename.mp4>" >&2; exit 1; }
SRC="$1"
CTA="$2"
OUT_NAME="$3"
ASSETS=$(dirname "$CTA")
TMP_DIR="$ASSETS/source_audio_clips"
mkdir -p "$TMP_DIR"
TMP_AUDIO="$TMP_DIR/$(basename "$SRC" .mp4)_full.mp3"
TMP_TRIM="$TMP_DIR/$(basename "$SRC" .mp4)_trimmed.mp3"
DUR=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$CTA")
DUR_INT=$(printf '%.0f' "$DUR")
FADE_START=$((DUR_INT - 1))
echo "Extracting full audio from $SRC..."
ffmpeg -y -loglevel error -i "$SRC" -vn -acodec mp3 -b:a 192k "$TMP_AUDIO"
echo "Trimming to ${DUR_INT}s with 1s fadeout..."
ffmpeg -y -loglevel error -i "$TMP_AUDIO" -t "$DUR_INT" -af "afade=t=out:st=$FADE_START:d=1" "$TMP_TRIM"
echo "Overlaying on $CTA..."
ffmpeg -y -loglevel error -i "$CTA" -i "$TMP_TRIM" -map 0:v -map 1:a -c:v copy -c:a aac -shortest "$ASSETS/$OUT_NAME"
echo "Done. Output: $ASSETS/$OUT_NAME"
ffprobe -v error -show_entries stream=codec_type,codec_name,duration -show_entries format=duration,size -of default=noprint_wrappers=1 "$ASSETS/$OUT_NAME"
```

### Usage

1. Find a trending sound on TikTok Creative Center (creativecenter.tiktok.com → Trends → Sounds).
2. Click the sound → open one of the top videos using it on TikTok → copy the URL.
3. Download the video: `yt-dlp -f mp4 "https://www.tiktok.com/@user/video/123" -o tiktok_source.mp4`
4. Bake: `./outbox/scripts/bake_audio.sh tiktok_source.mp4 outbox/assets/CTAvideo.mp4 CTAvideo.mp4` (overwrites silent CTA with audio version).

---

## Step 3: Source-channel scraper

### `outbox/scripts/scrape_shorts.py`

See full source in chico's `outbox/scripts/scrape_shorts.py`. Key behavior:

- Accepts a channel URL, `@handle`, or `UC...` channel ID + a count.
- Calls YouTube Data API v3 search endpoint with `videoDuration=short&order=viewCount`.
- Pulls 50-100 candidates, fetches `videos` endpoint for full duration + view count.
- Filters to videos ≤ 90 seconds (true Shorts cutoff, since `videoDuration=short` is "<4min").
- Sorts by view count desc, takes top N.
- Downloads each via yt-dlp into `outbox/assets/source_hooks/{channel_slug}/{video_id}.mp4`.
- Skips downloads that already exist on disk.
- Writes `manifest.json` with id, title, views, duration, url, local_path.

API quota cost: ~100 units per channel (search) + 1 unit per batch of 50 videos detail. Daily quota 10,000.

### Usage

```bash
./outbox/scripts/scrape_shorts.py https://www.youtube.com/@AlexHormozi 25
./outbox/scripts/scrape_shorts.py @MyFirstMillionPod 25
./outbox/scripts/scrape_shorts.py @ChrisWillx 10
```

---

## Step 4: Stitcher

### `outbox/scripts/stitch_hooks.py`

See full source in chico's `outbox/scripts/stitch_hooks.py`. Key behavior:

- Reads the channel's `manifest.json`.
- For each video, runs ONE ffmpeg call that: trims first 3 seconds of source, normalizes both source and CTA to 1080×1920 9:16 (`scale + pad`), concats with audio, encodes libx264 CRF 20 + AAC 192k.
- Skips video IDs that already have a finished file.
- Writes `outbox/assets/finished/{channel_slug}/{video_id}.mp4`.

### Usage

```bash
./outbox/scripts/stitch_hooks.py alex_hormozi
./outbox/scripts/stitch_hooks.py my_first_million
./outbox/scripts/stitch_hooks.py chris_williamson
```

Output: 9-second files (3s hook + 6s CTA), ready to upload.

---

## Step 5: Postiz uploader

### `outbox/scripts/upload_finished.py`

See full source in chico's `outbox/scripts/upload_finished.py`. Key behavior:

- Walks `outbox/assets/finished/{channel_slug}/*.mp4`.
- Calls `postiz upload` for each (CLI, returns JSON with hosted URL on uploads.postiz.com).
- Writes results to `outbox/assets/postiz_uploads.json` (the ledger).
- Skips files already present in the ledger.

### Usage

```bash
set -a && source .env && set +a            # load POSTIZ_API_KEY
./outbox/scripts/upload_finished.py        # uploads everything new across all channels
```

Ledger entry per video:
```json
"alex_hormozi/9uEU6bWB6_4": {
  "channel_slug": "alex_hormozi",
  "video_id": "9uEU6bWB6_4",
  "local_path": "outbox/assets/finished/alex_hormozi/9uEU6bWB6_4.mp4",
  "postiz_id": "5ed840eb-...",
  "postiz_url": "https://uploads.postiz.com/abcdef.mp4",
  "uploaded_at": "2026-05-09T22:05:00+00:00"
}
```

---

## Step 6: Scheduler

### `outbox/scripts/schedule_via_postiz.py`

See full source in chico's `outbox/scripts/schedule_via_postiz.py`. Key behavior:

- Loads ledger + source manifests, joins to get (video_url, source_title, source_views) per video.
- Filters out anything already scheduled (`scheduled_at_utc` set).
- Sorts by source views desc, takes top --count.
- Generates UTC schedule slots starting --start, every --interval hours.
- POSTs to `https://api.postiz.com/public/v1/posts` for each, with proper YouTube settings (title, description, visibility, tags, made-for-kids).
- Records `scheduled_at_utc` + `postiz_post_id` back to the ledger.
- `--dry-run` prints the schedule without posting.

### Usage

Always preview first:
```bash
set -a && source .env && set +a
./outbox/scripts/schedule_via_postiz.py --dry-run --count 50 --start 2026-05-10T01:00:00Z
```

Then go live:
```bash
./outbox/scripts/schedule_via_postiz.py --count 50 --start 2026-05-10T01:00:00Z --type schedule
```

For drafts (manual confirm before publish, recommended for week 1):
```bash
./outbox/scripts/schedule_via_postiz.py --count 28 --start 2026-05-10T01:00:00Z --type draft
```

---

## Operating loop (weekly rhythm)

**Sunday or Monday morning (planning):**
- Open Postiz dashboard. Verify last week's posts went out.
- Check YouTube Studio. Note top-performing shorts (view count, like rate, completion rate).
- Note any shadow-ban indicators (sudden drop in average views on otherwise normal posts).

**Monday or Tuesday (refill):**
- Run `scrape_shorts.py` for each source channel with `count` higher than last week (gets next-tier-down hits).
- Run `stitch_hooks.py` for each channel.
- Run `upload_finished.py`.
- Run `schedule_via_postiz.py --dry-run` to preview the next week's schedule.
- Run live to schedule the next 28-50 slots.

**Daily (passive):**
- Scroll the channel feed once. Skim comments. Reply to anything substantive.
- Note any video that pulled 5x+ the average — capture what was different (hook style, audio, source channel).

**Monthly (review):**
- Audit which source channels are converting best (clicks to your URL).
- Consider adding/removing source channels.
- Refresh trending audio on the CTA (re-run `bake_audio.sh` with a new TikTok download).
- Consider re-rendering the CTA with new copy if conversion data suggests it.

---

## Cadence + warnings

**4 posts per day, 6 hours apart** is the proven Mau / Prayer Lock cadence. Their queue had 2,000+ scheduled at the time they hit Silver Play Button. Slot times rotate through global time zones:

- 22:00 BRT / 21:00 ET / 18:00 PT (US primetime)
- 04:00 BRT / 03:00 ET / midnight PT (overnight Americas, mid-morning EU)
- 10:00 BRT / 09:00 ET / 06:00 PT (US morning)
- 16:00 BRT / 15:00 ET / 12:00 PT (US afternoon)

Adjust based on YouTube Analytics → Audience tab → "When your viewers are on YouTube."

**The shadow-ban warning (Mau's lesson):** YouTube's filter for automated uploads can hide your shorts from the discovery feed if you trip it. Two mitigations:

1. **Manual upload week 1.** Schedule first 7 days as `--type draft`. You confirm and publish each via the YouTube mobile app within minutes of the scheduled time. After 7 clean days, switch to `--type schedule` for auto-publish.
2. **Mix manual + automated.** Even in steady state, occasionally upload a video manually (with a different hook or different audio) to keep the channel's upload pattern varied.

**Content ID claims are normal.** The trending audio you bake into the CTA is owned by music labels. YouTube's Content ID will detect it and redirect monetization to the artist. Your videos stay up; you just don't earn YouTube ad revenue. This is fine if your business model is "drive subscribers to a destination," not "earn YouTube ad rev."

**Channel quality decays without curation.** After 100 videos, audit the top 10 and bottom 10 by retention. Drop hooks that consistently lose viewers in the first 3 seconds. Add hooks from new source channels that match the format of your top performers.

---

## Customization checkpoints

When Claude reads this playbook for a new project, it should walk the user through these decisions in order:

1. **Brand identity** — name, color, URL, founder voice (per Step 0 table).
2. **Source channel selection** — 2-4 YouTube channels whose audience overlaps with the user's customer.
3. **CTA copy** — three text strings (alarm headline, action headline, subhead) + the always-on URL.
4. **Background image generation** — render or commission three Midjourney images per the prompts (with the user's brand color substituted).
5. **Trending audio source** — user picks one trending TikTok sound and provides the URL.
6. **Posting cadence** — confirm 4/day every 6 hours, or adjust if user prefers different.
7. **Week-1 draft mode** — confirm `--type draft` for first 7 days, then `--type schedule` after.

---

## Anti-patterns (do NOT do these)

- ❌ Don't filter source hooks for thesis-fit. Pick by view count. The CTA does the audience filtering.
- ❌ Don't optimize the CTA before posting 50+ videos. Ship → measure → iterate.
- ❌ Don't change the title or description per video. Same on every post is the brand signal.
- ❌ Don't post more than 4-6 per day in week 1. The shadow-ban filter punishes burst patterns.
- ❌ Don't bake the audio at higher than 192kbps AAC — wastes file size, no quality gain on a phone speaker.
- ❌ Don't try to "improve" the source hook by editing it. Use the first 3 seconds, raw.
- ❌ Don't ship the CTA without testing it on a phone screen. What looks fine on a desktop preview can be unreadable at 320×570 in someone's feed.

---

## Scaling milestones

- **Week 1:** 28 shorts shipped, draft mode, manual confirmation. Watch first 1k views accumulate.
- **Week 2:** Auto-publish enabled. 28 more shorts. Look for the first short that breaks 5k views.
- **Week 4:** 112 total shorts. First subscriber data. Compute conversion rate (subs / total views).
- **Month 2:** 240 shorts. Add a 4th source channel. Refresh CTA audio with a new trending sound.
- **Month 3:** 360 shorts. First short to break 50k views. Consider rendering a second CTA variant for A/B test.
- **Month 6:** 720 shorts. Channel should be in YouTube Partner Program eligibility (1,000 subs + 4M shorts views in 90 days).
- **Month 8:** ~960 shorts. Mau's milestone — Silver Play Button (100k subs) territory if the destination + CTA actually convert.

---

## Files this playbook depends on

The full source code for every script referenced here lives in chico's `outbox/scripts/` and `remotion/` folders. To use this playbook:

1. Copy this markdown into your new project's root (or `playbooks/` folder).
2. Copy the actual script files from chico, OR have Claude read this playbook and recreate them from scratch (the descriptions in Steps 1-6 are detailed enough for a competent coding assistant).
3. Run through Step 0 (brand customization) with the user.
4. Run through Steps 1-6 in order.
5. Begin the operating loop.

---

## Lessons captured along the way

- The CTA video matters more than the source hook. A boring CTA with a great hook converts worse than a great CTA with a boring hook.
- Native CSS `text-decoration: line-through` with animated `text-decoration-color` alpha gives a clean strike-through animation that handles multi-line text correctly. Custom div overlays don't.
- Postiz REST API returns a list of post objects, not a single object — handle that in any response parser.
- YouTube's `videoDuration=short` parameter is "<4 minutes" not "<60 seconds." Always filter results down to ≤90s afterward to keep true Shorts.
- yt-dlp handles both `youtube.com/watch?v=` and `youtube.com/shorts/` URLs identically — same MP4 output.
- Mac `crontab` will silently stop running scheduled jobs if the laptop sleeps. For unattended runs, change Settings → Battery → "Prevent automatic sleeping when display is off." For laptop-closed-but-running, use clamshell mode with external display.
- Always `set -a && source .env && set +a` before invoking the Postiz CLI. The CLI doesn't auto-load `.env`.
- Always do `--dry-run` before any batch scheduling. 50 wrong posts is harder to undo than 0 right ones.
- Clean intermediate files at the end of every work pass. Old v0/v1/v2 renders, temporary frame extractions, intermediate audio extracts. Keep only the latest deliverable + regenerable source files.

---

End of playbook.
