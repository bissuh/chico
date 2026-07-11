---
name: optimize-post
description: Review and optimize an existing post, page, email, or caption for quality and engagement. Invoke when someone asks to "review this post," "optimize for engagement," "make this better," "why isn't this converting," "tighten this up," or pastes a draft and wants it improved. Scores the draft, then returns the improved version in the project's voice. Reads brand.md.
---

# optimize-post

Take a piece that already exists and make it pull harder. Diagnose what's weak, then fix it, in the project's voice.

**Before you start:** read the project's `brand.md` for voice, audience, the splinter, the primary conversion, and banned phrases.

## Inputs

- The draft (a post, page section, email, caption, thread)
- What it's for (the target action, if not obvious from brand.md)
- Optional: a performance signal ("0.4% CTR," "no replies")

## What you check (score each 1-3)

1. **Hook.** Does the first line stop the scroll and open a loop? (`turma:story-craft`)
2. **Mirror.** Does it name the reader's real situation, specifically, early? Or is it about the brand?
3. **Substance.** A real tactic, number, example, or named thing? Or generic advice?
4. **Momentum.** Curiosity gaps that pull the reader down? Or does it sag in the middle?
5. **Voice.** Does it sound like the brand.md voice, or like a bot? Any AI tells or dashes?
6. **CTA.** Coupled to the piece and pointing at the primary conversion? Or stapled on?

## Procedure

1. Read brand.md.
2. Read the draft twice. Score the six checks. Name the single weakest one. That's the leverage.
3. Rewrite: fix the weak checks, keep what works. Do not rewrite for the sake of it. In the brand voice.
4. Run `turma:anti-ai-linguo` as the final pass.
5. Deliver: the scorecard, the optimized version, and a one-line diff note (what was weak, what changed, why).

## Output

```markdown
# Optimized: [what it is]
**Target action:** [from brand.md]

## Scorecard
| Check | Score | Note |
|---|---|---|
| Hook | 1-3 | ... |
| Mirror | 1-3 | ... |
| Substance | 1-3 | ... |
| Momentum | 1-3 | ... |
| Voice | 1-3 | ... |
| CTA | 1-3 | ... |

**Weakest link:** [the one to fix first]

## The optimized version
[the rewrite, in brand voice]

## What changed
[one line]
```

## Hard rules

- Reads brand.md. Voice and target action come from there.
- Diagnose before rewriting. The scorecard shows the leverage.
- Never invents numbers or claims to make it stronger. Real or cut.
- Yellow if it ships under the brand: to `outbox/` for approval.
- No dashes, no AI tells. `turma:anti-ai-linguo` runs last.

## Related

- `turma:story-craft`: the 5-line diagnosis under the hood.
- `turma:anti-ai-linguo`: the voice pass.
- `turma:micromagnet-craft`: if the CTA needs a coupled lead magnet.
- The project's `brand.md`: voice, audience, target action.
