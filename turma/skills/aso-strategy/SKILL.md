---
name: aso-strategy
description: Strategize and execute App Store Optimization for a mobile app on the Apple App Store and Google Play. Invoke when someone asks "how do I get downloads," "nobody finds my app," "ASO," "app store keywords," "what should I name my app in the store," "why did my ranking drop," "how do I get more ratings," or is about to submit a first build. Runs three layers: the index (do you appear), the impression (do they install), and the post-install signals (do you keep the rank). Covers the 2026 store changes: AI tags, custom product page keyword binding, and the rebalance toward retention as a ranking input. Reads brand.md.
---

# aso-strategy

For most mobile apps the store is not one channel among many. It is the channel. And the listing is the entire funnel compressed into one screen: the index decides whether you appear at all, the first screenshot decides whether they tap, and what happens after the install decides whether you keep the rank you just earned.

That is the shape of this skill. Three layers, in that order, because they gate each other. Perfect screenshots on an unindexed app get no impressions to convert. A perfect keyword on a page that does not convert burns the impressions and the algorithm demotes you for it.

**Before you start:** read the project's `brand.md`, especially the ASO context block (platforms, store URLs, category, primary keyword, competitors, current rank). If that block is missing, help the owner fill it first; it is the same "load the business context once" move `turma:seo-strategy` opens with. You also need three facts the store pages will not tell you: how old the listing is, what the current install-to-page-view conversion rate is (App Store Connect and Play Console both report it), and whether the app has a runway measured in months or years. The last one changes the keyword strategy more than anything else on this page.

## When to invoke

- Before the first submission. The app name is the single heaviest ranking field, and renaming later throws away whatever equity the old name built.
- When downloads are flat and the owner is about to spend on ads. Same rule as the web: fix the free channel before buying a paid one.
- When impressions are healthy and installs are not. That is a conversion problem on the product page, not a keyword problem.
- When a ranking drops without a metadata change. Usually a post-install signal moved, not the index.
- When ratings are thin, or the average is dragging the listing down.
- On any localization or new-market decision.

## When NOT to invoke

- For a web product. That is `turma:seo-strategy`. The two share the intent-matching logic and share almost nothing else: different index, different fields, different ranking inputs, different tooling.
- For the offer and the price. `turma:conversion-craft` owns whether the thing is worth buying. This skill assumes it is and works on whether people find it and tap install.
- For whether users stay. `turma:retention-craft`. Which matters here more than it used to: see Layer 3.
- For the four minutes after the install. `turma:first-session` owns the onboarding flow, the demo, the permission priming and the in-app paywall. Layer 3's post-install signals are manufactured there, not here.
- For the brand name itself. `turma:name-craft` picks the name. This skill picks the **store title**, which is a different field with a different job.
- For paid user acquisition. Apple Ads and Play campaigns are a spend decision (Red), and they are for accelerating a listing that already converts, never for finding out whether it does.

## The rule that governs everything: the store title is not the brand name

The brand name and the store title are two different fields doing two different jobs, and treating them as one is the most common and most expensive ASO mistake an indie makes.

The brand name is the thing people say. `turma:name-craft` picks it, and it should be original, fluent, and unexpected. The store title is a 30-character search index entry. It should lead with the term a stranger types when they do not know you exist.

So the pattern for an unknown app is `[primary keyword]` then `[brand]`. HabitKit, a habit tracker built by a solo developer, is listed with "habit tracker" ahead of the brand for exactly this reason. Duolingo can put the brand first because "duolingo" is itself a high-volume search term. An app with no brand search volume that leads with its brand is spending its heaviest ranking field on a keyword nobody types.

Flip the order the day the brand outsearches the category term, and not before.

## Layer 1: the index (do you appear)

### What each store actually reads

The two stores are not variations on a theme. They index different fields, and a listing written for one is wrong on the other.

| Field | Apple App Store | Google Play |
| --- | --- | --- |
| App name / title (30 chars both) | Indexed, heaviest weight | Indexed, heaviest weight |
| Subtitle (30 chars) | Indexed | Does not exist |
| Short description (80 chars) | Does not exist | Indexed |
| Keyword field (100 bytes, hidden from users) | Indexed | Does not exist |
| Long description (4,000 chars both) | **Not indexed for search** | Fully indexed |
| User reviews | Not a text index | Contributes to relevance |

The asymmetry has one practical consequence worth stating plainly: on Apple, stuffing keywords into the description does nothing at all except make the page worse to read. On Google Play, the long description is a real ranking surface and is written like a web page.

### Apple's keyword field, rule by rule

Verified against Apple's documented behavior and current ASO practice. Every one of these costs you bytes if you get it wrong.

- **It is 100 bytes, not 100 characters.** ASCII letters cost one byte each. Accented and non-Latin characters cost more, so a German or Portuguese locale fits fewer terms than an English one.
- **Comma-separated, no space after the comma.** A space is a wasted byte.
- **Never repeat a word already in the name or subtitle.** Apple reads name, subtitle, and keyword field as one pool and builds phrase combinations across them. A repeat buys nothing and costs the bytes.
- **Singular only.** Apple stems, so "workout" already covers "workouts". Including both is a pure waste.
- **No competitor names, no trademarks you do not own.** This is not a gray area. It violates the guidelines and gets apps rejected or pulled. Generic words that happen to appear in a rival's name are fine; the rival's name is not.
- **Terms under three characters are generally not indexed.** Skip them.
- **Fill all 100 bytes.** Unused space is unclaimed ranking.

### Keyword research, and the one bet that decides the strategy

Use an LLM to map the landscape: what would someone type who has this problem and does not know this app exists. That is brainstorming, not data. Nothing an LLM invents ships until a tool confirms people search it.

Apple's own **Search Popularity** score is the only first-party volume signal, exposed through the Apple Ads API and surfaced by every serious ASO tool. Two things about it that most guides get wrong:

- It runs 5 to 100, and a term with effectively no traffic returns nothing at all. That absence is itself the answer.
- **The scale is exponential, not linear.** The distance from 50 to 60 is much larger than the distance from 20 to 30. Never average these numbers or treat a 10-point gap as a fixed quantity.

Then the actual decision, which is a bet on runway, not a scoring exercise. The prevailing indie advice is to fight for one hard, high-value primary keyword rather than dominate an easy dead one, and it is right when the timeline is years. HabitKit's own arc is the honest version of that promise: launched November 2022 and invisible, top 10 in smaller non-US markets at roughly six months, occasional US top 10 at about a year, consistent US top five at nearly three years.

That is the price of the hard keyword. So run the standard's own winnability test on it (`standards/social-app-design-principles.md`, Section 7, "Engineer the Size of the Competition"): a competition the player cannot plausibly win is demotivating whether the player is a user or a founder. If the runway is three months, or the project needs revenue to justify continuing, take the winnable term and the smaller storefront. A number two ranking in a market that exists beats a number forty in the market you wanted.

### Localization is the cheapest lever most listings skip

Apple and Google index per storefront. A listing translated properly into five more locales is five more indexes, and the competition in most of them is far weaker than in the US. This is where the winnability principle pays first, and it is why so many indie apps rank abroad long before they rank at home.

Translate the keyword research too. A literal translation of an English keyword set is not what people in that market type.

## Layer 2: the impression (do they install)

The product page is a landing page, so everything in `turma:conversion-craft` Layer 2 applies. Two things are specific to a store.

**Most visitors never swipe.** SplitMetrics (formerly StoreMaven) measured roughly 60% of visitors deciding inside the first impression frame, before scrolling past the first screenshots. The figure is dated and directional, but the direction has never been in dispute. Treat the first frame as the entire page.

So the first screenshot carries the single most visually distinct thing the product does, and it shows **real interface**. Not a welcome screen, not a login screen, not an abstract lifestyle photo that could belong to any app in the category. A visitor is deciding what they get, and a stock image tells them nothing.

**Then test it, because you cannot call this one.** Apple's Product Page Optimization, documented:

- Up to three treatments per test, varying app icon, screenshots, and app preview videos.
- Runs 90 days or until you stop it.
- You set the traffic proportion, split evenly across treatments. Allocate 40% across two treatments and each gets 20%, with 60% staying on the original.
- Apple recommends waiting for at least 90% confidence before applying or stopping.
- Alternate icons must already ship inside the published binary. A screenshots-only test can be submitted without a new app version.

Google Play's equivalent is store listing experiments: up to three variants against the current listing, with one default graphics experiment or up to five localized experiments running at once.

The lesson that makes this layer worth its own section: Sebastian Röhl had a designer build polished replacements for his self-made screenshots, was confident they would win, tested them, and **the original less-polished set converted better**. That is one result from one app and it is not a law that amateur beats professional. The law is that your confidence about a product page is worthless and the test costs nothing.

One honest limit: PPO needs traffic. A new app with a few dozen daily impressions will never reach 90% confidence inside 90 days. For a low-volume listing, decide with judgment, ship, and revisit when there is enough traffic to learn something. Running an underpowered test and acting on it is worse than not testing.

## Layer 3: the post-install signals (do you keep the rank)

Between roughly 2024 and 2026 both stores rebalanced away from pre-install signals (keyword match, raw download counts) and toward post-install ones: product page conversion rate, retention, engagement depth, and review velocity and recency. Apple publishes no algorithm, so this is industry consensus from ASO vendors, directional rather than law. But the direction is consistent across every credible source and it changes how the work is sequenced.

**The structural consequence: retention is now an acquisition lever.** A leaky product ranks worse, which sends fewer installs, which makes the leak more expensive. An app cannot outrun churn with metadata. When the diagnosis is a retention problem, this skill hands to `turma:retention-craft` and waits, because ASO work on a leaking product buys a temporary rank you then lose.

The leak usually starts earlier than anyone measures. Most of the signal in this layer is set in the first few minutes after the install, which is `turma:first-session`. A flow that converts hard and then refunds is charged twice here, once in the refund and once in the rank, so read install-to-paid and first-month cancel together before crediting any listing change.

### Ratings and reviews

Volume and recency both count, and they count separately. A 4.6 average from twelve thousand ratings carries more algorithmic weight than a 4.8 from two hundred, because volume is evidence of sustained quality rather than a snapshot. Google has said outright that newer ratings weigh more than older ones. So a large historical count with nothing recent is a decaying asset, and steady velocity beats a one-time push. Same principle `turma:seo-strategy` applies to Google Business Profile reviews.

**The prompt is scarce inventory.** Apple's `SKStoreReviewController` shows at most three prompts per user per 365 days, and even then it is a request the system can decline. You get three shots a year per user. Spend them at the moment the product delivered what it promised: the first habit completed, the first export finished, the first invoice paid. Never during onboarding, never after an error, never on launch.

If someone dismisses it, back off for a good while. An annoying prompt does not just fail, it costs you a bit of goodwill you needed for the next ask.

**Respond to every review.** Thank the good ones, actually fix the bad ones and say so. One-star reviews get revised upward more often than developers expect, and the response is public: the next reader sees a developer who shows up. Take the support-email version too, a genuine, low-friction request appended after you have just helped someone. It works because the help came first.

**Never gate, never buy, never incentivize.** Showing the prompt only to users you predict will rate five stars is review gating, it violates both stores' rules, and it is the same line `turma:seo-strategy` draws on Google reviews. There is no version of this that is worth the risk.

**Reviews are a free product backlog.** Twenty people asking for the same feature is a stronger signal than any survey you could run. And competitor reviews are public: mine them the same way, for the complaints that tell you what the incumbent will not fix.

## The 2026 layer (the part most ASO advice predates)

Three real changes landed after the playbooks were written, plus one claim to refuse.

- **AI-generated tags (iOS 26).** Apple's models generate descriptive tags from app metadata, human-reviewed before going live, displayed as tappable links that browse other apps carrying the same tag. Developers cannot pick tags from a list; the only input is metadata quality. Apple has not fully specified which fields feed generation. Practical effect: metadata hygiene now feeds a discovery surface you do not control, which raises the cost of a lazy description even on Apple, where the description does not rank.
- **Custom product page keyword binding (Apple, since July 2025).** You can assign keywords from the keyword field to a specific custom product page, so that page rather than the default appears in organic search results for those queries. Apple allows up to 70 custom product pages, and **each keyword combination must be unique to one page**, so map the whole keyword field across pages before assigning anything or one page silently takes the query and the other takes nothing. This is the app-store equivalent of matching a landing page to a search term, it is the highest-leverage feature most indie listings ignore, and it makes intent-matched screenshots possible for the first time.
- **The AI-assistant layer.** People ask an assistant for "the best habit tracker" and install what it names. A store listing is not a crawlable web page, so an app that exists only inside the store has no surface feeding that answer. The fix is the punch list `turma:seo-strategy` already carries: a real web page for the app, review directories, "best [category] app" listicles, and honest presence in the communities where the category gets discussed. Ranking number one in the store and being absent from that layer are entirely compatible states.
- **Screenshot text as a ranking input: unverified, do not build on it.** Vendors speculate Apple extracts text from screenshots for search. Apple has documented nothing. Write clear, readable screenshot copy because humans read it and because it plausibly feeds tag generation. If a ranking effect exists, take it as a bonus, and never present it to an owner as a mechanism.

## Modes

State the mode at the top of your output.

### Mode 1: AUDIT

Given the store listing (and any App Store Connect or Play Console data), score all three layers and find the binding constraint. Output: the title and subtitle scored against the primary keyword, the keyword field audited byte by byte for repeats, plurals, trademarks, and unused space, the first impression frame judged on differentiation and real interface, the conversion rate against the category, the ratings picture (volume, average, recency, velocity), and whether post-install signals are the actual problem. Close with the single change with the most upside and the skill that ships it. If the real problem is retention or positioning, say so and hand back rather than optimizing metadata on a leaking product.

### Mode 2: STRATEGY

Turn the audit into a sequenced plan. Order that holds unless the owner says otherwise: fix the title and subtitle first (heaviest field, and renaming later costs equity), then the keyword field, then the first impression frame, then the review-ask mechanics, then localization into the winnable storefronts, then custom product pages bound to the top queries. Name what will be measured and when it is fair to judge it, which for ASO is months rather than weeks.

### Mode 3: EXECUTE

Produce the assets: the store title and subtitle at exact character counts, the keyword field as a byte-counted comma-separated string with the count shown, the short and long descriptions written per store (indexed on Play, human-first on Apple), the screenshot brief in order with the reason each frame earns its slot, the PPO or store listing experiment plan with what is being tested and why, and the review-prompt trigger points named against real product events. Every character count and byte count is stated, never estimated.

## The scoreboard

Report what connects to installs and revenue, not vanity:

- **Impressions** per keyword (are you in the index).
- **Product page views to install conversion rate** (does the page work), against the category benchmark and against your own history.
- **Rank for the primary keyword**, per storefront, tracked over months.
- **Rating average, total count, and count added in the last 30 days.** The last one is the health metric; the total is the legacy.
- **Retention**, because it now feeds the first three.

Judge ASO on a multi-month curve. Reading a week of ranking movement produces confident nonsense.

## How it composes with other skills

- Runs **after** `turma:positioning` and `turma:conversion-craft`. Positioning decides the category you are competing in, which decides the primary keyword. conversion-craft owns the offer; this skill owns the listing that sells it.
- Hands to `turma:first-session` the moment the diagnosis is a post-install signal rather than an index or an impression problem. That skill makes the signals this one depends on.
- Runs **with** `turma:retention-craft`, not after it. Post-install signals feed ranking, so for an app the two skills are one loop and a retention verdict outranks any metadata plan.
- Hands the store title back to `turma:name-craft`, which owns the brand name. Two fields, two jobs.
- Sibling of `turma:seo-strategy`, which owns everything on the web including the app's own site and the AI-answer layer that store listings cannot reach.
- Calls `turma:optimize-post` and `turma:anti-ai-linguo` for the description and screenshot copy, and `turma:emotion-craft` to turn mined review language into that copy.
- Grades against `standards/social-app-design-principles.md`, Section 4 for the distribution bar and Section 7 for the winnability test applied to keyword choice.
- Reads and updates `brand.md`: the ASO context block and the scoreboard. Factual updates are Green; a change of primary keyword is a repositioning of the whole listing and is Yellow.

## Source

Distilled from Sebastian Röhl (HabitKit, FocusKit) on Starter Story Build, "ASO master class," 2026: the three foundations (keywords, screenshots, ratings), the keyword-in-the-title rule, the keyword-field rules, the first-screenshot discipline, the review-prompt timing, the support-email ask, reviews as product insight, and the multi-year patience argument. His revenue figures are his own account, directional and not citable; his published year-by-year numbers and the interview's headline figure do not fully agree, which is normal for founder self-reporting and is why the method carries and the numbers do not.

Everything the interview did not cover was added from research and marked for confidence. Verified against primary sources: the 30/30/100 field limits and Apple's non-indexing of the description, Apple's byte-not-character keyword field, stemming and the trademark prohibition, [Product Page Optimization mechanics](https://developer.apple.com/app-store/product-page-optimization) (three treatments, 90 days, traffic proportion, 90% confidence, the icon-in-binary requirement), [custom product pages and keyword binding](https://developer.apple.com/app-store/custom-product-pages) (up to 70 pages, unique keyword combinations), `SKStoreReviewController`'s three-prompts-per-year limit, Google Play's indexed long description and its store listing experiments, and Apple's exponential 5-to-100 Search Popularity scale. Directional rather than verified: the 2024-2026 rebalance toward post-install signals and the ratings volume-versus-recency weighting, both ASO-vendor consensus with no published algorithm behind them, and SplitMetrics' first-impression figure, which is real research but dated. Explicitly refused: the claim that Apple ranks text extracted from screenshots, which is vendor speculation Apple has never documented.

## Hard rules

- Reads `brand.md` first, including the ASO context block. Never hardcodes an app or a brand.
- Never puts a competitor name or an unowned trademark in any store field. It is against both stores' guidelines and the downside is removal.
- Never gates, buys, or incentivizes ratings and reviews. Prompt timing and honest responses are the whole toolkit.
- States exact character counts and byte counts for every field it produces, computed rather than estimated. The keyword field is a byte budget and a guess ships a truncated string.
- Never presents an undocumented ranking mechanism as fact. Apple publishes no algorithm: label vendor consensus as directional and refuse the speculation outright.
- Never recommends renaming a ranking app without stating what equity the rename destroys.
- Any paid ASO tool or store advertising spend is Red. Get owner sign-off first. See `turma/TOOLS.md`.
- Judges on a multi-month curve and says so. Reporting a week of ranking movement as a result is the fastest way to lose an owner's trust.
- No dashes, no AI tells in any copy produced. Run `turma:anti-ai-linguo` as the final pass.

## Related

- The project's `brand.md`: the ASO context block (platforms, store URLs, category, primary keyword, competitors, current rank).
- `turma:seo-strategy`: the web sibling. Owns the app's own site, the review directories, and the AI-answer layer a store listing cannot reach.
- `turma:first-session`: owns the install-to-first-payoff strip where Layer 3's signals are actually made.
- `turma:retention-craft`: the loop partner. Post-install signals feed ranking, so its verdict gates this skill's plan.
- `turma:conversion-craft`: the product page is a landing page. Its Layer 2 rules apply here in full.
- `turma:name-craft`: owns the brand name. This skill owns the store title, which is a different field.
- `turma:optimize-post`, `turma:emotion-craft`, `turma:anti-ai-linguo`: the copy layer for descriptions and screenshot text.
- `standards/social-app-design-principles.md`: Section 4 for the distribution bar, Section 7 for winnability applied to keyword choice.
- `turma/TOOLS.md`: the tool registry, including which ASO tools cost money and are therefore Red.
