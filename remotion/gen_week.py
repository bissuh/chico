#!/usr/bin/env python3
"""Generate the week's deep carousel slide props (green CleanSlide). One JSON per slide."""
import json, pathlib

PROPS = pathlib.Path("props")

carousels = {
 # ---------- SUN: The Stack ----------
 "stk": [
  {"layout":"cover","kicker":"The Stack","title":"The AI tools running one-person businesses in 2026","subtitle":"10 tools, what each is for, and when to reach for it.","footnote":"save this"},
  {"layout":"detail","kicker":"The map","title":"You don’t need all of them","body":"You need the right tool per job. Four jobs: build the thing, automate the boring parts, get paid, and grow. Here’s the one I’d reach for in each."},
  {"layout":"detail","kicker":"Build","title":"Cursor","body":"An AI code editor that writes and fixes code from plain English. The move: describe the feature, let it build, you review. Best if you want real control over the product."},
  {"layout":"detail","kicker":"Build · no code","title":"Lovable","body":"Describe an app in plain English, it ships a working full-stack version. The move: idea to clickable product in an afternoon, no coding. The best first tool for non-coders."},
  {"layout":"detail","kicker":"Build","title":"Supabase","body":"Your database, logins, and file storage, with a generous free tier. The move: it’s the backend your app saves data to. Pair it with Lovable or Cursor and you have a real product."},
  {"layout":"detail","kicker":"Automate","title":"n8n and Make","body":"Visual automation: connect apps so work happens without you. The move: auto-reply, auto-post, move data between tools. n8n if you want power and self-hosting, Make if you want easy."},
  {"layout":"detail","kicker":"Get paid","title":"Lemon Squeezy","body":"Take payments for digital products and let it handle the tax. The move: drop a buy button on anything in minutes. The fastest path from “I made a thing” to “someone paid me.”"},
  {"layout":"detail","kicker":"Grow","title":"beehiiv","body":"A newsletter platform built to grow and monetize an audience. The move: turn one-off followers into an email list you own, the only audience a platform can’t take from you."},
  {"layout":"detail","kicker":"Grow","title":"PostHog","body":"See exactly what users do in your product, free to start. The move: stop guessing, watch where people drop off, fix that, repeat. It’s how small products get good fast."},
  {"layout":"detail","kicker":"How to use this","title":"Buy nothing yet","body":"Don’t grab all ten. Find your current bottleneck, can’t build, can’t get paid, no audience, and pick the ONE tool for it. Add the next only when the first is working."},
  {"layout":"detail","kicker":"The tip","title":"Start on the free tiers","body":"Almost every tool here is free until you have real usage. Ship the thing before you pay for anything. If it works, the tools pay for themselves. If it doesn’t, you’re out nothing."},
  {"layout":"statement","title":"Pick one. Build something this week.","subtitle":"Save this for when you start. Which tool are you reaching for first? Tell me in the comments.","footnote":"save · comment"},
 ],
 # ---------- MON: Built With AI ----------
 "blt": [
  {"layout":"cover","kicker":"Built With AI","title":"A solo founder sold his AI app to Wix for $80M","subtitle":"Six months after launch. What he did, and what you can copy.","footnote":"save this"},
  {"layout":"detail","kicker":"Who","title":"One person. Maor Shlomo.","body":"He built Base44: a tool that lets anyone create a working app just by describing it. For most of the run it was a one-person operation. He hired his first few people only weeks before the sale."},
  {"layout":"detail","kicker":"The traction","title":"250,000 users. Profitable.","body":"Before selling, Base44 had around 250,000 users and was reportedly making about $189,000 a month in profit. Solo. In months. (Figures as reported.)"},
  {"layout":"detail","kicker":"The exit","title":"Wix bought it for $80M cash","body":"In June 2025, about six months after launch, Wix acquired Base44 for $80M cash, plus earn-outs that could roughly double it. Launch to life-changing in half a year."},
  {"layout":"detail","kicker":"Lesson 1","title":"He solved one painful problem","body":"Not ten. One: building apps is hard. He pointed AI at exactly that and made it easy. Narrow and painful beats broad and nice-to-have, every single time."},
  {"layout":"detail","kicker":"Lesson 2","title":"He shipped, then grew in public","body":"He didn’t wait for perfect. He launched, showed the progress, and let real users pull the product forward. Distribution and feedback first, polish later."},
  {"layout":"detail","kicker":"Lesson 3","title":"Solo plus AI replaced a team","body":"He stayed lean to the end. AI did the work a whole department used to do. That’s the shift: the headcount a real company needs just dropped toward one."},
  {"layout":"detail","kicker":"What you can copy","title":"You don’t need the $80M","body":"Copy the shape, not the number. Pick one painful task. Build the AI fix. Get 100 people who’ll pay for it. That’s a real business, exit or not."},
  {"layout":"detail","kicker":"The reframe","title":"The bar just dropped","body":"“One person can’t build a real company” stopped being true. Base44 is the proof. The only question left is which painful problem you point your AI at."},
  {"layout":"statement","title":"Pick your one painful problem.","subtitle":"Save this. What would you build if a team of one could do it? Tell me in the comments.","footnote":"save · comment"},
 ],
 # ---------- TUE: Steal This Prompt ----------
 "stl": [
  {"layout":"cover","kicker":"Steal This Prompt","title":"6 prompts to start a business this weekend","subtitle":"Copy them, paste into Claude, swap the brackets.","footnote":"save this"},
  {"layout":"prompt","kicker":"1 · Find the idea","title":"Find your weekend business","promptLabel":"Paste into Claude","prompt":"List 5 one-person businesses I could start this weekend with AI, given I’m good at [skill]. For each: who I pitch first, and the fastest path to $100."},
  {"layout":"prompt","kicker":"2 · Validate","title":"Check it before you build","promptLabel":"Paste into Claude","prompt":"I want to sell [idea]. Find 3 existing paid versions, their prices, their worst reviews, and the one angle none of them nail. Then tell me if it’s worth building."},
  {"layout":"prompt","kicker":"3 · The offer","title":"Write the offer","promptLabel":"Paste into Claude","prompt":"I can [skill]. Write a one-sentence offer, exactly who to sell it to, and a 3-message DM script that doesn’t sound desperate."},
  {"layout":"prompt","kicker":"4 · Price it","title":"Set the price","promptLabel":"Paste into Claude","prompt":"I’m selling [offer]. Give me 3 price tiers (good, better, best), what each includes, and which one a first customer is most likely to say yes to."},
  {"layout":"prompt","kicker":"5 · Find customers","title":"Find where they are","promptLabel":"Paste into Claude","prompt":"Where do [my customers] hang out, online and offline? Give me 10 specific places and a natural first-line opener for each."},
  {"layout":"prompt","kicker":"6 · Ship it","title":"Build the smallest version","promptLabel":"Paste into Claude","prompt":"Turn [offer] into the smallest version I can sell this weekend. List the exact steps to build it, and what to deliberately skip for now."},
  {"layout":"detail","kicker":"The meta-tip","title":"Get more from any prompt","body":"Three rules: give it your real context, not a generic ask. Demand specifics, not essays. End with “challenge my thinking.” That’s the gap between a toy answer and a useful one."},
  {"layout":"statement","title":"Six prompts. One weekend. No excuses.","subtitle":"Save this so you have it Saturday. Which one are you running first? Comment and I’ll help.","footnote":"save · comment"},
 ],
 # ---------- FRI: Real Niches ----------
 "nch": [
  {"layout":"cover","kicker":"Real Niches","title":"7 one-person businesses you can start with AI","subtitle":"Who pays, how much, and where to start. 2026.","footnote":"save this"},
  {"layout":"detail","kicker":"1","title":"AI automation agency","body":"Wire up workflows for one industry: clinics, agencies, real estate. Reported $2,000-$5,000 a month per client. Start: pick one industry you know, automate their most annoying task, charge monthly."},
  {"layout":"detail","kicker":"2","title":"Local SEO / Google Business","body":"Get plumbers, dentists, med spas onto Google Maps. They pay because leads are revenue. Start: fix one local business’s listing for free, show the extra calls, then charge a retainer."},
  {"layout":"detail","kicker":"3","title":"Content repurposing","body":"Turn one client video or podcast into a month of clips and posts. Reported $300-$1,000 a month each. Start: do it for one creator free for a week, then bill the time you save them."},
  {"layout":"detail","kicker":"4","title":"Faceless digital products","body":"Templates, prompt packs, mini-courses sold on autopilot. Start: make the one resource people keep asking you for, put it on Lemon Squeezy, point a no-face account at it."},
  {"layout":"detail","kicker":"5","title":"Micro-SaaS","body":"One narrow tool that solves one problem (think HeadshotPro, Base44). Start: build the smallest version with Lovable or Cursor, charge a small monthly fee, add features only when users ask."},
  {"layout":"detail","kicker":"6","title":"AI support setup","body":"Build a support or booking bot for one type of business. Reported $1,500-$5,000 to set up, plus monthly. Start: set one up for a local shop, let the result sell the next one."},
  {"layout":"detail","kicker":"7","title":"Paid newsletter","body":"Own an audience and charge for the best of it. Durable and on-brand. Start: write one free issue a week on something you know, build the list, add a paid tier once people show up."},
  {"layout":"detail","kicker":"How to pick","title":"Pick the one nearest your skill","body":"Don’t chase the biggest number. Pick the niche closest to something you already know or enjoy. That overlap is your unfair advantage, and the reason you won’t quit in week three."},
  {"layout":"statement","title":"Pick one. Get one customer. That’s the start.","subtitle":"Save this. Which niche fits you? Drop it in the comments and I’ll tell you the first move.","footnote":"save · comment"},
 ],
}

n = 0
for key, slides in carousels.items():
    total = len(slides)
    for i, s in enumerate(slides, 1):
        s["theme"] = "green"
        s["slideNo"] = i
        s["slideTotal"] = total
        s["handle"] = "@thebillionperson"
        (PROPS / f"{key}-{i}.json").write_text(json.dumps(s, ensure_ascii=False) + "\n")
        n += 1
print(f"wrote {n} slide props across {len(carousels)} carousels")
