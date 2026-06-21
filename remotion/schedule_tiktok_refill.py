#!/usr/bin/env python3
"""Refill the TBP TikTok queue for 2026-06-25..07-04 (10 days), TikTok ONLY, as DRAFTS.
IG + YouTube are already covered through ~July 1-3; only TikTok ran dry after 06-24.
Created as DRAFTS (Yellow tier): Bissuh reviews, adds a trending sound, then publishes.
Evergreen reposts of proven carousels, established captions. Run with POSTIZ_API_KEY in env.
  set -a; source ./.env; set +a; python3 remotion/schedule_tiktok_refill.py
"""
import json, os, subprocess

OUT = "/Users/bissuh/Documents/TBP/chico/remotion/out"
TT = "cmpiuhmut03mcqm0ykb99rjow"  # The Billion Person, TikTok
# Draft-friendly settings: UPLOAD (lands in TikTok inbox to finish) + no auto music
# so Bissuh adds a trending sound before publishing (silent slideshows get buried).
TT_BASE = {"privacy_level": "PUBLIC_TO_EVERYONE", "duet": False, "stitch": False,
           "comment": True, "autoAddMusic": "no", "brand_content_toggle": False,
           "brand_organic_toggle": False, "content_posting_method": "UPLOAD"}

POSTS = [
 {"id":"stl","n":9,"date":"2026-06-25T23:00:00Z","tt":"6 prompts to start a business this weekend",
  "cap":"6 prompts to start a business this weekend. Copy them, paste into Claude, swap the brackets. Save this so you have it Saturday. Which one are you running first? #aitools #promptengineering #sidehustle #aibusiness #buildinpublic"},
 {"id":"nch","n":10,"date":"2026-06-26T23:00:00Z","tt":"7 one-person businesses you can start with AI in 2026",
  "cap":"7 one-person businesses you can actually start with AI in 2026: who pays, how much, and the first step for each. Save this and tell me which one fits you. #aibusiness #sidehustle #indiehackers #nocode #onlinebusiness"},
 {"id":"hsp","n":10,"date":"2026-06-27T23:00:00Z","tt":"He turned selfies into a $3.6M business (solo)",
  "cap":"He turned selfies into a reported $3.6M-a-year business, solo, after selling an earlier AI tool for $1M. What Danny Postma did and what you can copy. Save this. (Figures reported.) #aibusiness #indiehackers #microsaas #buildinpublic #ai"},
 {"id":"skl","n":9,"date":"2026-06-28T23:00:00Z","tt":"5 AI skills that actually pay in 2026",
  "cap":"5 AI skills that actually pay in 2026, ranked by what is growing fastest on Upwork, with how to start each. Save this and pick one. Which fits you? Free playbook in bio. #aiskills #aitools #sidehustle #aibusiness #freelancing"},
 {"id":"prm","n":9,"date":"2026-06-29T23:00:00Z","tt":"6 prompts to get your first 10 customers",
  "cap":"6 prompts to get your first 10 customers, for when you built it but the sales are not coming yet. Copy, paste into Claude, swap the brackets. Save this. #aitools #marketing #sales #sidehustle #aibusiness"},
 {"id":"marc","n":9,"date":"2026-06-30T23:00:00Z","tt":"He made $1,032,000 in 2025, solo (Marc Lou)",
  "cap":"He made a reported $1,032,000 in 2025, one person, no team, and publishes every number. What Marc Lou did and the part you can copy. Save this. (Figures as reported by him.) #buildinpublic #indiehackers #microsaas #aibusiness #solopreneur"},
 {"id":"val","n":9,"date":"2026-07-01T23:00:00Z","tt":"Validate your business idea in an hour with AI",
  "cap":"How to validate a business idea in an hour with AI, before you waste months building the wrong thing. The exact steps and prompts inside. Save this and run it. #aibusiness #startups #indiehackers #nocode #buildinpublic"},
 {"id":"stk","n":12,"date":"2026-07-02T23:00:00Z","tt":"The AI tools running one-person businesses in 2026",
  "cap":"The AI tools quietly running one-person businesses in 2026, what each is for and when to use it. Save the stack and pick one to start with. Which would you add? Free playbook in bio. #aitools #indiehackers #nocode #aibusiness #buildinpublic"},
 {"id":"myth","n":9,"date":"2026-07-03T23:00:00Z","tt":"5 lies about making money with AI",
  "cap":"5 lies about making money with AI, and what's actually true. Each one sounds like caution and keeps you stuck. Send this to someone who still believes them. #aibusiness #startups #solopreneur #indiehackers #makemoneyonline"},
 {"id":"mst","n":8,"date":"2026-07-04T23:00:00Z","tt":"5 mistakes that kill a one-person business",
  "cap":"5 mistakes that kill a one-person business in the first months, and how to dodge all of them. Save this before you start. Which one stings? Free playbook in bio. #startups #solopreneur #indiehackers #aibusiness #buildinpublic"},
]

def upload(path):
    out = subprocess.run(["postiz","upload",path], capture_output=True, text=True).stdout
    i = out.find("{")
    if i == -1:
        raise RuntimeError(f"upload failed for {path}: {out[:200]}")
    return json.loads(out[i:])["path"]

def create(cap, media_csv, date, settings):
    # -t draft: stage in Postiz as a draft (does NOT publish). Bissuh reviews + publishes.
    r = subprocess.run(["postiz","posts:create","-c",cap,"-m",media_csv,"-i",TT,"-s",date,
                        "-t","draft","--settings",json.dumps(settings)],
                       capture_output=True, text=True)
    return (r.stdout + r.stderr)

res = []
for p in POSTS:
    files = [os.path.join(OUT, f"{p['id']}-{i}.png") for i in range(1, p["n"]+1)]
    missing = [f for f in files if not os.path.exists(f)]
    if missing:
        print(f"SKIP {p['id']}: missing {len(missing)} file(s): {missing[:2]}")
        res.append({"id":p["id"],"tt":False,"note":"missing files"}); continue
    print(f"=== {p['id']} {p['date']} ({len(files)} slides) ===")
    media = ",".join(upload(f) for f in files)
    tt = create(p["cap"], media, p["date"], {**TT_BASE, "title": p["tt"]})
    ok = "postId" in tt
    print("TT:", "OK" if ok else tt[-200:])
    res.append({"id":p["id"],"date":p["date"],"tt":ok})

print("\n===== SUMMARY =====")
for r in res:
    print(f"{r['id']:6} {r.get('date','')}  TT={'OK' if r['tt'] else 'FAIL'}")
print(f"\nScheduled OK: {sum(1 for r in res if r['tt'])}/{len(res)}")
