# S-Tier SaaS Dashboard Design Checklist (Inspired by Stripe, Airbnb, Linear)

## I. Core Design Philosophy & Strategy

- [ ] **Users First:** Prioritize user needs, workflows, and ease of use in every design decision.
- [ ] **Meticulous Craft:** Aim for precision, polish, and high quality in every UI element and interaction.
- [ ] **Speed & Performance:** Design for fast load times and snappy, responsive interactions.
- [ ] **Simplicity & Clarity:** Strive for a clean, uncluttered interface. Ensure labels, instructions, and information are unambiguous.
- [ ] **Focus & Efficiency:** Help users achieve their goals quickly and with minimal friction. Minimize unnecessary steps or distractions.
- [ ] **Consistency:** Maintain a uniform design language (colors, typography, components, patterns) across the entire dashboard.
- [ ] **Accessibility (WCAG AA+):** Design for inclusivity. Ensure sufficient color contrast, keyboard navigability, and screen reader compatibility.
- [ ] **Opinionated Design (Thoughtful Defaults):** Establish clear, efficient default workflows and settings, reducing decision fatigue for users.
- [ ] **Emphasis Where It Matters:** Add visual weight only to elements that truly need attention. When unsure, opt for simplicity over flashiness.
- [ ] **Visual Pattern Reuse:** Reuse visual patterns to create connections between related UI elements and reinforce consistency.

## II. Design System Foundation (Tokens & Core Components)

- [ ] **Define a Color Palette:**
  - [ ] **Primary Brand Color:** User-specified, used strategically.
  - [ ] **Derive a Ramp From the Primary:** Lighten the primary for subtle backgrounds and darken it for text and borders — this alone adds cohesive color to an otherwise drab design and gets you most of the way to a full ramp (the tints and shades larger teams use for chips, states, and charts).
  - [ ] **Neutrals:** A scale of grays (5-7 steps) for text, backgrounds, borders.
  - [ ] **Semantic Colors:** Define specific colors for Success (green), Error/Destructive (red), Warning (yellow/amber), Informational (blue).
  - [ ] **Dark Mode Palette:** Create a corresponding accessible dark mode palette.
  - [ ] **Accessibility Check:** Ensure all color combinations meet WCAG AA contrast ratios.
  - [ ] **The 60/30/10 Rule:** Apply color in balanced proportions:
    - 60% neutral color (white, light gray) for backgrounds
    - 30% complementary color (black, dark tones) for text and secondary elements
    - 10% main brand/accent color for CTAs and key highlights
    - Reserve strong colors (red, bright accents) only for elements that truly need attention
- [ ] **Establish a Typographic Scale:**
  - [ ] **Primary Font Family:** Choose a clean, legible sans-serif font (e.g., Inter, Manrope, system-ui).
  - [ ] **Maximum 4 Font Sizes:** Limit to 4 distinct sizes per screen/component to maintain hierarchy without visual noise.
  - [ ] **Maximum 2 Font Weights:** Use only 2 weights (e.g., Regular and SemiBold) to create contrast while keeping the design clean.
  - [ ] **Line Height:** Ensure generous line height for readability (e.g., 1.5-1.7 for body text).
  - [ ] **Monospace for Numbers:** Consider monospace or tabular figures for numerical data to prevent layout shifts when values change.
  - [ ] **One Font Family Is Usually Enough:** A single well-chosen sans-serif (see Primary Font Family above) covers almost any interface. Don't burn design time hunting typefaces — pick one and build hierarchy with size, weight, and spacing instead.
  - [ ] **Tighten Large Text (Pro-Polish Trick):** For headings and other large type, reduce letter-spacing to roughly -2% to -3% and drop line-height to ~110–120%. Loose tracking is what makes big text read as amateur; tightening it instantly looks more professional. Leave body text at its default tracking and generous line-height.
  - [ ] **Size Count Scales With Density:** How many distinct sizes you need grows with the surface. Content/landing pages can span up to ~6 sizes across a wide range; dense dashboards shrink dramatically and rarely exceed ~24px because information density carries the hierarchy.
- [ ] **Define Spacing Units (8-Point Grid System):**
  - [ ] **Base Unit:** Establish 8px as the base unit.
  - [ ] **Strict Divisibility:** All spacing values MUST be divisible by 8 or 4. Use 24px instead of 25px, 12px instead of 11px.
  - [ ] **Spacing Scale:** Use multiples of the base unit for all padding, margins, and layout spacing (4px, 8px, 12px, 16px, 24px, 32px, 40px, 48px).
  - [ ] **Why Multiples (The Halving Rule):** Multiples of the base aren't inherently prettier — they let you cleanly split any value in half (32→16→8→4), which is what keeps spacing consistent as components nest. Step down to a 4px sub-grid for tight, dense elements (icons, chips, compact inputs).
- [ ] **Define Border Radii:**
  - [ ] **Consistent Values:** Use a small set of consistent border radii (e.g., Small: 4-6px for inputs/buttons; Medium: 8-12px for cards/modals).
- [ ] **Develop Core UI Components (with consistent states: default, hover, active, focus, disabled):**
  - [ ] Buttons (primary, secondary, tertiary/ghost, destructive, link-style; with icon options)
  - [ ] Input Fields (text, textarea, select, date picker; with clear labels, placeholders, helper text, error messages)
  - [ ] Checkboxes & Radio Buttons
  - [ ] Toggles/Switches
  - [ ] Cards (for content blocks, multimedia items, dashboard widgets)
  - [ ] Tables (for data display; with clear headers, rows, cells; support for sorting, filtering)
  - [ ] Modals/Dialogs (for confirmations, forms, detailed views)
  - [ ] Navigation Elements (Sidebar, Tabs)
  - [ ] Badges/Tags (for status indicators, categorization)
  - [ ] Tooltips (for contextual help)
  - [ ] Progress Indicators (Spinners, Progress Bars)
  - [ ] Icons (use a single, modern, clean icon set; SVG preferred)
  - [ ] Avatars

## III. Layout, Visual Hierarchy & Structure

- [ ] **Responsive Grid System:** Design based on a responsive grid (e.g., 12-column) for consistent layout across devices.
  - [ ] **Grids Are Guidelines, Not Laws:** Not every element must snap to 12 columns or an exact 8px gap — custom landing pages routinely break the grid, and that's fine. Grids earn their keep on highly structured, repeating content (galleries, feeds, blogs), where they define responsive behavior: ~12 columns on desktop, 8 on tablet, 4 on mobile.
- [ ] **Strategic White Space:** Use ample negative space to improve clarity, reduce cognitive load, and create visual balance.
- [ ] **Clear Visual Hierarchy:** Guide the user's eye using typography (size, weight, color), spacing, and element positioning.
  - [ ] **Three Levers — Size, Position, Color:** Hierarchy is built almost entirely from these three. A flat grid of label/value pairs reads like a spreadsheet, not a design, until you vary them.
  - [ ] **Contrast Is What Creates Hierarchy:** It's the *difference* — big vs. small, colorful vs. muted, top vs. bottom — that ranks elements. When everything is emphasized, nothing is.
  - [ ] **Practical Moves:** Lead with an image (adds color, makes scanning easy); make the single most important element large, bold, and near the top; set a key value apart (e.g., right-align and color the price) so the eye jumps to it; and replace flat "from / to" text with an icon plus a connecting line to *show* the relationship instead of stating it.
- [ ] **Consistent Alignment:** Maintain consistent alignment of elements.
- [ ] **Main Dashboard Layout:**
  - [ ] Persistent Left Sidebar: For primary navigation between modules.
  - [ ] Content Area: Main space for module-specific interfaces.
  - [ ] (Optional) Top Bar: For global search, user profile, notifications.
- [ ] **Mobile-First Considerations:** Ensure the design adapts gracefully to smaller screens.

## IV. Copywriting & Microcopy

- [ ] **Communicate More with Less:** Every word must earn its place. Remove filler and redundancy.
- [ ] **Avoid Repetition:** Don't repeat context already visible elsewhere (e.g., don't write "last 10 votes" when there's already a "Voting" label above).
- [ ] **Reduce Cognitive Load:** Clear, concise labels reduce visual clutter without sacrificing clarity.
- [ ] **Action-Oriented Labels:** Use verbs for buttons (Save, Submit, Cancel) and clear nouns for navigation.
- [ ] **Consistent Terminology:** Use the same term for the same concept throughout the app.

## V. Interaction Design & Animations

- [ ] **Purposeful Micro-interactions:** Use subtle animations and visual feedback for user actions (hovers, clicks, form submissions, status changes).
  - [ ] Feedback should be immediate and clear.
  - [ ] Animations should be quick (150-300ms) and use appropriate easing (e.g., ease-in-out).
- [ ] **Loading States:** Implement clear loading indicators (skeleton screens for page loads, spinners for in-component actions).
- [ ] **Transitions:** Use smooth transitions for state changes, modal appearances, and section expansions.
- [ ] **Avoid Distraction:** Animations should enhance usability, not overwhelm or slow down the user.
- [ ] **Keyboard Navigation:** Ensure all interactive elements are keyboard accessible and focus states are clear.
- [ ] **Cinematic Thinking (The Senior Rule):** Don't design static screens in isolation. Piece screens together with motion and transitions to create memorable, delightful experiences. Think of UI as a movie, not a slideshow. (Reference: Phantom Wallet, Airbnb, Duolingo).

## VI. Specific Module Design Tactics

### A. Multimedia Moderation Module

- [ ] **Clear Media Display:** Prominent image/video previews (grid or list view).
- [ ] **Obvious Moderation Actions:** Clearly labeled buttons (Approve, Reject, Flag, etc.) with distinct styling (e.g., primary/secondary, color-coding). Use icons for quick recognition.
- [ ] **Visible Status Indicators:** Use color-coded Badges for content status (Pending, Approved, Rejected).
- [ ] **Contextual Information:** Display relevant metadata (uploader, timestamp, flags) alongside media.
- [ ] **Workflow Efficiency:**
  - [ ] Bulk Actions: Allow selection and moderation of multiple items.
  - [ ] Keyboard Shortcuts: For common moderation actions.
- [ ] **Minimize Fatigue:** Clean, uncluttered interface; consider dark mode option.

### B. Data Tables Module (Contacts, Admin Settings)

- [ ] **Readability & Scannability:**
  - [ ] Smart Alignment: Left-align text, right-align numbers.
  - [ ] Clear Headers: Bold column headers.
  - [ ] Zebra Striping (Optional): For dense tables.
  - [ ] Legible Typography: Simple, clean sans-serif fonts.
  - [ ] Adequate Row Height & Spacing.
- [ ] **Interactive Controls:**
  - [ ] Column Sorting: Clickable headers with sort indicators.
  - [ ] Intuitive Filtering: Accessible filter controls (dropdowns, text inputs) above the table.
  - [ ] Global Table Search.
- [ ] **Large Datasets:**
  - [ ] Pagination (preferred for admin tables) or virtual/infinite scroll.
  - [ ] Sticky Headers / Frozen Columns: If applicable.
- [ ] **Row Interactions:**
  - [ ] Expandable Rows: For detailed information.
  - [ ] Inline Editing: For quick modifications.
  - [ ] Bulk Actions: Checkboxes and contextual toolbar.
  - [ ] Action Icons/Buttons per Row: (Edit, Delete, View Details) clearly distinguishable.

### C. Configuration Panels Module (Microsite, Admin Settings)

- [ ] **Clarity & Simplicity:** Clear, unambiguous labels for all settings. Concise helper text or tooltips for descriptions. Avoid jargon.
- [ ] **Logical Grouping:** Group related settings into sections or tabs.
- [ ] **Progressive Disclosure:** Hide advanced or less-used settings by default (e.g., behind "Advanced Settings" toggle, accordions).
- [ ] **Appropriate Input Types:** Use correct form controls (text fields, checkboxes, toggles, selects, sliders) for each setting.
- [ ] **Visual Feedback:** Immediate confirmation of changes saved (e.g., toast notifications, inline messages). Clear error messages for invalid inputs.
- [ ] **Sensible Defaults:** Provide default values for all settings.
- [ ] **Reset Option:** Easy way to "Reset to Defaults" for sections or entire configuration.
- [ ] **Microsite Preview (If Applicable):** Show a live or near-live preview of microsite changes.

## VII. User Flow Design

- [ ] **Map the Full Flow Before Designing:** Sketch every screen as boxes. Identify every path the user can take before placing a single component.
- [ ] **Escape Hatches:** Always provide:
  - [ ] Skip buttons for optional steps.
  - [ ] Back buttons on every screen.
  - [ ] Search bars on any filtering or selection screen.
- [ ] **Empty States:** Design what every screen looks like with no data. Never leave a blank screen.
- [ ] **Edge-Case States:** Cover loading, error, success, and partially-loaded states for every view.
- [ ] **Utility Icons:** Add filter icons on search bars, save buttons in headers, and similar affordances proactively.
- [ ] **Navigation Completeness:** Verify every section has navigation links to related sections. No dead ends.

> A complete flow covers the happy path AND every exception. If a user can get stuck, they will.

## VIII. Visual Effects — Use Sparingly

- [ ] **Gradients:**
  - [ ] Avoid multi-color gradients (e.g., blue + green). They feel amateur.
  - [ ] If a gradient is needed, use variations of a single hue (e.g., light green → dark green).
  - [ ] Default choice: no gradient. A flat, confident color almost always looks cleaner.
- [ ] **Drop Shadows:**
  - [ ] Never ship default shadows as-is. Change shadow color from black to a soft gray and increase blur radius.
  - [ ] Prefer removing the shadow entirely. Use spacing or background contrast for separation instead.
  - [ ] **Scale strength to elevation:** the higher an element floats, the stronger the shadow. Resting cards need only a whisper; content stacked above other content (popovers, menus, dialogs) needs a deeper, softer shadow to read as lifted.
  - [ ] **Combine inner and outer shadows** for tactile, physical controls — e.g., a raised, pressable button.
  - [ ] **The notice test:** if the shadow is the first thing you see on a design, it's too strong.
- [ ] **Effect Audit Checklist:**
  - [ ] Does this gradient add clarity or just decoration? If decoration → remove it.
  - [ ] Does this shadow define depth or just add noise? If noise → remove it.
  - [ ] Does this glow/border/stroke help the user or is it residual styling? If residual → remove it.

> Every effect must earn its place. If removing it doesn't hurt usability, remove it.

## IX. Spacing — Practical Heuristics

- [ ] **Mobile-Specific Spacing:** On mobile, you need more breathing room than you think. If it looks too spaced out on your design screen, it's probably right on the actual device.
- [ ] **Vertical Rhythm:** For stacked/list content, increase vertical spacing between items. Group related items closer together; separate unrelated items further apart.
- [ ] **Component-Level Spacing:**
  - [ ] Use auto-layout (or flexbox/grid in code) for all repeating components like cards, chips, tags.
  - [ ] Adjust internal padding (horizontal and vertical) to feel neither cramped nor empty.
  - [ ] Repeat the same spacing logic across all components for consistency.

> Your first instinct is always too tight. Double it.

## X. Icon Usage Rules

- [ ] **Scan-First Design:** Add icons to cards, list items, and categories so users can scan visually instead of reading every label.
- [ ] **Size Icons to the Text Beside Them:** Default icon sizes are usually too big. Match the icon to the line-height of the adjacent text (e.g., 24px text → 24px icon), then tighten the gap so icon and label read as a single unit.
- [ ] **Single Library Per Zone:** All icons in the same context must share fill/stroke style, line weight, and corner style. Import from a single package per component area.
- [ ] **Labels and Tooltips:**
  - [ ] Widely understood icons (house, bookmark, user, search) → no label needed.
  - [ ] Ambiguous or uncommon icons → add a label or tooltip, especially during onboarding.
  - [ ] Never use non-standard icons without guidance.
- [ ] **Style Mixing:** Different icon styles may coexist only if they are in visually distinct zones (e.g., navbar vs. category vs. content). Never mix styles within the same component or section.

> A user should never have to think about what an icon means. If they do, it's either wrong or missing a label.

## XI. Redundancy Removal

- [ ] **Audit Every Element:** Ask for each element: *Is this telling the user something they don't already know, or guiding them somewhere they can't go otherwise?*
- [ ] **Common Redundancies to Remove:**
  - [ ] Swipe arrows on mobile carousels (swiping is standard behavior).
  - [ ] Decorative arrows that don't navigate anywhere.
  - [ ] Strokes/borders on cards that already have background contrast.
  - [ ] Repeated CTAs for the same action on the same screen.
- [ ] **Keep vs. Remove Guide:**

| Element | Keep If | Remove If |
|---|---|---|
| Arrows | Navigate to a non-obvious destination | User can swipe or the destination is obvious |
| Borders/Strokes | Creating contrast where background is identical | Element already has contrast via color/shadow/spacing |
| Labels | Icon is ambiguous or uncommon | Icon is universally understood |
| Secondary CTAs | Genuinely different action from primary | Just a dimmer version of the primary button |

> Simplify until it breaks, then add one thing back. Stop there.

## XII. Interactive Feedback

- [ ] **State Checklist for Every Interactive Element:** Every button, input, toggle, and tappable element must have:
  - [ ] Default — idle state.
  - [ ] Hover — visual change on mouse-over (web).
  - [ ] Active/Pressed — visual feedback on click/tap.
  - [ ] Disabled — visually distinct, non-interactive state.
  - [ ] Loading — spinner, skeleton, or progress indicator when waiting for a response.
- [ ] **Inputs Demand the Most States:** Beyond default, a text input needs a clear focus state when clicked into, an error state (red border plus an explanatory message), and — for soft/optional problems — a warning state. Never fail silently.
- [ ] **Button Anatomy:** A comfortable button pads to roughly a 2:1 width-to-height ratio (horizontal padding ≈ the button's height). Navigation links are really "ghost" buttons — no background until hovered; isolate and center one and it becomes a standalone secondary button. Pair a solid primary with a ghost/secondary CTA when you place two side by side.
- [ ] **Timing Thresholds:**
  - [ ] Every action needs a visible reaction within **100ms**. If nothing visually changes, there's a feedback problem.
  - [ ] If an action triggers a network request or transition that takes > **300ms**, provide a loading indicator.
- [ ] **Micro-Interaction Polish:**
  - [ ] Toggling a save/bookmark icon → fill the icon AND update a counter or badge.
  - [ ] Form submission → show inline success or error feedback, not just a toast.
  - [ ] Navigation transitions → animate between screens for spatial context.
  - [ ] Copy-to-clipboard → hover and press feedback alone don't tell the user it worked; slide in a small "Copied" chip to confirm the result. Micro-interactions like this range from purely practical confirmations to playful delight.

> If a user can click it and nothing visually changes within 100ms, you have a feedback problem.

## XIII. Chart & Data Visualization

- [ ] **Common Mistakes to Avoid:**
  - [ ] Missing vertical axis — users cannot read values.
  - [ ] Rounded bar tops — visual ambiguity about where the bar ends.
  - [ ] More data points than categories make sense (e.g., 16 bars for 7 days).
  - [ ] Overdesigning with gradients, shadows, or 3D effects on data.
- [ ] **Best Practices:**
  - [ ] Always include axis labels (both X and Y).
  - [ ] Use flat, squared bar tops for bar charts.
  - [ ] Match data points to actual data categories.
  - [ ] Strip all decoration that doesn't encode data: no gradients on bars, no heavy grid lines, minimal chart borders.
- [ ] **Readability Test:** Can the user read the answer in 3 seconds? If not, simplify.

> The most functional chart is almost always the most minimal chart. Let the data speak.

## XIV. Pre-Ship Checklist

Before shipping any interface, validate:

- [ ] **Flow** — Every screen has exit points, empty states, and edge-case states covered.
- [ ] **Effects** — All gradients, shadows, and glows are intentional and minimal.
- [ ] **Spacing** — Grid is applied. Vertical rhythm is consistent. Nothing feels cramped.
- [ ] **Consistency** — Corner radii, button styles, and input fields are identical across contexts.
- [ ] **Icons** — Single library per zone. Ambiguous icons have labels. Decorative icons removed.
- [ ] **Redundancy** — Every element was questioned. Nothing decorates for decoration's sake.
- [ ] **Feedback** — Every interactive element has hover, active, loading, and disabled states.
- [ ] **Charts** — Axes labeled. No over-designed visual effects. Data legible in under 3 seconds.
- [ ] **Copy** — Every word earns its place. No filler, no repetition.
- [ ] **Signifiers** — Interactive elements advertise themselves; nothing relies on an instruction that a visual cue could carry.
- [ ] **Hierarchy** — Size, position, and color rank the content; the most important element wins the eye in under a second.
- [ ] **Dark Mode** — If shipped, depth comes from surface lightness (not shadows), borders are softened, and contrast is re-verified.
- [ ] **Overlays** — Text over media uses a gradient scrim (not a flat wash) and stays legible on the busiest image in the set.

## XV. CSS & Styling Architecture

- [ ] **Choose a Scalable CSS Methodology:**
  - [ ] **Utility-First (Recommended for LLM):** e.g., Tailwind CSS. Define design tokens in config, apply via utility classes.
  - [ ] **BEM with Sass:** If not utility-first, use structured BEM naming with Sass variables for tokens.
  - [ ] **CSS-in-JS (Scoped Styles):** e.g., Stripe's approach for Elements.
- [ ] **Integrate Design Tokens:** Ensure colors, fonts, spacing, radii tokens are directly usable in the chosen CSS architecture.
- [ ] **Maintainability & Readability:** Code should be well-organized and easy to understand.
- [ ] **Performance:** Optimize CSS delivery; avoid unnecessary bloat.

## XVI. General Best Practices

- [ ] **Iterative Design & Testing:** Continuously test with users and iterate on designs.
- [ ] **Clear Information Architecture:** Organize content and navigation logically.
- [ ] **Responsive Design:** Ensure the dashboard is fully functional and looks great on all device sizes (desktop, tablet, mobile).
- [ ] **Documentation:** Maintain clear documentation for the design system and components.

## XVII. Signifiers & Affordances

Good UI explains itself. An *affordance* is what an element lets you do; a *signifier* is the visual cue that advertises it. When the signifiers are right, you rarely need written instructions — the interface shows the user how it works.

- [ ] **Group With Containers:** A container drawn around a set of items signals "these belong together" (and, by omission, what doesn't). Grouping is the cheapest way to communicate relationships.
- [ ] **Show Selection & Toggles:** A container or highlight around one option in a set reads as "selected" and implies the user can toggle to the others.
- [ ] **Signal Disabled State:** Graying an element out signifies it's inactive and won't respond — no explanation required.
- [ ] **Advertise Interactivity:** Press/active states, highlighted active nav items, hover states, and tooltips all signify that something is interactive and hint at what it will do. Every interactive element should carry at least one such cue.
- [ ] **Color as a Signifier (Semantic Color):** Meaningful color is a signifier too — blue for trust/links, red for danger or urgency, yellow for warning, green for success. Use color for purpose, not decoration (see Section II).

> If you're about to write a label explaining how something works, first ask whether a signifier could show it instead.

## XVIII. Dark Mode Design

Dark mode is not "invert the light theme." The rules of depth and contrast change.

- [ ] **Soften Borders:** A border that looked right on a light background is usually too harsh on dark. Lower its contrast against the surface.
- [ ] **Build Depth With Lightness, Not Shadow:** Shadows barely register on dark backgrounds. Signal elevation by making raised surfaces (cards, sheets) *lighter* than the background rather than by casting a shadow.
- [ ] **Tame Saturated Fills:** Bright chips and badges vibrate against dark. Dim their saturation and brightness for the fill, and invert the relationship for the text (lighter text on the dimmed fill) to preserve hierarchy.
- [ ] **Widen the Hue Range:** Dark UIs aren't limited to navy and gray — deep purples, reds, and greens all work as surface tints and add character.
- [ ] **Re-Check Contrast:** Text and semantic colors that passed WCAG on light backgrounds must be re-verified against dark surfaces.

## XIX. Image & Media Overlays

Text placed over photography or video is a common failure point — get it wrong and you ruin both the image and the legibility. Especially relevant to media-rich screens (recipe cards, class thumbnails, hero images).

- [ ] **Avoid the Flat Scrim:** A full-screen, semi-opaque overlay makes text readable but flattens and dulls the image beneath it.
- [ ] **Prefer a Gradient Scrim:** Use a linear gradient that stays transparent over the focal part of the image and ramps to an opaque, text-safe color exactly where the text sits. The image stays vivid; the text stays legible.
- [ ] **Progressive Blur (Optional Polish):** Layering a progressive blur over the gradient — sharp at one edge, softly blurred behind the text — gives a more modern, premium finish.
- [ ] **Verify on Real Content:** Test the overlay against the lightest and busiest images in your set, not just a convenient dark one.
