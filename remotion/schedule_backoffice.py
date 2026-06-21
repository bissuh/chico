#!/usr/bin/env python3
"""Schedule the 3 back-office filler carousels to IG + TikTok, 2026-06-22..06-24, 23:00 UTC.
Days 8-10 of the 10-day run. Run from remotion/ after rendering, after sourcing ../.env."""
import json, subprocess

IG="cmpisrqck03e2qm0yc8qzt72e"; TT="cmpiuhmut03mcqm0ykb99rjow"
IG_SET={"post_type":"post"}
TT_BASE={"privacy_level":"PUBLIC_TO_EVERYONE","duet":False,"stitch":False,"comment":True,
         "autoAddMusic":"yes","brand_content_toggle":False,"brand_organic_toggle":False,
         "content_posting_method":"DIRECT_POST"}

POSTS=[
 {"id":"inv","n":9,"date":"2026-06-22T23:00:00Z",
  "tt":"Automate your invoicing with AI in an afternoon",
  "cap":"Automate your invoicing with AI: create, send, chase, and reconcile invoices on autopilot. The no-code stack and the exact prompts, free tools first. Save this and build it this weekend. Free playbook in bio. #aitools #aibusiness #nocode #invoicing #solopreneur"},
 {"id":"chase","n":8,"date":"2026-06-23T23:00:00Z",
  "tt":"The AI prompt that gets late invoices paid",
  "cap":"The follow-up is where the money leaks. One AI prompt writes the reminder that gets late invoices paid, warm first, firmer at 30 days. Save it and run it on your oldest unpaid invoice tonight. Free playbook in bio. #aitools #invoicing #freelance #aibusiness #solopreneur"},
 {"id":"book","n":9,"date":"2026-06-24T23:00:00Z",
  "tt":"Automate your bookkeeping with AI",
  "cap":"Automate your bookkeeping with AI, no accounting degree. Connect your bank, let Claude categorize every transaction, get a plain-English monthly report. The no-code build inside. Save this. Free playbook in bio. #aitools #bookkeeping #aibusiness #nocode #smallbusiness"},
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
