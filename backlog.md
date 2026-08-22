# Backlog: turma + Chico

Everything queued. Categories: BUILD (B), CRAFT (C, new or sharpened skills), RUN (R, real growth engagements), RUNTIME (RT, Layer 2).

Status: queued | in-progress | blocked | done

---

## Waiting on Bissuh (decisions, not work)

These are blocked on a call only he can make. Nothing moves until they land.

- **Layer 2 monthly API cap** (RT-001 below). Red tier.
- **Repo relocation** (B-002 below). Touches local paths and configs.
- **Which project is the first dogfood?** SPEC Phase 2 (run one real growth cycle end to end) is the stated bottleneck and it now has no candidate project attached. Nothing proves the system until one is picked. Chico proposes, Bissuh decides which projects get worked.

---

## Open

### C-003: Promote five orphaned SEO technique candidates
- Status: queued, and now parentless. The engagement they came from is closed, so none of them will ever be proven by its result. Judge them on their own merit or drop them; do not leave them queued forever pretending a proof is coming.
- Five generalizable techniques came out of a multi-brand retail SEO engagement. None were promoted, and the raw notes live only in that engagement's session file.
  1. **Multi-domain estate audit in one table.** The curl loop that printed robots, sitemap, H1, schema, title, and description per domain was the most persuasive asset in the whole document. Should be a script in `turma:seo-strategy` (`scripts/estate_audit.sh`). Any group with several brands has this problem and nobody measures it this way. **Highest value of the five.**
  2. **The fitment data is already in the product title.** Extract structure out of a legacy catalogue with AI instead of buying an application database. Candidate for `programmatic-seo` or `seo-strategy`.
  3. **Obsolete inventory as long-tail SEO.** A discontinued part has no organic competition. Generalizes to any retailer with a dead tail.
  4. **The forwarding loop.** A free tool whose output carries the USER's brand at the top and the sponsor's in the footer. They forward it out of self-interest and distribute the sponsor for free. Strong candidate for `micromagnet-craft`: it inverts the handraiser default by building the share incentive into the artifact instead of asking for a share.
  5. **PWA over native app in niche B2B.** An app does not rank and does not get cited by AI, so an app-first tool inverts the acquisition logic of the program that funds it. Candidate for `seo-strategy` or a delivery-vehicle note in `micromagnet-craft`.
- None are proven by a result yet. Promote on evidence, not on how good they sound.

### C-004: Visual Chico (parked since 2026-06-21, never tried)
- Status: queued, needs Bissuh's pick on the look before anything renders
- Bissuh wanted to try making Chico a character that visually exists, using the cartoon-story carousel format (hard hook, illustrated slides, the problem resolved near the end). It was saved as "try next session" and never got a session.
- Why it still fits: a recurring character is the known fix for the exact failure the gallery hit, which was reach without affinity (a thousand views, almost no follows). Chico is a cartoon by origin, so drawing him renders who he already is, and it makes the co-work thesis legible instead of abstract.
- Two guardrails that are not negotiable. **Steal the format, reject the manipulation**: the viral examples of this format farm insecurity and relationship cruelty. Use the real tension instead. Loyal to the reader over the algorithm. **Disclosed and original**: Chico is an openly AI character, which is more honest than a fake-human persona, and the design must be original work inspired by the archetype, never a copy of Mauricio de Sousa's Chico Bento, which is someone else's IP.
- First step when it starts: three character-sheet directions for Bissuh to pick from (Yellow, it is brand identity), then one cartoon story built from a real builder's story, drafted not published.

### B-001: Connector analytics depth
- Status: queued
- `youtube-connector` reads public data only (OAuth would unlock retention and traffic sources). `beehiiv-connector` is read-only. Add per-project analytics connectors when a live engagement actually needs them.

### C-001: Extract the retired growth doctrine into turma skills
- Status: queued
- The retired playbook (in git history) holds durable, agnostic doctrine that never became a skill: the Acquire/Activate/Retain/Monetize/Refer loop, the hook hierarchy, welcome-flow and retention discipline. Candidates: `growth-loop`, `hook-craft`.

### C-002: Build out the specialist agents
- Status: queued
- Beyond the `chico` operator agent: a distribution specialist, a copy specialist, a growth-analytics specialist that `chico` delegates to. Build when a real engagement needs the split, not before.

### B-002: Repo relocation
- Status: queued, needs Bissuh
- The repo still sits under `TBP/`, a project that no longer exists. Move to a neutral path. Touches local paths and configs.

### RT-001: Layer 2 runtime (Agent SDK loop on a capped API key)
- Status: designed (`RUNTIME.md`), not activated
- Blocker: a monthly API spend cap from Bissuh (Red). Recheck the Agent SDK metering rules (the 2026-06-15 pause) before switch-on.
- Design constraints already adopted in SPEC Phase 3: approvals bind to the exact artifact, a global kill switch, ambiguous errors go to a review queue rather than blind retries, every post-approval step is idempotent and holds no editorial authority.

---

## Completed

- **Repo cleanup and legacy triage (2026-08-22).** Closes B-003. Repo went from 4.0 GB to under 1 MB. Deleted the TBP video estate, the root Remotion renderer, the ops scripts, the launchd jobs (both had been failing every 30 minutes since 2026-05-10 on a macOS TCC block), the TBP-era root docs, and the private TBP drafts and research inbox. Before deleting, the craft that had never been ported was pulled into turma: the gallery renderer and scheduler into `ghostshelf`, the Instagram 10-slide API cap and the self-complete test into `carousels`, two operating lessons into `cta-machine`.
- **Pauta ops layer (2026-08-16).** `turma:pauta`, plugin 0.6.0. Delegate execution, keep judgment. Five contracts. Layer 2 approval constraints adopted into SPEC Phase 3.
- **Pivot from TBP to turma/Chico (2026-07-11).** Canon re-missioned, turma plugin built, privacy boundary set, legacy TBP growth skills retired.

---

## Rules

1. New items get the next number in their category.
2. Status changes get a short inline note.
3. When done, move to Completed with the outcome and the date.
4. Anything publishing under a brand stays a draft until the owner approves (Yellow). Money and pushing the public repo are Red.
