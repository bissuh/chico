---
name: viral-teardown
description: Reverse-engineer why a piece went viral (or why a proven winner works) and extract the transferable pattern to run on your own project. Invoke when someone shares a viral post, thread, article, video, or ad and asks "why did this blow up," "break this down," "what made this work," "teardown this post," "how do I replicate this," or when your own piece just popped and you want to know exactly what carried it. Turns a winner into a reusable template plus a tagged learnings entry. Reads brand.md to translate the pattern into the project's voice.
---

# viral-teardown

Take a proven winner and cut it open. Not to copy it, to extract the transferable pattern and run it in your own voice. A viral piece is the market showing you what it wants. This skill turns that signal into a template and a logged technique.

**Before you start:** read the project's `brand.md` (audience, voice, splinter, primary conversion). The teardown ends by translating the winner's pattern into this project's world.

## When to invoke

- Someone shares a viral piece and asks why it worked or how to replicate it.
- Your own post just over-performed and you want to know exactly which element carried it (pairs with `turma:power-law` DOUBLE-DOWN).
- Building a swipe file of what actually works in the project's niche.
- Feeding the learnings loop: every teardown should leave a tagged, portable technique behind.

## When NOT to invoke

- Diagnosing your own unpublished draft before it ships. That is `turma:story-craft` REVIEW or `turma:optimize-post`.
- Anything that is not analysis of a proven winner. Use the specific skill for the job.

## The one rule: extract the pattern, never the content

You are stealing the structure, not the words, the topic, or the specifics. Copying the content is theft and it does not transfer anyway. Copying the pattern (the hook shape, the emotional driver, the proof style) is craft, and it does.

## The anatomy (go element by element)

For each element, name what it did and whether it is transferable or a one-off.

1. **The hook (first 3 seconds).** What stops the scroll? A concrete number, a pattern interrupt, a bold or contrarian claim, a self-deprecating confession, a curiosity gap. Quote the actual opening line.
2. **The open loop.** What unfinished business makes you keep reading or watching, and when does it pay off?
3. **The emotional driver.** What feeling does it trigger? Status anxiety, aspiration, relief or validation ("I'm not crazy"), outrage, awe, FOMO. Virality rides emotion. Name the specific one.
4. **The proof.** The specificity that earns belief: real numbers, named people or companies, concrete examples, a visible calculation. Vague claims do not travel.
5. **The reframe (the shareable atom).** The one counter-intuitive line that reorganizes how the reader sees something. Usually the single most screenshotted, most quoted unit. Find it and quote it.
6. **Format and friction.** Length, structure, scannability, native-to-the-platform shape, visuals. Why is it easy to consume and easy to pass on?
7. **Identity and shareability.** Does sharing it make the sharer look smart, early, in-the-know, or in-group? People share what says something about them. Name what this piece lets the sharer signal.
8. **Context and timing.** Why now? Riding a trend, a moment, or an evergreen nerve? Transferable, or a one-off that will not repeat?
9. **The conversion.** What does the hit funnel to (a follow, an opt-in, a link, a product), and how coupled is that to the content?

## After the pass: the scorecard and the steal

1. **Why it hit, in one line.** The single biggest driver, usually the reframe or the emotional driver plus the proof.
2. **The transferable pattern.** The reusable shape, stated so it works for any topic. Example: "confession hook with a shocking number gap, then stack the same principle across three unrelated domains, then show the math inline, then a freeing reframe."
3. **Steal this for [project].** Translate the pattern into the project's world using `brand.md`: the same shape, on the project's topic, in the project's voice, toward the project's conversion. Draft the hook.
4. **What is not transferable.** The luck, the timing, the author's existing audience. Be honest, so the project does not chase noise.

## Feed the learnings loop

Every teardown ends with a tagged entry for turma's write-back (`turma/templates/learnings.template.md`): the pattern, the vertical tag, the confidence. This is how the craft compounds. A pattern seen winning across three teardowns in one vertical graduates into a technique.

## Output

```markdown
# Teardown: [the piece, the author, the result number if known]
**What it is:** [format, platform, the result]

## Anatomy
| Element | What it did | Transferable? |
|---|---|---|
| Hook | ... | yes / no |
| Open loop | ... | ... |
| Emotional driver | ... | ... |
| Proof | ... | ... |
| Reframe | ... | ... |
| Format | ... | ... |
| Shareability | ... | ... |
| Timing | ... | ... |
| Conversion | ... | ... |

## Why it hit (one line)
[...]

## The transferable pattern
[the reusable shape]

## Steal this for [project]
[the pattern on the project's topic, in its voice, with a drafted hook]

## Not transferable
[the luck and the one-offs]

## Learnings entry
### [date] / viral-teardown / [vertical tag]
- Pattern: [...]
- Confidence: [hunch / signal / strong]
```

## Hard rules

- Extract the pattern, never the content. No copying words, topics, or specifics.
- Reads `brand.md`. The "steal this" step is always in the project's voice, toward its conversion.
- Be honest about what is luck versus craft. Do not send the project chasing an unrepeatable one-off.
- Every teardown feeds the learnings loop. A teardown that leaves nothing behind was a waste.
- No dashes, no AI tells on any drafted output. Run `turma:anti-ai-linguo`.

## Related

- `turma:power-law`: DOUBLE-DOWN mode calls this on your own hit to name what carried it.
- `turma:story-craft`: builds the new piece once the teardown hands you the pattern.
- `turma:optimize-post` and `turma:story-craft` REVIEW: for your own unpublished draft (a different job).
- `turma/templates/learnings.template.md`: where every teardown's pattern lands.
- The project's `brand.md`: voice and conversion for the "steal this" step.
