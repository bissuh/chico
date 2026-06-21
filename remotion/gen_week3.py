#!/usr/bin/env python3
"""Week 3 — CAROUSEL-ONLY week (7 carousels, 0 reels). Schedule 2026-06-07..06-13.
Carousel-only experiment: measure follower growth vs the reel weeks."""
import json, pathlib
PROPS = pathlib.Path("props")

carousels = {
 # SUN 6/7 — 7 AI tools that run a one-person business (double down on tool-list winner; honest free angle)
 "tools": [
  {"layout":"cover","kicker":"The Stack","title":"7 AI tools that quietly run a one-person business","subtitle":"Most are free or near-free. Here’s the stack and what each actually costs.","footnote":"save this"},
  {"layout":"detail","kicker":"Why this matters","title":"Your stack replaces a team","body":"A solo founder now runs on tools that used to need hires. The trick is knowing which are genuinely free and which quietly bill you. Here’s the honest stack, cheapest first."},
  {"layout":"detail","kicker":"1 · Free","title":"Gemini CLI","body":"Google’s terminal AI agent, and the biggest free tier in the category: around 1,000 requests a day on a personal account, with a 1M-token context. The free way to build with an agent."},
  {"layout":"detail","kicker":"2 · Free to self-host","title":"n8n","body":"Visual automation with a native AI agent node. Self-hosted Community Edition is free with unlimited runs; you pay roughly $3 to $7 a month for a server. The one people don’t realize is free."},
  {"layout":"detail","kicker":"3 · Free tier","title":"Supabase","body":"The database and login sitting under most no-code apps. Generous free tier. Worth naming so you know what’s powering the product you ship in Lovable or Bolt."},
  {"layout":"detail","kicker":"4 · $0 to start","title":"Cursor","body":"AI code editor for when you want to see the code, not just prompt it. Free Hobby tier, Pro at $20/mo. The best on-ramp if you want to actually understand what you build."},
  {"layout":"detail","kicker":"5 · Non-coder pick","title":"Lovable","body":"Describe an app, get a real full-stack build, not a toy. Paid, but it’s the one non-coders ship actual products with. It hit $200M ARR in 2025, so it’s battle-tested."},
  {"layout":"detail","kicker":"6 · The brain","title":"Claude","body":"The thinking and writing layer: drafts, customer replies, idea validation, voice. Free tier to start. Tests keep showing it reads the least like AI."},
  {"layout":"detail","kicker":"7 · Same-day MVP","title":"Bolt","body":"Browser prompt-to-app with instant deploy. The fast rough-draft cousin to Lovable. The free tier is enough to test an idea this weekend."},
  {"layout":"statement","title":"The tools are free. The bottleneck is you.","subtitle":"Save this stack. Which one are you missing? Tell me in the comments, I answer every one.","footnote":"save · comment"},
 ],
 # MON 6/8 — 5 prompts to find a business that fits YOU (double down on prompt-pack winner)
 "find": [
  {"layout":"cover","kicker":"Steal This Prompt","title":"5 prompts to find a business that fits you","subtitle":"Stop copying other people’s ideas. Find the one only you can run.","footnote":"save this"},
  {"layout":"detail","kicker":"Why you","title":"Fit beats hype","body":"The business that works is the one matched to your skills, your access, and your hours. These 5 prompts pull that out of you. Paste into Claude, fill the brackets, be honest."},
  {"layout":"prompt","kicker":"1 · Fit","title":"Find ideas that match you","promptLabel":"Paste into Claude","prompt":"Act as a scrappy indie-hacker mentor. Me: [skills], [topics I know], [audience I can reach], [hours/week], [budget]. Give 5 one-person AI business ideas that fit. For each: the customer, the painful problem, what I’d sell, and the fastest path to the first paying customer."},
  {"layout":"prompt","kicker":"2 · Unfair edge","title":"Name your advantage","promptLabel":"Paste into Claude","prompt":"From my background above, what is my single unfair advantage: a domain I know, a skill that feels like play, or an audience I can already reach? Pick one and tell me the business that exploits it best."},
  {"layout":"prompt","kicker":"3 · Demand check","title":"See who already pays","promptLabel":"Paste into Claude","prompt":"For [idea], find 3 existing paid products, their prices, and their worst reviews. Tell me the one thing buyers clearly wish existed that none of them delivers."},
  {"layout":"prompt","kicker":"4 · Riskiest assumption","title":"Find what could kill it","promptLabel":"Paste into Claude","prompt":"For [idea], name the riskiest assumption that has to be true for this to work, and the cheapest test I can run this week to find out, before I build anything."},
  {"layout":"prompt","kicker":"5 · First customer","title":"Map the first sale","promptLabel":"Paste into Claude","prompt":"Give me the 5 fastest places to find the first paying customer for [idea], plus a short, non-pushy message I can send today that leads with their problem, not my product."},
  {"layout":"detail","kicker":"The meta-tip","title":"Specifics in, specifics out","body":"These are only as good as the detail you feed them. Paste your real skills, your real hours, the real budget. Vague input gives vague ideas you can’t use."},
  {"layout":"statement","title":"Five prompts between you and the right idea.","subtitle":"Save this and run them tonight. Which one fits you? Comment it and I’ll help you tune it.","footnote":"save · comment"},
 ],
 # TUE 6/9 — 5 lies about making money with AI (EXPERIMENT: myth-bust, share-bait)
 "myth": [
  {"layout":"cover","kicker":"Myth-Bust","title":"5 lies about making money with AI","subtitle":"The ones keeping you stuck. Send this to someone who still believes them.","footnote":"send this"},
  {"layout":"detail","kicker":"Read this first","title":"The lies feel like caution","body":"Each of these sounds responsible. That’s exactly why they keep smart people on the sidelines for years. Here’s the lie, and what’s actually true."},
  {"layout":"detail","kicker":"Lie 1","title":"“You need to learn to code first”","body":"Truth: you need to ship one thing people pay for. Non-coders are shipping real products with Lovable and Bolt right now. You learn to read the code later, if ever. Start before you feel ready."},
  {"layout":"detail","kicker":"Lie 2","title":"“You need an audience first”","body":"Truth: you need one offer and ten real conversations. The first sale comes from a DM, not a following. Audience is what you build after the first dollar, not before it."},
  {"layout":"detail","kicker":"Lie 3","title":"“The good ideas are taken”","body":"Truth: taken ideas are proven ideas. A crowded market means people pay. You don’t need a brand-new idea, you need a sharper angle for one specific group nobody serves well."},
  {"layout":"detail","kicker":"Lie 4","title":"“AI will just replace whatever I build”","body":"Truth: AI replaces tasks, not businesses with distribution and trust. The build is the cheap part now. The audience and the relationship are the moat a model can’t copy."},
  {"layout":"detail","kicker":"Lie 5","title":"“You need money to start”","body":"Most of the stack is free until you have real usage: Gemini CLI, n8n self-hosted, Supabase, free tiers everywhere. The expensive input isn’t cash. It’s the hours you keep not starting."},
  {"layout":"detail","kicker":"The pattern","title":"Every lie buys you delay","body":"Notice what they share: each one gives you permission to wait. Coding, audience, ideas, money, all excuses wearing the costume of being careful. The fix is the same: start small this week."},
  {"layout":"statement","title":"Which lie has been holding you back?","subtitle":"Send this to the person who needs it. Then tell me in the comments which one was yours.","footnote":"send · comment"},
 ],
 # WED 6/10 — Built With AI #3: Marc Lou ($1,032,000 in 2025, his own public numbers)
 "marc": [
  {"layout":"cover","kicker":"Built With AI","title":"He made $1,032,000 in 2025. One person, no team.","subtitle":"Marc Lou. What he built, and the part you can copy.","footnote":"save this"},
  {"layout":"detail","kicker":"Who","title":"A solo builder who ships tiny","body":"Marc Lou builds small software products, alone, and publishes every number. In 2025 they added up to $1,032,000. No employees. The method matters more than the figure."},
  {"layout":"detail","kicker":"The numbers","title":"Many small bets, in the open","body":"ShipFast and CodeFast around $20K a month each. His analytics tool DataFast at $15.8K MRR with roughly 1,000 paying customers. He posts the full breakdown publicly, so it’s checkable. (As reported by him.)"},
  {"layout":"detail","kicker":"Lesson 1","title":"Ship in days, not months","body":"He launches products in 24 to 72 hours. Most never take off. A few compound. You can’t pick the winner in advance, so the real skill is shipping often enough to roll the dice many times."},
  {"layout":"detail","kicker":"Lesson 2","title":"Sell to people one step behind you","body":"His best sellers teach other beginners to ship. You don’t need to be the expert. You need to be one chapter ahead and willing to document the path you just walked."},
  {"layout":"detail","kicker":"Lesson 3","title":"Build in public, on purpose","body":"Posting the numbers is the marketing. Every revenue screenshot doubles as a trust signal and a free ad. The transparency that feels scary is the distribution."},
  {"layout":"detail","kicker":"Lesson 4","title":"Small and many beats big and one","body":"He didn’t bet everything on one perfect product. He made many cheap bets and let the market pick the winner. One person can run a whole portfolio when AI does the grunt work."},
  {"layout":"detail","kicker":"What you copy","title":"You don’t need the million","body":"You need the shape: ship something tiny this month, in public, to people one step behind you. Then do it again. The number is just that, repeated enough times."},
  {"layout":"statement","title":"What could you ship in 72 hours?","subtitle":"Save this for your next build. Tell me the tiny thing you’d ship first, comments are open.","footnote":"save · comment"},
 ],
 # THU 6/11 — n8n vs Make (EXPERIMENT: comparison carousel)
 "vs": [
  {"layout":"cover","kicker":"This vs That","title":"n8n vs Make: which should a beginner pick?","subtitle":"Both automate your busywork with AI. They bill in very different ways.","footnote":"save this"},
  {"layout":"detail","kicker":"Why it matters","title":"The wrong pick gets expensive","body":"Automation is how a one-person business runs while you sleep. But these two charge differently, and the wrong choice can quietly multiply your bill. Here’s the honest call."},
  {"layout":"detail","kicker":"Make","title":"Prettier, bills per operation","body":"Drag-and-drop, gentle first hour, Core plan around $9/mo for about 10,000 operations. Every step in a workflow burns operations, so complex flows get pricey fast. Good training wheels."},
  {"layout":"detail","kicker":"n8n","title":"Deeper, bills per run","body":"One full workflow run counts as a single execution, whether it has 3 steps or 30. Self-hosted Community Edition is free with unlimited runs; you pay about $3 to $7 a month for a server."},
  {"layout":"detail","kicker":"The crossover","title":"Where the money flips","body":"Simple flows: Make feels easier. The day your automation hits 10 or more steps, Make’s per-operation billing climbs and n8n can run 10 to 20x cheaper for the same job."},
  {"layout":"detail","kicker":"AI edge","title":"n8n for agents","body":"n8n’s native AI agent node is ahead for anything where a model decides what to do next. If your automation needs to think, not just move data around, n8n is the stronger base."},
  {"layout":"detail","kicker":"The verdict","title":"Make to learn, n8n to scale","body":"Never automated anything? Start on Make this week and get one win. The moment money or complexity shows up, move to n8n. Learn on the easy one, scale on the cheap one."},
  {"layout":"statement","title":"Make to learn. n8n to scale.","subtitle":"Save this before you pick. Which one are you on? Comment your setup and I’ll tell you if it fits.","footnote":"save · comment"},
 ],
 # FRI 6/12 — 5 signs you're tool-rich and business-poor (Checklist/Audit, send-bait; was the hot-take reel)
 "hoard": [
  {"layout":"cover","kicker":"Quick Audit","title":"5 signs you’re tool-rich and business-poor","subtitle":"You’ve tried every AI app and sold nothing. Here’s the pattern, and the fix.","footnote":"save this"},
  {"layout":"detail","kicker":"The trap","title":"Collecting tools feels like progress","body":"Every new app feels like a step forward. It isn’t. Tools don’t make money, customers do. Here are 5 signs you’re optimizing the wrong thing, and what to do instead."},
  {"layout":"detail","kicker":"Sign 1","title":"10 tools tried, 0 offers shipped","body":"Your bookmarks are full and your Stripe is empty. The fix: pick one tool you already have and use it to make one thing a real person can pay for this week."},
  {"layout":"detail","kicker":"Sign 2","title":"You research more than you build","body":"Another comparison video, another thread, another newsletter. Input feels safe. The fix: cap research at one hour, then spend the rest of the day building the smallest possible version."},
  {"layout":"detail","kicker":"Sign 3","title":"You can name 20 tools, 0 customers","body":"You know every AI app and not one person who’d pay you. The fix: spend a day finding ten people with the problem before you open another tool."},
  {"layout":"detail","kicker":"Sign 4","title":"You upgrade before you earn","body":"Paying for the Pro plan of a tool that hasn’t made you a dollar. The fix: stay on free tiers until a real customer’s money justifies the upgrade. Most tools are free until you have usage."},
  {"layout":"detail","kicker":"Sign 5","title":"Your “business” has no one to sell to","body":"You built the thing first and the audience never came. The fix: flip it. Find who you’d sell to, confirm they’ll pay, then build the smallest version that helps them."},
  {"layout":"detail","kicker":"The reframe","title":"One offer beats ten subscriptions","body":"Rich in tools, poor in customers is the default trap of 2026. The way out is boring: one tool, one problem, one person who pays. Everything else is procrastination with a login screen."},
  {"layout":"statement","title":"Which sign hit closest?","subtitle":"Send this to the friend with 30 tabs open and 0 sales. Then tell me your number in the comments.","footnote":"send · comment"},
 ],
 # SAT 6/13 — Turn one idea into a week of content (Step-by-step tutorial; was the vs reel)
 "week": [
  {"layout":"cover","kicker":"Do This Today","title":"Turn one idea into a week of content with AI","subtitle":"One topic. Seven posts. About an hour of work.","footnote":"save this"},
  {"layout":"detail","kicker":"Why","title":"You don’t have an idea problem","body":"You have a packaging problem. One real idea can become a week of posts if you slice it right. Here’s the exact system, faceless-friendly, no camera needed."},
  {"layout":"detail","kicker":"Step 1","title":"Pick one idea you can teach","body":"Not a topic, a single takeaway someone could act on today. “How to validate an idea in an hour.” If you can say it in one sentence, it’s sharp enough to build a week around."},
  {"layout":"prompt","kicker":"Step 2","title":"Slice it into seven angles","promptLabel":"Paste into Claude","prompt":"Take this one idea: [idea]. Break it into 7 distinct content angles for a faceless brand. For each: a scroll-stopping hook, the format (carousel or list), and 3 to 5 bullets of real substance. Make at least 3 of them numbered list posts."},
  {"layout":"detail","kicker":"Step 3","title":"Write the list posts first","body":"Numbered posts (“5 tools”, “6 prompts”) are the easiest to write and the most saved. Knock those out first. They carry the week while the deeper ones cook."},
  {"layout":"prompt","kicker":"Step 4","title":"Write each one in your voice","promptLabel":"Paste into Claude","prompt":"Here’s my angle: [angle]. Write the carousel: a cover hook, 6 to 8 content slides with one real idea each, and a final slide that asks for a save and a comment. Plain language, name real tools, no fluff."},
  {"layout":"detail","kicker":"Step 5","title":"Design once, reuse the template","body":"Build one clean slide layout and pour each post into it. Same look, different content. A code template (Remotion) or a Canva bulk-create turns seven posts into one batch, not seven projects."},
  {"layout":"detail","kicker":"Step 6","title":"Schedule the whole week at once","body":"Batch beats daily. Load all seven into a scheduler like Postiz on a fixed daily slot. Now you’re a week ahead and posting on autopilot while you build the next thing."},
  {"layout":"statement","title":"One idea. Seven posts. One hour.","subtitle":"Save this and run it on your next idea. What topic would you start with? Tell me in the comments.","footnote":"save · comment"},
 ],
}

n=0
for key, slides in carousels.items():
    total=len(slides)
    for i,s in enumerate(slides,1):
        s["theme"]="green"; s["slideNo"]=i; s["slideTotal"]=total; s["handle"]="@thebillionperson"
        (PROPS/f"{key}-{i}.json").write_text(json.dumps(s, ensure_ascii=False)+"\n")
        n+=1

print(f"wrote {n} carousel slides across {len(carousels)} carousels (carousel-only week)")
