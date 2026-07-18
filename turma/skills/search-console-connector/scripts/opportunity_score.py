#!/usr/bin/env python3
# Rank SEO opportunities by expected money, not vanity, from live GSC data.
# Reads the JSON output of search_console.py (query dimension) on stdin, then
# ranks two opportunity types by projected additional clicks:
#   QUICK_WIN     position 11-20  -> reachable page-1 spot (title/H1/first-100 fix)
#   UNDERPERFORMER position 1-10, CTR far below curve -> title/meta rewrite, no rank change needed
#
# Usage:
#   python3 search_console.py 2026-06-01 2026-06-30 query | python3 opportunity_score.py [target_position]
#   target_position defaults to 5. It is the position you assume the quick-win reaches;
#   the projection is "IF it reaches position N", stated openly so nobody mistakes it for a promise.
#
# Method distilled from Craig Hewitt's SEO Machine opportunity_scorer.py (MIT), rebuilt
# GSC-only (no paid API). The CTR curve is directional, from public studies (Backlinko's
# 4M-result analysis: position 1 ~= 27.6%). AI Overviews now compress these numbers
# (Ahrefs, Feb 2026: ~58% CTR cut for top results), so treat every projection as an
# upper bound, not a forecast.

import sys
import json

# Directional organic CTR by position. Public-study averages, pre-AI-Overview.
CTR_CURVE = {
    1: 0.276, 2: 0.155, 3: 0.110, 4: 0.080, 5: 0.060,
    6: 0.049, 7: 0.040, 8: 0.033, 9: 0.028, 10: 0.025,
    11: 0.018, 12: 0.015, 13: 0.013, 14: 0.012, 15: 0.011,
    16: 0.010, 17: 0.009, 18: 0.008, 19: 0.008, 20: 0.007,
}


def expected_ctr(position):
    p = int(round(position))
    if p < 1:
        p = 1
    return CTR_CURVE.get(p, 0.005)


def main():
    target = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    target_ctr = expected_ctr(target)

    raw = sys.stdin.read()
    if not raw.strip():
        sys.exit("No input. Pipe search_console.py <start> <end> query output into this script.")
    rows = json.loads(raw).get("rows", [])
    if not rows:
        sys.exit("No rows in GSC response. Widen the date range or check the property.")

    quick_wins, underperformers = [], []

    for r in rows:
        keyword = (r.get("keys") or ["(unknown)"])[0]
        pos = r.get("position", 100)
        impressions = r.get("impressions", 0)
        clicks = r.get("clicks", 0)
        ctr = r.get("ctr", 0.0)

        if 11 <= pos <= 20 and impressions > 0:
            projected = impressions * target_ctr
            gain = round(projected - clicks, 1)
            if gain > 0:
                quick_wins.append({
                    "keyword": keyword, "position": round(pos, 1),
                    "impressions": int(impressions), "clicks": int(clicks),
                    "projected_clicks_at_target": round(projected, 1),
                    "additional_clicks": gain,
                })
        elif 1 <= pos <= 10 and impressions > 0:
            exp = expected_ctr(pos)
            if ctr < exp * 0.5:  # earning less than half the curve for its rank
                recoverable = round(impressions * exp - clicks, 1)
                if recoverable > 0:
                    underperformers.append({
                        "keyword": keyword, "position": round(pos, 1),
                        "impressions": int(impressions), "clicks": int(clicks),
                        "actual_ctr": round(ctr * 100, 2), "expected_ctr": round(exp * 100, 2),
                        "recoverable_clicks": recoverable,
                    })

    quick_wins.sort(key=lambda x: x["additional_clicks"], reverse=True)
    underperformers.sort(key=lambda x: x["recoverable_clicks"], reverse=True)

    print("# Opportunity scan (GSC only)")
    print("Projection assumes quick-wins reach position %d. Directional, not a promise." % target)
    print("AI Overviews compress these CTRs; treat gains as an upper bound.\n")

    print("## Quick wins: page-2 keywords (position 11-20), ranked by expected +clicks/mo")
    if quick_wins:
        for i, q in enumerate(quick_wins[:20], 1):
            print("%2d. +%-7s %-45s pos %s, %s impr, %s clicks now" % (
                i, q["additional_clicks"], q["keyword"][:45],
                q["position"], q["impressions"], q["clicks"]))
    else:
        print("  none found in range")

    print("\n## Underperformers: ranking well, CTR below curve (rewrite title/meta)")
    if underperformers:
        for i, u in enumerate(underperformers[:15], 1):
            print("%2d. +%-7s %-45s pos %s, CTR %s%% vs %s%% expected" % (
                i, u["recoverable_clicks"], u["keyword"][:45],
                u["position"], u["actual_ctr"], u["expected_ctr"]))
    else:
        print("  none found in range")

    print("\n---\n// machine-readable")
    print(json.dumps({"quick_wins": quick_wins, "underperformers": underperformers}, indent=2))


if __name__ == "__main__":
    main()
