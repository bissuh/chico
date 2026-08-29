---
name: retention-craft
description: Decide whether users come back, and whether leaving costs them anything. Invoke when a product "has users but they don't stick," before adding any game mechanic (streak, points, badge, leaderboard, challenge), when churn is the number that hurts, or when someone proposes gamifying something. Runs a diagnosis first (is this even a retention problem, what is the natural cadence, does the curve flatten) and only then designs the two layers: the mechanics that pull a user back, and the investment that makes leaving expensive. Loads `standards/social-app-design-principles.md` sections 7 and 8 as the bar. Starts where `turma:conversion-craft` stops. Reads the project's brand.md.
---

# retention-craft

conversion-craft ends at the yes. This skill starts one second later.

Growth work usually stops at the signup, which is why so many projects have a chart that goes up and a business that does not. Acquisition is a leaky bucket argument: every user you keep is a user you never have to buy again, and retention is the only growth input that compounds without a budget attached.

It is also the place where good intentions do the most damage. Retention is one design decision away from manipulation, and the mechanics that look most obviously "retentive" (a streak, a badge, a leaderboard) have the longest documented failure record in product history. This skill exists so the work goes in the right order and stops at the honest line.

**This is turma's first product-side skill.** Every other one is content or distribution craft. It does not decide what to build, and it does not write code. It decides what happens to a user between session one and session one thousand.

**Before you start:** read the project's `brand.md` for the audience, the offer, the primary conversion goal, and the scoreboard. Then get three product facts it does not carry, from the owner or from the product itself:

1. **The core action.** The single thing a user does that creates the value they came for. Not "opens the app." The thing.
2. **The natural cadence.** How often a real user genuinely gets value. Daily, weekly, seasonally, once.
3. **The current picture.** Cohort retention if it exists, or honestly "we have never measured it."

If `brand.md` has no offer or the audience is "everyone," stop and run `turma:positioning`. Retention work on top of fuzzy positioning is a way of keeping the wrong people.

## When to invoke

- A product has users, or signups, or installs, and they do not come back.
- **Before** anyone ships a streak, points, badges, a leaderboard, a challenge, or a progress meter. This is the main one. The mechanic is cheap to build and expensive to remove.
- Churn is the number that hurts, or the number nobody will look at.
- Someone says "we should gamify this."
- Judging whether a product actually has a moat, as opposed to a head start.

## When NOT to invoke

- Before the offer converts at all. That is `turma:conversion-craft`, and it runs first. There is nothing to retain yet.
- When the audience or the painkiller is vague. That is `turma:positioning`.
- For where the users come from. The distribution skills own that (`turma:power-law`, `turma:seo-strategy`, `turma:ghostshelf`, `turma:cta-machine`).
- For the interface itself. Progress indicators, states, and feedback timing are `standards/design-principles.md`, section XX in particular. This skill decides *whether* a progress loop should exist; that standard decides how it should look.
- For the first session itself: the install-to-first-payoff strip, the questionnaire flow, the demo, permission priming. That is `turma:first-session`, and it runs immediately before this one. Onboarding is still a retention artifact, it just has an owner of its own now.
- For content that people subscribe to rather than use. An email list or a channel has its own retention shape and the metrics lie differently there. Some of this transfers; the mechanic layer mostly does not.

## The rule that governs everything: diagnose before you design

The failure mode of retention work is skipping straight to mechanics. Someone reads about streaks, ships a streak, and buries the actual finding under a feature. Steps 1 through 3 below exist to stop that, and most of the value in this skill is in them.

Three questions, in order, before a single mechanic is discussed.

### 1. Is it a retention problem?

Often it is not. Two checks.

**Split the borrowed floor from the organic inflow.** Find out where the users came from. Imported, bought, migrated from another product, launch-spike, or earned. A base that arrived in a bulk import never chose this thing, so every ratio computed against it lies: churn, engagement, activation, all of it. The team reads "we have a churn problem" and writes retention features, when the real finding is "we have no acquisition engine and never did." Those two diagnoses lead to opposite work. Report organic inflow per period as its own number, next to the total, and never let the total stand alone.

**Read cohorts, not the aggregate.** An aggregate active-user line can hold flat while every single cohort collapses, because new signups refill what churn drains. That chart is a treadmill drawn as a plateau. If the project cannot produce a cohort table, producing one is the first deliverable and everything else waits.

### 2. What is the natural cadence?

How often does a real user actually get value? Let the honest answer set the rhythm, because every mechanic downstream inherits it.

A product whose value lands weekly, wrapped in a daily streak, is punishing users for the product's own shape. They will feel the mismatch as guilt, blame themselves, and leave. This is the same question `turma:conversion-craft` asks about pricing (monetization follows retention), and the answer has to be the same answer in both places. If the pricing says monthly and the cadence says twice a year, one of them is lying.

Do not try to raise the cadence with mechanics. Raise it with the product, or design for the real one.

### 3. Does the curve flatten?

Retention curves do one of two things. They decay and then **asymptote**, which means a core of users found something durable and the flat part is the real business. Or they decay toward zero, which means nobody found it.

A curve that does not flatten cannot be fixed with a mechanic. That is a product finding, and the honest output of this skill in that case is "stop, this is not a retention problem, the product does not deliver repeat value to anyone yet." Say it plainly. It is the most valuable thing this skill produces and the least welcome.

Only once the curve flattens does the work below make sense. Then the job is raising the asymptote, and the two layers are how.

## Layer 1: the return (do they want to come back)

The mechanics layer. The bar lives in `standards/social-app-design-principles.md`, **Section 7, Retention Mechanics**. Load it and run its five-question mechanic test on every proposed mechanic. It is pass-all, not scored: a mechanic that fails any of the five is theater, and theater costs the same to build as the real thing.

The short version of what that section will tell you, so you know what you are walking into:

- **Points, badges, and leaderboards are the scoreboard, not the game.** They measure activity, they do not create it. Fine on top of a real loop, useless as the loop.
- **Engineer the size of the competition.** One global leaderboard motivates the top few percent. Winnability is the variable.
- **More mechanics reverses past a point.** Stacking is overload wearing engagement's clothes.
- **Streaks turn into obligation.** Conditional, not banned, and they need an agency wrapper.
- **Anticipation recharges, loss aversion burns out.** Two engines that look identical from outside.
- **Completion drive closes cleanly.** The strongest engine, because the loop actually ends.
- **Competence beats recognition.** Signal that the user got better at the real thing.

Three questions this skill adds on top of the standard, because they are about sequence rather than quality:

- **What is the loop without any mechanic?** Describe the reason a user returns if you ship nothing. If there is no answer, the mechanic is load-bearing and it will collapse. Fix the loop first.
- **What does the first session promise, and when is it kept?** Onboarding is a retention artifact. The gap between the promise and the first real payoff is where most churn lives, and closing that gap beats any mechanic you could add around it. `turma:first-session` owns that gap. If it has not run, run it before designing anything here.
- **What happens on the day they fail?** Every mechanic has a failure state. Design the miss, the broken streak, the empty week, before you design the win. Products lose users on the bad day, not the good one.

## Layer 2: the cost of leaving (does going elsewhere hurt)

The investment layer. The bar is `standards/social-app-design-principles.md`, **Section 8**. Load it and run its two test questions.

Layer 1 keeps users running. On its own it is a treadmill: it does not stop them stepping onto a newer, shinier one. Layer 2 is what makes the exit door heavy, and it is the difference between a head start and a moat.

The mechanism: every session should deposit something that makes the product better **for this specific user** and that the user cannot take with them. Not features, which make it better for everyone. Stored value that compounds.

The two tests, which are the whole layer:

1. **The compounding question.** Does session 1,000 give measurably better results than session 10? If they are identical, the project has engagement and zero investment.
2. **The exit question.** If a user left for a competitor today, what would they have to rebuild from scratch? If the answer is "not much," there is no moat yet.

What this skill adds: **the deposit has to be automatic and visible.** The strongest investment loops never ask a user to consciously invest, because conscious investment is work and work gets skipped. And the accumulation has to be shown ("1,095 nights tracked"), because seen investment reads as partnership while hidden investment reads as a trap the moment someone tries to leave.

## The honest bar

Both layers pass through one filter before anything ships:

> Does this produce a real outcome the user would defend to a friend, or only a number that makes the dashboard look alive?

The healthy version of retention is a user who stays because staying keeps paying off, and who could leave. The unhealthy version is a user who stays because leaving was made to hurt. They look identical on a chart for about two quarters, and then one of them churns all at once.

Concretely, this skill refuses to design: a loop the user cannot pause or exit, a progress meter padded with steps the user did not ask for, a mechanic whose value to the user is zero and whose value to the dashboard is the whole point, and any streak aimed at minors. That last one is also becoming a regulatory question rather than a taste question.

## Modes

State the mode at the top of your output.

### Mode 1: AUDIT

Given an existing product, diagnose the retention picture. Output, in this order: where the users came from (borrowed floor versus organic inflow, as two numbers); what the cohort curves do and whether they flatten; the natural cadence and whether the product's rhythm matches it; every existing mechanic run through the standard's five-question test with a verdict each; the two investment questions answered honestly; and then the single change with the most upside, named concretely, with the skill or the owner who ships it.

If the curve does not flatten, stop at step three and say so. Do not produce a mechanics section for a product that has not earned one.

### Mode 2: BUILD

Given a product whose curve flattens, design the two layers. Output: the core action and the cadence, stated plainly; the loop as it exists without any mechanic; the mechanics proposed, each with its five-question test result and its failure state designed; the investment loop (what gets deposited, how it is automatic, how it is made visible); the honest-bar check on all of it; and the two or three measures the owner should watch, added to the `brand.md` scoreboard.

Leave the build to the owner. This skill produces the design and the reasoning, not the implementation.

## How it composes with other skills

- Runs **after** `turma:first-session`, which is the nearer upstream sibling. That skill owns the install-to-first-payoff strip and hands this one a live user with something already deposited. If the first session never delivers a payoff, no mechanic here will hold.
- Runs **after** `turma:conversion-craft`. That skill makes attention into a customer; this one decides whether the customer stays. Both ask the cadence question and the answers must match.
- Runs **after** `turma:positioning`, at a distance. If retention work keeps finding that users cannot say what the product is for, that is a positioning failure surfacing late.
- For a mobile app, feeds `turma:aso-strategy` directly and runs alongside it rather than before it. Both stores now weigh post-install signals (product page conversion, retention, review recency) in search ranking, so a cohort curve that flattens is not only a revenue fact, it is a distribution asset. The reverse holds harder: no amount of metadata work outranks churn.
- Feeds the **distribution** skills (`turma:power-law`, `turma:seo-strategy`, `turma:ghostshelf`, `turma:cta-machine`) a reason to be worth running. Traffic into a bucket with no bottom is the most expensive mistake in the stack.
- Shares an axis with `turma:power-law` and should not be confused with it. See "The axis the law does not cross" there: more independent bets wins, more mechanics inside one product reverses.
- Hands the interface layer to `standards/design-principles.md`, section XX for progress and completion in particular. This skill says whether a loop should exist; that standard says how it should look on screen.
- Reads and updates `brand.md`: the scoreboard, when a retention measure joins it. Factual updates are Green; changing what the project is measured on is Yellow.

## Source

The mechanics layer is distilled from Tim Gabe's gamification breakdown (YouTube, 2026) and, more usefully, from the papers it points at, each verified independently: Yu-kai Chou's PBL framing, the Frontiers in Psychology 2025 S-curve study on feature richness, Diefenbach and Müssig's Habitica field study (IJHCS 2019), the Belgian Snapchat streak survey (Telematics and Informatics Reports 2023), and Li, Hew and Du's self-determination meta-analysis (ETR&D 2024). Several of that video's headline figures failed verification and are deliberately absent here; the record of which is in Chico's memory.

The investment layer builds on Nir Eyal's stored value from _Hooked_ (2014) and the Norton, Mochon and Ariely IKEA-effect work, extended in `standards/social-app-design-principles.md` into intelligence lock-in.

The diagnosis layer is ours, and it came from a real engagement rather than a book. A project once reported a healthy-looking audience number that turned out to be almost entirely a bulk import from an unrelated source, with organic inflow near zero. Everyone read it as a churn problem. It was never a churn problem. That is why step one of this skill is splitting the floor from the inflow, and why the cohort rule sits ahead of every mechanic.

## Hard rules

- Reads the project's `brand.md` first. Never hardcodes a brand.
- Diagnose before you design, without exception. No mechanic gets proposed before the curve question is answered. If the curve does not flatten, the honest output is "this is not a retention problem" and the skill stops there.
- Load `standards/social-app-design-principles.md` before running either layer, and run `./standards/sync.sh` first. That file is a fork with local additions, so `--diff` shows what moved upstream; never `--pull` over it. A stale bar is worse than no bar.
- Never duplicate the standard into the output. The standard is the bar, this skill is the method. If a rule belongs to the rubric, cite the section and move on.
- Refuses to design a loop the user cannot exit, a padded progress meter, a mechanic whose only beneficiary is the dashboard, or any streak aimed at minors.
- Does not decide what to build and does not write the implementation. It produces the design and the reasoning; the owner ships.
- The most valuable output is usually the unwelcome one: "the curve never flattens," "this is an acquisition problem," "your best mechanic is the one you already have and are about to bury." Say it plainly.
- Never edits operating canon (`SOUL.md`, `IDENTITY.md`, `CLAUDE.md`, `SPEC.md`, `memory/`).
- No AI tells, no dashes on any owner-facing copy produced. Run `turma:anti-ai-linguo` as the final pass.

## Related

- `turma:first-session`: the immediate upstream sibling. Owns everything between the install and the first real payoff, including onboarding, the demo, and permission priming.
- `turma:conversion-craft`: the upstream sibling one step further out. It ends at the yes; this one starts there. The two share the cadence question.
- `turma:positioning`: further upstream. Chronic retention failure is often positioning surfacing late.
- `turma:power-law`: the portfolio axis, and the boundary that keeps "more is better" out of a single product.
- `turma:aso-strategy`: the loop partner for a mobile app. Retention feeds store ranking, so this skill's verdict gates that one's plan.
- `standards/social-app-design-principles.md`: sections 7 and 8 are the bar this skill grades against.
- `standards/design-principles.md`: section XX, how a progress loop should look once this skill has decided it should exist.
- The project's `brand.md`: audience, offer, conversion goal, scoreboard.

## A note on contracts

This skill needs three product facts `brand.md` does not carry: the core action, the natural cadence, and the current cohort picture. It asks for them at invocation rather than requiring a new contract file, because one skill is not enough reason to change the shape of every installed project. If product-side work becomes routine and a second skill needs the same facts, a `product.md` sibling contract is the right move then, not now.
