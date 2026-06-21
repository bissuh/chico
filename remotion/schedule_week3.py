#!/usr/bin/env python3
"""Upload + schedule Week 3 (CAROUSEL-ONLY) to IG + TikTok. 7 carousels, 2026-06-15..06-21, 23:00 UTC.
Run from remotion/ after rendering (out/<id>-<i>.png exist) and after `set -a && source ../.env && set +a`.
  cd /Users/bissuh/Documents/TBP/chico/remotion && python3 schedule_week3.py
No YouTube here (carousel-only week; YT is for reels)."""
import json, subprocess

IG="cmpisrqck03e2qm0yc8qzt72e"; TT="cmpiuhmut03mcqm0ykb99rjow"
IG_SET={"post_type":"post"}
TT_BASE={"privacy_level":"PUBLIC_TO_EVERYONE","duet":False,"stitch":False,"comment":True,
         "autoAddMusic":"yes","brand_content_toggle":False,"brand_organic_toggle":False,
         "content_posting_method":"DIRECT_POST"}

POSTS=[
 {"id":"tools","n":10,"date":"2026-06-15T23:00:00Z",
  "tt":"7 AI tools that run a one-person business",
  "cap":"7 AI tools that quietly run a one-person business, cheapest first, with what each actually costs. Most are free or near-free. Save this and pick the one you're missing. Free playbook in bio. #aitools #aibusiness #solopreneur #indiehackers #nocode"},
 {"id":"find","n":9,"date":"2026-06-16T23:00:00Z",
  "tt":"5 prompts to find a business that fits you",
  "cap":"5 prompts to find a business that actually fits you, not someone else's idea. Paste into Claude, fill the brackets, be honest. Save this and run them tonight. Free playbook in bio. #aitools #aibusiness #sidehustle #buildinpublic #claude"},
 {"id":"myth","n":9,"date":"2026-06-17T23:00:00Z",
  "tt":"5 lies about making money with AI",
  "cap":"5 lies about making money with AI, and what's actually true. Each one sounds like caution and keeps you stuck. Send this to someone who still believes them. #aibusiness #startups #solopreneur #indiehackers #makemoneyonline"},
 {"id":"marc","n":9,"date":"2026-06-18T23:00:00Z",
  "tt":"He made $1,032,000 in 2025, solo (Marc Lou)",
  "cap":"He made a reported $1,032,000 in 2025, one person, no team, and publishes every number. What Marc Lou did and the part you can copy. Save this. (Figures as reported by him.) #buildinpublic #indiehackers #microsaas #aibusiness #solopreneur"},
 {"id":"vs","n":8,"date":"2026-06-19T23:00:00Z",
  "tt":"n8n vs Make: which should a beginner pick?",
  "cap":"n8n vs Make for a beginner. Both automate your busywork with AI, but they bill very differently and the wrong pick gets expensive. The honest call inside. Save this before you choose. #n8n #make #automation #aitools #aibusiness"},
 {"id":"hoard","n":9,"date":"2026-06-20T23:00:00Z",
  "tt":"5 signs you're tool-rich and business-poor",
  "cap":"5 signs you're tool-rich and business-poor, and the fix for each. You've tried every AI app and sold nothing? This is the pattern. Send it to the friend with 30 tabs open. #aitools #solopreneur #indiehackers #aibusiness #startups"},
 {"id":"week","n":9,"date":"2026-06-21T23:00:00Z",
  "tt":"Turn one idea into a week of content with AI",
  "cap":"Turn one idea into a week of content with AI. One topic, seven posts, about an hour. The exact steps and prompts inside, faceless-friendly. Save this and run it on your next idea. #contentcreation #aitools #faceless #aibusiness #buildinpublic"},
]

def upload(p):
    out=subprocess.run(["postiz","upload",p],capture_output=True,text=True).stdout
    i=out.find("{")
    if i==-1: raise RuntimeError(f"upload fail {p}: {out[:150]}")
    return json.loads(out[i:])["path"]

def create(integ,cap,media,date,settings):
    r=subprocess.run(["postiz","posts:create","-c",cap,"-m",media,"-i",integ,"-s",date,
                      "-t","schedule","--settings",json.dumps(settings)],capture_output=True,text=True)
    return (r.stdout+r.stderr)

res=[]
for p in POSTS:
    assert p["n"]<=10, f"{p['id']} has {p['n']} slides; IG API rejects >10"
    files=[f"out/{p['id']}-{i}.png" for i in range(1,p["n"]+1)]
    print(f"\n=== {p['id']} {p['date']} ({len(files)} slides) ===")
    media=",".join(upload(f) for f in files)
    ig=create(IG,p["cap"],media,p["date"],IG_SET); print("IG:", "OK" if "postId" in ig else ig[-200:])
    tt=create(TT,p["cap"],media,p["date"],{**TT_BASE,"title":p["tt"]}); print("TT:", "OK" if "postId" in tt else tt[-200:])
    res.append({"id":p["id"],"ig":"postId" in ig,"tt":"postId" in tt})

print("\n===== SUMMARY =====")
for r in res:
    print(f"{r['id']:8} IG={'OK' if r['ig'] else 'FAIL'} TT={'OK' if r['tt'] else 'FAIL'}")
