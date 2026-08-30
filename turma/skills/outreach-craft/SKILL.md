---
name: outreach-craft
description: Run cold outreach as a campaign instead of a hope. Invoke when someone wants to "send cold emails," "cold DM someone," "reach out to prospects, partners, investors, press or creators," "build an outreach campaign," "pitch a collab," "get a meeting," "write a follow-up sequence," or says "nobody replies to my emails." Covers the four layers a campaign needs: the machine (sending domains, warmup, deliverability, the law where the recipient sits), the list (who, and how few), the message (five lines, one ask), and the loop (send, read replies, kill, double down). Also covers the single high-stakes door-knock that is not a campaign at all. Composes the `cold-email` skill for B2B message craft when it is installed. Reads brand.md.
---

# outreach-craft

Cold outreach is the only distribution channel that works on day zero with an audience of nobody. SEO takes months to compound. Social takes a following. Ads take money the underdog does not have. An email takes a name and a real reason. That is why it belongs to the projects this crew works on.

It is also the channel most likely to be run badly, because the failure is invisible. A post that flops shows you a zero. A cold campaign that flops looks identical to a cold campaign that was never delivered, and most of the time the second one is what happened.

The writing is almost never the problem. The problem is sending from a domain you cannot afford to burn, to a list you never qualified, with an ask that costs the reader more than a reply is worth.

**Before you start:** read the project's `brand.md`. The offer, the audience, the primary conversion goal, the voice. Outreach on top of fuzzy positioning is spam with good grammar. If the offer is still a vitamin or the audience is "everyone," stop and run `turma:positioning`. No subject line fixes that.

## When to invoke

- Any first-contact message to someone who does not know the project: email, X DM, LinkedIn, Instagram, a contact form, a form on a label's site.
- Building a campaign end to end: the list, the sequence, the sending setup, the measurement loop.
- One high-stakes send. The investor, the distributor, the podcast host, the creator whose audience is exactly yours.
- Diagnosing a dead campaign. "We sent 200 and got nothing."
- Before anyone buys a sending platform or a data seat. That is money, so it is Red, and it is usually unnecessary for the first hundred sends.

## When NOT to invoke

- Warm lifecycle email: welcome flows, newsletter editions, re-engagement of people who opted in. Different law, different craft. Platform work is `turma:beehiiv-connector`, the writing is `turma:story-craft`.
- The offer or the landing page the outreach points at. That is `turma:conversion-craft`, and it comes first. A reply that lands on a broken page is a wasted reply.
- What you sell and to whom. `turma:positioning`.
- The final voice pass. `turma:anti-ai-linguo`, Mode 4 (Outreach). Always last, after this skill.
- Bulk marketing mail to a list that opted in. That is email marketing, not outreach.

## The rule that governs everything: earn the send

The rate limit on outreach is not your typing speed. It is the number of people you can write a real reason for. A campaign is a list of reasons, one per human. When you cannot write the reason, cut the name.

That is not ethics as decoration. It is the arithmetic:

- Tight lists reply harder. Vendor data across the category puts small, precisely targeted campaigns multiples above the same copy blasted wide. Directional, not measured law, but every source agrees on the direction.
- A bad list bounces. Bounces and complaints are what providers actually score, and the reputation you burn takes months to rebuild on a domain you may still need.
- One reply from the right person outweighs four hundred non-replies from the wrong ones. Outreach is the cheapest place in the whole growth stack to play a power law, because a ticket costs a few minutes and the top prize is a trajectory change. See `turma:power-law`.

The test before any name goes on the list: **could this person tell, from the first line alone, that this email could not have been sent to anyone else?** If no, you are not ready to send to them.

## Layer 0: the machine (the gate before anything else)

Most outreach advice starts at the subject line. It should start here, because this layer decides whether the subject line is ever seen. Skip it and the best email you ever wrote lands in a spam folder, silently, and you conclude that cold email does not work.

### Never send cold from the primary domain

Buy a separate sending domain for outbound. If a cold domain gets blocklisted and it is the domain the product lives on, you have taken out the website, the support inbox, and every transactional email in one move. A lookalike domain (the `.co` of your `.com`, or `get[brand].com`) costs a few dollars a year and is the cheapest insurance in this whole document.

Buying a domain is Red. Ask first.

### Authenticate or get rejected

These come from the providers themselves, not from a vendor blog:

- **Google and Yahoo.** Any domain sending 5,000 or more messages a day to Gmail is classified a bulk sender, and that classification does not expire when volume drops. Bulk senders need SPF, DKIM and DMARC, one-click unsubscribe (RFC 8058), and a spam complaint rate under 0.30%. Google's own guidance is to stay under 0.10%; 0.30% is where enforcement starts, not where safety lives.
- **Microsoft.** Since 2025-05-05, domains sending 5,000 or more a day to Outlook consumer mailboxes must pass SPF, DKIM and DMARC or the message is rejected at SMTP with `550 5.7.15 Access denied`.
- **Below 5,000 a day**, which is where every campaign in this repo will sit, you are not formally a bulk sender. Authenticate anyway. SPF and DKIM are expected of all senders, and DMARC at `p=none` costs nothing but a DNS record.

Verify the records before the first send, not after the first silence. Google Postmaster Tools, MXToolbox and dmarcian all read them for free.

### Warm the inbox before you use it

Numbers here are vendor consensus, not measured law. Treat them as a starting ramp and watch your own bounce rate.

| Week | Per inbox per day | What it is |
| --- | --- | --- |
| 1 | ~5 | Automated warmup only |
| 2 | 5 to 10 | Warmup plus a few real sends |
| 3 | 10 to 20 | Real outreach begins |
| 4+ | 20 to 50 | Working ceiling, warmup mail included in the count |

Three to five inboxes per domain. Spread volume across two or three domains rather than pushing one hard. Keep 5 to 10 warmup messages a day running under the real traffic even once you are at cruise, because engagement signal is what the providers are scoring.

Three weeks of ramp before the first real send is the single most common step skipped, and skipping it is why "cold email does not work for us."

### Verify the list and watch the bounce

Run every list through validation before the campaign, and keep bounce under 2%. Above that, pull the domain out of rotation immediately and find out why. Bounce rate is the fastest signal that the list is garbage, and it is a signal the providers see before you do.

### Send plain

Plain text. One link at most, and prefer zero on the first touch. No HTML template, no images, no signature graphic, no open-tracking pixel.

Open tracking loads a pixel from a redirect domain that filters read as marketing, and the number it returns is junk anyway: Apple Mail Privacy Protection fires opens that never happened (see the open rate note in memory, and `turma:beehiiv-connector` for the same problem on the newsletter side). You are trading real deliverability for a fake metric.

Reply rate is the only number here that survives contact with 2026 email infrastructure. Judge on replies.

### The law, by where the recipient sits

Not legal advice. This is the map of where to be careful, and the compliance call is the owner's.

| Where | Basis | What it means in practice |
| --- | --- | --- |
| United States | CAN-SPAM. No prior consent needed for B2B | Honest subject and header, a real physical postal address, a working opt-out honored promptly. Civil penalty is set per email and adjusted for inflation, currently in the low fifty thousands of dollars per message. Per message, not per campaign |
| EU, opt-out states (France, Netherlands, Ireland, Sweden and others) | GDPR Art. 6(1)(f), legitimate interest | Business address, business-relevant message, clear sender identity, easy opt-out, and a written legitimate interest assessment on file |
| EU, opt-in states (Germany, Italy, Spain, Austria, Poland, Belgium) | Prior consent required, even B2B | Germany's UWG treats unconsented email advertising as harassment whether the recipient is a person or a company. Do not run a cold campaign into these markets without counsel |
| Canada | CASL. Express or implied consent required before sending | The strictest of the majors, with penalties into the millions. Assume you cannot cold email Canada without a consent basis |
| Brazil | LGPD, legitimate interest available (Art. 7, VI) | Structurally close to GDPR. Fines run to 2% of Brazilian revenue, capped at BRL 50 million per infraction |
| United Kingdom | PECR plus UK GDPR | Corporate subscribers can be emailed on a legitimate interest basis with identification and opt-out. Sole traders and partnerships are treated as individuals |

Two rules that hold everywhere and are cheap: **write to a business address about their business**, and **honor an opt-out the moment it arrives**, even when the law where they sit does not require you to offer one.

The EU split is the trap. Most cold email guides say "GDPR allows B2B outreach under legitimate interest" and stop there. GDPR is consistent across the union; the ePrivacy Directive is transposed country by country, and that is where Germany and Italy diverge from France and the Netherlands. Segment the list by country before the send, not after the complaint.

## Layer 1: the list

The list is the campaign. Copy is a multiplier on a list; a great email to the wrong hundred people converts at zero and teaches you nothing.

**Build it by reason, not by filter.** The wrong way is to set a filter (industry, headcount, title), export 2,000 rows, and start writing. The right way is to write the reason first: "companies that just posted a job for the role our product replaces," "creators whose last three videos were about the exact problem we solve," "stores that already stock the adjacent product." Then find the people who match the reason. A filter produces names. A reason produces a first line.

**Signals that carry a real first line** (with where they live):

| Signal | Where | Why it works |
| --- | --- | --- |
| A post, talk or video they made | X, LinkedIn, YouTube, podcasts | The only signal that proves you engaged with them and not their company row |
| Hiring for a specific role | Careers page, LinkedIn Jobs | Names the problem they have already decided to spend money on |
| Funding, launch, acquisition | Crunchbase, press, their own announcement | Timely, and a new budget usually follows |
| A visible gap in their own funnel | Their site, their store listing, their SERP | The strongest one for this crew, because the audit is the gift. See `turma:micromagnet-craft` |
| Tech or platform in use | BuiltWith, Wappalyzer, the page source | Only useful when the stack is the problem |

**How few.** One to two people per company, never ten. Emailing five people at the same company reads as a blast to all five and to their spam filter. Keep the campaign small enough that you could defend every name in it out loud.

**Where the list lives.** In `clients/<project>/` or the project's gitignored `growth/`. Never in a tracked file. It is other people's contact data and it falls squarely under the privacy boundary in `CLAUDE.md`.

**Tools.** For the first hundred sends you need none, and paid seats are Red. Manual research on a list of thirty beats an export of three thousand. When volume genuinely warrants it, see `turma/TOOLS.md` for what is registered and what its cost status is. Never quote a price from memory.

## Layer 2: the message

If the `cold-email` skill is installed, load it for the message layer. It owns B2B message craft in depth: subject line data, a four-level personalization system, framework catalog, and benchmarks. This skill does not repeat it. What follows is the shape that holds across every channel and every use, B2B or not.

### Five lines

The whole email:

1. **Proof you paid attention.** One sentence about them: their post, their product, their store, the thing they said. Specific enough that it could not be pasted to anyone else.
2. **Why you are writing, framed around them.** Not who you are. The problem the signal in line 1 implies.
3. **What you have, as an outcome.** One sentence. What it does for them, not what it is. "This might save your team five hours a week" beats a feature list every time.
4. **The ask, sized so a yes is cheaper than a no.** "Mind if I send a two minute demo?" or "Worth a look, or should I close this out?" Never "would love to connect," which is the email equivalent of "let's grab coffee sometime."
5. **Your first name.** Alone.

If you cannot say it in five lines, you do not understand your own offer well enough yet. That is a positioning problem wearing an email costume.

### The template

Fill the brackets. Do not add a sixth line.

```
Subject: [the specific thing they did, in 2 to 4 lowercase words]

Hey [first name],

[One sentence proving you paid attention. Their post, their talk, their
product, their words. Something only they did.]

[One sentence on why that made you write, framed around their problem.
Not who you are.]

[One sentence on what you have, as an outcome for them.]

[The ask, sized so yes costs one word.]

[Your first name]
```

Worked, so the shape is unmistakable. A fictional analytics tool writing the founder of a small paid newsletter:

```
Subject: your churn post

Hey [name],

Saw your post about losing a third of paid subs at the three month mark
and not knowing which ones were coming.

That's usually a signal problem rather than a content problem, and the
signals are already sitting in your open and click history.

We flag the accounts that go quiet about six weeks before they cancel,
so you get a window to do something about it.

Mind if I send a two minute teardown of your last cohort?

Chico
```

Count what that does. Line one is unrepeatable. Line two names a problem they already told the world they have. Line three is one outcome, no features. Line four asks for permission to give, not for thirty minutes to take. Nine of ten cold emails fail on line one alone.

**The channel variants.** Same five lines, less of them.

```
X DM (2 to 3 lines, lowercase, no signature):
saw your post on [thing]. [one sentence, the problem it implies]
built [outcome] for exactly that. want me to send it over?
```

```
LinkedIn connection note (300 characters is the whole email):
[first name], your [post/talk] on [thing] is why I'm connecting.
We [outcome] for [their kind of company]. Worth a look?
```

```
Instagram (reply to a story, do not open a cold thread):
[one specific reaction to what is actually in the story]
+ [one line that earns the next message]
```

### Personalization, and the thing that kills it

Personalization is not the first name. It is not the company name. Those are merge fields, and every recipient has been trained to see through them.

The ladder, weakest to strongest:

1. **Merge field.** Name, company, title. Table stakes and worth almost nothing.
2. **Segment.** A problem true of their industry or company stage. Scales well, converts modestly.
3. **Role.** A problem specific to their job and seniority. Better, still guessable.
4. **Individual and timely.** Something this person did recently, that you can point at. This is the only tier that earns a reply from a stranger.

**The rule that decides whether tier 4 works** (from the `cold-email` skill's references, credited there to Clay): if the personalization has nothing to do with the problem you solve, it is just an attention hack. Complimenting their podcast and then pitching invoicing software does not read as attention. It reads as a technique, and the reader has seen it.

Two tests, both cheap:

- **The deletion test.** Cut line one. Does the email still make sense? If yes, the personalization was decoration bolted onto a template. The observation has to be load bearing, meaning line two only exists because line one is true.
- **The paste test.** Would line one be true of ten other people on the list? Then it is a merge field with extra words. Rewrite it or cut the name.

Where the observations come from is Layer 1. The signal table there is the sourcing method; this is the bar it has to clear.

### The subject line

Specific enough that only one person could have received it. Short, lowercase, and boring in the way an internal email is boring. It has one job, which is getting opened, and selling in the subject line is what makes it look like what it is.

Dead on arrival: "Quick question," "Following up," "Partnership Opportunity," anything with your product name in it, anything with an emoji, and any fake `Re:` or `Fwd:`, which is a trust bomb with a delay fuse.

### Tone

Write like a smart friend, not an applicant. Contractions. Fragments. First name signature. The tone matters more than the credentials, because the credentials are not why they reply. They reply because it reads like a person wrote it to them at their desk.

Then run `turma:anti-ai-linguo` in Mode 4. The outreach tells are their own family and they are the fastest way to get deleted unread.

### The five-line email and the five-line story

`turma:story-craft` has a five-line framework too, and they are cousins, not the same thing. The story framework (mirror, friction, realization, shift, invitation) is for a reader who chose to be there. Cold outreach has no such reader, so it compresses: line 1 does the mirroring with a fact about them instead of a scene, and lines 2 and 3 carry friction and shift in a sentence each. When an outreach email is going to a warm-ish audience with attention to spare (an investor update, a long pitch to someone who already knows you), reach for `story-craft` instead.

## Layer 3: the sequence

Most replies do not come from the first email. No reply is not a no; it is a busy person.

| Touch | Day | Job |
| --- | --- | --- |
| 1 | 0 | The five lines. Maximum research investment goes here |
| 2 | 3 | New angle or a small piece of value, not a bump |
| 3 | 7 or 8 | Proof: a result, a similar case, a thing you built since |
| 4 | 14 | One useful thing with no ask attached |
| 5 | 21 to 28 | The close-out. Give them the easy exit |

Four to five touches total, widening the gap each time. Every message has to stand alone, because they probably never read the previous one.

### Run the sequence on updates, not on reminders

This is the mechanism that makes a sequence work instead of annoying someone into a block, and it is the part most campaigns skip because it is the only part that requires you to have been doing something.

A nudge says "I still want the thing I wanted last week." That is not new information, so it gives the reader no new reason to act, and it quietly signals that nothing has happened since. An update says "the situation changed." That is a reason to reply that did not exist before, and it puts the reader's non-answer in a different light without a word of pressure.

The canonical shape, a founder writing an investor who went quiet:

```
following up from last week. we just crossed 500 users and $10k MRR.
would love to revisit the conversation.
```

That is not a bump. That is traction. Traction is the best follow-up there is, and the same move works outside fundraising: a shipped feature, a customer result, a number that moved, a thing you built specifically because of the problem you named in the first email.

**The update inventory.** Before writing a sequence, list what you will plausibly be able to report over the next four weeks. These are the ones that carry:

| Update | Why it moves them |
| --- | --- |
| You shipped something | Proof the project is alive and moving |
| A number crossed a threshold | The cleanest possible signal, no interpretation needed |
| A customer got a result | Their outcome, demonstrated on someone like them |
| You published something relevant to them | Value with no ask attached |
| You built the thing for them | The audit, the teardown, the mockup. Strongest of all, and see `turma:micromagnet-craft` |
| Their world changed | They launched, hired, raised, or got hit by the exact problem. This resets the whole conversation |

**The cadence follows the updates, not the calendar.** The day table above is a default for when you have nothing better. If a real update lands on day 5, send it on day 5. If nothing has happened by day 14, do not send day 14's email; send something useful instead, or say nothing and wait for something to be true.

**This is why outreach and building are the same loop.** A project that ships every week has a follow-up engine that runs itself, because there is always something true to report. A project that ships nothing has only nudges, and nudges are what get you marked as spam. If a campaign's follow-ups feel like begging, the honest diagnosis is often not the copy. It is that nothing happened between touch one and touch four.

**When you genuinely have no update,** send something useful with no ask attached, or send the close-out. Those are the only two moves. Never send a reminder that you want something.

### The follow-up templates

```
Touch 2 (day 3, or the day a real update lands):
[the update, one line, specific and numeric where possible]
[one line connecting it to the thing you said in touch 1]
[the same ask, or a smaller one]
```

```
Touch 3 (day 7 or 8, proof):
[a result from someone like them, one line, with the number]
[one line on why it is relevant to their situation specifically]
[the ask]
```

```
Touch 4 (day 14, value with no ask):
[the useful thing itself, or a link to it]
no ask this time. thought it was relevant to [their specific problem].
```

```
Touch 5 (day 21 to 28, the close-out):
haven't heard back, so I'll assume the timing is wrong and stop here.
[one line of genuine value or insight, free, no strings]
if that changes, reply any time. good luck with [their actual goal].
```

**Give them the easy out.** "Worth a quick look, or should I close this out?" outperforms another polite nudge, because it costs the reader one word to end it and, oddly, that makes them more likely to engage. Use it once per sequence. Used repeatedly it becomes a tic, and a tic is a tell.

**Give them the easy out.** "Worth a quick look, or should I close this out?" outperforms another polite nudge, because it costs the reader one word to end it and, oddly, that makes them more likely to engage. Use it once per sequence. Used repeatedly it becomes a tic, and a tic is a tell.

**Banned in every follow-up:** "just checking in," "circling back," "touching base," "per my last email," "I never heard back." They carry no information and one of them is passive aggressive.

## Layer 4: the channel

Same rules, different energy. Read the room.

- **Email.** Structured but direct. Five lines. This is the default and the only channel with real infrastructure risk.
- **X DM.** Shorter than short. Two or three lines, lowercase, no signature. Engage with their posts before the DM, so the name is not cold when it lands.
- **LinkedIn.** The connection note is the message; treat 300 characters as the whole email. Do not pitch in the note and again in the first message.
- **Instagram DM.** Reply to a story rather than opening a thread. The reply lands in a different, softer place than a cold DM request.
- **Investors.** Lead with traction and the numbers. No fluff, no preamble, no deck attached to a first email.
- **Press and podcasts.** The pitch is the angle, not the product. Give them the story their audience wants, and make it obvious you have consumed their work.
- **Creators and partners.** Lead with what they get. Most creator pitches fail because they read like a request for free distribution.

## Layer 5: the loop

Volume plus iteration is the actual secret, and it is a power law. `turma:power-law` owns the doctrine. Here is how outreach sits inside the barbell.

**The cheap tickets:** batches of 20 to 50 qualified names, one variable changed per batch. Nothing here should take more than a few minutes per name.

**The concentrated bet:** the one hand-built email to the person who could change the trajectory. Hours of research, sent to one human. The Farza email in the source material is exactly this, and it is a different act from a campaign even though it uses the same five lines.

**What to track.** One row per batch, in the project's gitignored notes:

| Field | Why |
| --- | --- |
| Batch, list definition, date | So a winner can be reproduced |
| Sent | The denominator |
| Bounced | The list quality alarm. Over 2% and you stop |
| Replies | The real numerator |
| Positive replies | The only number that maps to the goal |
| Meetings or conversions | The scoreboard number from `brand.md` |
| The one variable changed | Otherwise you learn nothing |

Do not track opens. See Layer 0.

**Calibration.** Across published vendor benchmarks for 2025 and 2026, average campaign reply rates sit around 3 to 6%, the top quartile above 5.5%, and the top decile above 10%. Those are directional, self reported, and gathered by companies selling sending tools. Use them to know whether you are in the game, never to promise a number to an owner. A hand-built list of thirty behaves nothing like a benchmark of two million sends.

**The moves.** Kill anything below the batch median fast. When a batch outperforms, do not admire it: rerun the same list definition at wider scope within days, while the signal is fresh. Change one thing per batch or the result is noise.

**Expect the first fifty to be bad.** That is not failure, that is the price of the data. The people who win at cold outreach are not better writers. They are more willing to hit send, then honest about what came back.

## The door-knock (one shot, not a campaign)

Everything above is machinery for repeated sends. The other half of cold outreach has no machinery at all, and it is the half this crew exists for.

Most people see a closed door and stop. They assume there is a process, that someone has to introduce them, that people like them do not get to ask. So they never ask. The worst realistic outcome is being ignored, which is where you already were.

This is how an underdog project gets a distributor, a first press mention, a collab with someone ten times its size, a slot on a podcast, a mentor, a discount, a yes on something that was never advertised as available. It runs on the same five lines and none of Layer 0, because you are sending one message from your real inbox with your real name on it.

Rules for the one shot:

- Research until you can write a first line nobody else could write. Hours, not minutes.
- Ask for the specific thing. Not "any chance we could work together." The exact thing, so the answer can be one word.
- Send it from a real address, as yourself.
- Follow up more than feels comfortable, with a gap that grows and news when you have it. The source's own example ran fifteen follow-ups over four years and ended in a yes.
- Then let it go. A no or a silence costs nothing you had.

For a project, name the ten doors before writing anything. The ten people or companies whose yes would change the year. That list is worth more than the next two thousand prospects.

## The pre-send gate

Nothing goes out until every line passes. Outreach reaches real people under a project's name, which makes it **Yellow**: draft it fully, then get the owner's sign-off before it sends.

**The machine**
- [ ] Sending from a domain that is not the primary domain
- [ ] SPF, DKIM and DMARC verified on the sending domain today
- [ ] The inbox is past its warmup ramp
- [ ] List validated, expected bounce under 2%
- [ ] Plain text, no tracking pixel, at most one link
- [ ] The recipients' countries checked against the law table, opt-in states excluded or consented

**The list**
- [ ] Every name has a written reason
- [ ] One or two contacts per company, not more
- [ ] The list lives in a gitignored path
- [ ] Nobody on it has opted out before

**The message**
- [ ] Five lines or fewer
- [ ] Line 1 could not have been sent to anyone else (paste test)
- [ ] Line 1 is load bearing: delete it and the email stops making sense (deletion test)
- [ ] More "you" than "we"
- [ ] One ask, and a yes is cheaper than a no
- [ ] Subject line is specific and would not sell anything on its own
- [ ] A working opt-out where required, honored fast
- [ ] `turma:anti-ai-linguo` Mode 4 run, zero matches
- [ ] No dashes, no fabricated numbers, no claim without a source

**The loop**
- [ ] The tracking row exists before the send, not after
- [ ] One variable is being tested
- [ ] The follow-up sequence is written now, not improvised later
- [ ] The update inventory exists: what will plausibly be true to report in weeks one through four

**The mirror test**
- [ ] You would be fine receiving this, from a stranger, on a Tuesday morning
- [ ] The owner would be fine seeing it screenshotted publicly with their name on it

If the last two do not pass, nothing else matters. Fix the email, not the checkbox.

## Three modes

### Mode 1: CAMPAIGN
Build the whole thing. Read `brand.md`, define the reason and the list, run the Layer 0 gate, write the five lines plus the sequence, set up the tracking row, run the pre-send gate, hand the owner a package that is one approval away from sending.

Output: the list definition (not the list itself in any tracked file), the sending setup with what is still missing, the first-touch email and every follow-up written out, the update inventory the sequence runs on, the tracking table, and the gate with each box marked.

### Mode 2: DOOR-KNOCK
One target, one shot. Research until the first line is unrepeatable, write the five lines, name the exact ask, plan the follow-up horizon. No infrastructure, no campaign.

Output: the research that earned the first line, the email, the follow-up schedule, and the honest odds.

### Mode 3: REVIEW
A campaign that is not working. Diagnose in this order, because a lower layer being broken makes every layer above it unreadable: machine, then list, then message, then sequence. Most "our copy is not working" is a Layer 0 or Layer 1 problem, and rewriting the email would have changed nothing.

Output: which layer is broken, the evidence, the single change to make first.

## What we refused from the source

The source material is a good copy lesson and it is not a campaign system. Kept honest, here is what did not make it in:

- **"40%+ reply rate."** Self reported, unverifiable, and an order of magnitude above every published benchmark. Plausible for a handful of hand built emails to perfectly chosen people, meaningless as a campaign number. Never quote it to an owner.
- **"Send 100 emails."** As written, from an unwarmed primary domain, this is the instruction that burns the project's domain. Volume is the tail of the barbell, and it comes after Layer 0 or not at all.
- **The chapter heading "The Thing No One Tells You."** Textbook pseudo-contrarian construction, banned by `turma:anti-ai-linguo`. The idea underneath it is good, so it is here under a name that does not fake authority.
- **The founder story numbers** ($20k scholarship, the flight three days later). The story is verifiable and worth telling as a story. The figures are one person's account and are not evidence of a technique's success rate.

What we took: the five-line email and its template, the ask sizing, the specificity bar on line one, the run-on-updates follow-up engine (the source's single best operational idea, and the one this skill extended into an update inventory and a cadence rule), the easy out, the channel calibration, and the door-knock thesis, which is the most valuable part of the piece and the part every SDR guide leaves out.

## How it composes

- `turma:positioning` runs first. Outreach cannot fix a vague offer.
- `turma:conversion-craft` runs before the campaign sends, on whatever the reply lands on.
- `turma:micromagnet-craft` supplies the ask. The strongest cold ask is a small free useful artifact, not a meeting request. "Mind if I send a two minute demo" is a micro-magnet wearing a question mark.
- `turma:story-craft` for anything longer than five lines, or any warm follow-up that needs a narrative.
- `turma:power-law` owns the barbell this loop sits inside.
- `turma:anti-ai-linguo` Mode 4 is the last pass, always.
- `cold-email` (not part of turma) carries the deep B2B message layer when installed: subject line data, four-level personalization, the framework catalog, the benchmark tables. Load it for message work and let this skill own the machine, the list, the loop and the door-knock.

## Hard rules

1. **Never send cold from the primary domain.** No exception worth the risk.
2. **Never send before the pre-send gate passes.** Outreach is Yellow, always. The owner signs off before it goes.
3. **Every name has a written reason, or the name is cut.**
4. **No prospect list in a tracked file, ever.** Other people's contact data lives in gitignored paths.
5. **Judge on replies.** Not opens. Open tracking off by default.
6. **Honor an opt-out immediately**, whether or not the law where they sit requires you to.
7. **No fake `Re:`, no fake urgency, no invented mutual connection, no fabricated compliment.** A trick that gets a reply costs the project the relationship it was trying to start.
8. **Do not quote a benchmark as a promise.** Vendor numbers are directional. Say so when you cite one.
9. **Paid tools and domains are Red.** Ask before spending anything.
10. **The mirror test is not optional.** If you would not want to receive it, it does not send.

## Sources

- "The Cold Outreach Bible," Adrianna Lakatos (Founders, Inc.), Apr 2026. The five lines, the ask sizing, the follow-up discipline, the door-knock thesis. Her cold email to Farza Majeed at buildspace, and the move to San Francisco that followed, is independently documented.
- Google and Yahoo bulk sender requirements (Feb 2024, in force through 2026): authentication, one-click unsubscribe, the 0.30% ceiling and the 0.10% target.
- Microsoft Outlook high volume sender requirements, effective 2025-05-05: SPF, DKIM and DMARC or `550 5.7.15`.
- FTC CAN-SPAM compliance guidance and its inflation adjusted civil penalty; GDPR Art. 6(1)(f) with the ePrivacy country split; CASL; LGPD Art. 7 VI and Art. 52.
- Deliverability and warmup ranges: consensus across sending-tool vendor documentation, 2026. Directional, and labeled as such wherever it appears above.
- `cold-email` skill v1.1.0 (installed separately) for the B2B message layer this skill deliberately does not duplicate.

## Related

- `turma:positioning`, `turma:conversion-craft` (upstream, both)
- `turma:micromagnet-craft` (the ask)
- `turma:story-craft` (anything longer than five lines)
- `turma:power-law` (the loop this sits inside)
- `turma:anti-ai-linguo` (Mode 4, last pass)
- `turma/TOOLS.md` (cost and status of anything named here)
