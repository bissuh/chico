#!/usr/bin/env bash
# Render the 3 back-office filler carousels (inv 9, chase 8, book 9 = 26 slides) to out/.
set -uo pipefail
cd "$(dirname "$0")"
R=node_modules/.bin/remotion
total=0; ok=0
for pair in inv:9 chase:8 book:9; do
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
