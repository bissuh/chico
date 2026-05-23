# TBP Faceless Gallery Engine: Operating Playbook

TBP's own no-face Instagram + TikTok engine. We dogfood the `ghostshelf` skill in public: post value carousels/slideshows atomized from our newsletter, funnel to the newsletter and the free skills, show every number, and feed what we learn back into the skill and the article.

Origin: built 2026-05-23 alongside the `ghostshelf` skill and the 2026-05-25 edition. Research basis: `knowledge-base/faceless-gallery-model/research-dossier.md`. Sister engine to `playbooks/youtube-shorts-cta-machine.md`.

---

## Why we run this

- **Distribution is TBP's actual bottleneck.** The newsletter is bleeding net subs (acquisition < churn); YouTube has reach but ~0 trackable conversion. The faceless gallery engine is a top-of-funnel acquisition channel we control.
- **It proves the thesis.** A regular operator building real distribution with AI, no face, in the open. If it works, we have proof. If it flops, readers are spared the trouble. Either way it is content.
- **It dogfoods Ghostshelf.** We cannot honestly sell a skill we have not run ourselves.

## The page (identity)

- **Handle:** `@thebillionperson` on Instagram and TikTok (match the YouTube handle). Confirm availability at creation; fallback `@the.billion.person`.
- **It is openly TBP.** Faceless = no-face content (gallery slides, no talking head), not hidden ownership. This keeps it consistent with build-in-public.
- **Bio:** who it helps + what they get + one clean direct link. Draft: "Build a real business with AI. No code, no face required. Free weekly playbook ↓" + link. No URL shorteners (shadowban trigger).
- **Link in bio:** newsletter opt-in first, skills second. Use UTMs: `https://join.thebillionperson.com/?utm_source=instagram&utm_medium=bio&utm_campaign=faceless` (and `utm_source=tiktok`). This is also how we finally attribute social-driven signups.

## The shelf (what we sell)

1. **Primary:** the free newsletter (owned audience, the only platform-proof asset).
2. **Lead magnets:** the free skills in the public repo (Ghostshelf, gbp-audit, etc.).
3. **Later:** a low-ticket paid product (a template/guide), once we see which topics convert. This is when we become a true Ghostshelf case study with our own revenue number.

## Visual system (two systems, simplest wins)

The brand constant is the teal (#2A7A6D family), the type system, and a small subtle handle tag. We do NOT make every slide a magazine cover. The content is the design.

**1. Clean editorial (DEFAULT, `remotion/src/CleanSlide.tsx`).** Type-driven, no heavy photo. **Default theme: solid brand green #2A7A6D background, white text, simple readable font.** Layouts: `cover`, `list` (Top X, numbered), `prompt` (steal-this monospace card), `statement`. Type: **Inter** (headlines heavy weight + body, kept simple and readable, no condensed display face) + JetBrains Mono (prompt cards). Small handle tag bottom-corner, not a lockup. Dark and light themes exist as occasional alternates, but green is the brand default. Drawn entirely in React/CSS, no Midjourney/Canva.

**2. Dore cinematic (`remotion/src/CarouselSlide.tsx`).** The engraving + teal wash hero look. Reserve for occasional cover/manifesto moments, not everyday value drops. Backgrounds are the only Midjourney-dependent input (reuse/expand the `remotion/public` library).

Rule: most posts use the clean system. The Dore look is a special-occasion accent, not the baseline. Simplest template that lands the idea wins.

## Content engine

- **Source = the weekly distill (part of the article workflow, not a separate task):** every week, when the newsletter edition + its research are produced, also distill **3 to 10 STANDALONE carousel posts** from that same research. Each is its own original value (a tip, a list, a prompt, a step, a number), written fresh. They do NOT reference or say "read our newsletter", they stand alone. We already did the research, so we write new content from it. Angle-shift across the batch (data / story / tactical / list / prompt) so they never look same. This is a required output of producing the weekly article. Back catalog is months of additional fuel.
- **DEPTH STANDARD (non-negotiable).** A carousel is a complete, genuinely useful mini-guide, NOT thin one-liners. Rules:
  - **10-15 slides** for a real teaching post (not 3-4). Use the `detail` layout for real paragraphs, the `prompt` layout for actual copy-paste prompts.
  - **Every slide earns its place:** one real idea with a paragraph, a concrete example, a number, a named tool, or a real prompt. If a slide says nothing a stranger can act on, cut it.
  - **Name real things.** Actual tools (Claude, Canva Bulk Create, Remotion, Postiz), actual steps, actual prompts people can paste. Show the part most guides skip.
  - **Titles stand alone.** A cold viewer who never saw our newsletter must get value and want to save. No insider references ("this week's keepers", "the Monday post"). Slide 1 = tension + payoff promise, not a flat headline.
  - **Self-complete test (apply to every carousel):** if someone read ONLY these slides, with no caption and no newsletter, would they know exactly what to do, with no missing step, tool, or prompt? If they'd still have questions, it isn't done. Add the missing slide.
  - **When teaching the content/build workflow, show the AI-native stack: Claude Code + Remotion + Postiz**, not Canva. (Canva stays in the public `ghostshelf` skill as the non-technical fallback. Our own posts teach the "build it with AI" path.) Explain unfamiliar tools inline with a small tip box (`tip` / `tipLabel` in CleanSlide).
  - **Last slide invites engagement:** ask for a save AND a comment ("Stuck on a step? Ask in the comments, I answer every one"). Comments are a strong reach signal and the questions feed next week's content.
  - Someone should finish the carousel and be able to DO the thing. That is the micro-magnet bar.
- **Slide skeleton (inside the depth standard):** Hook (tension, readable <2s) → promise → real value slides (one substantive idea each) → CTA (save + send + bio).
- **Cadence: 7 posts/week, 1 per day**, each cross-posted to IG + TikTok (automated, so weekends count). Format split ~4 carousels + 3 Reels.
- **Sourcing is WEB-FIRST.** Roughly 4-5 of the 7 posts come from fresh web research each week (the live hot lists, what is spiking in AI/indie hacking, new prompts). Only ~2-3 come from the newsletter distill. Do NOT default to recycling our own posts; go pull hot content. Refresh the research weekly, do not reuse last week's lists.
- **The 7-day lineup (one named recurring segment per day, builds habit):**
  1. **Mon: The Stack** — Top 5/10 (tools / skills / niches, rotating). List carousel. Drives saves + comments. Web.
  2. **Tue: Steal This Prompt** — prompt of the week. Prompt card carousel. Drives saves (highest) + opt-in. Chico/web.
  3. **Wed: Built With AI** — a real person who built a business/tool with AI. Case-study carousel. Drives saves + trust + completion. Web + our anchors. (Most on-thesis: "if they can, I can.")
  4. **Thu: Do This Today** — one concrete money task, step by step. Tutorial carousel. Drives saves + "I can do this." Our expertise + web.
  5. **Fri: Hot Take Friday** — myth-bust / contrarian on what is spiking. Reel. Drives sends + comments (reach). Web.
  6. **Sat: This vs That** — X vs Y decision, or a tier list. Reel. Drives sends + debate (reach). Web.
  7. **Sun: The Sunday Drop** — week recap + the newsletter distill. Reel or carousel. Drives habit + loops back to the newsletter. Newsletter + web.

  Logic: Mon-Thu are save-formats (carousels, convert/reference), Fri-Sat are send-formats (Reels, cold discovery), Sun is the habit anchor. Web-first (Mon/Fri/Sat + most Wed pull fresh research weekly). Content bank seed: `outbox/faceless-launch/editorial-content-bank.md`. All original editorial we compile, never reposts.
- **Captions:** keyword in the first sentence (both platforms are search engines), 3-5 relevant hashtags only, alt text on IG. Last slide + caption ask for the SAVE and the SEND (top 2026 reach signals).

## Pipeline + tooling (validated 2026-05-23)

TBP renders slides AND Reels in **Remotion** (`remotion/`), not Canva. We control it end to end: exact brand green #2A7A6D, simple Inter type, white text. The default `CleanSlide` composition (green theme, 1080x1350) outputs editorial slides; `CarouselSlide` is the Doré cinematic alternate; Reels render to 1080x1920. Proven 2026-05-23: green editorial samples in `remotion/out/green-*.png`, zero Midjourney/Canva dependency.

1. Claude writes the slide copy for the chosen format.
2. Remotion renders the slides as PNGs and Reels as MP4 (one idea -> carousel + Reel).
3. **Backgrounds are the only input that benefits from Midjourney.** Reuse/expand a small Doré background library (currently bg1-3 in `remotion/public`). New ones: MJ prompts (Bissuh runs them, no MJ API) or Canva/Postiz image gen. Everything else is code.
4. **Postiz schedules** to IG + TikTok (connected from the CTA machine; Bissuh connecting @thebillionperson; verify TikTok photo-carousel support in-app, else Metricool/Later).
5. Ledger tracks each post + its numbers.

(Note: the public `ghostshelf` skill recommends Canva Bulk Create instead, since readers will not have our Remotion setup. Remotion is TBP's internal edge.)

## Cadence + the weekly read

Weekly: post the batch, reply to every comment/DM, read three numbers only:
- **Saves + sends per post** (is it worth keeping/sharing).
- **Profile visits → bio clicks** (is the hook earning curiosity).
- **Newsletter opt-ins (UTM-tagged) + any sales** (is it converting).

Then act: keep the post styles that earn saves/sends, cut the rest, ship the next batch.

## Account-setup checklist (Bissuh, one-time)

- [ ] Create IG `@thebillionperson`, TikTok `@thebillionperson` (confirm handles).
- [ ] Set profile image (TBP mark), bio (above), bio link with UTM.
- [ ] Connect both to Postiz.
- [ ] Confirm Account Status is clean (IG Settings → Account → Account Status).
- [ ] Tell Chico the live handles so we wire them into the article + bio links.

## Learnings log (living: this is the loop)

We update the `ghostshelf` skill and the article from what we learn here. Hypotheses to test in the first 30 days:
- Which hook type earns the most saves (contrarian "you don't need a face" vs numbers "$10K/mo" vs how-to)?
- Do TikTok slideshows out-reach IG carousels for our niche, as the research suggests?
- Does the engraving look help or hurt swipe-completion vs plain high-contrast text?
- Real opt-in conversion from bio (the dossier could only find directional numbers).

Log dated entries here as results come in. When a finding is solid, push it into `skills/ghostshelf/SKILL.md` and the next edition.

## Honest expectations

Expect a 2-4 month slow ramp. Judge on saves/sends + opt-ins, not follower count. If 8 weeks of genuinely useful posting yields no saves/opt-ins, the niche or the hook is wrong, not the algorithm.
