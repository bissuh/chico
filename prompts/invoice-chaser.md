# The Invoice Chaser

A copy-paste prompt that turns Claude (or any AI) into your accounts-receivable assistant. It writes the follow-ups that get late invoices paid, so you stop leaving money you already earned in someone else's account.

The average small business is owed [$17,500 in unpaid invoices, with 47% more than 30 days late](https://quickbooks.intuit.com/r/small-business-data/small-business-late-payments-report-2025/). Most of that is not a cash-flow problem. It is follow-ups that never got sent, because chasing feels rude and you are tired. Hand that job to the prompt below.

## 1. The chaser (the one that gets you paid)

Paste this into Claude or ChatGPT, fill the brackets, and send what it writes. Run it when an invoice crosses 7 days, again at 14, again at 30.

```
Write a payment follow-up email for an invoice that is [X] days overdue.
Tone: warm for the first nudge, firmer at 30 days.
Under five sentences. Reference invoice [#], restate the amount owed, and make
paying the single easy next step. No guilt, no apology.

Client: [name]
Invoice: [#], [amount], due [date]
What the work was: [one line]
```

## 2. The line-item cleaner (so the invoice writes itself)

Before you even send the invoice, turn a rough note into clean line items:

```
You are my billing assistant. Turn this raw work note into clean invoice line
items as JSON: description, quantity, unit price, total.
Note: "[paste the raw note]". My standard rate is [$X per hour].
Flag anything ambiguous instead of guessing.
```

The "flag instead of guess" line matters. You want it to stop and ask, not invent a number.

## Make it run on autopilot

These two prompts are the brain. To make them fire by themselves, wire them into a no-code automation (n8n or Make) that watches for unpaid invoices and triggers the chaser on a schedule. The full afternoon build, with the exact tools, is here: [How to Automate Invoicing With AI](https://www.thebillionperson.com/p/how-to-automate-invoicing-with-ai).

## Get one of these every week

This prompt is from The Billion Person, a newsletter for regular people building one-person AI businesses. One human founder, one AI co-founder, building in public. [Subscribe free](https://www.thebillionperson.com/subscribe).
