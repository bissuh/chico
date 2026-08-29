---
name: first-session
description: Design or audit everything between the install and the first real payoff, on mobile especially. Invoke when someone asks for an onboarding flow, a questionnaire or quiz onboarding, a welcome flow, a first-run experience, permission priming, or "why do people install and never come back." Splits the strip into the two jobs it actually contains (the commitment funnel that sells, and the first session that activates), makes the demo the hinge between them, and refuses the parts of the popular pattern that manufacture personalization. Answers the question `turma:retention-craft` asks and does not own. Reads the project's brand.md.
---

# first-session

conversion-craft ends at the yes. retention-craft starts at session two. This skill owns the strip in between, which on mobile is where most of the money and most of the churn are decided in about four minutes.

It exists because that strip is the seam between three skills and belonged to none of them. `turma:conversion-craft` owns the offer and the page, shaped for the web. `turma:aso-strategy` owns everything up to the install and then says, correctly, that post-install signals decide whether you keep the rank. `turma:retention-craft` asks one question in passing, "what does the first session promise, and when is it kept," and hands it nowhere. This is the nowhere.

**Before you start:** read the project's `brand.md` for the audience, the offer, the price, and the primary conversion goal. Then get four facts it does not carry:

1. **The core action.** The one thing a user does that creates the value they came for. Same definition `turma:retention-craft` uses, and it must be the same answer.
2. **The current numbers.** Install to onboarding-complete, onboarding-complete to trial, trial to paid, and cancel-within-first-month. Or honestly "we have never measured it."
3. **The drop map.** Where users leave the current flow, per screen. If that data does not exist, instrumenting it is the first deliverable and everything else waits.
4. **Whether the app can actually deliver on day one.** Some products need data, a week, a habit, or other people before they are worth anything. That answer changes the whole design.

If the offer is still vague or the audience is "everyone," stop and run `turma:positioning`. A questionnaire cannot personalize a product that has not decided who it is for.

## When to invoke

- Someone wants an onboarding flow built, or wants the questionnaire-style flow they saw on a competitor.
- Installs are healthy and paid conversion is not. Or paid conversion is healthy and first-month cancels are not, which is the more interesting version.
- Before wiring any system permission dialog. That prompt is one-shot and priming has to be designed before it fires.
- The app has a paywall but no story leading into it.
- `turma:aso-strategy` diagnosed a post-install signal problem and the listing is fine.
- A team is about to copy Noom, Cal AI, or Duolingo screen for screen. Especially then.

## When NOT to invoke

- For the store listing, the screenshots, or the keywords. That is `turma:aso-strategy`, and it runs before this one. There is no first session without an install.
- For the offer, the price, or a web landing page. `turma:conversion-craft`. This skill assumes the offer is worth buying and works on whether the first four minutes prove it.
- For session two onward: cadence, mechanics, streaks, the investment loop. `turma:retention-craft`, and it runs after this one.
- For what the product should be. This skill designs the entrance, not the building.
- For the visual layer. Progress bars, states, feedback timing and the completion pattern are `standards/design-principles.md`, section XX in particular. This skill decides what a screen is for; that standard decides how it looks.

## The rule that governs everything: this strip is two jobs, not one

The popular framework (Mob, Noom, Cal AI, and the skills built to clone them) presents a single numbered sequence and calls all of it onboarding. It is not one thing. It is two, with different owners and opposite failure modes, fused at a hinge.

**Job one, the commitment funnel.** Welcome, goal question, pain questions, social proof, the mirrored solution, the comparison table, the processing moment, the paywall. Every one of these sells. Nothing in this half teaches the user how the product works or gives them anything they keep. It is a sales page rebuilt as a wizard, and it works for the same reason a good sales page works: escalating small commitments, then a personalized-looking conclusion, then the price. Noom's runs to roughly 113 screens. That is not a defect, it is the design.

**Job two, the first session.** The user does the core action, gets a real result, and learns why they would open the app tomorrow. This half is what `turma:retention-craft` and `turma:aso-strategy` are both waiting on.

**The hinge is the demo,** and it is the only screen doing both jobs at once. The user performs a reduced version of the core action and gets a tangible output back. That output is the proof the funnel was promising and the first deposit of the investment loop. The source framework calls this "the hardest and most important screen" and then lists it as one of fourteen equals. It is not one of fourteen. It is the gate: a flow with the funnel and no demo is a sales page with a subscription attached, and it will convert and then refund.

The consequence to say out loud to an owner: **the funnel borrows against the product, and the product repays it in the first month or the store collects.** A hard paywall converts far better per download than freemium (RevenueCat's 2025 dataset puts the medians near 12 percent against 2 percent, vendor data, directional, re-check the current report before quoting), and roughly a third of annual subscribers cancel inside the first month. Both stores now weigh retention and review recency in ranking. So a funnel that outruns the product is charged twice, once in refunds and once in rank. Design the repayment before the borrowing.

## Diagnose before you design

Three questions, in order, same discipline as `turma:retention-craft`. Skipping them is how a team ships fourteen screens that answer nothing.

### 1. Is this even a first-session problem?

Look at where the drop actually is. Installs falling off before screen two is a store-listing mismatch: the screenshots promised something the app does not open with, and that is `turma:aso-strategy`. Users finishing the flow, subscribing, and cancelling in week two is a product problem wearing an onboarding costume. Users finishing the flow and never returning without cancelling is the case this skill is for.

Also split the borrowed floor from the organic inflow before reading any ratio, exactly as `turma:retention-craft` does. A cohort that arrived from a paid burst or a launch spike never chose this thing, and every conversion rate computed against it lies.

### 2. What is the shortest honest path to the first real payoff?

Name the payoff concretely: the shopping list, the workout, the categorized month, the first tracked meal. Then count how many taps and how many seconds stand between opening the app and holding it. That number is the thing to optimize. Every screen in the flow either shortens it, or earns its place by making the payoff land harder, or gets cut.

If the honest answer is "there is no payoff available in the first session, this product needs a week of data," say it. Then the design changes completely: the first session's job becomes setting an accurate expectation and earning the second one, and a demo that fakes a day-one result will be punished when the real thing arrives.

### 3. Does every question change something?

The single sharpest operational rule in this whole pattern, and the one most flows fail:

> Every question must change a later screen. Name the screen. If you cannot name it, cut the question.

A branch, a recommendation, a line of paywall copy, the contents of the demo. Something visible. Questions that go nowhere are not free: users notice when the answers do not come back, and the moment they notice, every personalized-looking thing after it reads as theater. This is the same refusal `turma:retention-craft` makes about a padded progress meter, applied one layer earlier.

## Layer 1: the commitment funnel

Once the three questions are answered, this half is craft rather than invention. What actually carries:

- **Open on the end state, not the app.** The first screen shows what the user's life looks like after, not what the product is called. Same job as `turma:conversion-craft`'s value proposition, one screen wide.
- **Aspiration before pain.** Ask what they want first, then what stops them. Reversing it opens on an accusation.
- **Use their words back.** The pain options are only useful if they are the sentences a real user would say. Generic options produce generic answers and the mirror screen has nothing to reflect. Pull the language from reviews, support threads, and competitor one-star reviews, which `turma:aso-strategy` already tells you to mine.
- **The mirror screen is the payoff of the questions.** Their stated pain in small text, the specific way this product handles it in bold. This screen is the reason the questions were worth asking, and it is the screen that proves the answers were read.
- **The processing pause is allowed to exist only when something happened.** See the honest bar below.
- **The paywall is a conclusion, not an ambush.** By the time it appears the user has stated a goal, been understood, seen proof, made something, and held the result. Restate their goal on it. One strong, real piece of social proof. Trial terms in plain language.

What this skill does not prescribe: **a screen count.** The evidence runs in both directions. One entertainment app's long flow beat having no onboarding at all by around 40 percent on payment conversions, and shortening that same flow cost it 13 percent. Another app cut screens and raised completion by 20 percent and week-one retention by 15 percent. Both are vendor case studies, both directional, and together they say the only honest thing available: length is a variable to test against your own drop map, never a number to copy from a teardown. Anyone quoting a magic number of screens is selling something.

## Layer 2: the demo, the hinge

Build this one first. If it cannot be built, the flow is a sales page and the owner should know that before the copy gets written.

**How to find it.** Take the core action. Reduce it until it fits in 30 to 60 seconds with a single interaction type and a fixed target ("pick three"). Feed it with real data from the product's own models where possible. Produce an output the user can see, keep, and describe to someone else.

**What makes it work is that the user does it, not watches it.** A tour, a carousel of screenshots, or a coach mark is not a demo. The user has to perform the action and receive a result, because the result is what the paywall is then asking them to keep, and because the effort spent is the first deposit in the investment loop `turma:retention-craft` Layer 2 owns.

**The output is the shareable moment,** and it is the only organic distribution this pattern generates on its own. Design it to be worth sending to one person. Then hand the sharing surface itself to the distribution skills rather than inventing one here.

**Gating the output behind an account or the paywall is legitimate on one condition:** the product genuinely delivers the thing. The user made something real, and signing in keeps it. If the app cannot actually produce that output in normal use, the demo is a mock-up and gating it is a bait. That is the line, and it is not a close call.

## Layer 3: permission priming

Cross-cutting, and worth its own section because the prompt is one-shot inventory and most flows spend it badly.

**Never fire a system dialog cold.** Show a screen first that frames the value, not the permission. "Never miss the day your plan resets" rather than "Enable notifications." Two or three concrete things they get. A visible, unpunished way to decline. Vendor data across the push tooling market puts primed opt-in somewhere around 60 to 75 percent against 35 to 45 percent for a cold prompt, roughly a 2 to 3 times lift. No first-party study backs the exact figures, so treat the direction as reliable and the numbers as illustrative.

**Ask in context, not in onboarding, whenever the product allows it.** Camera permission belongs on the first tap of "scan," not on screen nine. Notification permission belongs after the demo, when the user knows what they would be notified about. Onboarding is the right place only when the permission gates the demo itself.

**Only prime what the app actually uses.** Detect the declared permissions from the codebase (`Info.plist`, `AndroidManifest.xml`, or the framework's equivalent) and prime from that list, never from a wishlist. Priming a permission the product does not need is the cheapest way to lose someone at the exact moment they were deciding to trust you.

**Platform facts worth carrying:** iOS notification permission is one-shot through `UNUserNotificationCenter`, and App Tracking Transparency is a separate prompt with its own Apple rules. Android 13 and above requires a runtime prompt for `POST_NOTIFICATIONS`; below that it is granted at install. A denial is recoverable only by sending the user to Settings, which is why the priming screen is not optional.

**The review prompt is the same economics and a different budget.** `turma:aso-strategy` owns it: at most three requests per user per 365 days on iOS, spent at the moment the product delivered. Never in the first session. The first session has not earned it.

## The honest bar

Everything in this strip passes one filter before it ships:

> Did the thing the screen claims happened actually happen?

Concretely, this skill refuses to design:

- **A processing screen that processes nothing.** The animated "building your plan just for you" pause is fine when a plan is genuinely being assembled from the answers, and it is a lie when the delay is a `sleep` and the next screen is identical for every user. Same rule, one layer up, as the fake-remainder line in `standards/design-principles.md` section XX. Either compute something or cut the screen.
- **Invented testimonials.** A pre-launch app with no users writes no reviews. "Aspirational testimonials to be replaced later" are fabricated social proof shipped to real people, and on an app store they are close to a policy problem as well as an honesty one. Use the founder's own story, a beta tester's real words with permission, or nothing.
- **Invented statistics.** "Users save 25 percent" from a product that has never measured it is a fabricated parameter, which is the one thing turma never ships. If a number is a cited industry benchmark, cite the industry and say so on the screen. If it is a projection, do not present it as a result.
- **Number cosmetics.** The advice that 83 sounds more credible than 80 is advice about making a figure feel true independently of whether it is. Report the number you have.
- **Pain amplification with no output.** Swipe-to-agree cards over statements the user is meant to nod at are a mood, not a question, unless the answers change a later screen. Run them through the question gate like everything else. Most of the time they fail it.

The healthy version of this strip is a user who paid because they saw the thing work. The unhealthy version is a user who paid because the wizard made them feel understood. They look identical on the conversion chart for about thirty days, which is exactly when the second one cancels.

## Modes

State the mode at the top of your output.

### Mode 1: AUDIT

Given an existing flow (screenshots, a recording, or the code), output in this order: the drop map screen by screen, or the note that it does not exist and must be built first; which half of the strip each screen belongs to, funnel or first session; every question run through the question gate with the screen it changes or a verdict of cut; whether a demo exists and whether the user performs it or watches it; the honest-bar check on the processing, proof and stats screens; time from open to first real payoff, in seconds and taps; and then the single change with the most upside, named concretely.

If paid conversion is healthy and first-month cancels are not, say plainly that the finding is a debt, not a win, and hand to `turma:retention-craft`.

### Mode 2: BUILD

Given a product that can deliver something on day one, design the flow. Output: the core action and the reduced demo, first; the payoff the demo produces; the question set, each with the screen its answer changes; the funnel sequence with the specific headline for each screen (not the archetype label); the permission plan, with what is primed in-flow and what is deferred in-context; the paywall's restated promise; and the measures to add to the `brand.md` scoreboard.

Design the demo before the copy. A flow whose demo cannot be built does not need copy, it needs a different plan.

## The scoreboard

Four numbers, and the fourth is the one that keeps the other three honest.

1. **Time to first real payoff.** Seconds and taps from open. The only number this skill is trying to push down.
2. **Completion by screen.** The drop map. Aggregate completion rate hides which screen is doing the damage.
3. **Install to paid.** The number everyone already watches.
4. **Cancel and refund inside the first month.** The repayment. Read numbers 3 and 4 together always, never 3 alone. A flow that moves 3 up and 4 up further has lost money and rank at the same time.

Add whichever of these `brand.md` does not already carry. Adding a measure is a factual update and Green; changing what the project is judged on is Yellow.

## How it composes with other skills

- Runs **after** `turma:aso-strategy`. No first session without an install, and a drop at screen one is usually a listing that promised something else.
- Runs **after** `turma:conversion-craft`, which settles the offer and the price this flow is selling. The pricing model has to match the cadence, and the answer must be the same one `turma:retention-craft` gives.
- Runs **before** `turma:retention-craft`, and hands it a live user with something already deposited. This skill answers the question that skill asks in its Layer 1 and does not own.
- Feeds `turma:aso-strategy` Layer 3 directly. Post-install signals are made here, so a first session that lands is a ranking asset and one that does not is a ranking liability.
- Calls the copy skills for every screen: `turma:story-craft` for the transformation narrative, `turma:emotion-craft` where the shareable output is designed, `turma:anti-ai-linguo` as the final pass on everything user-facing.
- Hands the interface layer to `standards/design-principles.md`, section XX for the progress bar and the completion pattern.
- Reads and updates `brand.md`: the scoreboard, and the audience language the questions are written in.

## Source

Built from Adam Lyttle's `app-onboarding-questionnaire` Claude skill (MIT, 2026), which distills the Mob recipe app's flow and the pattern shared by Noom, Headspace, Duolingo and Cal AI. Its genuine contributions are the demo screen, the permission-priming section, and the insistence that the user perform rather than watch. Those are taken here and promoted: the demo from one screen among fourteen to the gate the whole design turns on.

The rest was reworked rather than adopted. Its numbered 14-screen sequence is a paywall funnel labelled as onboarding, which is the confusion this skill exists to undo. Its instruction to write aspirational testimonials for an app with no users, to use "industry benchmarks or logical projections" as if they were the product's own results, and to prefer 83 over 80 because it feels more credible, are all refused above.

The question gate ("every question must change a later screen, name it or cut it") comes from the web-to-app funnel literature, sharpest in RevenueCat's Noom teardown and FunnelFox's onboarding work. The conversion and cancellation medians are RevenueCat's State of Subscription Apps dataset, vendor data, directional, and worth re-reading in the current year's edition before quoting to an owner. The permission-priming lift is vendor-reported across the push tooling market with no first-party study behind the exact figures. The evidence on flow length was deliberately gathered in both directions, and it stays contradictory on purpose.

One number to leave alone: the promotional post for the source skill cited Cal AI at a million dollars a month. Cal AI reported roughly 30 million dollars of revenue across 2025 and around 5.7 million in January 2026 before being acquired by MyFitnessPal, so the figure in circulation is stale by a wide margin. It is a reminder that the numbers attached to a pattern are usually marketing for the pattern. The method is what carries.

## Hard rules

- Reads the project's `brand.md` first. Never hardcodes a brand.
- Design the demo before the copy. If no demo can be built, say so before anything else gets written.
- The question gate is not optional. Every question names the screen its answer changes, or it is cut.
- Never fabricate a testimonial, a statistic, or a personalization. A processing screen that computes nothing is a fabricated parameter with an animation on it.
- Never fire a system permission dialog without a priming screen, and never prime a permission the app does not use.
- Read install-to-paid and first-month cancel together, always. Reporting conversion alone from this skill is a misrepresentation.
- Does not write the implementation unless asked separately. Writing the code is Green; shipping it to users is Yellow.
- The most valuable output is usually the unwelcome one: "this is a listing problem," "there is no day-one payoff to demo," "your conversion went up and your refunds went up further." Say it plainly.
- Never edits operating canon (`SOUL.md`, `IDENTITY.md`, `CLAUDE.md`, `SPEC.md`, `memory/`).
- No AI tells, no dashes on any owner-facing copy produced. Run `turma:anti-ai-linguo` as the final pass.

## Related

- `turma:aso-strategy`: upstream. Gets them to install, and depends on this skill for the signals that hold the rank.
- `turma:conversion-craft`: upstream. The offer, the price, and the web-shaped version of the same persuasion.
- `turma:retention-craft`: downstream. Session two onward, and the owner of the mechanics and the investment loop this skill makes the first deposit into.
- `turma:positioning`: further upstream. A questionnaire cannot personalize a product with no segment.
- `turma:story-craft`, `turma:emotion-craft`, `turma:anti-ai-linguo`: the copy layer for every screen.
- `standards/design-principles.md`: section XX, the progress and completion pattern, including the fake-remainder rule this skill extends.
- The project's `brand.md`: audience, offer, price, conversion goal, scoreboard.

## A note on contracts

This skill needs the same product facts `turma:retention-craft` asks for at invocation (the core action, the current numbers) plus two of its own (the drop map, whether a day-one payoff exists). That is now two skills asking for overlapping facts `brand.md` does not carry, which is the trigger CLAUDE.md names for a sibling contract. A `product.md` holding the core action, the cadence, the payoff and the cohort picture would serve both without touching `brand.md`'s shape. Worth building when a third skill needs it, or the next time either of these two runs on a real project.
