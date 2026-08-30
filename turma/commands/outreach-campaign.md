---
description: Build a cold outreach campaign end to end. Reads brand.md, defines the list by reason, runs the deliverability and compliance gate, writes the five-line email and the follow-up sequence, and hands back a package that is one approval away from sending.
---

Build a cold outreach campaign for the current project.

Load `turma:outreach-craft` and run it in CAMPAIGN mode. If the ask is one high-stakes message to a single person rather than a campaign, run DOOR-KNOCK mode instead. If an existing campaign is failing, run REVIEW mode.

1. Read `brand.md` (`./brand.md` or `./growth/brand.md`). If none exists, run `turma:positioning` (INTAKE mode) to bootstrap and write `./growth/brand.md` from the project itself, then continue. Don't ask the owner to create the file.
2. **Name the reason before the list.** One sentence: what is true about these people that makes this message worth their time. If you cannot write it, the problem is positioning, not outreach. Say so and stop.
3. **Run the Layer 0 gate.** Sending domain, SPF/DKIM/DMARC, warmup state, list validation, plain text, and the law where the recipients sit. Report each as ready, missing, or unknown. Missing infrastructure is the finding; do not write copy around it and hope.
4. **Build the list by reason,** not by filter. Thirty qualified names beat three thousand rows. One or two contacts per company. Every name carries its own written reason. The list goes in a gitignored path, never in a tracked file.
5. **Write the message and the sequence.** Five lines for the first touch. Four to five touches, widening gaps, each standing alone, news over nudge, an easy out at the end.
6. **Set up the tracking row** before the send: batch, list definition, sent, bounced, replies, positive replies, the scoreboard number from `brand.md`, and the one variable being tested. No open tracking.
7. **Run `turma:anti-ai-linguo` Mode 4** on every message, then the full pre-send gate from the skill. Report each box.
8. Return the package: the reason, the list definition, the infrastructure state with what is still missing, the messages, the tracking table, and the gate.

Outreach is Yellow. It reaches real people under the project's name, so it ships only with the owner's sign-off. Paid tools and domain purchases are Red; ask before spending anything.

$ARGUMENTS
