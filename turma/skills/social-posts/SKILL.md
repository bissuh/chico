---
name: social-posts
description: Write channel-native social posts (LinkedIn, X, Instagram) from a topic or a source piece, in the project's voice, engineered to earn engagement. Invoke when someone asks to "write a LinkedIn post," "give me X posts," "post about this," "turn this article into social posts," "write LinkedIn content," or wants ready-to-publish posts for a channel. Reads brand.md and composes emotion-craft, story-craft, and anti-ai-linguo.
---

# social-posts

Write posts that stop the scroll and earn a comment, in the project's voice, native to the channel they run on. This is a composition skill: it picks the emotional lever, structures the post, and cleans the voice, using the crew.

**Before you start:** read the project's `brand.md` for voice, audience, the primary conversion, and which channels matter.

## Inputs

- A topic or angle, or a source piece (an article, a transcript, a newsletter) to repurpose
- The channel(s): LinkedIn, X, Instagram caption
- How many posts, and the goal (engagement, or drive to the primary conversion)

## The method (chain the crew)

1. **Read brand.md.** Voice, audience, primary conversion, channels.
2. **Pick the emotional lever** with `turma:emotion-craft`: a primary and a secondary trigger. A post that only informs will flat-line. Decide what the reader should *feel*.
3. **Structure it.** For a story-shaped post, run `turma:story-craft` (the 5 lines, compressed). For a punchy single post, use hook plus two to four short beats plus a close. The hook does the emotional work in the first line.
4. **Write it native to the channel** (see channel notes). Same idea, different shape per platform.
5. **Close with action.** A question that invites a comment, or a handraiser toward the primary conversion (`turma:micromagnet-craft` if a magnet fits).
6. **Voice pass.** `turma:anti-ai-linguo`. No dashes, no AI tells, no manufactured controversy or fake FOMO. Emotional truth only.
7. **Deliver** to `outbox/` with `status: review-needed` (Yellow).

## Channel notes

**LinkedIn.**
- The first line is everything. Only the first couple of lines show before "see more," so the hook has to earn the click to expand. Lead with the emotional trigger, never a warm-up.
- Short lines, whitespace between them. Dense paragraphs die. One idea per line.
- Professional-casual. Talk like a smart operator, not a press release.
- CTA: a genuine question, or "comment [WORD] and I'll send it" for a handraiser. Comments are weighted heavily, so a post that earns a real back-and-forth outperforms one that just earns likes.

**X / Twitter.**
- Tighter. The first tweet is the hook and must stand alone. If the idea needs room, make it a thread where each tweet is one beat.
- Character economy. Cut every word that is not carrying weight.

**Instagram caption.**
- The hook shows before "more." Shorter than LinkedIn. Often paired with a carousel (`turma:carousels`) or a reel, so the caption supports the visual, it does not repeat it.
- Emoji only if `brand.md` voice allows.

## The content waterfall

One idea rarely justifies one post. From a source piece, pull the strongest angle and waterfall it: the LinkedIn post (the full emotional version), the X thread (one beat per tweet), the IG caption (compressed, visual-led). Do not write three unrelated posts, write one idea three native ways. `turma:power-law` decides which angle is the bet worth waterfalling.

## Output

```markdown
# Social posts: [topic]
**Channel(s):** [...]  **Primary trigger:** [from emotion-craft]  **Goal:** [engagement / conversion]

## LinkedIn
[hook line]
[body, short lines]
[CTA]

## X (thread)
1/ [hook]
2/ [beat]
...

## IG caption
[hook + support + CTA]

**Note:** [which post is the bet, and what it's engineered to make the reader feel]
```

## Hard rules

- Reads `brand.md`. Voice, audience, conversion, and channels come from there.
- Every post is engineered to make the reader feel something (`turma:emotion-craft`), run through the honesty guardrails. No manufactured controversy, no fake FOMO.
- Native to the channel. A LinkedIn post is not an X post with different line breaks.
- Yellow: posts go to `outbox/` for the owner's approval before publishing.
- No dashes, no AI tells. `turma:anti-ai-linguo` runs last.

## Related

- `turma:emotion-craft`: picks the lever the post pulls. Run first.
- `turma:story-craft`: structures a story-shaped post.
- `turma:carousels`: when the idea is better as slides than a caption.
- `turma:micromagnet-craft`: when the post is a handraiser for a magnet.
- `turma:power-law`: which angle is the bet worth waterfalling across channels.
- `turma:anti-ai-linguo`: the final voice pass.
- The project's `brand.md`: voice, audience, conversion, channels.
