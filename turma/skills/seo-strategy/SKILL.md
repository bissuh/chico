---
name: seo-strategy
description: Strategize and execute SEO for a project, local (Google Business Profile + map pack) or national/content, and win the 2026 AI-answer layer too. Invoke when someone asks to "improve SEO," "why aren't we ranking," "SEO strategy," "local SEO," "rank in the map pack," "Google Business Profile," "keyword strategy," "get found on Google," or "get cited by AI." Organizes the work under Google's Relevance/Distance/Prominence framework, runs competitor-gap audits, and composes the connectors and the installed SEO skills. Reads brand.md.
---

# seo-strategy

SEO's only job is to get a project found by the people ready to act, and the only scoreboard that counts is calls, signups, bookings, and revenue from organic, not total traffic or domain rating. This skill is the brain that decides what to fix and in what order. The tactical execution runs through the connectors and the installed SEO skills; this skill supplies the strategy.

**Before you start:** read `brand.md`, especially the optional SEO context block (site, GBP, service areas, target keywords, competitors). The first question it answers: is this a **local** business (a physical location or a service area, so GBP and the map pack dominate) or **national / online / SaaS** (so content and authority dominate)? That split decides which levers matter. If the SEO context is missing, help the owner fill it first. It is the same "load your business context once" move that makes every downstream prompt sharper.

## The framework (everything ladders up to three pillars)

Google ranks local results on **Relevance, Distance, and Prominence**, weighed together (Google's own framework; the [Whitespark 2026 Local Search Ranking Factors](https://whitespark.ca/local-search-ranking-factors/) survey of 47 experts puts the rough weights at proximity ~55%, GBP signals ~32%, reviews 16-20% and rising, on-page ~19%). These weights are survey-directional, not law, but the priority order is solid. Every tactic below is tagged to the pillar it moves.

- **Relevance:** how well the business matches the search. You control this: primary category, services, description, review keywords, on-page content.
- **Distance (proximity):** how close the searcher is. The single biggest factor, and mostly outside your control. You cannot move the business, so you win distance indirectly: service-area pages, neighborhood mentions, and geo-signals expand your footprint, and strong relevance or prominence can override a small distance gap.
- **Prominence:** how known and trusted the business is. Reviews, citations, backlinks, brand mentions, and entity recognition in Google's Knowledge Graph.

For national / content SEO, the same logic drops distance and leans on relevance (content that matches intent) and prominence (authority and links).

## The core method: competitor-gap auditing

This is the engine. For any asset, audit what the top 3 competitors have that the project does not, then sort:
- **Table stakes:** all 3 competitors have it. Do it immediately, it is why they outrank you.
- **Strong:** 2 of 3 have it. Do it next.
- **Differentiation:** only 1 has it. An opportunity to get ahead.

Run this on every lever below. The competitor set comes from `brand.md`. Use `turma:viral-teardown` when you need to understand *why* a competitor's asset works, not just that it exists.

## Local levers (GBP, the map pack), by pillar

- **Primary category (Relevance, highest-ROI fix).** The wrong primary category is one of the most common reasons a business ranks poorly. Pick the most specific match, then add every secondary category the competitor-gap audit surfaces.
- **Attributes, services + descriptions, GBP description (Relevance).** Fill every field, keyword-aware but human. The services section and the 750-character description are copy you fully control; write and A/B test them (`turma:optimize-post` for the copy).
- **Reviews (Prominence).** Velocity beats total count: consistent new reviews signal an active business. Respond to reviews (a high response rate, roughly 80%+, correlates with a ranking lift), and let responses carry service and city keywords. Never fabricate, gate, or incentivize reviews; that violates Google policy and the trust it buys. Mine competitor reviews for the exact language customers use, then feed it to copy via `turma:emotion-craft`.
- **GBP posts + photos (Prominence, activity signal).** Consistent posting and steady photo uploads (with geo-relevant naming) tell Google the business is alive. Build a calendar; beat the competitor's velocity.
- **NAP citations (Prominence).** Name, address, phone must be identical across Google, Bing, Apple, Yelp, and industry directories. Inconsistency suppresses rankings and is one of the fastest fixes to show results.
- **Service-area + city pages (Distance).** Google ranks pages, not sites. A dedicated [service] in [city] page is how you rank in cities you do not sit in. Build the stack, one page per service per city, with `turma:optimize-post`.

## Website levers (national and local)

- **The page-2 goldmine (the highest-ROI move in all of SEO).** Pull Search Console via `turma:search-console-connector` and find every keyword ranking in positions 11-20 with real impressions. A jump from 15 to 5 is worth more than ten new pages. For each, check whether the keyword is in the title, H1, and first 100 words, then fix exactly that. This is the first thing to run on any site with history.
- **Keyword-gap and content-gap.** Find the keywords and content competitors rank for that the project lacks (paid tools like SEMrush/Ahrefs make this fast, but the free stack plus the installed `seo-audit` gets far). Filter to the local-intent sweet spot (roughly 100-2,000 volume, low difficulty, buyer-intent words).
- **On-page + schema.** Title, H1, first-100-words, meta, internal links, and structured data. Hand the deep schema work to the installed `schema-markup` skill.
- **Free-tool ranking pages (the FounderPal play).** One of the strongest national/SaaS levers there is: build a small, genuinely useful, ungated web tool (a generator, calculator, analyzer/checker, or template) and give it its own page targeting one long-tail keyword the buyer already types (`[job] generator`, `[thing] calculator`, `[input] checker`). Dan Kulkov ran FounderPal past $200k almost entirely on this. Why it wins: the page ranks itself and compounds forever, it earns organic shoutouts and AI-answer citations because it does real work, and the paid product upsells organically inside the tool's result. Source the keyword the same way you source any content-gap (buyer-intent, low-difficulty long-tail; the tool niches sit in the 100-2,000 volume sweet spot and there are databases of them). Do not gate the tool behind an email; the ranking traffic and word-of-mouth are worth more than the captured addresses (email is a secondary layer, not the toll gate). Shape the tool and the organic upsell with `turma:micromagnet-craft` (the pull motion); rank the page here; build many such pages at scale with the installed `programmatic-seo` skill.

## Search intent, mapped to the buyer journey

Most projects waste SEO on high-volume awareness terms that bring traffic and no calls. Map every keyword to a stage and prioritize the bottom of the funnel:
- **Stage 1, problem-unaware** ("water coming through ceiling"): problem-ID content, builds early trust.
- **Stage 2, problem-aware** ("how to fix a leaking roof"): educational blog content.
- **Stage 3, solution-aware** ("plumber vs DIY"): comparison and FAQ pages.
- **Stage 4, ready-to-hire** ("emergency plumber [city]"): service pages and GBP. Lower volume, converts 5-10x. Chase these first.

## The 2026 AI-answer layer (do not skip this)

Search is shifting from ranked links to AI Overviews and generative answers, and a project's GBP is often the primary source AI pulls for local answers. So the game is also **AEO/GEO**: making the business easy for AI to extract, verify, and cite.
- Strengthen the **entity**: schema (LocalBusiness JSON-LD), consistent NAP everywhere, presence on authoritative sites, brand mentions. A recognized entity in the Knowledge Graph earns prominence and gets cited.
- Make content **citation-ready**: clear, structured, answer-first.
- Hand the deep AEO work to the installed `turma:ai-seo` skill. Track AI citations (tools like Otterly.ai, Promptmonitor, Peec) alongside `search-console-connector`.

## The scoreboard (money, not vanity)

Report only what connects to revenue. From Search Console: clicks, impressions, average position, the page-2 movers. From GBP: profile views, calls, direction requests, website clicks. Ignore total traffic and DR as goals. The monthly report is one page: 3 wins, 3 problems, the single most important next action, and whether calls went up or down.

## Modes

State the mode at the top.

- **AUDIT.** Run the competitor-gap audit across the relevant levers (local or national, per brand.md). Output: a prioritized gap list (table stakes, strong, differentiation), tagged by pillar and by impact/effort, with the page-2 goldmine list on top.
- **STRATEGY.** Turn the audit into a sequenced 90-day plan: quick wins first (categories, attributes, page-2 fixes), then full GBP, then site and city pages, then authority and citations, then content and entity, then measure. Quick wins before long plays unless the owner says otherwise.
- **EXECUTE.** Produce the actual assets: optimized GBP and service descriptions, city pages, review-response templates, the posting calendar, the schema. Compose `turma:optimize-post` and `turma:emotion-craft` for copy, `schema-markup` for structured data.

## Source

The tactics are distilled from Sarvesh Shrivastava's "Top 20 Claude Prompts for SEO" (9.2M views), a strong local-SEO prompt system, and a sales piece for his agency. His revenue claims are his marketing, not cited. The strategic framework (Relevance / Distance / Prominence), the factor weights ([Whitespark 2026](https://whitespark.ca/local-search-ranking-factors/)), and the 2026 AI-answer layer the article omitted were added from research. The free-tool ranking-page lever comes from Dan Kulkov's field-tested FounderPal / MakerBox engine; his revenue figures are his marketing, directional and not citable. Blog and survey stats are directional, not law.

## Hard rules

- Reads `brand.md` first, including the SEO context block. Local vs national decides the levers.
- Money metrics, never vanity. Calls and revenue from organic, not total traffic or DR.
- Never fabricate, gate, or incentivize reviews. Real reviews only; response strategy is fine.
- Cite only verified factors. The Whitespark weights are survey-directional; the article's revenue numbers are not citable.
- Composes, does not re-derive: `search-console-connector` for data, `ai-seo` / `seo-audit` / `schema-markup` / `programmatic-seo` (installed) for execution, `optimize-post` and `emotion-craft` for copy.
- No dashes, no AI tells on any copy produced. Run `turma:anti-ai-linguo`.

## Related

- The project's `brand.md`: the SEO context block (site, GBP, service areas, keywords, competitors).
- `turma:search-console-connector`: the live GSC data this strategy runs on.
- `turma:ai-seo`, `seo-audit`, `schema-markup`, `programmatic-seo` (installed marketing skills): the tactical execution.
- `turma:optimize-post`: on-page copy and title/meta/H1 fixes.
- `turma:emotion-craft`: turn mined review language into website and GBP copy.
- `turma:viral-teardown` and `turma:power-law`: competitor teardown and quick-win prioritization.
- `turma:micromagnet-craft`: shapes the ungated ranking tool and its organic upsell (the pull motion) that the free-tool ranking-page lever ranks.
