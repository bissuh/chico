#!/usr/bin/env python3
"""
Schedule a rendered batch to Instagram, TikTok, and YouTube Shorts via Postiz.

Each post is uploaded once and scheduled per platform separately, so one
platform rejecting a post does not block the others. Every result is written
to a ledger so a re-run can tell what already went out.

Usage:
  set -a && source .env && set +a
  ./schedule_batch.py batch.json --dry-run     # preview every call, send none
  ./schedule_batch.py batch.json               # live

Requires in .env:
  POSTIZ_API_KEY
  POSTIZ_INSTAGRAM_INTEGRATION_ID   (only for posts that list "instagram")
  POSTIZ_TIKTOK_INTEGRATION_ID      (only for posts that list "tiktok")
  POSTIZ_YOUTUBE_INTEGRATION_ID     (only for posts that list "youtube")

List your integration IDs with:
  curl -s -H "Authorization: $POSTIZ_API_KEY" https://api.postiz.com/public/v1/integrations

APPROVAL BINDING (turma:pauta, contract 4): the approval the owner gave is for
this exact manifest. Caption, media, destination, and publish time are one unit.
Change any of them and the approval is void; take it back to the owner.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

import requests

BASE = "https://api.postiz.com/public/v1"


def env(name):
    v = os.environ.get(name)
    return v.strip() if v else None


def media_for(post, out):
    """Carousel: every slide PNG in order. Reel: the single MP4."""
    if post.get("type", "carousel") == "reel":
        return [out / f"{post['slug']}.mp4"]
    d = out / post["slug"]
    if not d.is_dir():
        return []
    return sorted(d.glob("slide-*.png"), key=lambda p: int(re.search(r"slide-(\d+)", p.name).group(1)))


def upload(path):
    """Postiz CLI upload. Returns {"id", "path"} or None."""
    r = subprocess.run(["postiz", "upload", str(path)], capture_output=True, text=True)
    m = re.search(r"\{.*\}", r.stdout, re.S)
    if not m:
        print(f"    upload failed for {path.name}: {r.stdout[:120]} {r.stderr[:120]}")
        return None
    d = json.loads(m.group(0))
    return {"id": d["id"], "path": d["path"]}


def settings_for(platform, post, batch):
    if platform == "instagram":
        return {"__type": "instagram-standalone", "post_type": "post"}
    if platform == "tiktok":
        return {
            "__type": "tiktok",
            "privacy_level": "PUBLIC_TO_EVERYONE",
            "duet": False,
            "stitch": False,
            "comment": True,
            "autoAddMusic": "no",
            "brand_content_toggle": False,
            "brand_organic_toggle": False,
            "content_posting_method": "DIRECT_POST",
        }
    if platform == "youtube":
        tags = post.get("shorts_tags") or batch.get("shorts_tags") or []
        return {
            "__type": "youtube",
            "title": post.get("shorts_title") or post.get("slug"),
            "type": "public",
            "selfDeclaredMadeForKids": "no",
            "tags": [{"value": t, "label": t} for t in tags],
        }
    return None


def schedule(api, integration_id, settings, caption, images, date_iso, dry):
    payload = {
        "type": "schedule",
        "date": date_iso,
        "shortLink": False,
        "tags": [],
        "posts": [
            {
                "integration": {"id": integration_id},
                "value": [{"content": caption, "image": images}],
                "settings": settings,
            }
        ],
    }
    if dry:
        return True, "dry-run"
    r = requests.post(
        f"{BASE}/posts",
        headers={"Authorization": api, "Content-Type": "application/json"},
        json=payload,
        timeout=60,
    )
    if r.status_code >= 300:
        return False, f"HTTP {r.status_code}: {r.text[:240]}"
    return True, (r.text[:160] or "ok")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", help="schedule just this slug")
    ap.add_argument("--workdir", default=None, help="where out/ lives (default: manifest's folder)")
    a = ap.parse_args()

    api = env("POSTIZ_API_KEY")
    if not api:
        sys.exit("POSTIZ_API_KEY missing. set -a && source .env && set +a")

    manifest = Path(a.manifest).resolve()
    if not manifest.exists():
        sys.exit(f"manifest not found: {manifest}")
    work = Path(a.workdir).resolve() if a.workdir else manifest.parent
    out = work / "out"

    batch = json.loads(manifest.read_text())
    start = batch.get("start")
    if not start:
        sys.exit('manifest needs a "start" (ISO 8601, e.g. "2026-09-01T13:00:00Z")')
    base = datetime.fromisoformat(start.replace("Z", "+00:00"))
    cadence = int(batch.get("cadence_days", 1))

    integrations = {
        "instagram": env("POSTIZ_INSTAGRAM_INTEGRATION_ID"),
        "tiktok": env("POSTIZ_TIKTOK_INTEGRATION_ID"),
        "youtube": env("POSTIZ_YOUTUBE_INTEGRATION_ID"),
    }

    results = []
    for i, post in enumerate(batch.get("posts", [])):
        slug = post["slug"]
        if a.only and slug != a.only:
            continue

        platforms = post.get("platforms") or batch.get("platforms") or ["instagram", "tiktok"]
        missing = [p for p in platforms if not integrations.get(p)]
        if missing:
            print(f"{slug}: no integration id for {', '.join(missing)}, skipping those")
            platforms = [p for p in platforms if integrations.get(p)]
        if not platforms:
            continue

        files = media_for(post, out)
        if not files or not all(f.exists() for f in files):
            print(f"{slug}: MEDIA MISSING in {out}. Run render_batch.py first.")
            results.append({"slug": slug, "error": "media missing"})
            continue

        date_iso = (base + timedelta(days=i * cadence)).isoformat().replace("+00:00", "Z")
        print(f"\n{slug}  ({len(files)} file(s))  {date_iso}")

        media = [upload(f) for f in files]
        if any(m is None for m in media):
            print("  upload failed, skipping post")
            results.append({"slug": slug, "error": "upload failed"})
            continue
        images = [{"id": m["id"], "path": m["path"]} for m in media]

        row = {"slug": slug, "date": date_iso}
        for platform in platforms:
            settings = settings_for(platform, post, batch)
            ok, msg = schedule(api, integrations[platform], settings, post.get("caption", ""), images, date_iso, a.dry_run)
            row[platform] = ok
            if not ok:
                row[f"{platform}_msg"] = msg
            print(f"  {platform:<10} {'OK' if ok else 'FAIL ' + msg}")
        results.append(row)

    ledger = out / "schedule-ledger.json"
    if results and not a.dry_run:
        out.mkdir(parents=True, exist_ok=True)
        ledger.write_text(json.dumps(results, indent=2))

    for platform in ("instagram", "tiktok", "youtube"):
        n = sum(1 for r in results if r.get(platform))
        if n:
            print(f"{platform}: {n} scheduled")
    if a.dry_run:
        print("\nDRY RUN. Nothing was sent.")
    else:
        print(f"\nLedger: {ledger}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
