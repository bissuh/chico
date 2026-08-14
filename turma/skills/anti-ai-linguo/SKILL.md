---
name: anti-ai-linguo
description: Final-pass voice check that strips AI tells (banned phrases, structural patterns, dashes, pseudo-contrarian hooks, hedged opinions, formatting tics) from any project's public draft. Auto-runs as the LAST review pass before any newsletter, X post, LinkedIn post, IG caption, or video script is marked review-ready, after turma:story-craft and turma:micromagnet-craft. Three modes: long-form (articles), short-form (social), video (scripts). Reads the project's brand.md for brand-specific banned phrases and house style, enforced on top of the universal rules. Skip only for internal notes and any surface brand.md marks owner-only.
---

# anti-ai-linguo

The final voice-check pass on any project's public draft. Three modes share the same banned lists but apply different structural rules.

**Before you start:** read the project's `brand.md` for its banned phrases and house style on top of the universal rules. The universal AI-tell lists and the dash rule below are turma defaults that hold for every project. On top of them, `brand.md` section 6 ("AI tells to strip", "Never say", "Dashes") and section 5 ("two lines that sound WRONG for this brand") add the brand-specific banned phrases and house style. Enforce both layers: the universal set, plus whatever `brand.md` adds. Section 7 ("Channels") tells you which surfaces this project actually ships.

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

Grep for these. Zero matches before review-ready. Grouped so you can scan a draft by family:

**Transitions and throat-clearing:**
- Furthermore, Moreover, Additionally
- In conclusion, Ultimately, At the end of the day
- Indeed, Notably (as sentence starters)
- In today's fast-paced world, In a world where, When it comes to
- Without further ado, It turns out

**Announcements and meta-commentary** (telling the reader what you're about to do instead of doing it):
- It's worth noting, It is important to note
- Let's dive in, Let's unpack, Let's explore, Let's break this down
- Here's what you need to know, Let me walk you through
- In this section we'll, As we'll see, The rest of this piece

**AI verb cluster:**
- Delve into, Dive deep into, Unpack
- Leverage (as a verb), Unleash, Elevate, Empower, Harness
- Foster, Garner, Showcase, Underscore (as a verb)
- Navigate (challenges/uncertainty), Lean into

**Adjective and noun inflation:**
- Robust, Comprehensive, Seamless, Holistic, Streamline
- Game-changer, Game-changing, Paradigm shift, Transformative
- Crucial, Pivotal, Vibrant, Intricate, Enduring
- The [X] landscape, Tapestry (figurative), Interplay, Journey (figurative)
- This is a testament to

**Authority tropes** (pretending to cut through to a deeper truth, then restating an ordinary point):
- At its core, Fundamentally, In reality
- The real question is, What really matters, The deeper issue, The heart of the matter

**Emphasis crutches:**
- Full stop. / Period. (as standalone emphasis)
- Let that sink in, Read that again
- Make no mistake, This matters because, Here's why that matters

**Vague declaratives** (announcing importance without naming the thing):
- The implications are significant, The stakes are high
- The reasons are structural, The consequences are real
- Any "[thing] is [important-adjective]" sentence with no specific behind it. Name the specific or cut the sentence.

**Hedged authority:**
- One could argue, It could be argued
- Experts argue, Industry reports suggest, Observers have noted (name the actual source or cut the claim)

### Brand-specific banned phrases (from brand.md)

Before the final grep, pull `brand.md` section 6 ("AI tells to strip" and "Never say") and section 5 ("two lines that sound WRONG for this brand"). Add every item to the grep alongside the universal list. Same bar: zero matches before review-ready. A brand can ban words the universal list allows (a competitor's name, an in-house cliche that got tired, a claim it can't legally make). When section 6 lists a compliance constraint (no health, financial, or legal claim without a source), treat an unsourced claim of that kind as a banned match too.

### The pseudo-contrarian list

These sound bold but signal AI faking authority. Cut every time:

- "Nobody is talking about..."
- "The thing nobody tells you..."
- "What they don't want you to know..."
- "The harsh truth is..." / "The uncomfortable truth is..."
- "The part everyone misses..."
- "Most people don't realize..."
- "What gurus won't tell you..."
- "Let me be clear..." / "I'm going to be honest..."
- "What if I told you..."

Trust the reader. Just state the thing.

### The structural tells

Words are half the fingerprint. The other half is shape. These structures read as AI even when every individual word is clean:

| Shape | Example | Fix |
|---|---|---|
| Binary contrast | "It's not about X. It's about Y." / "Not because X. Because Y." / "The answer isn't X. It's Y." | State Y directly. One earned contrast per piece, maximum. |
| Negative listing | "Not a trend. Not a hack. A system." | Say the thing. The reader doesn't need the runway. |
| Staccato drama | Three or more clipped fragments in a row. "No prior. No preference. No mercy." | One short sentence lands. A run of them is engineered. |
| Forced rule of three | Every list has exactly three items, every claim three adjectives | Use the natural number. Two is fine. Four is fine. |
| Synonym cycling | "The founder... the entrepreneur... the builder..." for the same person | Repeat the clearest word. Repetition is human. |
| -ing tails | "...grew 40%, highlighting the power of retention" | Cut the tail or make it a real claim with its own evidence. |
| False ranges | "From cold outreach to brand loyalty, from clicks to community" | List the actual things. |
| Copula dodging | "serves as", "stands as", "boasts", "represents" instead of "is" / "has" | Write "is". Write "has". |
| False agency | "The complaint becomes a fix." "The decision emerged." | Name the person. Someone fixed it. Someone decided. |
| Narrator-from-a-distance | "People tend to...", "Nobody designed this." | Put the reader in the scene. "You" beats "people". |
| Aphorism formulas | "Consistency is the currency of trust." "X is the Y of Z." | Replace the fake proverb with the concrete claim it gestures at. |
| Significance inflation | "...marking a pivotal moment in the brand's evolution" | The fact, plain. Cut the ceremony around it. |
| Generic upbeat ending | "The future looks bright. Exciting times ahead." | End on the last concrete fact, or the CTA. Never a send-off. |
| Perfect quotables | Every paragraph closes like a pull-quote | Vary the endings. Earn one quotable per piece, if any. |

### The formatting tells

AI formatting habits that mark a draft even before anyone reads a sentence:

- **Bolded-header bullets** ("**Speed:** the system is fast"). Convert to prose or plain bullets.
- **Boldface sprinkled for emphasis.** Almost none. Let the sentence do the emphasis.
- **Emoji as decoration** (🚀 ✅ ✨ on headings and bullets). Zero, unless `brand.md` explicitly asks.
- **Title Case On Every Heading.** Sentence case by default; `brand.md` can override.
- **Formula sections** ("Challenges", "Future Outlook", "Conclusion" as reflex scaffolding). Keep the facts, cut the template.
- **A heading followed by a one-line restatement of the heading.** Cut the warm-up line; start with the content.

### The dash rule (non-negotiable)

No em dashes (—). No en dashes (–). No unicode dashes of any kind. Use periods, commas, colons, or parens. Or rewrite. ASCII hyphens for true hyphens (compound words, number ranges) are fine. Also catch spaced em dashes and double hyphens (` -- `) doing the same job.

Pre-review grep: `[—–]` must return zero matches.

This is the turma default. If `brand.md` section 6 ("Dashes") explicitly allows them for this project, honor that. Absent an explicit allow, dashes stay off.

### Specificity without fabrication

Every vague claim gets a number, a name, or a specific moment. Or it gets cut.

- "$400M in revenue" beats "massive company"
- "60 people" beats "small team"
- "Day 4. Dashboard at zero." beats "early stage was rough"

The guard: **the specific must come from the source material, the project's own data, or the owner.** If the number doesn't exist, ask for it or write the plain version without it. Never invent a number, name, date, quote, or citation to pass this rule. A fabricated specific is worse than a vague claim: it's a lie that scans well. Same discipline as turma's no-fabricated-params rule, applied to copy.

### Opinions plain

Cut every "I think that," "I believe that," "in my opinion," "perhaps," "potentially," "may." Say what you mean.

- "I don't buy that framing." beats "One could argue that this framing is questionable."

### Clusters, not convictions

One tell is weak evidence. Wikipedia's AI-cleanup project found untrained readers barely beat chance at spotting AI text; what convicts a draft is the pile-up. One "however" is a transition. "However" plus a forced triad plus an -ing tail plus a "Conclusion" section is a confession.

The same judgment protects good writing. Do not gut prose for a single match when the sentence is otherwise doing real work. And when the draft came from a human (Bissuh, a client, a guest), preserve the human signals instead of sanding them off:

- Odd, hard-to-fabricate specifics ("the lawyer who worked upstairs from my dentist")
- Mixed feelings and unresolved tension ("mostly good, still bothers me, can't say why")
- Self-corrections and asides mid-thought
- Era-bound slang and references
- Uneven rhythm, imperfect structure

Over-editing into sterile flatness is its own tell. Voiceless clean is just as obviously machine as slop.

### Tells rot

Every stock phrase list has a shelf life. Phrases this very skill once prescribed as voice anchors are now documented AI tells, because every model learned the same tricks. Retired from this skill's recommendations, strip on sight in public drafts:

- "Here's the thing."
- "Full stop." / "That's it."
- "Read that again. Seriously."
- "Let me break it down."
- "Look." / "Honestly?" as a standalone theatrical opener before an ordinary point

The durable rule: **voice anchors come from the project's `brand.md` sample lines, never from a stock list in this skill.** A phrase pulled from the brand's own mouth can't rot into a generic tell, because it isn't generic. And whenever a new AI-tells source gets mined, run it against this skill's own recommendations first. The craft that doesn't audit itself becomes the slop it polices.

---

## Mode 1: Long-form (articles, newsletter editions, deep dives)

### Paragraph and sentence mechanics
- Maximum 3 sentences per paragraph. Most should be 1-2.
- One-line paragraphs encouraged for emphasis. One at a time, never a run.
- Mix sentence lengths. Short, short, long. Short.
- Cut intensifier adverbs. "Very," "really," "extremely," "quite," "literally," "genuinely." An adverb survives only when it carries information the verb can't ("quietly shipped" earns its place; "truly great" doesn't).

### Voice anchors come from brand.md
Do not decorate the draft with stock personality phrases. Pull anchors from `brand.md` section 5: the sample lines, the register, the two lines that sound RIGHT for this brand. If the brand's voice has a signature move (a recurring word, a way of opening a take), use that. A stock phrase from any skill's list is pre-rotted (see Tells rot).

### The honest-take rule
Any company, tool, or strategy described needs both sides. Pattern:
1. Impressive part with full credit.
2. Flag the turn plainly, in the brand's own words. No drumroll.
3. Specific evidence, not vague concerns.
4. Nuanced close: both things can be true.

### Engagement touchpoints
At least one per major section:
- Direct questions to the reader's situation
- Practical nudges: "Open a tab. Search [X]. 30 seconds."
- Personal asides, parentheticals, brief reactions

### Pre-publish check (long-form)
1. Grep banned phrases (universal plus brand.md). Zero.
2. Grep `[—–]`. Zero.
3. Scan the structural-tells table. No binary-contrast runs, no staccato drama, no -ing tails.
4. No paragraph longer than 3 sentences.
5. Every section has at least one engagement moment.
6. Vague claims replaced with specifics, and every specific traceable to a source.
7. Read aloud. Sounds like a friend talking, not an essay.
8. Run the audit pass (below).

---

## Mode 2: Short-form (X, LinkedIn, IG, Threads)

### The first line rule
The first line must do ONE of:
1. Sharp claim ("Most freemium dies in month 4.")
2. Specific moment ("11pm. You're still tweaking the landing page.")
3. Number that doesn't compute ("3 days. 1 person. $4,200.")

Never start with: "Here's a thread on..." / "Let me share..." / "Today I want to talk about..." / "Have you ever..." / "What if I told you..."

### Length and rhythm
- One idea per line. One line per beat.
- Most lines: 5 to 12 words.
- Break every paragraph. White space is the format.
- One-word lines: at most one per post. ("Wild.") A run of them is manufactured drama.
- Mix line lengths. Three short, one long, one short.

### Thread structure (X / LinkedIn carousel)
1. Hook line.
2. Setup (1-2 lines context).
3. The turn (contradicts the expected story). Write the turn as a claim, not as a "Not X. Y." template; the mechanical contrast is a documented tell.
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
4. Scan the structural-tells table. No "not X, it's Y" turn, at most one one-word line.
5. Every claim has a number, name, or specific moment, traceable to a source.
6. Cut 20% on the second pass.
7. Read aloud. Sounds like a person, not an essay.
8. Run the audit pass (below).

---

## Mode 3: Video (YouTube long-form, Shorts, Reels, TikTok)

### The fundamental shift
You are not writing prose. You are writing speech. Every line must pass the read-aloud test before it ships. Spoken rhythm earns moves that die on paper (a triad, a fragment), but only in small doses; the caps below are the doses.

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

### Repetition is your friend (in speech, in doses)
Patterns that land out loud:
- Triple beat: "It's cheap. It's fast. It works." Maximum one per script; a second one turns the script into a template.
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
- Sentence fragments. Never three in a row (see structural tells: staccato drama holds even out loud).
- Trailing thoughts. "And that's the thing..."
- Restarts. "The thing is. No. The real thing is..."
- One-word reactions. "Wild." "Insane."

### Pre-publish check (video)
1. First 5 seconds (or 2 for Shorts) pass the hook test.
2. Grep banned phrases (universal plus brand.md). Zero.
3. Grep `[—–]`. Zero.
4. Scan the structural-tells table. One triple beat max, no fragment runs.
5. Every sentence is one breath.
6. At least one "you" anchor per 30 seconds.
7. At least one "but" pivot per beat.
8. Read aloud, end to end, without stumbling.
9. Cut 20% on second pass.
10. Run the audit pass (below).

---

## The audit pass (all modes)

After the rewrite, before marking review-ready, read the draft fresh and answer two questions in one or two honest sentences each:

1. **"What here still reads as obviously AI-written?"** Not "does it" but "what does". Something always survives the first pass: a leftover triad, a too-neat closer, a paragraph of uniform mid-length sentences. Fix what you name.
2. **"Does the draft state any fact, number, name, date, or quote that isn't in the source material or the project's data?"** If yes, that's a fabrication even if it sounds better than the vague original. Cut it or ask the owner for the real one.

Then, and only then, run the final greps.

## The single test (all modes)

When in doubt, ask: would the voice in `brand.md` actually say this out loud, to a friend, at the kitchen table?

If no, rewrite it.

---

## Hard rules

- Reads the project's `brand.md` first. The universal banned lists and the dash rule are the floor; `brand.md` section 5 and section 6 stack the brand-specific layer on top. Never hardcode a brand's banned words into this skill.
- Runs LAST. After `turma:story-craft`, after `turma:micromagnet-craft`, after every structural edit. Voice integrity is the last gate, not the first.
- Never fabricates a specific to satisfy the specificity rule. Numbers, names, dates, and quotes come from the source, the project's data, or the owner. No exceptions.
- Judges clusters, not single matches, when deciding how hard to rewrite. Protects human signals in human-written drafts instead of sanding them off.
- Never edits operating canon (`SOUL.md`, `IDENTITY.md`, `CLAUDE.md`, `SPEC.md`, `memory/`). This pass edits the draft, not the project's operating system.
- Skips any surface `brand.md` marks owner-only. That voice is hands-off.
- A pass is not done until the audit pass ran and the banned-phrase grep (universal plus brand.md) and the `[—–]` grep both return zero.

## Sources

The tell catalogs in this skill draw on, and were audited against:

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. The pattern canon, built from thousands of observed instances. Also the source of the cluster principle and the false-positive guard.
- [blader/humanizer](https://github.com/blader/humanizer) by Siqi Chen. The skill-ification of the Wikipedia page; source of the no-fabrication rule, the audit-pass loop, and the preserve-human-signals list.
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) by Hardik Pandya. Source of the structural-tells framing: binary contrasts, negative listing, false agency, narrator-from-a-distance, vague declaratives.

## Related

- The project's `brand.md`. Section 5 (voice) and section 6 (house style / banned) supply the brand-specific layer that stacks on top of the universal rules. Section 7 (channels) says which surfaces this project ships.
- `turma:story-craft`. Runs BEFORE this skill, on persuasive narrative content. anti-ai-linguo is the voice pass after the structural work is done.
- `turma:micromagnet-craft`. Runs alongside this skill on public content. Different question (is there a magnet hiding inside?), same final-pass discipline.
- `turma:name-craft`. Separate use case (naming things). No overlap.
