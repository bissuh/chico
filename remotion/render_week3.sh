#!/usr/bin/env bash
# Render all Week 3 carousel slides (7 carousels, 63 slides) to out/.
# bash 3.2-safe (no associative arrays). Run from anywhere:
#   bash /Users/bissuh/Documents/TBP/chico/remotion/render_week3.sh
set -uo pipefail
cd "$(dirname "$0")"

R=node_modules/.bin/remotion
total=0; ok=0
for pair in tools:10 find:9 myth:9 marc:9 vs:8 hoard:9 week:9; do
  id="${pair%%:*}"; n="${pair##*:}"
  for i in $(seq 1 "$n"); do
    total=$((total+1))
    if "$R" still src/index.ts CleanSlide "out/${id}-${i}.png" --props="props/${id}-${i}.json" --log=error; then
      ok=$((ok+1)); echo "  ok ${id}-${i}"
    else
      echo "  FAIL ${id}-${i}"
    fi
  done
done
echo "rendered $ok / $total slides"
