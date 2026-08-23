# turma/TOOLS.md

The tool registry. Every external tool a turma skill names, in one place, with what it costs and how confident we are about that.

It exists for three reasons. Skills kept naming tools inline, so the same tool got described three different ways in three files. Cost is a permission question, not a footnote: **every paid tool is Red and needs the owner's sign-off before anyone subscribes.** And a price quoted from memory is a fabricated parameter, which is the one thing turma never ships.

## How to read this

**Cost** is what we actually verified, with the date we verified it. **Status** is one of:

- `verified` we checked the vendor's own page on the date shown.
- `free` no payment path at all, or a free tier that covers the use the skill describes.
- `unverified` the tool is real and the skill names it, but nobody has confirmed the current price. Never quote a number from an `unverified` row to an owner. Check first.

Prices move. A row older than a few months is a hint, not a fact.

## Adding a tool

Add it when a skill starts recommending it, not before. One row, the vendor's own URL, the price from the vendor's own page with today's date, and the skills that use it. If you cannot verify the price in one visit, write `unverified` and say so in the skill too.

Never add a tool because it looks useful. This registry tracks what the craft actually uses.

---

## Free

| Tool | What it does | Used by |
| --- | --- | --- |
| [Apple Search Ads](https://ads.apple.com/) (Campaign Management API) | The only first-party App Store keyword volume signal. Search Popularity, 5 to 100, exponential scale. Reading the data is free; running ads is not | `aso-strategy` |
| [App Store Connect](https://appstoreconnect.apple.com/) | First-party app analytics, impressions, product page conversion rate, and Product Page Optimization A/B tests | `aso-strategy` |
| [Google Play Console](https://play.google.com/console) | First-party Android equivalent, plus store listing experiments | `aso-strategy` |
| [Google Search Console](https://search.google.com/search-console) | Organic queries, positions, impressions, clicks. The data the opportunity scorer runs on | `seo-strategy`, `search-console-connector` |
| [Google Trends](https://trends.google.com/) | Rising and breakout queries, and whether interest is real or one platform's bubble | `ghostshelf`, `seo-strategy` |
| [TikTok Creative Center](https://ads.tiktok.com/business/creativecenter) | Official trend discovery: hashtags, songs, creators, top ads, keyword insights. The best free read on what is spiking | `ghostshelf` |
| [F5Bot](https://f5bot.com/) | Free keyword alerts on Reddit and Hacker News. Finds the threads worth commenting in | `seo-strategy` |
| [dotchk](https://github.com/dotchk/dotchk) | Fast NS-record domain availability checker, installed via `cargo install dotchk`. Always WHOIS-verify before purchase | `name-craft` |

## Paid, verified

| Tool | What it does | Cost | Verified | Used by |
| --- | --- | --- | --- | --- |
| [Astro](https://tryastro.app/) | macOS ASO app for the Apple App Store. Unlimited keyword tracking across 60+ countries, popularity and difficulty pulled from Apple Search Ads, competitor keyword extraction, DeepL translations. Built for indie developers, which is why it is the default recommendation over an enterprise seat | $9/month billed annually, $108/year, single Mac license. Requires macOS 14+ | 2026-08-22 | `aso-strategy` |

## Paid, price unverified

Named by a skill, real, but nobody has confirmed the current price. Check the vendor's page before quoting anything.

| Tool | What it does | Used by |
| --- | --- | --- |
| [DataForSEO](https://dataforseo.com/) | Pay-as-you-go SERP and keyword APIs. The low-cost way to get search volume and difficulty without a full seat | `seo-strategy` |
| [Ahrefs](https://ahrefs.com/), [SEMrush](https://www.semrush.com/) | The premium keyword and backlink suites. Fast, and priced like it | `seo-strategy` |
| [Otterly.ai](https://otterly.ai/), Promptmonitor, Peec | Track whether AI answers cite the project | `seo-strategy` |
| [Postiz](https://postiz.com/) | Open-source social scheduling with an MCP server. Self-hostable, which changes the cost question | `ghostshelf`, `cta-machine` |
| [Canva](https://www.canva.com/), [Midjourney](https://www.midjourney.com/), [Ideogram](https://ideogram.ai/) | Visual production: batch design, image generation, text-in-image | `ghostshelf`, `thumbnail-craft`, `carousels` |
| [Metricool](https://metricool.com/), [Later](https://later.com/) | Social scheduling and analytics | `ghostshelf` |
| [beehiiv](https://www.beehiiv.com/) | Newsletter platform. turma ships a read-only connector for it | `beehiiv-connector` |
| [Remotion](https://www.remotion.dev/) | React video rendering, the engine behind the ghostshelf renderer. Open source, but the license charges companies above a size threshold. Verify before any commercial use | `ghostshelf` |

## Rejected and retired

Kept so nobody re-adds them.

| Tool | Why it is not here |
| --- | --- |
| Paid trend dashboards (the TikTok and Instagram outlier scanners) | They mostly repackage TikTok Creative Center plus alerting. Start free, prove the engine, then price a subscription against the hours it actually saves |
| Enterprise ASO suites (Sensor Tower, AppTweak, MobileAction tier) | Real tools, wrong buyer. An indie listing does not need a seat priced for a UA team. Astro or the free first-party consoles cover the work `aso-strategy` describes |

## Claims we checked and refused

A third-party blog said Astro ships an MCP server for AI-assisted keyword research. Astro's own site does not mention one as of 2026-08-22. It may exist and be undocumented, but a competitor's comparison page is not a source. Do not repeat it until the vendor says it.
