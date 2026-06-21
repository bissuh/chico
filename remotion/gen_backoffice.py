#!/usr/bin/env python3
"""Back-office fillers (3 carousels) distilled from the 2026-06-15 newsletter research.
Days 8-10 of the 10-day IG/TikTok run: 2026-06-22..06-24. Carousel-only, CleanSlide green."""
import json, pathlib
PROPS = pathlib.Path("props")

carousels = {
 # MON 6/22 — Automate invoicing with AI (tutorial)
 "inv": [
  {"layout":"cover","kicker":"Do This Today","title":"Automate your invoicing with AI in an afternoon","subtitle":"The no-code stack that creates, sends, and chases invoices while you work.","footnote":"save this"},
  {"layout":"detail","kicker":"Why this","title":"Invoicing is pure overhead","body":"You finish the work, then lose an evening copying numbers, emailing, and forgetting to follow up. The average small business is owed $17,500 in unpaid invoices. It is the easiest job to hand to AI."},
  {"layout":"detail","kicker":"The shape","title":"Three moves, on repeat","body":"A messy input, a tool that does the job, and an AI that glues them together. Once you see it, you spot it everywhere in a one-person business."},
  {"layout":"detail","kicker":"1 · Trigger","title":"Start from a real event","body":"Pick the moment a job becomes billable: a deal marked won, a row added to a done sheet. In n8n or Make, that is your trigger node. Not a calendar reminder you will ignore."},
  {"layout":"prompt","kicker":"2 · Clean it up","title":"Let Claude write the line items","promptLabel":"Paste into Claude","prompt":"You are my billing assistant. Turn this work note into clean invoice line items as JSON: description, quantity, unit price, total. Note: '[paste]'. My rate is [$X/hr]. Flag anything ambiguous instead of guessing."},
  {"layout":"detail","kicker":"3 · Send","title":"Stripe or Lemon Squeezy sends it","body":"Pass the clean items to Stripe Invoicing or Lemon Squeezy. It creates the invoice, brands it, and emails it with a payment link. Both have full APIs, so n8n and Make connect out of the box."},
  {"layout":"prompt","kicker":"4 · Chase","title":"The follow-up that gets you paid","promptLabel":"Paste into Claude","prompt":"Write a payment follow-up for an invoice that is [X] days overdue. Tone: warm first, firmer at 30 days. Under five sentences. Reference invoice [#], restate the amount, make paying the easy next step. No guilt."},
  {"layout":"detail","kicker":"5 · Reconcile","title":"Close the loop on its own","body":"When the payment-received event fires, the automation marks it paid, logs it in your books, and stops the reminders. Your records update themselves."},
  {"layout":"statement","title":"Invoicing, on autopilot by Friday.","subtitle":"Save this and build it this weekend. Stuck on a step? Ask in the comments, I answer every one.","footnote":"save · comment"},
 ],
 # TUE 6/23 — The invoice-chaser prompt (steal-this-prompt)
 "chase": [
  {"layout":"cover","kicker":"Steal This Prompt","title":"The AI prompt that gets your late invoices paid","subtitle":"The follow-up is where the money leaks. Automate the one step most people skip.","footnote":"save this"},
  {"layout":"detail","kicker":"The leak","title":"You send once, then go quiet","body":"Chasing feels rude, so the invoice sits unpaid. That is money you already earned, parked in someone else's account. The fix is not sending invoices. It is chasing them."},
  {"layout":"detail","kicker":"The cadence","title":"Nudge at 7, 14, and 30 days","body":"Warm at first, firmer later. Most invoices get paid the moment a polite reminder lands. You just never send it. Let the prompt write it so you actually do."},
  {"layout":"prompt","kicker":"The prompt","title":"Paste this into Claude","promptLabel":"Fill the brackets","prompt":"Write a payment follow-up email for an invoice that is [X] days overdue. Tone: warm for the first nudge, firmer at 30 days. Under five sentences. Reference invoice [#], restate the amount owed, make paying the single easy next step. No guilt, no apology."},
  {"layout":"detail","kicker":"Make it auto","title":"Fire it without lifting a finger","body":"Wire it into n8n or Make: watch for unpaid invoices, and when one crosses 7, 14, or 30 days, the AI drafts the reminder and sends it. You approve the tone once and forget it."},
  {"layout":"detail","kicker":"Why it works","title":"Easy to pay beats polite","body":"The email restates the amount and makes paying one click. No apology, no guilt-trip. You are not being pushy. You are removing the friction between you and money you are owed."},
  {"layout":"detail","kicker":"The number","title":"$17,500, on average","body":"That is what a typical small business is owed in unpaid invoices, 47% of them more than 30 days late. The follow-up you automate today is the cash you collect this month."},
  {"layout":"statement","title":"Get paid weeks sooner.","subtitle":"Save this and run it on your oldest unpaid invoice tonight. How much are you owed right now? Comments are open.","footnote":"save · comment"},
 ],
 # WED 6/24 — Automate bookkeeping with AI (tutorial)
 "book": [
  {"layout":"cover","kicker":"Do This Today","title":"Automate your bookkeeping with AI","subtitle":"No accounting degree. Connect your bank, let AI categorize, get a plain-English report.","footnote":"save this"},
  {"layout":"detail","kicker":"Why this","title":"The weekend that never happens","body":"Three months of uncategorized transactions you keep meaning to deal with. Bookkeeping is the same three moves on repeat, the exact boring loop AI is built for. You stay the boss who approves."},
  {"layout":"detail","kicker":"What you need","title":"Three tools, mostly free","body":"Claude to categorize and explain, n8n or Make to move the data, QuickBooks or Xero (or a free Google Sheet) to hold it. Both accounting tools have public APIs and pull your bank feed automatically."},
  {"layout":"detail","kicker":"1 · Connect","title":"Pipe in the transactions","body":"Link your business bank to QuickBooks or Xero so transactions flow in on their own. Not ready to pay? Export a CSV into a Google Sheet. One place where every raw transaction lands without typing."},
  {"layout":"prompt","kicker":"2 · Categorize","title":"Let Claude sort every line","promptLabel":"Paste into Claude","prompt":"You are my bookkeeping assistant. Given a transaction (date, amount, merchant), return ONLY JSON: category (Software, Contractors, Marketing, Office, Travel, Income, Fees, Other), confidence (high/medium/low), note. If low, still pick the best and say why. Transaction: {{tx}}"},
  {"layout":"detail","kicker":"3 · Reconcile","title":"Only check the fuzzy 10%","body":"Write each categorized line back to your books, then filter for medium and low confidence and review only those. You spot-check the unclear ones instead of touching all of them."},
  {"layout":"prompt","kicker":"4 · Report","title":"A monthly summary in plain English","promptLabel":"Paste into Claude","prompt":"Here are my categorized transactions for the month as JSON. Write a short summary for a non-accountant: total income, total expenses, net, top 3 expense categories with amounts, and one plain observation about cash flow. Under 200 words. Data: {{month}}"},
  {"layout":"detail","kicker":"5 · Catch problems","title":"Flag what a tired human misses","body":"Add one check: ask Claude to scan the month for duplicates, a doubled subscription, an unknown vendor, anything far outside the usual range. The thing you skip at 11pm, the automation never does."},
  {"layout":"statement","title":"Clean books, zero spreadsheets.","subtitle":"Save this and build it this weekend. A human accountant still owns your taxes, this just keeps the records current. Questions? Comment them.","footnote":"save · comment"},
 ],
}

n=0
for key, slides in carousels.items():
    total=len(slides)
    for i,s in enumerate(slides,1):
        s["theme"]="green"; s["slideNo"]=i; s["slideTotal"]=total; s["handle"]="@thebillionperson"
        (PROPS/f"{key}-{i}.json").write_text(json.dumps(s, ensure_ascii=False)+"\n")
        n+=1

print(f"wrote {n} slides across {len(carousels)} carousels (back-office fillers)")
