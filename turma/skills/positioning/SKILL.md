---
name: positioning
description: Sharpen what a project actually sells and to whom, before any distribution work. Invoke at the start of a new engagement, when filling or fixing a project's brand.md, when a project "won't convert no matter the channel," or when the offer feels vague. Runs two diagnostics: the painkiller-vs-vitamin test (is this even distributable) and the seven strategy questions (problem, segment, alternative, edge, price, first ten customers). Reads and writes toward brand.md sections 1-4. This is the upstream skill; most conversion problems are positioning problems wearing a channel costume.
---

# positioning

Most "our marketing isn't working" problems are not marketing problems. They are positioning problems. The product solves a fuzzy problem, or solves it for no one in particular, or is a nice-to-have the reader forgets by lunch. No channel fixes that. You can pour perfect copy and a flawless funnel onto a vitamin and it still won't sell, because the reader was never in pain.

positioning is the skill that runs *before* the distribution skills. It answers one question with brutal specificity: **what are we selling, to whom, and why do they have to have it?** Everything downstream (`micromagnet-craft`, `seo-strategy`, `social-posts`, `power-law`) works better, or only works at all, once this is sharp. When a project can't convert, come back here first.

**Before you start:** read the project's `brand.md`, especially sections 1-4 (the project, the audience, the goal, the offer). positioning's job is to *fill those sections sharply* or *stress-test them* when they read vague. If `brand.md` doesn't exist yet, this skill is the interview that produces its first draft.

## When to invoke

- At the very start of a new engagement, before touching any channel.
- When filling a project's `brand.md` for the first time (this is the intake interrogation).
- When a project "won't convert no matter what we try." The channel is usually innocent.
- When the one-liner, the audience, or the offer in `brand.md` reads vague, hedged, or "for everyone."
- Before building a micromagnet or a ranking tool: the splinter it removes has to ladder up to a real painkiller.

## When NOT to invoke

- When positioning is already sharp and the real question is distribution. Don't re-litigate a solid `brand.md`; go do the channel work.
- For line-level copy. That's `turma:story-craft`, `turma:optimize-post`, `turma:social-posts`.
- To decide what to *build*. This skill is not product management. It sharpens how an existing (or planned) product is framed and sold. If the honest verdict is "this is a vitamin," name it plainly and hand that back to the owner as a product decision, don't paper over it with marketing.

## Diagnostic 1: painkiller or vitamin

A painkiller removes a pain the reader is already feeling. A vitamin is good for them in the abstract. Painkillers sell themselves; vitamins need constant convincing. Before any distribution plan, place the offer on these axes. This is a widely-used startup frame; the specific diagnostic axes and the strategy questions below are sharpened from Dan Kulkov's field-tested version (FounderPal, MakerBox).

| Painkiller (distributable) | Vitamin (fights you) |
|---|---|
| Sounds boring, obviously useful | Sounds hype, needs a pitch |
| Real negative consequence if unsolved | Mild "would be nice" if unsolved |
| Mostly B2B (someone's job or money on the line) | Mostly B2C impulse |
| Used weekly or daily | Used once, or a few times a year |
| Boring to explain, easy to justify buying | Fun to explain, hard to justify buying |

The reader buys a painkiller because *not* buying hurts. Read the offer against every row. If it lands mostly in the right column, the honest report is: distribution will be an uphill grind, and the move with the most upside is to sharpen the offer toward a real pain, not to add another channel. Say that out loud. It is the most valuable thing this skill produces, and the one most likely to be unwelcome.

Three ways a vitamin becomes a painkiller without rebuilding the product:
- **Narrow the audience** to the slice that *does* feel the pain acutely. "Note-taking app" is a vitamin for everyone; it's a painkiller for a consultant who bills by the reconstructed meeting.
- **Reframe the job** to the painful outcome, not the pleasant feature. Not "organize your thoughts" but "stop losing the client detail that costs you the renewal."
- **Re-anchor the moment** to when the pain is sharpest, so the offer shows up mid-wince, not mid-calm.

## Diagnostic 2: the seven strategy questions

The interrogation that produces a sharp `brand.md`. Answer all seven in the project owner's actual words, not marketing gloss. Vague answers are the finding; push until each is specific enough to act on.

1. **What one problem am I solving?** One. If the answer is a list, the positioning is unfocused. Force the single most painful one.
2. **Which audience segment craves this solution the most?** Not "everyone who could use it." The hungriest, narrowest slice. This is the `brand.md` audience and the person every downstream skill writes to.
3. **What's the current go-to solution for this problem?** There is always an alternative, even if it's a spreadsheet, a VA, or doing nothing. Name it honestly. You are competing with it, not with a blank slate.
4. **What's good and bad about that alternative?** The bad is your wedge. The good is what you must at least match or the switch never happens.
5. **How is my product actually better than the alternative?** In the reader's terms (time, money, pain, risk), not features. If you can't state the edge in one sentence a stranger nods at, you don't have one yet.
6. **What price is a no-brainer for the audience and still a good deal for me?** Where the switch is obvious for them and the unit economics work for the project. If those two don't overlap, the segment or the offer is wrong.
7. **How will I get the first ten customers?** Named, manual, specific. Not "content marketing." The literal first ten humans and how each hears about it. If there's no concrete answer, positioning isn't done, distribution can't start.

The point of the seven is not the answers in isolation. It is that a shift in any one ripples through the rest. Change the segment (Q2) and the alternative (Q3), the edge (Q5), and the price (Q6) all move. Run them as a system.

## Modes

State the mode at the top of your output.

### Mode 1: DIAGNOSE
Given an existing project or `brand.md`, run both diagnostics and return a verdict. Output: where the offer lands on the painkiller/vitamin axes (row by row), the seven questions answered from whatever the owner and `brand.md` provide, the gaps where answers are vague or missing, and the single sharpest change to positioning that would unblock conversion. If the honest verdict is "vitamin," say so and give the three reframe paths above.

### Mode 2: INTAKE
No `brand.md` yet, or a hollow one. This mode owns the file end to end. The owner never creates, places, or hand-edits it.

1. **Bootstrap from the project first.** Before asking the owner anything, read what the project already tells you: `README`, the landing page or site, `package.json` / marketing copy, pinned posts, any existing content in the repo. Pre-fill every `brand.md` field you can infer, and mark each inferred field so the owner knows it's a guess, not a fact from them.
2. **Interview only the gaps.** Run the seven strategy questions, but skip what the bootstrap already answered. Ask only what you couldn't infer, one question at a time, pushing each to specific. This is the one thing that must come from the owner: the strategic facts only they know. Everything else, you do.
3. **Write the file.** Produce the full `brand.md` from the template (all sections, not just 1-4), and write it to disk yourself at the project's `./growth/brand.md` (create the `growth/` folder if needed; fall back to `./brand.md` only if the project already keeps it at root). Fill sections 1-4 from this skill; leave a clear `[fill: ...]` marker on any section outside this skill's scope (SEO context, assets) with a one-line note on who fills it (`turma:seo-strategy` for the SEO block).
4. **Protect it.** If the project is a git repo, add `growth/brand.md` to that project's `.gitignore` (business data stays out of version control, same privacy boundary as the Chico repo). Tell the owner you did.
5. **Confirm the strategy, not the file.** Show the owner the painkiller/vitamin verdict and the sections 1-4 you wrote, and ask them to confirm the positioning. The file work is done; only the judgment needs a nod (Yellow).

### Mode 3: SHARPEN
The positioning is roughly right but soft. Take one weak element (a mushy one-liner, a too-broad audience, a me-too edge) and tighten it, showing the before and after and which of the seven questions drove the change.

## Owning the brand.md file (create, update, manage)

`brand.md` is a living file, and Chico maintains it. The owner never does filesystem work and is never asked to create, move, or hand-edit the file. Chico owns the mechanics; the owner owns the strategy.

**Where it lives.** In the project being worked, at `./growth/brand.md` (preferred) or `./brand.md` (only if the project already keeps it there). Chico is invoked inside the project, so the working directory is the project. Create the `growth/` folder if it's missing. One `brand.md` per project; never reach into another project's file.

**Keeping it current.** When the owner states a fact that changes the file (a new channel goes live, the primary conversion changes, a price moves, the scoreboard number updates, a positioning learning lands), update the file in place immediately. Don't let it drift and don't ask the owner to edit it. Read it at the start of any engagement; if reality has moved past what it says, fix it.

**The Green / Yellow line on edits.** The permission boundary is about *judgment*, not *keystrokes*:
- **Green (just do it):** create the file from an intake the owner participated in; update factual fields the owner just told you (channel added, price changed, a new scoreboard number, a logged learning); fix a stale field to match current reality; add it to `.gitignore`.
- **Yellow (write it, then confirm):** a material repositioning, the core audience, the primary conversion, or the painkiller framing in sections 1-4. Make the edit, show the before/after diff, and get the nod. You still do the file work; the owner only signs off on the strategy shift.

Never make the owner touch the file to remove friction from a Yellow call. Do the edit, surface the diff, ask about the substance.

## How it composes with other skills

- Runs **before** every distribution skill. A sharp painkiller and a named segment are what `turma:micromagnet-craft`, `turma:seo-strategy`, `turma:social-posts`, and `turma:power-law` all assume but none establish.
- Feeds `brand.md` sections 1-4 directly. The audience splinter this skill names is the same splinter `micromagnet-craft` builds around.
- `turma:name-craft` names the offer *after* positioning fixes what it is. Naming a vitamin doesn't help.
- `turma:story-craft` dramatizes the pain this skill identifies; positioning finds the pain, story-craft makes the reader feel it.
- When the verdict touches what to *build* (not just how to sell it), that's the owner's call. Hand it back as a product decision, don't absorb it into a marketing plan.

## Source

The painkiller-vs-vitamin metaphor is long-standing startup vocabulary. The specific diagnostic axes and the seven strategy questions are distilled from Dan Kulkov's "How to do Marketing" guide (FounderPal, MakerBox), a field-tested solo-founder system. His revenue figures are his marketing, directional and not citable; the method is what carries. Adjacent framing cross-checked against standard positioning practice (segment, alternative, differentiation, price, first-ten-customers).

## Hard rules

- Reads the project's `brand.md` first. Sharpens sections 1-4; never hardcodes a brand.
- Owns the `brand.md` file: creates, writes, and updates it in the project directory so the owner never does filesystem work. Green for creation and factual updates, Yellow for material repositioning (see "Owning the brand.md file").
- Never edits operating canon (`SOUL.md`, `IDENTITY.md`, `CLAUDE.md`, `SPEC.md`, `memory/`).
- One `brand.md` per project, in that project's directory. Never read or write another project's file. Business data stays out of git (add it to the project's `.gitignore`).
- Tells the truth about a vitamin. The most valuable output is often the unwelcome one: "no channel fixes this offer as framed." Say it plainly, then give the reframe paths.
- Does not decide what to build. Positioning sharpens the framing and selling of a product; product scope is the owner's.
- Specific over gloss. A vague answer to any of the seven is the finding, not an acceptable stopping point.
- No AI tells, no dashes on any owner-facing copy produced. Run `turma:anti-ai-linguo` as the final pass.

## Related

- The project's `brand.md`: sections 1-4 are what this skill fills and stress-tests. Source of truth for specifics.
- `turma:micromagnet-craft`: builds on the splinter this skill names; run positioning first.
- `turma:seo-strategy`, `turma:social-posts`, `turma:power-law`: the distribution skills that assume sharp positioning.
- `turma:name-craft`: names the offer after positioning fixes what it is.
- `turma:story-craft`: dramatizes the pain this skill identifies.
- `turma:anti-ai-linguo`: the final voice pass on any owner-facing copy.
