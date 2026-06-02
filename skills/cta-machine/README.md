# CTA Machine

An AI-assisted YouTube Shorts growth machine you can clone and run on your own channel.

Stitch one branded CTA outro onto the front-hooks of already-viral Shorts, schedule them 4/day on autopilot, and drive viewers to a single destination (a newsletter, app, or product). Built and open-sourced by [The Billion Person](https://thebillionperson.com). We run this exact machine ourselves.

The method is fully here. Our own results aren't: the running teardown with real numbers lives in the newsletter.

## The fastest path: let Claude run it

This folder is a Claude Code skill. The whole point is that you don't wire it by hand.

1. Install [Claude Code](https://claude.ai/code).
2. Copy this `cta-machine/` folder into a new project (or clone the repo it lives in).
3. Open Claude Code in that folder and say:
   > Read SKILL.md and walk me through setting up the CTA machine for my channel.
4. Claude takes you through Step 0 (brand) to Step 6 (scheduling), running the scripts as you go.

`SKILL.md` is the full method. Read it even if you wire it yourself.

## Or run it by hand

```bash
cp .env.example .env        # fill in your keys (instructions inside)

# 1. Build your CTA
cd remotion && npm install && npm run dev    # tweak copy live in Remotion Studio
npm run render && cp out/cta.mp4 ../assets/cta.mp4
cd ..

# 2. Add audio
./scripts/bake_audio.sh trending.mp4 assets/cta.mp4 cta.mp4

# 3. Scrape -> stitch -> upload -> schedule
./scripts/scrape_shorts.py @SomeCreator 28
./scripts/stitch_hooks.py some_creator
set -a && source .env && set +a
./scripts/upload_finished.py
./scripts/schedule_via_postiz.py --dry-run --count 28 --start now
```

## What's in here

```
cta-machine/
├── SKILL.md                 # the full method (read this)
├── README.md                # you are here
├── .env.example             # keys + post config, copy to .env
├── scripts/
│   ├── scrape_shorts.py     # top Shorts by view count -> local MP4s + manifest
│   ├── stitch_hooks.py      # first 3s of each hook + your CTA -> finished MP4
│   ├── upload_finished.py   # push finished shorts to Postiz, ledger them
│   ├── schedule_via_postiz.py  # schedule on YouTube, 4/day, same title every time
│   ├── append_cta.sh        # one-off: glue your CTA onto any single clip
│   └── bake_audio.sh        # overlay a trending sound onto the CTA
└── remotion/                # the branded CTA video (parametrized, brand-neutral)
    ├── src/CtaVideo.tsx      # the 3-scene CTA component
    ├── src/Root.tsx          # your brand defaults live here
    └── public/               # drop bg1/bg2/bg3 here (optional)
```

## Cost

About $10/year for a domain, plus a Postiz plan and Claude Code. The video processing (ffmpeg, yt-dlp) and the YouTube Data API are free.

## The honest part

This works because it borrows other creators' hooks and a label's trending audio. Your videos will get Content ID claims (the artist gets any ad revenue; your video stays up). YouTube's filter can shadow-ban automated uploads if you get sloppy. `SKILL.md` covers both, and the mitigations. Read the "When to use this" and "Cadence and warnings" sections before you ship.

## License

Use it, fork it, ship your own. A link back to [thebillionperson.com](https://thebillionperson.com) is appreciated, not required.
