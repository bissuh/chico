---
description: Audit a project's growth. Reads its brand.md (and any reachable analytics), then returns the 2-3 highest-leverage moves and the single first action to ship.
---

Run a growth audit for the current project.

1. Read `brand.md` (`./brand.md` or `./growth/brand.md`). If none exists, run `turma:positioning` (INTAKE mode) to bootstrap and write `./growth/brand.md` from the project itself, then continue. Don't ask the owner to create the file.
2. Read what's reachable: any analytics the project exposes (a connected connector via `turma:beehiiv-connector` / `turma:youtube-connector`, a Supabase or GA export the owner points you at, the site itself). If little is wired, say so and work from brand.md.
3. Assess the funnel against the primary conversion goal in brand.md: where attention comes from, where it converts, where it leaks.
4. Return:
   - **The state:** one honest paragraph. What's working, what's leaking, what's missing.
   - **The 2-3 highest-leverage moves,** ranked by impact over effort, each tied to a turma skill (story-craft, micromagnet-craft, power-law, ghostshelf, cta-machine, name-craft).
   - **The first action:** the single thing to ship this week. Concrete, with which skill runs it.
5. Offer to run the first action now.

Keep it honest and specific. No vanity metrics, no generic advice. Use the project's real numbers if reachable, say "not wired" if not. No dashes, no AI tells.

$ARGUMENTS
