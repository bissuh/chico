#!/usr/bin/env python3
"""Upload + schedule the week's posts to IG + TikTok via the postiz CLI.
Run with POSTIZ_API_KEY in env (source ../.env first)."""
import json, subprocess, sys

IG = "cmpisrqck03e2qm0yc8qzt72e"
TT = "cmpiuhmut03mcqm0ykb99rjow"
IG_SETTINGS = {"post_type": "post"}
TT_BASE = {"privacy_level": "PUBLIC_TO_EVERYONE", "duet": False, "stitch": False,
           "comment": True, "autoAddMusic": "yes", "brand_content_toggle": False,
           "brand_organic_toggle": False, "content_posting_method": "DIRECT_POST"}

POSTS = [
 {"id":"stk","kind":"carousel","n":12,"date":"2026-05-24T23:00:00Z",
  "tt_title":"The AI tools running one-person businesses in 2026",
  "caption":"The AI tools quietly running one-person businesses in 2026, what each is for and when to use it. Save the stack and pick one to start with. Which would you add? Free playbook in bio. #aitools #indiehackers #nocode #aibusiness #buildinpublic"},
 {"id":"blt","kind":"carousel","n":10,"date":"2026-05-25T23:00:00Z",
  "tt_title":"He sold his AI app to Wix for $80M in 6 months (solo)",
  "caption":"A solo founder built an AI app and sold it to Wix for $80M, six months after launch. What he did, and what you can copy, no $80M required. Save this. What would you build? #aibusiness #indiehackers #microsaas #buildinpublic #ai"},
 {"id":"stl","kind":"carousel","n":9,"date":"2026-05-26T23:00:00Z",
  "tt_title":"6 prompts to start a business this weekend",
  "caption":"6 prompts to start a business this weekend. Copy them, paste into Claude, swap the brackets. Save this so you have it Saturday. Which one are you running first? #aitools #promptengineering #sidehustle #aibusiness #buildinpublic"},
 {"id":"nch","kind":"carousel","n":10,"date":"2026-05-27T23:00:00Z",
  "tt_title":"7 one-person businesses you can start with AI in 2026",
  "caption":"7 one-person businesses you can actually start with AI in 2026: who pays, how much, and the first step for each. Save this and tell me which one fits you. #aibusiness #sidehustle #indiehackers #nocode #onlinebusiness"},
 {"id":"sat-reel","kind":"reel","file":"out/sat-reel.mp4","date":"2026-05-28T23:00:00Z",
  "tt_title":"Cursor vs Lovable: which should a beginner start with?",
  "caption":"Cursor vs Lovable for a total beginner: start with one, graduate to the other. Which are you using? Free tool stack in bio. #nocode #aitools #vibecoding #indiehackers #buildinpublic"},
 {"id":"fri-reel","kind":"reel","file":"out/fri-reel.mp4","date":"2026-05-29T23:00:00Z",
  "tt_title":"You don't need an audience to make your first $1,000",
  "caption":"You don't need an audience to make your first $1,000 online. You need one offer and 10 conversations. Agree or disagree? Free playbook in bio. #sidehustle #onlinebusiness #indiehackers #aibusiness #startups"},
]

def upload(path):
    out = subprocess.run(["postiz","upload",path], capture_output=True, text=True).stdout
    i = out.find("{")
    if i == -1:
        raise RuntimeError(f"upload failed for {path}: {out[:200]}")
    return json.loads(out[i:])["path"]

def create(integration, caption, media_csv, date, settings):
    r = subprocess.run(["postiz","posts:create","-c",caption,"-m",media_csv,
                        "-i",integration,"-s",date,"-t","schedule",
                        "--settings",json.dumps(settings)], capture_output=True, text=True)
    return (r.stdout + r.stderr).strip()

results = []
for p in POSTS:
    if p["kind"] == "carousel":
        files = [f"out/{p['id']}-{i}.png" for i in range(1, p["n"]+1)]
    else:
        files = [p["file"]]
    print(f"\n=== {p['id']} ({p['date']}) uploading {len(files)} file(s) ===")
    urls = [upload(f) for f in files]
    media = ",".join(urls)
    tt_settings = {**TT_BASE, "title": p["tt_title"]}
    ig = create(IG, p["caption"], media, p["date"], IG_SETTINGS)
    print("IG:", ig.splitlines()[-3:] if ig else "no output")
    tt = create(TT, p["caption"], media, p["date"], tt_settings)
    print("TT:", tt.splitlines()[-3:] if tt else "no output")
    results.append({"id":p["id"],"date":p["date"],"ig":ig,"tt":tt})

print("\n===== SUMMARY =====")
for r in results:
    ig_ok = "postId" in r["ig"]
    tt_ok = "postId" in r["tt"]
    print(f"{r['id']:9} {r['date']}  IG={'OK' if ig_ok else 'FAIL'}  TT={'OK' if tt_ok else 'FAIL'}")
