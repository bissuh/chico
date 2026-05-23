---
description: Produce + schedule one full week (7 posts) of TBP faceless gallery content, end to end, to the depth standard. Not lazy Chico.
---

You are producing AND scheduling ONE WEEK of The Billion Person faceless content for Instagram + TikTok (and YouTube Shorts for the reels). The whole point is DEPTH and REAL VALUE. Do not ship thin one-liners. Follow this runbook exactly.

## Read first (load the standards)
- `playbooks/faceless-gallery-engine.md` — the DEPTH STANDARD, the 7-day lineup, the posting recipe.
- `knowledge-base/faceless-gallery-model/format-library.md` — the formats and which signal each drives.
- Memory: `project_tbp_faceless_gallery_engine`, `feedback_carousels_go_deep`.
- Voice: no em or en dashes, no "nobody [verb]" phrases, follow the TBP Writing Manual.

## 1. Research (WEB-FIRST, fresh every week)
Pull current, hot content. Do not recycle the newsletter as the main source. Rotate the lineup types across the 7 days: Top [X] (tools/skills/niches/trends), Steal This Prompt, Built With AI (a real, verified solo-or-tiny-team AI builder with citable numbers), Tutorial (one concrete how-to), Real Niches or Mistakes, Hot Take reel, This vs That reel. ~5 deep carousels + 2 reels. Verify every number; frame anything unverified as "reported".

## 2. Write deep content
Each carousel = 9 to 15 slides. Use CleanSlide layouts: `cover`, `detail` (real paragraphs), `prompt` (real copy-paste prompts), `list`, `statement`; `tip`/`tipLabel` for an inline callout.
- One real idea per slide: a tool, a number, a prompt, a step. Cut anything a stranger can't act on.
- Name actual tools. Teach the AI-native stack (Claude Code + Remotion + Postiz), not Canva.
- Standalone titles: tension + payoff, no insider references. Slide 1 must stop the scroll.
- Last slide asks for a SAVE and a COMMENT ("ask in the comments, I answer every one").
- SELF-COMPLETE TEST: reading only the slides, could a stranger do the thing with no missing step/tool/prompt? If not, add the slide.
Write into a generator script `remotion/gen_weekN.py` (theme `green`, handle `@thebillionperson`). Reels: `GreenReel` props, 4 punchy lines + a CTA.

## 3. House grep (must be zero)
`grep -P '[—–]'` and `grep -iE 'nobody (tells|knows|wants|says|talks|cares|gives)'` over the new props.

## 4. Render (Remotion, from remotion/)
`node_modules/.bin/remotion still src/index.ts CleanSlide out/<f>.png --props=props/<f>.json` per carousel slide (1080x1350). `remotion render src/index.ts GreenReel out/<reel>.mp4 --props=...` per reel. Big batches: run in background. Spot-check the densest slides for overflow.

## 5. Schedule (postiz CLI — the MCP is unreliable)
`set -a && source .env && set +a` first (loads POSTIZ_API_KEY). `postiz upload <file>` per asset returns a hosted URL. Then one `postiz posts:create -c "<caption>" -m "<comma-sep urls>" -i <integrationId> -s "<ISO8601 UTC>" -t schedule --settings '<json>'` PER PLATFORM. Daily slot: 7pm ET = 23:00 UTC.
- IG `cmpisrqck03e2qm0yc8qzt72e` settings `{"post_type":"post"}`
- TikTok `cmpiuhmut03mcqm0ykb99rjow` settings `{"privacy_level":"PUBLIC_TO_EVERYONE","duet":false,"stitch":false,"comment":true,"autoAddMusic":"yes","brand_content_toggle":false,"brand_organic_toggle":false,"content_posting_method":"DIRECT_POST","title":"<=90 chars"}`
- YouTube (reels only) `cmoyuys5108jxl70yk63ihmco` settings `{"title":"<=100>","type":"public","selfDeclaredMadeForKids":"no"}`
Each post: keyword-first caption + 3-5 relevant hashtags + save/comment CTA. Mirror `remotion/schedule_week2.py` (copy it to `schedule_weekN.py`, edit content + dates).

## 6. Verify, log, clean
`postiz posts:list` shows the new posts as QUEUE at 23:00. Log the week to `outbox/faceless-launch/` and update memory. Delete superseded/intermediate renders (cleanup protocol).

## Engine 2: YouTube CTA Shorts refill (the OTHER engine)
This command runs BOTH engines. After the faceless week above, top up the borrowed-hook CTA Shorts machine (the channel-subs experiment, separate from the faceless feed; see `playbooks/youtube-shorts-cta-machine.md`). Keep its queue ahead by ~8 days.
1. Ensure the CTA bumper exists: `outbox/assets/CTAvideo_v7.mp4` (re-render from Remotion TBPCta if missing).
2. Schedule existing unscheduled finished shorts first (`outbox/assets/postiz_uploads.json`, entries with no `scheduled_at_utc`): `python3 outbox/scripts/schedule_via_postiz.py --start <ISO after current queue end> --count <N> --interval 6` (needs POSTIZ_API_KEY + POSTIZ_YOUTUBE_INTEGRATION_ID=cmoyuys5108jxl70yk63ihmco). 4/day = 32 for 8 days.
3. If inventory is short, scrape fresh hooks (`scrape_shorts.py @channel N`), stitch (`stitch_hooks.py <slug> outbox/assets/CTAvideo_v7.mp4 3`), upload (`upload_finished.py`), then schedule.

## Authority
Publishing under TBP is Yellow, but Bissuh has authorized the ongoing faceless launch + CTA experiment: schedule, do not ask per-post. Only stop to flag a genuinely shaky fact. Quality bar is the 12-slide tutorial (`remotion/out/tut-*`) and week-2 carousels, match it.

## NOTE on automation limits
A cloud /schedule routine canNOT post: it has no access to local `.env` (POSTIZ_API_KEY), the global `postiz` CLI, or a guaranteed render env. Postiz already auto-publishes whatever is SCHEDULED. So the realistic split: a routine can research + write next week's content and open a PR; the render + schedule-into-Postiz runs where the key + tools live (locally, via this command). True zero-touch posting from the cloud is not available with the current setup.
