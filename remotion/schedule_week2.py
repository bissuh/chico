#!/usr/bin/env python3
"""Upload + schedule week 2 to IG + TikTok (carousels) and IG + TikTok + YouTube (reels)."""
import json, subprocess

IG="cmpisrqck03e2qm0yc8qzt72e"; TT="cmpiuhmut03mcqm0ykb99rjow"; YT="cmoyuys5108jxl70yk63ihmco"
IG_SET={"post_type":"post"}
TT_BASE={"privacy_level":"PUBLIC_TO_EVERYONE","duet":False,"stitch":False,"comment":True,
         "autoAddMusic":"yes","brand_content_toggle":False,"brand_organic_toggle":False,
         "content_posting_method":"DIRECT_POST"}

POSTS=[
 {"id":"skl","kind":"carousel","n":9,"date":"2026-05-30T23:00:00Z",
  "tt":"5 AI skills that actually pay in 2026",
  "cap":"5 AI skills that actually pay in 2026, ranked by what is growing fastest on Upwork, with how to start each. Save this and pick one. Which fits you? Free playbook in bio. #aiskills #aitools #sidehustle #aibusiness #freelancing"},
 {"id":"mst","kind":"carousel","n":8,"date":"2026-05-31T23:00:00Z",
  "tt":"5 mistakes that kill a one-person business",
  "cap":"5 mistakes that kill a one-person business in the first months, and how to dodge all of them. Save this before you start. Which one stings? Free playbook in bio. #startups #solopreneur #indiehackers #aibusiness #buildinpublic"},
 {"id":"hsp","kind":"carousel","n":10,"date":"2026-06-01T23:00:00Z",
  "tt":"He turned selfies into a $3.6M business (solo)",
  "cap":"He turned selfies into a reported $3.6M-a-year business, solo, after selling an earlier AI tool for $1M. What Danny Postma did and what you can copy. Save this. (Figures reported.) #aibusiness #indiehackers #microsaas #buildinpublic #ai"},
 {"id":"prm","kind":"carousel","n":9,"date":"2026-06-02T23:00:00Z",
  "tt":"6 prompts to get your first 10 customers",
  "cap":"6 prompts to get your first 10 customers, for when you built it but the sales are not coming yet. Copy, paste into Claude, swap the brackets. Save this. #aitools #marketing #sales #sidehustle #aibusiness"},
 {"id":"val","kind":"carousel","n":9,"date":"2026-06-03T23:00:00Z",
  "tt":"Validate your business idea in an hour with AI",
  "cap":"How to validate a business idea in an hour with AI, before you waste months building the wrong thing. The exact steps and prompts inside. Save this and run it. #aibusiness #startups #indiehackers #nocode #buildinpublic"},
 {"id":"vibe-reel","kind":"reel","file":"out/vibe-reel.mp4","date":"2026-06-04T23:00:00Z",
  "tt":"Vibe coding is a debt machine","yt":"Vibe coding is quietly a debt machine",
  "cap":"Hot take: vibe coding is building a debt machine. AI ships more bugs, so the skill that pays next is verifying and fixing it. Agree? Free playbook in bio. #vibecoding #aitools #coding #indiehackers #aibusiness"},
 {"id":"vs2-reel","kind":"reel","file":"out/vs2-reel.mp4","date":"2026-06-05T23:00:00Z",
  "tt":"Audience first or product first?","yt":"Audience first or product first?",
  "cap":"Audience first or product first? Do both small: share what you learn while you build. The audience funds the product. Which are you doing? Free playbook in bio. #buildinpublic #indiehackers #onlinebusiness #aibusiness #startups"},
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
    files=[f"out/{p['id']}-{i}.png" for i in range(1,p["n"]+1)] if p["kind"]=="carousel" else [p["file"]]
    print(f"\n=== {p['id']} {p['date']} ({len(files)} file) ===")
    media=",".join(upload(f) for f in files)
    ig=create(IG,p["cap"],media,p["date"],IG_SET); print("IG:", "OK" if "postId" in ig else ig[-200:])
    tt=create(TT,p["cap"],media,p["date"],{**TT_BASE,"title":p["tt"]}); print("TT:", "OK" if "postId" in tt else tt[-200:])
    row={"id":p["id"],"ig":"postId" in ig,"tt":"postId" in tt}
    if p["kind"]=="reel":
        yt=create(YT,p["cap"],media,p["date"],{"title":p["yt"],"type":"public","selfDeclaredMadeForKids":"no"})
        print("YT:", "OK" if "postId" in yt else yt[-200:]); row["yt"]="postId" in yt
    res.append(row)

print("\n===== SUMMARY =====")
for r in res:
    extra=f" YT={'OK' if r.get('yt') else '-'}" if 'yt' in r else ""
    print(f"{r['id']:10} IG={'OK' if r['ig'] else 'FAIL'} TT={'OK' if r['tt'] else 'FAIL'}{extra}")
