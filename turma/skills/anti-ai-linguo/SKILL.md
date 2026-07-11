---
name: anti-ai-linguo
description: Final-pass voice check that strips AI tells (banned phrases, dashes, pseudo-contrarian hooks, hedged opinions) from any project's public draft. Auto-runs as the LAST review pass before any newsletter, X post, LinkedIn post, IG caption, or video script is marked review-ready, after turma:story-craft and turma:micromagnet-craft. Three modes: long-form (articles), short-form (social), video (scripts). Reads the project's brand.md for brand-specific banned phrases and house style, enforced on top of the universal rules. Skip only for internal notes and any surface brand.md marks owner-only.
---

# anti-ai-linguo

The final voice-check pass on any project's public draft. Three modes share the same banned list but apply different structural rules.

**Before you start:** read the project's `brand.md` for its banned phrases and house style on top of the universal rules. The universal AI-tell list and the dash rule below are turma defaults that hold for every project. On top of them, `brand.md` section 6 ("AI tells to strip", "Never say", "Dashes") and section 5 ("two lines that sound WRONG for this brand") add the brand-specific banned phrases and house style. Enforce both layers: the universal set, plus whatever `brand.md` adds. Section 7 ("Channels") tells you which surfaces this project actually ships.

**When to run:** as the LAST pass before marking anything review-ready. After `turma:story-craft`, after `turma:micromagnet-craft`, after every structural edit. Voice integrity is the last gate, not the first.

**Skip:** internal notes, working sessions, and any surface `brand.md` marks owner-only (that voice is hands-off).

## Mode selection

Pick by format, not by length. `brand.md` section 7 says which of these channels this project runs; the modes below cover all of them.

- **Long-form.** Articles, newsletter editions, deep dives, lead-magnet pages. Anything meant to be read silently in a feed reader or browser.
- **Short-form.** X threads, X posts, LinkedIn posts, IG captions, Threads posts. Anything that lives inside a social feed.
- **Video.** YouTube long-form scripts, Shorts, Reels, TikTok scripts. Anything that will be read out loud on camera.

If the draft spans formats (e.g. a thread plus a blog post version), run the relevant mode for each separately.

---

## Universal rules (turma defaults, apply to all three modes)

These are the floor. They hold for every project, even one whose `brand.md` says nothing about voice. `brand.md` then stacks its own banned phrases and "never say" list on top. You enforce both.

### The banned phrase list

Grep for these. Zero matches before review-ready:

- Furthermore, Moreover, Additionally
- It's worth noting, It is important to note
- In conclusion, Ultimately, At the end of the day
- Delve into, Dive into, Dive deep into, Unpack, Let's unpack, Let's dive in
- Leverage (as a verb), Unleash, Elevate, Empower
- Robust, Comprehensive, Streamline, Seamless, Holistic
- Game-changer, Game-changing, Paradigm shift
- This is a testament to
- One could argue, It could be argued
- The [X] landscape, Navigate the landscape
- Without further ado
- Indeed, Notably (as sentence starters)
- In today's fast-paced world

### Brand-specific banned phrases (from brand.md)

Before the final grep, pull `brand.md` section 6 ("AI tells to strip" and "Never say") and section 5 ("two lines that sound WRONG for this brand"). Add every item to the grep alongside the universal list. Same bar: zero matches before review-ready. A brand can ban words the universal list allows (a competitor's name, an in-house cliche that got tired, a claim it can't legally make). When section 6 lists a compliance constraint (no health, financial, or legal claim without a source), treat an unsourced claim of that kind as a banned match too.

### The pseudo-contrarian list

These sound bold but signal AI faking authority. Cut every time:

- "Nobody is talking about..."
- "The thing nobody tells you..."
- "What they don't want you to know..."
- "The harsh truth is..."
- "The part everyone misses..."
- "Most people don't realize..."
- "What gurus won't tell you..."

Trust the reader. Just state the thing.

### The dash rule (non-negotiable)

No em dashes (—). No en dashes (–). No unicode dashes of any kind. Use periods, commas, colons, or parens. Or rewrite. ASCII hyphens for true hyphens (compound words, number ranges) are fine.

Pre-review grep: `[—–]` must return zero matches.

This is the turma default. If `brand.md` section 6 ("Dashes") explicitly allows them for this project, honor that. Absent an explicit allow, dashes stay off.

### Specificity over abstraction

Every vague claim gets a number, a name, or a specific moment. Or it gets cut.

- "$400M in revenue" beats "massive company"
- "60 people" beats "small team"
- "Day 4. Dashboard at zero." beats "early stage was rough"

### Opinions plain

Cut every "I think that," "I believe that," "in my opinion," "perhaps," "potentially," "may." Say what you mean.

- "I don't buy that framing." beats "One could argue that this framing is questionable."

---

## Mode 1: Long-form (articles, newsletter editions, deep dives)

### Paragraph and sentence mechanics
- Maximum 3 sentences per paragraph. Most should be 1-2.
- One-line paragraphs encouraged for emphasis.
- Mix sentence lengths. Short, short, long. Short.
- Cut every adverb you can. "Very," "really," "extremely," "quite." Almost always cut.

### Voice anchors (use sparingly, one or two per section)
- "Here's what I think."
- "Let me break it down."
- "Here's the part that matters."
- "Now." (one-word transition)
- "Full stop."
- "That's it."
- "Be honest with yourself."

### The honest-take rule
Any company, tool, or strategy described needs both sides. Pattern:
1. Impressive part with full credit.
2. Transition: "Now the ugly part."
3. Specific evidence, not vague concerns.
4. Nuanced close: "Both things are true."

### Engagement touchpoints
At least one per major section:
- Pause moments: "Read that again. Seriously."
- Direct questions to the reader's situation
- Practical nudges: "Open a tab. Search [X]. 30 seconds."
- Personal asides, parentheticals, brief reactions

### Pre-publish check (long-form)
1. Grep banned phrases (universal plus brand.md). Zero.
2. Grep `[—–]`. Zero.
3. No paragraph longer than 3 sentences.
4. Every section has at least one engagement moment.
5. Vague claims replaced with specifics.
6. Read aloud. Sounds like a friend talking, not an essay.

---

## Mode 2: Short-form (X, LinkedIn, IG, Threads)

### The first line rule
The first line must do ONE of:
1. Sharp claim ("Most freemium dies in month 4.")
2. Specific moment ("11pm. You're still tweaking the landing page.")
3. Number that doesn't compute ("3 days. 1 person. $4,200.")

Never start with: "Here's a thread on..." / "Let me share..." / "Today I want to talk about..." / "Have you ever..."

### Length and rhythm
- One idea per line. One line per beat.
- Most lines: 5 to 12 words.
- Break every paragraph. White space is the format.
- One-word lines are fine. ("Wild.") ("Same.") ("Stop.")
- Mix line lengths. Three short, one long, one short.

### Thread structure (X / LinkedIn carousel)
1. Hook line.
2. Setup (1-2 lines context).
3. The turn (contradicts the expected story).
4. The proof (numbers, names, specific moment).
5. The lesson (one line, plain).
6. The ask (reply, follow, or click. ONE CTA).

Never end with "What do you think?" Ask a specific question or none at all.

### Platform-specific
- **X tweet 1 must work alone.** If only T1 got seen, would it still land?
- **LinkedIn drafts always run 30-40% too long.** Force-cut 20% on second pass.
- **IG captions:** front-load the hook in the first 125 characters (the visible-before-"more" zone).

### Pre-publish check (short-form)
1. First line passes hook test.
2. Grep banned phrases (universal plus brand.md). Zero.
3. Grep `[—–]`. Zero.
4. Every claim has a number, name, or specific moment.
5. Cut 20% on the second pass.
6. Read aloud. Sounds like a person, not an essay.

---

## Mode 3: Video (YouTube long-form, Shorts, Reels, TikTok)

### The fundamental shift
You are not writing prose. You are writing speech. Every line must pass the read-aloud test before it ships.

### The first 5 seconds (or 2 seconds for Shorts)
First beat must do ONE of:
1. Contradiction ("I built $300K with no employees. Here's the part that almost killed it.")
2. Specific moment ("Day 4. Dashboard at zero. I'm refreshing it like an idiot.")
3. Promise ("Next 90 seconds, the exact spreadsheet that made me $42K.")
4. Pattern break ("Everyone tells you to find your niche. They're wrong.")

Never start with: "Hey guys" / "What's up everyone" / "In today's video" / "I want to talk about" / "So a lot of people ask me"

### Sentence length is breath length
- Most lines: 8 to 15 words.
- If you can't read it in one breath without rushing, break it.
- Each punctuation mark is a breath instruction.

### Repetition is your friend (in speech)
Patterns that land:
- Triple beat: "It's cheap. It's fast. It works."
- Echo: "The product was fine. The product was always fine. The problem was nobody knew."
- Setup and payoff: "She said it would take a month. It took a month."

### The "you" anchor
Every 20-30 seconds, return to "you":
- "You know that feeling when..."
- "You've done this. I've done this."
- "Look at your last 7 days. How much was actually shipping?"

### The "but" pivot
Every video needs at least one. Setup the expected read. Then "But." Then the real read.

### Cut every sentence that doesn't move the story
Especially cut:
- "So as I was saying..."
- "Now, going back to..."
- "Before I get to that, let me mention..."
- Sentences that announce what you're about to do instead of doing it.

### Short-form video specific (under 60s)
- Hook in 2 seconds.
- ONE idea. Cut everything else.
- 90-120 words for 60s. 45-60 words for 30s.
- End with a hard stop. Last 3 words land. Cut.
- Never "follow for more." Make them want to.

### Long-form video specific (10-25 min, YouTube)
- Chapter the script every 2-4 minutes.
- Chapter 1 MUST end with unresolved tension that pulls them to chapter 2. Never resolve early.
- Every 90 seconds, ask: would I still be watching? If no, beat shift, story, hard stop.
- Don't summarize what you just said.
- End with one specific question, not "let me know what you think."
- Frame success around AVD (average view duration) and watch time, not raw views.

### Speech patterns that humanize
Use sparingly (1-2 per minute):
- Sentence fragments.
- Trailing thoughts. "And that's the thing..."
- Restarts. "The thing is. No. The real thing is..."
- One-word reactions. "Wild." "Insane."
- Filler that breathes. ("Now.") ("Look.")

### Pre-publish check (video)
1. First 5 seconds (or 2 for Shorts) pass the hook test.
2. Grep banned phrases (universal plus brand.md). Zero.
3. Grep `[—–]`. Zero.
4. Every sentence is one breath.
5. At least one "you" anchor per 30 seconds.
6. At least one "but" pivot per beat.
7. Read aloud, end to end, without stumbling.
8. Cut 20% on second pass.

---

## The single test (all modes)

When in doubt, ask: would the voice in `brand.md` actually say this out loud, to a friend, at the kitchen table?

If no, rewrite it.

---

## Hard rules

- Reads the project's `brand.md` first. The universal banned list and the dash rule are the floor; `brand.md` section 5 and section 6 stack the brand-specific layer on top. Never hardcode a brand's banned words into this skill.
- Runs LAST. After `turma:story-craft`, after `turma:micromagnet-craft`, after every structural edit. Voice integrity is the last gate, not the first.
- Never edits operating canon (`SOUL.md`, `IDENTITY.md`, `CLAUDE.md`, `SPEC.md`, `memory/`). This pass edits the draft, not the project's operating system.
- Skips any surface `brand.md` marks owner-only. That voice is hands-off.
- A pass is not done until the banned-phrase grep (universal plus brand.md) and the `[—–]` grep both return zero.

## Related

- The project's `brand.md`. Section 5 (voice) and section 6 (house style / banned) supply the brand-specific layer that stacks on top of the universal rules. Section 7 (channels) says which surfaces this project ships.
- `turma:story-craft`. Runs BEFORE this skill, on persuasive narrative content. anti-ai-linguo is the voice pass after the structural work is done.
- `turma:micromagnet-craft`. Runs alongside this skill on public content. Different question (is there a magnet hiding inside?), same final-pass discipline.
- `turma:name-craft`. Separate use case (naming things). No overlap.
