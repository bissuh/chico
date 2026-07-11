#!/usr/bin/env python3
# Read-only Google Search Console search-analytics.
# Needs SEARCH_CONSOLE_KEY (service-account JSON path) and SEARCH_CONSOLE_SITE_URL
# in the host project's .env. Setup steps are in this connector's SKILL.md.
#   pip install google-auth requests
#
# Usage: search_console.py <startDate YYYY-MM-DD> <endDate YYYY-MM-DD> [dim1,dim2]
#   dimensions default to "query". Others: page, date, country, device.

import os
import sys
import json
import urllib.parse

try:
    from google.oauth2 import service_account
    from google.auth.transport.requests import AuthorizedSession
except ImportError:
    sys.exit("Missing deps. Run: pip install google-auth requests")

SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"

key = os.environ.get("SEARCH_CONSOLE_KEY")
site = os.environ.get("SEARCH_CONSOLE_SITE_URL")
if not key or not site:
    sys.exit("Set SEARCH_CONSOLE_KEY and SEARCH_CONSOLE_SITE_URL in .env. See SKILL.md setup.")

if len(sys.argv) < 3:
    sys.exit("Usage: search_console.py <startDate YYYY-MM-DD> <endDate YYYY-MM-DD> [dim1,dim2]")

start, end = sys.argv[1], sys.argv[2]
dimensions = sys.argv[3].split(",") if len(sys.argv) > 3 else ["query"]

creds = service_account.Credentials.from_service_account_file(key, scopes=[SCOPE])
session = AuthorizedSession(creds)

url = "https://www.googleapis.com/webmasters/v3/sites/%s/searchAnalytics/query" % urllib.parse.quote(site, safe="")
body = {"startDate": start, "endDate": end, "dimensions": dimensions, "rowLimit": 100}

resp = session.post(url, json=body)
if resp.status_code != 200:
    sys.exit("Search Console API error %s: %s" % (resp.status_code, resp.text))
print(json.dumps(resp.json(), indent=2))
