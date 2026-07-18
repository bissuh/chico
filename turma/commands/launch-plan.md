---
description: Build a launch plan for a new product or feature. Reads brand.md and produces a pre-launch, launch, and post-launch sequence with content and CTAs.
---

Build a launch plan for the current project's new product or feature.

1. Read `brand.md` (`./brand.md` or `./growth/brand.md`) for voice, audience, primary conversion goal, channels, and the offer. If none exists, run `turma:positioning` (INTAKE mode) to bootstrap and write `./growth/brand.md` first; don't ask the owner to create the file.
2. Confirm what's launching (ask the owner one question if it's thin): what it is, who it's for, when, and the one action you want people to take.
3. Produce the sequence:
   - **Pre-launch:** build anticipation. Waitlist or handraiser (use `turma:micromagnet-craft` if a lead magnet fits), teasers, the story (use `turma:story-craft`).
   - **Launch:** the announcement across the brand.md channels, each with a coupled CTA. The email or post that does the actual selling.
   - **Post-launch:** follow-ups, social proof, last call, and what to do with the people who didn't convert.
4. Give a simple day-by-day timeline and name the one metric that says the launch worked (from brand.md).
5. Run `turma:anti-ai-linguo` on the copy. Drop the plan in `outbox/` with `status: review-needed` (Yellow).

$ARGUMENTS
