# Skills

Skills are repeatable workflows Chico can invoke by name. Each skill is a folder with a `SKILL.md` file describing when to use it and how.

Skills are earned, not assumed. We add a skill when a workflow has shipped cleanly at least twice and is ready to be systematized, OR when the skill is plumbing that unlocks other skills (like API access).

## Hard rules for every skill

These apply to every skill, however it's invoked (scheduled by launchd, fired by a script, or run manually). Keeps automation from quietly rewriting the operating canon.

1. **No auto-editing of operating canon.** A skill, however invoked, may not auto-edit `CLAUDE.md`, `SPEC.md`, `SOUL.md`, `IDENTITY.md`, `memory/permissions.md`, `memory/division-of-labor.md`, `memory/core.md`, or `memory/playbook.md`. All proposed changes go via `inbox/` as rule candidates for Bissuh's review. Interactive Chico and Bissuh sessions are governed by the normal Yellow/Red tier system; this rule is about skills, not interactive work.

Adopted 2026-04-19 from the `consolidate-memory` v0.1 per-skill constraint. Source: `inbox/rule-candidates-2026-04-19.md` candidate 1.

## Built

Skills that exist and are usable today.

1. **consolidate-memory** — nightly (02:00) job that compresses sessions into dated memory and proposes rule candidates. Manually invocable at end of heavy days.
2. **beehiiv-api** — read-only access to TBP's beehiiv publication (subscribers, posts, stats, segments). Invoke when answering questions about current list state or before producing any health-of-the-business report. Write operations deliberately NOT included.

## Starter skill queue (not built yet, in order of expected build)

1. **draft-x-post** — produce a TBP-voice X post from a topic, outline, or newsletter edition
2. **competitive-teardown** — analyze a newsletter or creator's content using the teardown format in `knowledge-base/README.md`
3. **lead-magnet-outline** — turn a topic into a lead magnet outline (PDF checklist, playbook, template)
4. **welcome-email-iterate** — propose improvements to the welcome email based on reply signal
5. **weekly-review** — scoreboards + experiment results + next week's plan (depends on `beehiiv-api`)

## Skill file structure

```
skills/
  draft-x-post/
    SKILL.md            (when to use, inputs, outputs, constraints)
    examples/           (good examples, bad examples, with Bissuh's edits visible)
    template.md         (starting scaffold, optional)
```

## When to build a new skill

A workflow becomes a skill when:
- Chico has produced it at least twice, successfully (Bissuh approved with minimal edits), OR
- The skill is plumbing that unlocks other skills (API wrappers, data access). These exceptions should be rare and named in the justification.
- The inputs and outputs are stable enough to document
- The downside of a bad output is small or recoverable

Until then, just do the work directly. Don't premature-systematize.
