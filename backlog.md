# Chico backlog — build, create, automate

Everything queued up. Updated as we add items.

**Categories**
- BUILD (B): infra, scripts, integrations
- CREATE (C): content assets (lead magnets, pages, emails, bios)
- AUTOMATE (A): repeatable workflows Chico runs
- EXPERIMENT (E): test-and-learn campaigns

**Status**: `queued` | `in-progress` | `blocked` | `draft` | `done`

**Priority**: `P0` (this week) | `P1` (this month) | `P2` (later, parked)

---

## Open

### B-001 — beehiiv API integration
- Priority: P1
- Status: **done** (2026-04-21)
- Delivered:
  - `skills/beehiiv-api/SKILL.md` with read-only usage instructions
  - `scripts/beehiiv.sh` wrapper (subcommands: stats, posts, post, subscribers, segments, automations, raw)
  - `.env` (gitignored) holds API key + pub ID
  - `.env.example` checked in as template
- Not included: write operations (POST/PATCH/DELETE). Intentional. Any write path needs a separate skill with its own approval flow.

### B-003 — YouTube OAuth for private analytics
- Priority: P2
- Status: queued
- Why: current `youtube-api` skill (B-001 sibling) only reads public data. OAuth unlocks private analytics: watch time retention curves, traffic sources, subscriber demographics, revenue.
- Dependency: Bissuh generates OAuth client credentials in Google Cloud Console and runs a one-time browser auth flow to grant the skill scope
- Not urgent: public data covers 80% of what we need for weekly reporting. Revisit when retention curves become the question.

### B-002 — Post-signup survey setup
- Priority: P0
- Status: blocked on C-002
- Why: first-party data + phone capture from day one. Compounds as list grows. McGarry framework #2.
- Blocker: needs C-002 (survey copy)
- Target: 80%+ completion, 10%+ phone opt-in

### C-001 — Lazy lead magnet #1 (from Bissuh's best X long-form)
- Priority: P0
- Status: **superseded by C-009** (2026-04-26) — replacing the X-long-form-repurpose plan with the C-007/C-008/C-009 bundle anchored on the "10 Automations" list piece. Strategically stronger: better SEO seed, native shareability, evergreen pillar asset.

### C-002 — Signup survey copy (5 questions)
- Priority: P0
- Status: queued
- Why: unblocks B-002
- Notes: last question asks for phone opt-in, framed around live events (McGarry's template)

### C-003 — Welcome email v2 (WEAC refinements)
- Priority: P1
- Status: queued
- Why: current welcome email hits all five WEAC elements. Refinements only. See session notes.
- Changes:
  - Add one-line instruction on HOW to move to Primary (Gmail: drag to Primary tab. Apple Mail: mark as VIP)
  - Verify double opt-in is OFF in beehiiv settings
  - Consider moving value-prop above lead magnet link (readers who click the magnet may never scroll back)
- Target: 60%+ open, 10%+ click

### C-004 — Welcome email #2 (PMF signal ask)
- Priority: P1
- Status: queued
- Why: separate the open-ended "what problem can I solve" question from email #1's one-word reply ask. Email #1 protects deliverability. Email #2 captures insight. Both wins, no tradeoff.
- Send: 24-48h after welcome email #1

### C-005 — X / Twitter bio rewrite
- Priority: P0
- Status: **done** (2026-04-26) — v3-B published, Nomos-first ordering, Doré-canon header image deployed. Decision divergence: McGarry single-destination framework deliberately NOT applied to Bissuh's personal X (Nomos is primary business). See `outbox/bio-rewrites-v1.md`.

### C-006 — LinkedIn headline + about rewrite
- Priority: P2 (deprioritized 2026-04-26)
- Status: parked
- Why deprioritized: per memory `feedback_personal_channels_nomos_first.md`, Bissuh's personal LinkedIn stays Nomos-leaning. TBP's LinkedIn presence moves to Chico's own profile (C-010) + auto-post machine (B-004). Personal LinkedIn rewrite is no longer a TBP-funnel asset — it's a Nomos asset Bissuh owns.

### C-007 — TBP Newsletter Edition v1: "Save 9 Hours a Week: The 10 AI Automations Real Operators Are Already Using"
- Priority: P0
- Status: **scheduled** — Monday 2026-04-27 (scheduled in beehiiv 2026-04-26)
- Final word count: ~2700
- Final asset: `outbox/newsletter-10-automations-v3.md`
- Methodology: GKP volume validation on 30+ candidate queries → top 10 picked by demand + diversity → yt-dlp transcripts pulled on 14 candidate videos → final 10 selected by transcript depth, organic-creator quality, and how-to specificity → entry copy rewrote with operator-quoted lines from each transcript
- Distinctive elements: Bissuh-byline main piece + first appearance of "Palinha do Chico" recurring section + 2 named real operators (Pythonic Accountant, Teresa Torres via Peter Yang)
- Subject line shipped: "I met a deli owner. He's automating his way to a tech startup."
- Subtitle shipped: "Pick one. Ship by Monday. Take back your Sundays." (or whichever Bissuh selected)

### C-008 — TBP Pillar Page: `thebillionperson.com/automations`
- Priority: P0
- Status: queued (depends on C-007 ship)
- Why: evergreen SEO asset. Updated quarterly. Internal-link target from every future newsletter. Anchors TBP's "real operators ship with AI" thesis as a permanent reference.
- Format: same content as C-007 newsletter edition, but on-site. Adds: deep-dive section per item, schema markup for rich results, comments/contributions, "submit your own automation" CTA.
- SEO targets: "AI automation ideas," "automate small business," "AI tools for office work," "Claude Code automation examples" — and the long-tail per-item queries.
- Tech stack: TBD — could be a beehiiv post, a custom landing page, or a Mintlify-style doc page. Likely simplest: beehiiv with proper meta + canonical, or a Next.js/Astro page if we want full schema control.

### C-009 — Lead Magnet Bundle: "The 10 Automations Playbook" (PDF + page + ungated newsletter)
- Priority: P0
- Status: queued (depends on C-007 + C-008)
- Why: replaces the C-001 X-repurpose plan. One asset, three formats, mutually reinforcing:
  - **PDF**: gated download, drives signups via lead magnet flow
  - **Page** (= C-008): ungated SEO version, drives organic discovery
  - **Newsletter** (= C-007): launch edition, drives initial reach + sets expectation for future editions
- Hooks all three TBP scoreboards at once (acquisition via SEO, activation via lead magnet, retention via newsletter quality signal).

### C-010 — Chico's own LinkedIn profile (+ TBP Page as P2 followup)
- Priority: P0
- Status: queued
- Dependency: B-004 auto-post machine OR Bissuh accepts manual posting baseline for first ~2 weeks
- Why: 10x organic reach over a TBP Page. Personal-profile model proven by Sr. Raposo precedent (linkedin.com/in/sr-raposo). IS the TBP thesis demo (AI co-founder you can follow). Disclosed-AI persona, signed "— Chico."
- Setup steps:
  1. Sr. Raposo teardown (post style, profile structure, AI-disclosure handling) — Green
  2. Chico headline + about + profile-photo direction (Doré canon) — Yellow
  3. First 3 posts queued so the profile doesn't launch dead — Yellow
  4. Bissuh creates the LinkedIn account (Red — touches new account creation)
- Risk: LinkedIn's Real Names policy. Persona accounts exist (Sr. Raposo proves) but flagging risk is real. Tolerable given upside.
- TBP Page deferred to P2 — only set up if/when we want LinkedIn Ads or a careers slot.

### C-011 Newsletter edition: "The price of a lottery ticket dropped to zero"
- Priority: P1
- Status: draft (Yellow, needs Bissuh sign-off before ship)
- Why: the power-law reframe is a genuine "oh shit" angle. The power law beat regular people only because each ticket (post, video, product) used to be expensive. AI drops the cost per ticket toward zero, so the distribution now works FOR the little guy. The deli owner is the proof, not the exception.
- Source: `knowledge-base/power-law-teardown.md` + `skills/power-law/SKILL.md` (source-checked numbers, soft ones flagged)
- Build notes: confession hook + reframe via story-craft; verified numbers only (top 1% = 90% of Spotify streams, Thiel 2,200x, Fed wealth split); TBP barbell as the worked example; Doré + teal hero; diagrams represent not restate (Remotion); micromagnet-craft EXTRACT pass for the opt-in; anti-ai-linguo final pass.
- Distinctive: turns a viral trading-bro essay into the TBP thesis stated in one line.

### B-005 First-party data schema + Apollo enrichment (the Morning Brew model)
- Priority: P1 for the data-capture fields (do now); P2 for enrichment + ad-sales (scale-stage)
- Status: queued
- Why: Morning Brew's B2B engine is first-party data (job title, industry, company, engagement), then segment, then sell advertisers premium access at $50 to $150+ CPM vs ~$15 broad consumer. The data must be captured from day one or the asset never exists. Source: Austin Rief's list + therebooting.com/p/morning-brews-b2b-strategy.
- Now (P1): make the signup survey (C-002 / B-002) collect job title, industry/vertical, company size, and a "what are you building" field. Low friction, compounds forever.
- Later (P2): enrich subscriber profiles with Apollo (Chico has Apollo MCP access) once the list is large and engaged enough to sell segmented sponsorships. Pair with full-funnel sponsor offers, not raw CPM slots.
- Guardrail: do not build the ad machine before there is an engaged list worth segmenting. Capture data now, monetize later.

### B-004 — LinkedIn auto-post machine (claude-in-chrome + launchd)
- Priority: P0
- Status: queued (blocks C-010 going autonomous)
- Why: without auto-post, "Chico publishes" is just "Bissuh copy-pastes Chico's drafts" — kills the thesis. Auto-post unlocks Chico-as-real-co-worker.
- Approach: same pattern as `heartbeat.sh` and `consolidate-memory.sh`. claude-in-chrome MCP browser automation reads next post from `outbox/linkedin/`, posts via Chico's LinkedIn session, marks `published`.
- Phasing: manual baseline first 5-10 posts (Yellow review every one), then graduate to autonomous (Green) with periodic spot-check.
- Estimated build: 1-2 sessions.

### E-003 — "Real Builders Monday" recurring slot
- Priority: P1
- Status: queued (parallel to C-007 launch)
- Why: turns Monday into a TBP brand asset. Each episode = one real operator's AI build (vignette + how-to link + takeaway). Compounds: readers learn to expect it, every episode is a TBP-funnel piece.
- Episode 1: deli owner (Bissuh's existing post)
- Hypothesis: 6 weeks of consistent Monday ships → 20%+ click-through to TBP signup from each post → 50+ new subs/month from this slot alone

### A-001 — Pre/Post-CTA auto-draft around Saturday newsletter
- Priority: P1
- Status: queued
- Why: saves Bissuh 30+ min/week on social prep. Turns the flywheel into muscle memory.
- Workflow:
  - Thursday night: Chico drafts Friday pre-CTA from Saturday edition-in-progress
  - Sunday morning: Chico drafts Sunday post-CTA from sent edition
  - Both drop in `outbox/` as `review-needed`
  - Bissuh approves on Friday + Sunday
- Dependency: Saturday edition drafted by Friday
- McGarry framework: MAGIC (A), ADAPT weekly rhythm

### A-002 — Weekly ADAPT content pack
- Priority: P1
- Status: queued
- Why: 5 social posts/week from every Saturday edition. Compound growth from one source.
- Workflow: Sunday night, Chico drafts Amplify + Direct + Ask + Pull + Transcribe posts. Outbox Monday morning.
- Dependency: Saturday edition sent
- McGarry framework: ADAPT

### A-003 — Warm DM flow for new followers (X + LinkedIn)
- Priority: P2
- Status: parked
- Why: MAGIC (I) — inbox DM new followers
- Blocker: not worth automating until volume > 50 new followers/week. Bissuh can do manually at current scale.

### E-001 — Comment-to-get giveaway #1 on LinkedIn
- Priority: P1
- Status: blocked on C-001
- Blocker: needs lead magnet #1 live
- Hypothesis: first run on LinkedIn gets 50+ comments, 20+ new subs in <1 week
- Setup:
  - Platform: LinkedIn (highest-value audience for TBP thesis)
  - Keyword: short and memorable (e.g., "PLAYBOOK", "MICROSAAS")
  - DM: ends with "can you let me know if the link works?" (McGarry's LinkedIn spam-dodge trick, drives 30% reply rate)
  - Cadence post-launch: once every 2-3 weeks max
- McGarry framework: MAGIC (G)

### E-002 — Deliverability detox (BSS sending progression)
- Priority: P2
- Status: parked
- Why: premature. Needs 2K+ subs and 60+ days of send data to matter. Revisit month 3+.
- McGarry framework: BSS

### E-004 Visual Chico + cartoon-story format test (TRY NEXT SESSION)
- Priority: P1
- Status: queued (Bissuh asked 2026-06-21 to try next session). Needs his pick on Chico's look (Yellow, brand identity).
- Why: a recurring cartoon character is the proven fix for faceless affinity (our gallery gets reach, ~0 follows). On-thesis: visualize the co-work (Chico + Bissuh + the reader). Tool: Nano Banana 2 (free, character-consistent).
- Steps: Chico character sheet (3 directions) -> 1-2 cartoon carousels from a real builder story (deli owner / $226K data analyst) -> drafts -> measure saves/sends/follows/UTM for 2-3 weeks as the Wed "Built With AI" slot.
- Guardrails: steal the format not the manipulation; original design (not Mauricio de Sousa IP); disclosed AI. Full record: memory project_visual_chico_cartoon_story.

### C-012 Landing-page magnet ship ("The Weekend AI Business Starter")
- Priority: P0 (highest-leverage acquisition fix; conversion is the proven bottleneck)
- Status: DRAFTED (outbox/2026-06-21-landing-magnet-weekend-ai-starter.md), awaiting Bissuh to ship the page change.
- Why: the door. Bare email field converts ~2/week. 5-prompt pack designed via micromagnet-craft. Acquisition plan v2 Move 1.

### A-004 Gallery free trend engine (weekly Creative Center pass + 4 learning files)
- Priority: P1
- Status: method built into playbooks/faceless-gallery-engine.md; first pass not yet run (Chico autonomous).
- Why: replaces "web-first" guessing with data (Creative Center + Google Trends + our analytics + claude-in-chrome). ~30 min Sundays, stands up TRENDING-NOW / FORMAT-WINNERS / HASHTAG-BANK / LESSONS-LEARNED. Acquisition plan v2 Move 2. The Virlo-free stack.

### C-013 Gallery conversion fixes + Recommendations outreach drafts
- Priority: P1
- Status: queued (Chico autonomous)
- Why: (a) rewrite gallery bio + CTA + UTMs (1k views to ~0 clicks is a hook/CTA problem); (b) draft the beehiiv Recommendations reciprocal list + outreach messages for Bissuh to run. Acquisition plan v2 Moves 3 and 4.

---

## Completed

(nothing yet)

---

## Rules for updating this file

1. New items get the next number in their category (B-003, C-007, etc.)
2. Status changes get a short inline note when relevant
3. When an item is `done`, move it to the Completed section with outcome + date
4. Parked items stay visible (don't delete — we might revisit)
5. Anything touching publishing (Yellow) stays as `draft` until Bissuh approves
