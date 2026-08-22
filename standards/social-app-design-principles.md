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

> Retention has two layers: **engagement** (this section) keeps users running; **investment** (Section 7) is what stops them jumping to a newer treadmill. You need both.

---

## 7. The Investment Layer (Intelligence Lock-In)

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

## 8. Product Signals

### Positive Signals

| Signal                           | Meaning                                          |
| -------------------------------- | ------------------------------------------------ |
| Product offends someone          | Probably one version away from something special |
| High retention in small niche    | Ready to expand                                  |
| Organic growth without marketing | Product-market fit emerging                      |
| Long-term users outperform new ones | Investment layer is compounding — the moat is tightening |

### Warning Signs

| Signal                                        | Action                                  |
| --------------------------------------------- | --------------------------------------- |
| 6 months without testing on external audience | You're probably in for a rude awakening |
| Need nationwide launch to test                | Redesign the test                       |
| Depends on a partnership                      | Abandon or rethink                      |
| Repeated inconclusive tests                   | Stop everything and fix methodology     |
| Session 1,000 feels the same as session 10    | No investment layer — a shiny competitor away from churn |

---

## 9. Epistemic Humility

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

---

_Mandatory reference document for Product, Design, and Development teams._
