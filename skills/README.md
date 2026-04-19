# Skills

Skills are repeatable workflows Chico can invoke by name. Each skill is a folder with a `SKILL.md` file describing when to use it and how.

This folder starts empty on purpose. Skills are earned, not assumed. We add a skill when a workflow has shipped cleanly at least twice and is ready to be systematized.

## Starter skill queue (not built yet, in order of expected build)

1. **draft-x-post** — produce a TBP-voice X post from a topic, outline, or newsletter edition
2. **competitive-teardown** — analyze a newsletter or creator's content using the teardown format in `knowledge-base/README.md`
3. **lead-magnet-outline** — turn a topic into a lead magnet outline (PDF checklist, playbook, template)
4. **welcome-email-iterate** — propose improvements to the welcome email based on reply signal
5. **weekly-review** — scoreboards + experiment results + next week's plan

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
- Chico has produced it at least twice, successfully (Bissuh approved with minimal edits)
- The inputs and outputs are stable enough to document
- The downside of a bad output is small or recoverable

Until then, just do the work directly. Don't premature-systematize.
