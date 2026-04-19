# SUBAGENT-POLICY.md — when to delegate, when to stay in the loop

Claude Code's Task tool spawns subagents with isolated context. They can run in parallel, they return a single summary. They are a force multiplier when used right, a context-waster when used wrong.

This file is the rule for when to use them.

## The core distinction

- **Main loop (Chico)**: carries identity, voice, permissions, memory, the whole OS. Every session file, every draft in Chico's voice, every Bissuh conversation — all main loop.
- **Subagent (Task tool)**: a fresh Claude instance with a narrow brief. No SOUL, no IDENTITY, no memory. It is competent but anonymous. It cannot "be Chico."

Use the main loop for anything that needs judgment, voice, or identity.
Use subagents for bounded, factual work that would otherwise clog main-loop context.

## Delegate (Task tool) when

- **The task is a search or scan.** "Find every mention of lead magnets in the knowledge base." "List every file in `Articles/` that covers paid acquisition." A single summary is more useful than a page of raw results in the main context.
- **The task is a teardown or ingestion.** "Read this 40-page McGarry PDF and extract 10 actionable tactics." "Summarize Dan Koe's last 5 long-form posts into a one-pager." Main loop does not need the full text; the extract is enough.
- **The task can run in parallel with other work.** "While I draft the X post, pull competitive examples from the knowledge base." Parallel dispatch saves wall time.
- **The task has a clean factual output with no voice requirement.** A list, a summary, a count, a grep.
- **The output is throw-away context** the main loop would otherwise have to load and forget.

## Do NOT delegate when

- **The output is TBP-voice content.** Social posts, emails, landing pages, lead magnet prose, newsletter drafts. A subagent does not have IDENTITY.md loaded. It will produce a competent AI draft that reads like every other newsletter. That is exactly what we are trying not to do.
- **The task is a decision.** "Should we use Typefully or Buffer?" is not a delegation question. It is a conversation between Chico and Bissuh, with memory and context.
- **The task requires Chico's memory.** Subagents cannot see `memory/` unless the prompt hands it over. If the task needs cross-session continuity, it stays in the main loop.
- **The task touches permissions or canon.** Editing CLAUDE.md, proposing rule candidates, deciding tier tags — all main loop.
- **The work is short enough that the delegation overhead costs more than the delegation saves.** Reading one file and writing two lines is not a subagent job.
- **The output needs to land in a specific place the main loop is managing** (outbox file, session log, inbox reply). Let the main loop do the write.

## When delegating, follow these rules

From the main loop's perspective, the Task tool takes a prompt and returns a summary. The quality of that summary depends almost entirely on the prompt.

1. **Brief the subagent like a smart colleague who just walked in.** Self-contained. No "as you know from earlier." It has no memory of this conversation.
2. **State the goal in one sentence, then the constraints.** "Find X. Report under 200 words. Include file paths and line numbers." Specifics get better returns than vague briefs.
3. **Name the output shape.** Bullet list, paragraph, table, JSON — say so. Otherwise you will get prose when you wanted a list.
4. **Cap the response length.** Subagents default to comprehensive. You want tight. Ask for tight.
5. **Never delegate understanding.** Do not write "figure out X and fix it." That pushes synthesis onto the subagent. Write "read X, report Y, I will decide Z."
6. **If you need multiple independent results, dispatch in parallel** — one message, multiple Task calls, not sequential.

## The voice test

Before delegating, ask: **if the output of this task appeared under Chico's name, would a reader notice it was generic?**

- If yes (output is TBP content): main loop only.
- If no (output is internal research, data, a list): subagent is fine.

## Examples

**Good delegations:**
- "Scan `knowledge-base/` for every tactic Matt McGarry has written about welcome flows. Return a table: tactic, source URL or filename, and whether it has been ported to `memory/playbook.md` yet."
- "Read Articles/<old Semana em AI edition> and tell me in under 150 words what the three biggest structural mistakes were."
- "Grep the whole workspace for any file that uses the word 'leverage' or 'elevate'. Return paths only."

**Bad delegations (do in main loop instead):**
- "Draft an X post about AI-powered micro-SaaS." (voice + output under Chico)
- "Decide which lead magnet format to ship first." (decision, needs memory and conversation with Bissuh)
- "Rewrite the welcome email." (voice-sensitive, lands in outbox, Yellow tier)
- "Update `memory/playbook.md` with insights from this teardown." (touches memory, main loop responsibility)

## A note on the `Explore` subagent type

Claude Code ships a specialized `Explore` subagent for codebase searches. When Chico is looking around the filesystem for something factual (where does X live, how many files reference Y), `Explore` beats writing a custom prompt. Use it freely for that.

## When in doubt

Default to main loop. Delegation is a tool, not a default. The cost of a bad subagent output is a throwaway summary. The cost of a subagent-drafted TBP post is readers noticing the voice is off. The second is a brand problem.
