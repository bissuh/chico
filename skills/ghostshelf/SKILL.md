---
name: ghostshelf
description: Build and run a faceless (no-face) content page that sells a small digital product, end to end. Invoke when someone wants to start a faceless Instagram or TikTok gallery account, create and sell a digital template/guide/spreadsheet on Gumroad, choose a profitable no-face niche, batch carousel/slideshow content, or wire a link-in-bio funnel to a newsletter and product. Walks the user through niche choice, product creation, content batching, distribution, and the weekly operating loop, with honest odds baked in.
---

# Ghostshelf

Build a shelf, not a stage. This skill helps a person with knowledge but no audience and no desire to be on camera build a faceless content page that sells one small, useful digital product, and then runs the weekly loop that grows it.

It is the honest version. It tells the user the real odds before they spend a weekend, and it optimizes for the one lever that actually decides the outcome: distribution of a specific fix to the people who already pay for it.

Built by The Billion Person. Research and sources behind every number: `knowledge-base/faceless-gallery-model/research-dossier.md`.

## Read this first: the honest odds

Say this to the user before anything else. Do not skip it.

- The model is real. People have built six and seven figure businesses selling templates with no face attached (Thomas Frank ~$2.1M, Easlo ~$500k). Margins are ~95%; you keep ~$17-18 of every $20 on most platforms.
- The default outcome is close to zero. The median Gumroad product earns ~$364 over its whole life. The top 1% of products take 77% of all revenue. ~42% of faceless creators make under $500/month.
- The people loudest about this online are usually selling the course or the service, not living off the pages. Treat screenshots as advertising.
- The one real lever is distribution + a painfully specific problem + volume of products over time. This skill points all effort there.

If the user still wants in after hearing that, proceed. Honest expectation setting is the first deliverable.

## The operation, in seven steps

Work the user through these in order. Do one step per working session if needed. Never let them skip Step 1.

### Step 1. Pick the problem (the decision that decides everything)

Interview the user. Pull out 3-5 things they know how to do that other people pay to have done. For each candidate, score it against four filters. All four must be a clear yes:

1. **One breath.** Can they say the problem in one sentence? "Freelancers don't know what to charge." "New managers have no 1:1 structure." If it takes a paragraph, it is too vague to sell. Sharpen or drop it.
2. **Already paid for.** Do people pay to fix this right now, somewhere? Search Gumroad, Etsy, and Google for existing paid solutions. An ugly $30 version already selling is a green light, not a reason to quit.
3. **Weekend-sized fix.** Can the first product be built in a weekend? First products are one template, one checklist, one spreadsheet. Not a course.
4. **Feed-able.** Could they make 30 useful slides about this problem without running dry? If yes, there is a content engine. If no, pick again.

Output: one chosen problem, written as a single sentence, plus the evidence that people already pay for the fix. Do not move on until this exists.

### Step 2. Build the product with Claude

Build the smallest version that fully solves the one problem. Match the format to the problem: Notion template, Google Sheet, fillable PDF, swipe file, prompt pack, checklist.

- Draft the full content with the user, in their real expertise. Do not invent facts; ask the user for the specifics only they know.
- Make it genuinely good. The whole bet is that the work is the thing people meet first.
- Write the product title and the Gumroad description: lead with the outcome, name the buyer, list what is inside, set the price.
- Starting price: $19-$49. Raise after the first 3 happy buyers leave proof.

### Step 3. Set up the storefront

- Gumroad is the simplest start (handles global tax; ~10% + $0.50 per sale). Lemon Squeezy or Payhip cost less at volume; note this but do not block on it.
- One product page. Clean cover image in the brand style (Step 4). Clear outcome headline. Three to five bullets. One price. One buy button.
- Set up the file delivery and a one-line thank-you that asks the buyer to reply with how it goes (early testimonials).

### Step 4. Build the no-face page (the brand is the look, not a person)

Open one Instagram and one TikTok account for the page. With no face, visual consistency IS the brand. Lock a small system the user cannot break later:

- 2 fonts max (one display, one body), 3-5 colors max.
- A signature visual wrapper. (The Billion Person uses a Gustave Dore 19th-century engraving look, monochrome with teal #2A7A6D and crosshatching. The user should pick their own one recognizable wrapper.)
- Fixed logo/handle lockup position on every slide.
- A clean bio: who it helps, what they get, one direct link (no shorteners, they can trigger shadowbans).

### Step 5. Make the content (pick a format, then fill the skeleton)

**First, pick a format. This is a creative decision, not a default.** Do not pour every idea into the same generic template. The fastest way to look like dead faceless spam is template sameness: same layout, swapped words. Pick a deliberate format, chosen by the signal you need this week:

- **Need conversion (saves + opt-ins):** Swipe File ("steal these prompts/templates"), Checklist / Audit, Step-by-Step, Framework, Q&A. The Swipe File is the strongest bridge to an opt-in: preview the assets, trade the full version for a subscribe.
- **Need reach (sends/shares beyond your followers):** Myth-Bust, Contrarian, Comparison ("X vs Y"), Tier List, Identity ("which one are you"). These get forwarded and tagged.
- **Need proof / authority:** Case Study, Before/After, By-the-Numbers, Report / Findings.

Vary the format week to week. Keep the look identical (that is the brand), change the structure (that is the format). Full menu + per-format slide structures live in `knowledge-base/faceless-gallery-model/format-library.md`.

**Discovery note:** carousels win saves but mostly reach people who already follow you. Short video (Reels, TikTok video) is the cold-discovery engine. To grow from zero, run video alongside the carousels; do not rely on carousels alone.

Then fill this skeleton (works inside any format):

```
S1  HOOK     stops the scroll, readable in under 2 seconds. [audience] + [tension] + [payoff promise]
S2  PROMISE  who it is for + what they will get
S3  CONTEXT  the problem / why the usual way fails (open loop)
S4-7 STEPS   ONE idea per slide, lots of whitespace
S8  PROOF    a number, a before/after, a mini result
S9  RECAP    the one thing to remember
S10 CTA      ask for the save + the send + the bio click
```

Hook types that work: Mistake, Contrarian, Numbers, Story (start mid-scene), How-To (outcome + timeframe). The number one failure is an informational headline with no tension.

Batching workflow (a month in one afternoon):
1. Take one long piece (a newsletter issue, a guide, the product itself). Atomize: one idea -> one carousel. Aim for 3-5 carousels per source.
2. Draft all the copy as a spreadsheet: one row = one carousel, one column = one slide field (`S1_title`, `S1_body`, `S2_title`...).
3. In Canva: design ONE on-brand template per slide type, then use Bulk Create / Connect Data to map the spreadsheet columns and generate every carousel at once.
4. Generate the art wrapper (backgrounds only) in your image tool. Do not bake text into AI images; AI cannot reliably render legible type or an exact hex. Set the type and the exact brand color in Canva.
5. Resize to 1080x1920 for TikTok, trim text further, add a strong cover frame and mood audio.

Posting mix for a new account: lean on Reels / Carousel-Reels for discovery (small accounts get more reach there), use static carousels for saves and depth. 3-5 posts a week, consistency over volume.

### Step 6. Wire the funnel (own the audience)

- Link in bio goes to the email opt-in first, the product second. The email list is the only asset the platform cannot take away.
- Front-load the keyword in the first sentence of every caption (both platforms are search engines now). 3-5 relevant hashtags, not 30. Add alt text on Instagram.
- Last slide asks for the save and the send ("send this to the friend who keeps saying they can't..."). Sends and saves drive reach more than likes in 2026.

### Step 7. The weekly loop and reading the numbers

Each week: post the batch, reply to every comment and DM, and read three numbers only:
- **Saves + sends per post** (is the content worth keeping/sharing).
- **Profile visits -> bio clicks** (is the hook earning curiosity).
- **Email opt-ins + sales** (is it converting).

Then act: keep the post styles that earn saves/sends, cut the ones that do not, and every few weeks ship another small product (multi-product sellers earn far more than single-product ones).

## Honest expectations and when to pivot

- Expect a 2-4 month slow ramp before anything accelerates. Judge progress on saves/sends and email opt-ins, not follower count. A 500-follower page with high saves beats a 10k page with none.
- If after ~8 weeks of consistent, genuinely useful posting there are no saves and no opt-ins, the problem is usually the niche (Step 1) or the hook (Step 5), not the algorithm. Re-run Step 1.
- If it works, do not scale the posting. Scale the shelf: ship product number two for the same audience.

## Guardrails (so the page does not get throttled)

- Original content only. In 2026 Instagram penalizes recycled/aggregated posts (cuts you from non-follower reach) and TikTok bans copy-paste faceless accounts. Make your own slides. Never screen-record someone else's post.
- No face required, but the work must be real. The honest version is the only one with a future.
- If this skill produces public copy for The Billion Person, it must pass the house rules: no em or en dashes, no "nobody [verb]" pseudo-contrarian phrases, no AI tells. Grep before shipping.

## Resources

- Research + sources: `knowledge-base/faceless-gallery-model/research-dossier.md`
- Scheduling that supports TikTok photo carousels + IG carousels via API (verified): Metricool, Later. (Verify live pricing before paying.)
- Storefronts: Gumroad (simplest), Lemon Squeezy / Payhip (cheaper at volume).
- Design + batching: Canva Pro (Brand Kit + Bulk Create).
