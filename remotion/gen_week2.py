#!/usr/bin/env python3
"""Week 2 deep carousel slide props (green CleanSlide)."""
import json, pathlib
PROPS = pathlib.Path("props")

carousels = {
 # SAT 5/30 — 5 AI skills that pay (Upwork 2026 growth data)
 "skl": [
  {"layout":"cover","kicker":"The Skills","title":"5 AI skills that actually pay in 2026","subtitle":"Ranked by what’s growing fastest, and how to start each.","footnote":"save this"},
  {"layout":"detail","kicker":"Why now","title":"Demand more than doubled","body":"On Upwork, demand for AI skills grew over 100% this year. These five grew fastest, and a non-coder can learn every one of them. Pick the one closest to what you already do."},
  {"layout":"detail","kicker":"1","title":"AI automation and agents","body":"Up ~178% on Upwork this year. Businesses know they should automate but can’t. You connect their tools (email, CRM, sheets) with an AI layer. The highest-demand, least-crowded skill for non-coders."},
  {"layout":"detail","kicker":"2","title":"AI video creation","body":"The single fastest-growing AI skill, up ~329%. Brands need short video constantly and can’t make it fast enough. You generate and edit it with AI. Bonus: it’s the exact skill behind faceless content."},
  {"layout":"detail","kicker":"3","title":"AI image creation","body":"Up ~95%. Every brand needs product shots, ads, and thumbnails without hiring a photographer or designer. Learn the tools, sell the output. (HeadshotPro is just this skill, productized.)"},
  {"layout":"detail","kicker":"4","title":"Vibe coding, plus the fix","body":"Anyone can prompt an app into existence now. The money is in the people who can also check it works and patch what breaks. Studies show AI code ships more bugs, so the verify-and-fix layer pays."},
  {"layout":"detail","kicker":"5","title":"AI content and AI-search SEO","body":"Companies are scrambling to get cited inside ChatGPT and Perplexity answers, not just rank on Google. Learn to build AI content systems that get a brand mentioned where people now ask."},
  {"layout":"detail","kicker":"How to start","title":"One skill. One free project.","body":"Don’t learn all five. Pick one, do one project free for a real business, screenshot the result, then charge for the next. Reported beginner rates run a few hundred per project, rising fast with proof."},
  {"layout":"statement","title":"Pick one skill. Land one client.","subtitle":"Save this. Which one fits you? Tell me in the comments and I’ll point you to the first step.","footnote":"save · comment"},
 ],
 # SUN 5/31 — 5 mistakes that kill a one-person business
 "mst": [
  {"layout":"cover","kicker":"Avoid These","title":"5 mistakes that kill a one-person business","subtitle":"Most fail for the same few reasons. Here they are.","footnote":"save this"},
  {"layout":"detail","kicker":"Mistake 1","title":"Building before validating","body":"The number one killer. Around 40% of startups die because there was no real market need. You fall in love with your idea and build for months before one person agrees to pay. Talk to buyers first."},
  {"layout":"detail","kicker":"Mistake 2","title":"Polishing instead of shipping","body":"Endless tweaking with zero customer feedback feels like progress. It isn’t. Ship the version that slightly embarrasses you, then let real usage tell you what to fix. Perfect is just fear in a nicer outfit."},
  {"layout":"detail","kicker":"Mistake 3","title":"No distribution plan","body":"“Build it and they’ll come” is not a plan. In a world where anyone can build the same tool in a weekend, the product is no longer the moat. Distribution is. Decide how people will find it before you build it."},
  {"layout":"detail","kicker":"Mistake 4","title":"Burning runway too early","body":"Paying for tools and ads before there’s a dollar of revenue, or quitting the job too soon. Stay cheap and employed until the thing makes money. Most tools you need are free until you have real usage."},
  {"layout":"detail","kicker":"Mistake 5","title":"Doing every single thing yourself","body":"Around 70% of solo founders quit within two years, vs ~40% of teams. The fix isn’t hiring. It’s narrowing scope and handing the grunt work to AI, so you make good calls instead of burning out."},
  {"layout":"detail","kicker":"The pattern","title":"They’re all one mistake","body":"Building in a vacuum. Talk to buyers, ship early, plan distribution, stay lean. Do that and you dodge all five at once. The work isn’t the risk. Doing it alone in the dark is."},
  {"layout":"statement","title":"Which one were you about to make?","subtitle":"Save this before you start. Tell me in the comments which one stings, I answer every one.","footnote":"save · comment"},
 ],
 # MON 6/1 — Built With AI #2: HeadshotPro
 "hsp": [
  {"layout":"cover","kicker":"Built With AI","title":"He turned selfies into a $3.6M-a-year business. Solo.","subtitle":"Danny Postma, HeadshotPro. What he did, what you copy.","footnote":"save this"},
  {"layout":"detail","kicker":"Who","title":"One founder, from Bali","body":"Danny Postma built HeadshotPro: upload a few selfies, get professional corporate headshots from AI. No team. He’d built and sold AI products before, working solo from a laptop."},
  {"layout":"detail","kicker":"The numbers","title":"~$300K a month","body":"Within about a year, HeadshotPro was reportedly making around $300,000 a month, roughly $3.6M a year. One person, one narrow product. (Figures as reported.)"},
  {"layout":"detail","kicker":"And before that","title":"A $1M exit in 8 months","body":"His earlier AI product, Headlime, sold for $1,000,000, about eight months after launch. He’s done the solo-to-exit move more than once. It’s a repeatable pattern, not a fluke."},
  {"layout":"detail","kicker":"Lesson 1","title":"He sold the outcome, not the AI","body":"Nobody buys “diffusion models.” They buy “a great headshot without a photographer.” He wrapped one AI capability in a dead-simple promise and charged for the result."},
  {"layout":"detail","kicker":"Lesson 2","title":"Distribution was the real product","body":"SEO and affiliates drove the growth, reportedly $50K a month from affiliates alone. The AI was copyable. The traffic engine wasn’t. He won on distribution, not technology."},
  {"layout":"detail","kicker":"Lesson 3","title":"No face required","body":"He didn’t need a personal brand or a daily posting habit. The tool solved a real problem and the funnel sold it. Faceless, on purpose."},
  {"layout":"detail","kicker":"What you copy","title":"Package what AI does well","body":"Pick one thing AI is genuinely good at. Wrap it in a simple paid tool with a clear promise. Drive traffic with SEO or partners. You don’t need the $3.6M, you need the shape."},
  {"layout":"detail","kicker":"The reframe","title":"You don’t invent AI. You package it.","body":"The opportunity isn’t building the model. It’s packaging what already exists for the people who won’t. That gap is wide open, and one person can fill it."},
  {"layout":"statement","title":"What would you package?","subtitle":"Save this. Tell me the one thing AI does well that you’d turn into a product. Comments are open.","footnote":"save · comment"},
 ],
 # TUE 6/2 — Steal This Prompt #2: get your first customers
 "prm": [
  {"layout":"cover","kicker":"Steal This Prompt","title":"6 prompts to get your first 10 customers","subtitle":"For when you’ve built it but nobody’s buying yet.","footnote":"save this"},
  {"layout":"prompt","kicker":"1 · Reach out","title":"Cold DMs that don’t suck","promptLabel":"Paste into Claude","prompt":"I sell [offer] to [audience]. Write 5 cold DMs that lead with their problem, not my product. Each under 4 sentences, friendly, no “hope you’re well.”"},
  {"layout":"prompt","kicker":"2 · Proof","title":"Turn a thank-you into proof","promptLabel":"Paste into Claude","prompt":"Here’s a happy customer message: [paste]. Turn it into 3 short social-proof posts and a one-paragraph case study, in plain language, no hype."},
  {"layout":"prompt","kicker":"3 · Objections","title":"Handle the no","promptLabel":"Paste into Claude","prompt":"List the top 7 reasons someone won’t buy [offer], and a one-line, non-pushy response to each that I could actually say out loud."},
  {"layout":"prompt","kicker":"4 · Content","title":"Posts that attract buyers","promptLabel":"Paste into Claude","prompt":"Give me 10 post ideas about [topic] that attract people who’d buy [offer], not just random likes. For each, the hook and the one takeaway."},
  {"layout":"prompt","kicker":"5 · Follow up","title":"The “maybe later” save","promptLabel":"Paste into Claude","prompt":"Write a 3-message follow-up for a lead who said “maybe later,” spaced over two weeks. Helpful, not annoying. Each message gives value before it asks."},
  {"layout":"prompt","kicker":"6 · Price","title":"Make the price an easy yes","promptLabel":"Paste into Claude","prompt":"I sell [offer] at [price]. Write the offer copy that makes it an obvious yes, and add a higher-priced option to anchor against so the main one feels fair."},
  {"layout":"detail","kicker":"The meta-tip","title":"Specifics in, specifics out","body":"These work as well as the context you give them. Paste real details: your actual offer, real customer words, the true price. Vague prompts give vague answers you can’t use."},
  {"layout":"statement","title":"Six prompts between you and your first sale.","subtitle":"Save this for launch day. Which one do you need most? Comment it and I’ll help you tune it.","footnote":"save · comment"},
 ],
 # WED 6/3 — Tutorial: validate an idea in an hour
 "val": [
  {"layout":"cover","kicker":"Do This Today","title":"Validate your idea in an hour, before you build","subtitle":"The cheapest hour you’ll ever spend.","footnote":"save this"},
  {"layout":"detail","kicker":"Why","title":"Most ideas die from being wrong","body":"The top reason one-person businesses fail is building something nobody wanted. One hour of real validation can save you three months of building the wrong thing. Here’s the hour."},
  {"layout":"detail","kicker":"Step 1","title":"Write the problem in one line","body":"Not your solution, the problem. “Freelancers don’t know what to charge.” If you can’t say it in one sentence, you don’t understand it yet, and neither will a buyer."},
  {"layout":"prompt","kicker":"Step 2","title":"See who already pays","promptLabel":"Paste into Claude","prompt":"Find 3 existing paid products that solve [problem], their prices, and their worst reviews. Tell me what buyers clearly wish existed but none of them deliver."},
  {"layout":"prompt","kicker":"Step 3","title":"Ask 5 real people","promptLabel":"Paste into Claude","prompt":"Write 5 questions I can ask potential buyers of [offer] that reveal whether they’d actually pay, without leading them or pitching. Focus on what they do now and what it costs them."},
  {"layout":"detail","kicker":"Step 4","title":"Ask for money or an email","body":"The only real validation. Put up a one-page offer or waitlist and ask for a pre-order or a signup. People say “great idea” to be nice. They give money or their email only when they mean it."},
  {"layout":"detail","kicker":"Step 5","title":"Read the signal honestly","body":"Green light: people pre-pay or sign up fast. Red light: lots of polite “cool, keep me posted.” Compliments are not customers. Believe the behavior, not the encouragement."},
  {"layout":"detail","kicker":"The rule","title":"Money or emails. Nothing else.","body":"Validation is people giving you their money or their email. Likes, “love this,” and your own excitement don’t count. Get one of the two before you build the whole thing."},
  {"layout":"statement","title":"One hour now saves three months later.","subtitle":"Save this and run it before your next build. Stuck on a step? Ask in the comments.","footnote":"save · comment"},
 ],
}

n=0
for key, slides in carousels.items():
    total=len(slides)
    for i,s in enumerate(slides,1):
        s["theme"]="green"; s["slideNo"]=i; s["slideTotal"]=total; s["handle"]="@thebillionperson"
        (PROPS/f"{key}-{i}.json").write_text(json.dumps(s, ensure_ascii=False)+"\n")
        n+=1
print(f"wrote {n} slides across {len(carousels)} carousels")
