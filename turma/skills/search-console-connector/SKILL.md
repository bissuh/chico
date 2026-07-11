---
name: search-console-connector
description: Pull live Google Search Console data (organic traffic, top queries, top pages, clicks, impressions, CTR, average position) for SEO analysis. Invoke when someone asks to "check the SEO traffic," "analyze SEO," "what are we ranking for," "top search queries," "organic performance," or any SEO report that needs real numbers. If Search Console access is not configured yet, this skill walks the user through granting it once, then reads live data. Reads brand.md for the site.
---

# search-console-connector

Read-only access to a project's Google Search Console data, so SEO analysis runs on live numbers instead of copy-paste.

**Before you start:** read the project's `brand.md` for the site URL, the audience, and any target keywords.

## The rule

If the credentials are not configured, do NOT ask the owner to paste screenshots or exports. Give them the one-time setup below, wait for them to do it, then pull the data yourself. Copy-paste is the fallback only if they can't or won't set up access.

## Is it configured?

Check the project's `.env` for:
- `SEARCH_CONSOLE_KEY`: absolute path to a service-account JSON key
- `SEARCH_CONSOLE_SITE_URL`: the property, e.g. `https://yoursite.com/` or `sc-domain:yoursite.com`

If both are set, skip to Read. If not, give the owner the setup.

## Setup (the owner does this once, ~10 minutes)

Hand the owner these steps. They happen in their own Google account, so they do the clicks. You just guide.

1. **Google Cloud Console** (console.cloud.google.com): create or pick a project.
2. **Enable the API:** APIs & Services, Library, search "Google Search Console API", Enable.
3. **Create a service account:** IAM & Admin, Service Accounts, Create service account. Give it a name, no roles needed. Open it, Keys, Add key, Create new key, JSON, download. Note the `client_email` inside that JSON file (looks like `name@project.iam.gserviceaccount.com`).
4. **Grant it access to the property:** in Search Console (search.google.com/search-console), pick the site, Settings, Users and permissions, Add user, paste the service account's `client_email`, permission Full or Restricted. This is the step that lets it read the data.
5. **Wire the creds** into the project's gitignored `.env`:
   ```
   SEARCH_CONSOLE_KEY=/absolute/path/to/service-account.json
   SEARCH_CONSOLE_SITE_URL=https://yoursite.com/
   ```
   Keep the JSON file out of git (it's a credential). Use the `sc-domain:yoursite.com` form if the property is a domain property.
6. **Install the client:** `pip install google-auth requests`.

The scope used is read-only: `https://www.googleapis.com/auth/webmasters.readonly`. The service account can only read, never change anything.

## Read (once configured)

Run the wrapper in this skill's folder:

```
python3 scripts/search_console.py <startDate YYYY-MM-DD> <endDate YYYY-MM-DD> [dimensions]
# examples:
python3 scripts/search_console.py 2026-06-01 2026-06-30 query      # top queries
python3 scripts/search_console.py 2026-06-01 2026-06-30 page       # top pages
python3 scripts/search_console.py 2026-06-01 2026-06-30 date       # traffic over time
```

It returns clicks, impressions, CTR, and average position per row. Under the hood it POSTs to `https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/searchAnalytics/query` with the service-account token.

## Then do the analysis

Feed the live data into the SEO read: the `seo-audit` / `ai-seo` skills if they're installed in the session, or your own analysis, framed by `brand.md` (the audience and the target keywords). Report the highest-leverage moves, not a data dump. Honest numbers, ranked actions.

## Hard rules

- Read-only. This connector never writes to Search Console.
- Credentials live in the project's gitignored `.env`. Never commit the JSON key or the key path to a public file.
- brand.md first: the site URL and the keywords that matter come from there.
- No dashes, no AI tells in the report. Run `turma:anti-ai-linguo`.

## Related

- The project's `brand.md`: the site, audience, target keywords.
- `seo-audit` / `ai-seo` (installed marketing skills): the analysis, once this connector supplies the data.
- `beehiiv-connector`, `youtube-connector`: sibling read connectors, same `.env` pattern.
