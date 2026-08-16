---
name: pauta
description: The operating layer around a project's content production. Who decides, who executes, and where ideas live between capture and publish. Installs five contracts. The reference bank (capture), the grounding packet (context), the owner interview (the judgment gate before opinion-led drafts), approval binding (what "approved" actually attaches to), and the engagement boundary (conversations stay human). Invoke when bootstrapping a project's content operation, when drafts read generic despite good production skills, when ideas keep dying between capture and creation, when nobody can say what exactly was approved, or before wiring any automation that publishes. Reads brand.md. Runs upstream of the production skills; turma:anti-ai-linguo still runs last.
---

# pauta

"Pauta" is Brazilian newsroom vocabulary: the assignment agenda, and the meeting where editors decide what gets covered and from what angle before anyone writes a word. That layer is what most AI content operations are missing. This skill installs it.

The principle underneath: **delegate execution, keep judgment.** Most AI content systems get the split backwards. They keep the human doing the repetitive publishing work while asking the model to manufacture the opinion. The output becomes correct, readable, and interchangeable: it could have come from anyone with access to the same model. The right split is the opposite one. The agent collects the raw material, recovers the context, challenges the first idea, asks the questions the owner would skip, and handles every repetitive step after the decision. The point of view is earned by the owner, outside the model.

turma's production skills make individual pieces good. pauta makes the operation around them sound: generation sits near the end of the process, not the beginning.

**Before you start:** read the project's `brand.md`. Positioning (sections 1-4) decides which references matter. Channels (section 7) decide where approved work flows. If a surface is marked owner-only, pauta never routes drafts onto it.

## When to invoke

- Bootstrapping a project's content operation, right after `turma:positioning` fills brand.md.
- Drafts keep coming out generic even though the production skills are doing their job. That is usually a missing judgment gate, not a writing problem.
- Ideas appear in chats, podcasts, and conversations, then die before they become content. That is a missing reference bank.
- The owner asks "wait, what exactly did I approve?" or an edited draft ships under an old approval. That is missing approval binding.
- Before wiring ANY automation that publishes (schedulers, pipelines, autonomous agents). Contract 4 is the safety layer such automation must inherit.

## When NOT to invoke

- Mid-draft on a single piece with no operation problems. Just use the production skill.
- To automate replies, comments, or DMs. pauta exists partly to stop that. See contract 5.
- As a reason to build infrastructure a small project does not need. See the minimum install.

## Three modes

State the mode at the top of the output.

- **INSTALL.** Bootstrap the contracts into a project: create `growth/references.md` from the template, agree the interview trigger and approval ladder with the owner, record both in a short note. One pass, then the operation runs.
- **RUN** (default). Execute the loop for a specific piece: bank check, grounding packet, interview if opinion-led, hand off to the production skill, bind the approval.
- **AUDIT.** Review an existing operation against the five contracts. For each: present, partial, or missing, with the one fix that pays most. A missing judgment gate outranks missing tooling every time.

## The judgment ledger

The whole skill in one table. When in doubt about who does a thing, look it up here.

| The owner keeps | The agent takes |
|---|---|
| Which topics matter for the positioning, and why now | Capture, transcription, distillation into the reference bank |
| The angle of a piece | Surfacing connections between references and past content |
| The opinion, stated in their own words | The grounding packet before drafting |
| What evidence they actually have | Running the interview: asking, pushing back, challenging the first idea |
| The boundaries: claims not to make, topics not to touch | Drafting after the gate, in the brand.md voice |
| Final approval of the exact artifact | Formatting, adaptation per channel, scheduling mechanics |
| Replies, comments, DMs | Performance reads, and harvesting conversations back into the bank |

The line that holds it together: **the agent can suggest an angle. It cannot own the angle.** When the angle, the opinion, or the evidence gets delegated to the model, the output is shallow no matter how good the production skills are.

## Contract 1: the reference bank

Ideas arrive at the worst possible moments: mid-podcast, mid-conversation, mid-commute. By the time there is space to create, the context around the idea is gone. The bank fixes the fragmentation, which wears an operator down more than the writing does.

- **One durable home.** Default: `growth/references.md`, created from `turma/templates/references.template.md`. If the project already keeps references somewhere real (a Notion database, a notes system), the contract is the fields, not the tool. What is banned is "everywhere": chat scrollback, browser history, five apps.
- **Capture anywhere, land in one place, same day.** The capture interface can be anything the owner already uses. It is an interface, not a memory.
- **Distill on capture.** Every reference gets one line of reusable insight in the owner's or agent's own words, one line on why it matters for this project's positioning, and its connections to earlier references or published pieces. A raw link is a bookmark, not a reference.
- **The agent maintains it.** Transcribe, distill, connect, prune. Surfacing a connection between two references that look unrelated is some of the highest-value work the agent does here. The connection becomes useful when the owner can say why they belong together; that part is theirs.

## Contract 2: the grounding packet

Never draft opinion-led work from a blank prompt when the project has history. Before drafting, assemble a short packet:

1. **Positioning:** the relevant lines from brand.md sections 1-4.
2. **References:** the bank entries that touch this topic.
3. **Prior art:** what the project already published on it, so the new piece extends instead of repeats.
4. **Performance context:** how adjacent pieces performed, from the connectors when wired (`turma:search-console-connector`, `turma:beehiiv-connector`, `turma:youtube-connector`) or the platform's native analytics.

The packet is the input to the interview, and after the gate it travels with the brief to the production skill. Keep it under a page. A packet nobody reads is ceremony.

## Contract 3: the owner interview (the judgment gate)

Before drafting anything opinion-led (an essay, a take, a newsletter with a point of view, a positioning piece), the agent interviews the owner against the grounding packet. Five questions:

1. **The angle.** Concretely, what is this piece saying? One sentence.
2. **The tension.** What does it push against: the default advice, a competitor's framing, the owner's own past position?
3. **The opinion.** What does the owner actually believe here, in their words?
4. **The evidence.** What do they really have: numbers, cases, experience? Name it.
5. **The boundaries.** What must this piece not claim, promise, or touch?

The rules of the gate:

- **Weak material gets more questions, never filler.** If the answers are thin, the piece is not ready. Keep asking, or park it back in the bank. Filling the gaps with plausible language is exactly the failure this skill exists to prevent, and `turma:anti-ai-linguo` cannot fix it downstream: a language pass cannot fix an unearned opinion.
- **Capture answers verbatim.** The owner's phrasing is the draft's spine and its voice anchors. Anchors pulled from the owner's own mouth cannot rot into generic tells (see anti-ai-linguo, "Tells rot").
- **Challenge the first idea.** The agent's job in the interview is not stenography. Push back once where the angle is weak, then defer.
- **Scale the gate to the piece.** A how-to, a data piece, or a volume ticket (`turma:power-law`) needs only questions 1 and 4, often answered from the packet in seconds. The full gate is for craft bets and anything carrying an opinion. The gate earns its keep by being cheap on cheap pieces.
- **Interview once per angle, not once per artifact.** One gate covers the whole waterfall of a single idea across channels.

## Contract 4: approval binding

"Approved" is the most abused word in content operations. This contract pins it down.

- **Approval attaches to the exact artifact:** this text, this asset, this destination, this publish time. Change any one of them and the approval is void; the piece goes back to review. No "small tweak after the yes" ships unreviewed.
- **A status ladder with one meaning per rung.** Whatever ladder the project uses (turma default: `draft`, `review-needed`, `approved`, `published`, `dropped`), only the owner moves work into `approved`, and `approved` means the exact bound artifact.
- **Everything after approval is mechanical.** Formatting, scheduling, posting: execution steps that decide nothing. Safe to automate precisely because no step downstream of the gate holds editorial authority. Running a step twice must not publish twice.
- **A kill switch.** The owner can freeze all publishing with one word, no questions asked.
- **Ambiguity stops the line.** A failed post, a changed asset, anything unexpected goes to the owner as a review item. Never blind retries, never "probably fine."

This contract is cheap discipline for a manual operation and a hard requirement before any autonomous publishing exists. Wiring automation that publishes is an owner sign-off decision, always; any paid tool in that stack is a spend decision the owner makes first.

## Contract 5: the engagement boundary

Replies, comments, and DMs are not a chore to automate. They are where the owner's point of view forms: someone's experience contradicts the argument, a reader describes the problem in words the owner would never choose, a question exposes the weak part of a published piece. These conversations are the beginning of the next piece. Automate them and you have automated away the judgment the rest of the system exists to protect.

- **Default: the owner runs their own conversations.** The agent never replies as the owner.
- **The agent harvests.** Pull the pushback, the surprising phrasings, and the exposed weak points into the reference bank as first-class references. Read comment patterns to see which part of an idea created the reaction, and feed that to `learnings.md`.
- **The agent can draft.** Reply options for the owner to send are fine. Sending is theirs.
- **If an agent ever does post in a public conversation** (a project may choose this for support-style replies), it identifies as AI up front. Non-negotiable, turma-wide.

## The minimum install

This whole skill runs with zero infrastructure, which is the point for an underdog project:

1. One `growth/references.md` file from the template.
2. The five interview questions, asked in chat before opinion-led drafts.
3. The approval ladder with binding, tracked in filenames or frontmatter.

That is a complete pauta. Tooling (databases, schedulers, pipelines) gets added only when volume makes the file hurt, and it inherits the same contracts. The contracts are the operation; the tools are furniture. Models change too; the workflow, the context, and the quality bar need a stable home that survives them.

## Composing with the crew

- `turma:positioning` runs first on a new engagement. pauta's "why it matters here" filter is positioning's output put to work.
- Production skills (`turma:social-posts`, `turma:carousels`, the produce-week command, `turma:story-craft` pieces) consume the grounding packet and respect the gate. They own the craft of the artifact; pauta owns the decision around it.
- `turma:anti-ai-linguo` stays the LAST pass. pauta is the input-side guard (no unearned opinions in), anti-ai-linguo is the output-side guard (no AI language out). A draft failing the audit pass for missing point of view comes back through the interview, not through another rewrite.
- `turma:power-law` classifies the piece (bet or ticket), which sets the gate depth in contract 3.
- The connectors supply contract 2's performance context.
- `turma:optimize-post` and `turma:viral-teardown` read results; their findings enter the bank and `learnings.md`.

## Hard rules

- Reads `brand.md` first. Positioning decides relevance; owner-only surfaces stay untouched.
- The agent proposes angles, challenges ideas, and drafts. It never owns the angle, the opinion, or the evidence. Thin answers stop the draft; they are never filled with plausible language.
- Approval binds to the exact artifact. Any change voids it. Only the owner approves.
- No autonomous step downstream of the gate holds editorial authority, and nothing publishes without a bound approval. Wiring publishing automation requires the owner's explicit sign-off; paid tooling is a spend decision the owner makes first.
- The agent never replies to a project's audience as the owner. If it posts at all, it identifies as AI.
- Raw references can hold private material. The bank lives gitignored with the rest of `growth/`. Only sanitized technique crosses into turma via `learnings.md`.
- Never edits operating canon (`SOUL.md`, `IDENTITY.md`, `CLAUDE.md`, `SPEC.md`, `memory/`).
- No dashes, no AI tells in anything produced. `turma:anti-ai-linguo` runs last.

## Sources

- Bernardo Precht ([@berprecht](https://x.com/berprecht)), "How I'm building a content agent that actually works: breakdown and architecture," X Article, August 2026. The architecture this skill generalizes: capture through WhatsApp as interface not memory, the interview step, judgment gates, strict approval binding, and the refusal to automate DMs. His specific stack (agent, Notion, Drive, scheduler) is his runtime, not the contract; this skill keeps the contracts and drops the tools.
- Osvald Nitski (CPO, Mercor) on [20VC, July 2026](https://thetwentyminutevc.libsyn.com/20vc-mercor-cpo-on-revenue-concentration-from-frontier-labs-why-large-enterprise-is-scared-to-partner-with-frontier-labs-why-small-specialised-models-is-the-future-with-osvald-nitski). Origin of "delegate execution, keep judgment": AI is for execution, not for the judgment calls that define the job, because delegating decisions to models degrades the capability over time.
- Tiago Forte, "Building a Second Brain" (the CODE method: capture, organize, distill, express). Prior art for contract 1's capture-and-distill discipline. His line fits the bank exactly: you are building a factory, not a library.
- Nicolas Cole, ["The Art of Interviewing Clients as a Ghostwriter"](https://nicolascole77.medium.com/the-art-of-interviewing-clients-as-a-ghostwriter-fc3650a5610f). The human-ghostwriter ancestor of contract 3: great ghostwriting is great interviewing, and the client's own words are the material.

Rejected from the sources: performance claims (none exist; these are architecture pieces), the specific tool stacks, and full content-OS infrastructure as a default (the minimum install exists because most projects need the discipline, not the plumbing).

## Related

- The project's `brand.md`: positioning, channels, owner-only surfaces.
- `turma/templates/references.template.md`: contract 1's file, copied into the project as `growth/references.md`.
- `turma:positioning`: upstream. Fills the brand.md this skill filters against.
- `turma:social-posts`, `turma:carousels`: production skills that consume the packet and respect the gate.
- `turma:anti-ai-linguo`: the output-side twin. Always last.
- `turma:power-law`: sets gate depth (bet or ticket).
- `turma:optimize-post`, `turma:viral-teardown`: results reads that feed the bank.
- `turma/templates/learnings.template.md`: where sanitized lessons cross back into the craft.
