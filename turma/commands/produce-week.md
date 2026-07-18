---
description: Produce a week of content for the current project, mapped to the channels in its brand.md, drafted and voice-checked.
---

Produce a week of content for the current project.

1. Read `brand.md` (`./brand.md` or `./growth/brand.md`) for voice, audience, primary conversion goal, and the priority channels. If none exists, run `turma:positioning` (INTAKE mode) to bootstrap and write `./growth/brand.md` first; don't ask the owner to create the file.
2. Pick the week's core story or angle (use `turma:story-craft`). One core idea waterfalls across channels. Don't invent seven unrelated pieces.
3. Draft the week mapped to the brand.md channels. For each piece: the channel, the hook, the body, and the coupled CTA toward the primary conversion. Apply the `turma:power-law` barbell (a couple of craft bets, the rest fast volume tickets).
4. Run `turma:anti-ai-linguo` on every piece as the final pass. No dashes, no AI tells, in the project's voice.
5. Drop the week in `outbox/` with `status: review-needed`. This is Yellow: the owner approves before anything ships.

Note which piece is the craft bet, which are volume tickets, and which one you'd double down on if it hits.

$ARGUMENTS
