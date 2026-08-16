---
name: carousels
description: Generate social carousels (Instagram, LinkedIn, TikTok slideshows) from a topic or a source piece. Invoke when someone asks to "make carousels," "generate N carousels for social," "turn this into a carousel," "carousel for the launch," or wants swipe-through slide content. Produces deep, standalone mini-guides in the project's voice, not thin one-liners. Reads brand.md.
---

# carousels

Generate scroll-stopping social carousels that are actually useful. A good carousel is a mini-guide someone saves and sends to a friend, not a thin list of one-liners.

**Before you start:** read the project's `brand.md` for voice, audience, the splinter, the primary conversion goal, and the channels.

## The depth standard (do not violate)

A carousel goes deep or it does not ship.
- 8 to 12 slides (up to 15 for a real guide). Not 3-4 one-liner slides.
- Each slide earns its swipe: real substance, a specific tactic, a named tool, an actual example or prompt. Not a fortune cookie.
- The title slide is a standalone hook that works as a thumbnail. It makes the scroller stop and swipe.
- Every content slide leaves a small open loop the next slide pays off (see `turma:story-craft`, curiosity gaps).
- The last slide is the CTA, coupled to the topic and pointing at the primary conversion from brand.md.

Thin, generic carousels get reach and zero saves. Depth is what gets saved and shared.

## Inputs

- A topic or angle, or a source piece (a post, an article, a transcript) to adapt
- How many carousels (default: as asked, e.g. 5)
- Optional: which channel (IG, LinkedIn, TikTok) if it changes the format

## Procedure

1. **Read brand.md.** Voice, audience, splinter, primary conversion, channels.
2. **Ground it** (`turma:pauta`). Check the reference bank and what the project already published on this topic; mine the bank for angles before inventing new ones. For opinion-led carousels, gate the angle with the owner first.
3. **Find the angles.** From a topic, break it into N distinct standalone carousel angles (each a different useful cut). From a source piece, mine it for the N strongest ideas. Apply `turma:power-law`: some are craft bets, treat them that way.
4. **Build each arc** with `turma:story-craft`: a hook title, a build (each slide one beat with real substance), a payoff, a coupled CTA.
5. **Write every slide in full.** Title slide (the hook), content slides (the actual substance, tools, examples, numbers), CTA slide. In the project's voice.
6. **Voice pass.** Run `turma:anti-ai-linguo`. No dashes, no AI tells, brand voice.
7. **Deliver** the N carousels to `outbox/` with `status: review-needed` (Yellow). For each: the slide-by-slide text, a one-line note on the hook, and which one you'd bet on.

## Output (per carousel)

```markdown
## Carousel [n]: [standalone title / hook]
**Angle:** [the one useful cut]. **Bet:** [craft bet or volume ticket]

- Slide 1 (title): [the hook, thumbnail-ready]
- Slide 2: [substance]
- Slide 3: [substance, opens a loop]
- ...
- Slide N-1: [payoff]
- Slide N (CTA): [coupled to the topic, toward the primary conversion]

**Design note:** [visual direction, if relevant]
```

## Hard rules

- Reads brand.md. Voice and CTA come from there.
- The depth standard is non-negotiable. No thin carousels.
- Never invents fake numbers, tools, or examples. Real or nothing.
- Yellow: carousels go to `outbox/` for the owner's approval before posting.
- No dashes, no AI tells. `turma:anti-ai-linguo` runs last.

## Related

- `turma:pauta`: the operating layer. Angles come from the reference bank; opinion-led angles pass the gate first.
- `turma:story-craft`: the arc inside each carousel.
- `turma:power-law`: which carousels are bets vs tickets.
- `turma:ghostshelf`: the faceless-page engine carousels often feed.
- `turma:anti-ai-linguo`: the final voice pass.
- The project's `brand.md`: voice, audience, CTA.
