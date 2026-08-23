# Product Guidelines: Principles for Viral Growth and Network Effects

> Based on 10 years of experience building consumer social apps. Use this document as a mandatory checklist before approving any feature or product.

---

## 1. Testing Mindset

### Speed > Vision

A reproducible testing process is more valuable than any one idea. **Innovate here first.**

All things equal, a team with more shots at bat will win against a team with an audacious vision.

### Conclusive Tests are Mandatory

Nothing slows down teams more than inconclusive tests. If you're walking away from tests saying "maybe we needed more downloads" or "people needed more friends," **your biggest priority should be fixing your testing tactics**.

You need to be able to pivot with conviction.

### Scoping Rules

- If you need to launch nationwide to test your product, **it's not a good test**
- You will prematurely exhaust your audience's attention and limit future shots
- If your product works in one community (like a high school), it should work in all of them
- If it fails in three communities, it should fail in all of them

---

## 2. Idea Filtering

### Most Ideas are Dead On Arrival

Most product ideas are DOA because the conditions to derive value are impossible to orchestrate.

**Reality Check:** Getting 7 adult friends to install an app on a reproducible basis is non-trivial. If you can figure out how to do that, **that's a bigger idea than your original concept**.

### Mandatory Checklist Before Building

Before approving any feature, answer:

| Question                                 | Required Answer        |
| ---------------------------------------- | ---------------------- |
| Do we have a clear distribution channel? | Yes, specified         |
| Can the product grow organically?        | Mechanism defined      |
| Which core human need does it solve?     | One of the three below |

### The Three Needs That Drive Downloads

People download apps to solve:

1. **Finding love**
2. **Making or saving money**
3. **Play/entertainment**

People rarely take time out of their day for anything else.

> ⛔ **NEVER** build an app to "meet up with friends"

---

## 3. Target Audience

### Small Niches are Strategic

Don't be embarrassed to have a narrow target audience. **All big things grow from small wedges in the market.**

### Ideal Beachhead Audiences

Audiences that exhibit obsessive behavior tend to be the best entry points:

- Gamers
- Teens
- Hobbyists

You need this obsessive engagement at the beginning to get the flywheel spinning.

### Reality About Age

The number of social products that took off among older audiences can be counted on **one finger**. Our habits become immutable as we exit our formative years.

### Life Inflection Points

Great products take off by targeting a specific life inflection point, when the urgency to solve a problem is most acute:

| Product  | Inflection Point       |
| -------- | ---------------------- |
| Facebook | Starting at a school   |
| LinkedIn | Getting your first job |
| Slack    | Starting a company     |

---

## 4. Distribution and Marketing

### Be Unapologetically Relevant

The only way to push through the noise of the App Store is to be **unapologetic about marketing** to your first users.

If your first users are Berkeley students, go ahead and call the app "Berkeley Memes." It's hard enough to get the flywheel spinning without being obnoxiously relevant.

### Recurring Organic Exposure

Habit formation requires recurring organic exposure on other networks.

After people install your app, they need to see your content elsewhere to remind them that your app exists:

- Instagram photos on Facebook
- TikTok videos on Instagram
- Tweets on LinkedIn

### Don't Depend on Partnerships

> ⛔ If your product requires a "partnership" to work, **run**.

### Ignore Fear of Incumbents

Incumbent advantage is frequently overstated. Well-crafted products that harness unique distribution channels can take the world by storm—sometimes in a matter of days.

---

## 5. Product Design

### People > Polish

The people and content on an app always trump slick design and novel interactions.

**Focus more on:**

- Getting network effects
- Solving the "cold start" problem

### The Toilet Test

If you can't use your app from the toilet or while distracted—like driving—your users will have few opportunities to form a habit.

> There is a graveyard of live video apps that didn't make it because of the attention they require.

### Long Sign-Up Flows Are OK

Excessively long sign-up flows are fine **if they lead to higher activation rates**. Most people don't bail after installing something.

---

## 6. Engagement Loops

### Positive Feedback Loops

Positive feedback loops are necessary to reach "escape velocity."

**Target heuristic:** Each app session should trigger 7 new people to open your app.

Examples of explosive loops:

- **Tinder:** Match → Conversation → Invites friends to see
- **Snapchat:** Snap received → Opens app → Sends snap → Recipient opens app

### Escape Velocity Metrics

If the product is retentive, investors will line up to bankroll your growth. Focus on retention first.

> Retention has three layers: **engagement** (this section) keeps users running; **mechanics** (Section 7) decide whether that running is real or theater; **investment** (Section 8) is what stops them jumping to a newer treadmill.

---

## 7. Retention Mechanics (Gamification That Isn't Theater)

Section 6 builds the loop. This section decides which mechanics go inside it. Most gamification fails in a predictable way, and the failures are better documented than the wins.

### The PBL Fallacy

Points, badges, and leaderboards are the three mechanics every product reaches for first. They are also the three with the longest failure record.

Yu-kai Chou's framing is the one to keep: **PBL is the scoreboard of the game, not the game.** Nobody walks into a stadium, looks at the scoreboard, and feels like playing. Most products build the scoreboard and never build the game.

The receipts:

| Product    | What happened                                                                                                                                              | The lesson                                                                                            |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| LinkedIn   | Retired the gold Community Top Voice badge in October 2024. It was awarded automatically on contribution volume, so it rewarded quantity and LinkedIn could not hold a quality bar. | A badge awarded on volume gets optimized on volume.                                                     |
| Foursquare | Split into Swarm and Foursquare in 2014 and stripped mayorships and badges. Users revolted, and mayorships returned to Swarm in June 2015.                    | Cutting the mechanic is not the fix either, once users have built identity on it. Build the game underneath. |

> Read the Foursquare case both ways. The mechanic was hollow **and** removing it hurt, because by then it was the only thing users had. That is the trap: a hollow mechanic still accumulates attachment, and you end up able to neither keep it nor kill it.

### Engineer the Size of the Competition

One global leaderboard is close to useless. It motivates the top few percent and tells everyone else they cannot catch up.

Strava's segments are the counter-design. Any user-defined stretch of road becomes its own leaderboard, sorted into age and gender cohorts. That turns one unwinnable ranking into thousands of small winnable ones. The hill on your morning route is a competition you might actually place in.

**Winnability is the variable, not competition itself.** When a leaderboard is failing, the first question is not "should we remove it" but "how big is the pool, and can a median user place in it?"

One caution on the social side. A study of five Strava clubs (Franken et al., _Social Networks_, 2023) found that receiving kudos did raise running frequency and volume. It also found peer influence mattered more than kudos, and that users converged toward their **less** active friends more than their more active ones. Simulated without any influence effects, those users would have run more. Social comparison in a network pulls toward the middle, not upward. Do not assume a social feed only ratchets behavior up.

### The S-Curve: More Mechanics Reverses

Gamification feature richness follows an S-curve. Adding mechanics raises engagement up to a point, and past that point it lowers it (Frontiers in Psychology, 2025, on exercise adherence intention). That study measures stated intention rather than logged behavior, so treat the shape as the finding and the magnitude as unproven.

Habitica is the worked example. Tasks become quests, habits become character stats, missing a task costs HP. In the field study (Diefenbach and Müssig, _International Journal of Human-Computer Studies_, 2019, 45 users over two weeks) every participant reported counterproductive effects to some degree. The most common was being punished by the system during their most productive stretches. Users ended up managing the game layer instead of doing the work.

> ⛔ If you are stacking streaks **plus** points **plus** badges **plus** challenges **plus** leaderboards, assume you are past the peak, not climbing it. Cognitive overload reads as engagement right up until it reads as churn.

### The Streak Trap

Streaks shift from motivational to obligational the longer they run. The user moves from "I want to do this" to "I cannot miss today." That is loss aversion doing the work, and loss aversion burns the user out on the way to retaining them.

It is also the mechanic under regulatory attention. The Snapchat streak literature is the most cited (a survey of 2,483 Dutch-speaking Belgian early adolescents, mean age 13.5, in _Telematics and Informatics Reports_, 2023, linking streak engagement to FOMO and problematic smartphone use, though the reported correlations are weak). The European Commission is expected to propose a Digital Fairness Act in Q4 2026, explicitly targeting addictive design with minors as a stated focus.

Streaks are not banned. They are conditional. Duolingo ships one and retains on it, but wrapped in agency: the user picks the goal level, can buy a streak freeze, can pause. **The design under scrutiny is a streak the user cannot pause, influence, or escape.** If a streak is the primary retention mechanic rather than one of several, that is the warning sign.

### Anticipation Beats Loss Aversion

There are two engines, and from the outside they look similar.

|                  | Streak                                | Variable reward                          |
| ---------------- | ------------------------------------- | ---------------------------------------- |
| Emotional driver | Fear of losing what you built         | Pull toward what might be next           |
| Over time        | Accumulates obligation, then burns out | Recharges itself                         |
| Fails when       | The user misses once                  | The reward distribution becomes predictable |

The mechanic that carries anticipation is **variable magnitude plus staged reveal**. The user knows a reward is coming and does not know how big. Then the reveal is broken into stages so one event becomes several: a pack of cards flipped one at a time resets the anticipation cycle per card, instead of dumping the same information at once.

Two design notes. The unknown has to be genuine, or the reveal becomes a cutscene the user learns to skip. And this is the loot-box structure, so it carries real addiction adjacency. Put it on something the user wants more of, never on something they are trying to ration.

### Completion Drive

The strongest alternative to both engines. The brain treats an incomplete pattern as demanding completion (the Gestalt principle of closure, the same family as the Zeigarnik effect). A ring at 90% is an open loop, and the user wants to close it.

Apple's activity rings are the reference implementation. Three rings, close all three, the day is done. Analysis of the Apple Heart and Movement Study (over 140,000 participants) found people who regularly closed their rings were 48% less likely to report poor sleep quality. The important part is not the number. It is what the number is about: the mechanic drove a real-world outcome, not app opens.

**Completion drive is the cleanest engine because closure satisfies instead of coercing.** The loop ends. A streak never ends, which is exactly why it turns into obligation.

The rules that come with it:

- The loop has to be closable today. A goal that cannot be met by bedtime is not an open loop, it is a debt.
- Show the gap, not just the progress. The remaining 10% is what does the work.
- Closing has to mean something outside the app. If closing the ring only proves the user opened the app, that is theater with better psychology.

### Competence Over Recognition

The most useful finding for anyone choosing between mechanics. A meta-analysis of 35 gamified-learning interventions (Li, Hew and Du, _Educational Technology Research and Development_, 2024) found gamification reliably improves perceived autonomy (g = 0.638) and relatedness (g = 1.776), and barely moves competence (g = 0.277). Competence is the need most tied to long-term intrinsic motivation.

Read plainly: most products engineer recognition and forget to engineer mastery. The meta-analysis covers classroom learning rather than consumer apps, so treat it as a strong prior about the mechanism, not a measured result for products.

The distinction is whether a mechanic is evidence of skill or evidence of attendance:

| Evidence of skill                                                     | Evidence of attendance                     |
| --------------------------------------------------------------------- | ------------------------------------------ |
| A rating that moves when you actually get better (Chess.com Elo)      | A badge for logging in 30 days running     |
| Output measured live, personal records logged automatically (Peloton) | A points total that only counts sessions   |
| A readiness or baseline score derived from your own history (Garmin, Oura) | A leaderboard rank driven mostly by time spent |

A "100 rides" badge is not theater, because it represents 100 actual rides. A "100 logins" badge is.

### The Mechanic Test

Before shipping any game mechanic, answer all five:

- [ ] **Game or scoreboard?** Does this mechanic create the activity or only measure it? Measuring is fine, as long as something else is creating the activity.
- [ ] **Winnable?** Can a median user place, or does this only speak to the top few percent?
- [ ] **Where on the S-curve?** Count the mechanics already shipped. Is this one climbing or overloading?
- [ ] **Which engine?** Loss aversion (obligation, burns out), anticipation (recharges), or completion (closes cleanly). Name it. If it is loss aversion, what is the agency wrapper?
- [ ] **Skill or attendance?** Does this signal the user got better at the real thing, or that they opened the app a lot?

> ⚠️ The bar for all of it: does the mechanic produce a real-world outcome the user would defend, or only a number that makes the dashboard look alive?

---

## 8. The Investment Layer (Intelligence Lock-In)

Engagement is **layer one**. It's necessary — but on its own it's a treadmill: it keeps users running, it doesn't stop them jumping onto a newer, shinier one. The products people genuinely _can't_ quit add a **second layer** — every session deposits something irreplaceable that compounds and that the user cannot take with them.

### Stored Value, Supercharged by AI

Nir Eyal named **stored value** in _Hooked_ (2014): users who invest in a product stick around. AI turned this into something stronger. The deposit is no longer just data — each session **trains an intelligence** (a model of _this specific user_) that can't be exported, transferred, or rebuilt overnight.

> Regulation (e.g. the EU Data Act) can force you to export the _data_. It cannot export the _model trained on you_. The container is freed; the intelligence stays put — the shift from **data lock-in** to **intelligence lock-in**.

### Why Investment Beats Engagement: The IKEA Effect

Norton, Mochon & Ariely found people assign **63% more value** to things they helped build. Every ranking, correction, mood board, or rule a user contributes makes the product feel like _theirs_ — and makes leaving feel like discarding their own work.

### Three Proofs, One Mechanism

| Product        | Intelligence trained about you                                                             | What a competitor can't hand you                                        |
| -------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Midjourney** | A submodel of your visual taste (warm/cool, minimal/maximal, photoreal/painterly) via image-pair ranking | Your creative fingerprint — switch and you "start with a stranger's eyes" |
| **Oura**       | Your body's baselines over 1,095+ nights (sleep, HRV, temperature)                        | The model calibrated to _your_ physiology — the CSV is numbers, not intelligence |
| **Ramp**       | Your company's financial logic (spend rules, policies, vendor categories)                 | Years of encoded decisions plus every system wired into it              |

In each case a better-funded competitor with strong design and engagement (Adobe/DALL·E, generic wearables, Brex) got users _in the door_. Only the product with a compounding investment layer **made the exit door heavier with every session**.

### How to Build It

- [ ] **Map the investment loop.** For every core action ask: does this make the product better _for this specific user_, or just better in general? General = you're shipping features, not stored value.
- [ ] **Find the compounding action** — your equivalent of Midjourney's ranking — and make it **frictionless**.
- [ ] **Automate the deposit.** The strongest loops never ask the user to consciously invest; every transaction, generation, or night trains the model on its own.
- [ ] **Make the investment visible.** Show the growing corpus ("1,095 nights tracked"). Seen investment reads as **partnership**, not entrapment.
- [ ] **Count your integration roots.** Every external system wired in (accounting, HR, calendar, Slack) is one more reason leaving hurts.

### Two Questions That Test For It

1. **The compounding question:** does session 1,000 give measurably better results than session 10? If they're identical, you have great engagement and _zero_ investment layer.
2. **The exit question:** if a user left for a competitor today, what would they rebuild from scratch? If "not much," the intelligence layer isn't there yet.

> ⚠️ Keep it honest. The healthy version is **compounding user value the user can see and benefit from** — not a dark pattern that hoards value to trap them. Visible, genuinely personalized intelligence retains; hidden hostage-taking churns the moment a better option appears.

---

## 9. Product Signals

### Positive Signals

| Signal                           | Meaning                                          |
| -------------------------------- | ------------------------------------------------ |
| Product offends someone          | Probably one version away from something special |
| High retention in small niche    | Ready to expand                                  |
| Organic growth without marketing | Product-market fit emerging                      |
| Long-term users outperform new ones | Investment layer is compounding — the moat is tightening |
| Users compete in small local pools | Winnability is engineered, not left to chance (Section 7) |
| A mechanic was removed and users complained | It had stopped being a scoreboard and become part of their identity |

### Warning Signs

| Signal                                        | Action                                  |
| --------------------------------------------- | --------------------------------------- |
| 6 months without testing on external audience | You're probably in for a rude awakening |
| Need nationwide launch to test                | Redesign the test                       |
| Depends on a partnership                      | Abandon or rethink                      |
| Repeated inconclusive tests                   | Stop everything and fix methodology     |
| Session 1,000 feels the same as session 10    | No investment layer — a shiny competitor away from churn |
| A streak is the primary retention mechanic    | Obligation risk plus regulatory exposure. Add agency or add a second engine |
| Five or more game mechanics stacked           | Past the S-curve peak. Cut before adding |
| Every mechanic measures attendance, none measures skill | Recognition without mastery. Build a competence signal |

---

## 10. Epistemic Humility

### About This Document

- Every blockbuster product is an outlier
- Breaks the rules
- May have been the result of luck or timing

### What You Can Do

1. Get to know your user better than anyone else
2. Trust your instincts
3. Iterate rapidly

### Final Warning

Very few people in this industry have seen the inflection point of product-market fit firsthand. Even for the founders who have seen it, take their advice with caution—**including all the suggestions in this list**.

---

## Quick Checklist for Feature Approval

Before starting any development, the feature must pass this filter:

- [ ] Does it solve one of the 3 core needs (love, money, play)?
- [ ] Do we have a defined distribution channel?
- [ ] Can it be tested in a small scope (one community)?
- [ ] Does it work in the "toilet/distracted" context?
- [ ] Does it contribute to an engagement loop (1 session → 7 people)?
- [ ] Does it generate content that can appear on other networks?
- [ ] Does it NOT depend on an external partnership?
- [ ] Can we measure success/failure conclusively?
- [ ] Does it deepen a per-user intelligence the user can't export (investment layer)?

**If it doesn't pass at least 7 out of 9, reconsider before proceeding.**

**Extra gate, only if the feature adds a game mechanic:** it must also clear all five
questions of the Mechanic Test in Section 7 (game or scoreboard, winnable, where on the
S-curve, which engine, skill or attendance). This one is pass-all, not 7-out-of-9. A
mechanic that fails any of the five is theater, and theater costs the same to build.

---

_Mandatory reference document for Product, Design, and Development teams._
