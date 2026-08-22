#!/usr/bin/env bash
# standards/sync.sh: keep the local standards honest against their upstream sources.
#
#   ./standards/sync.sh              check every standard for drift, write nothing
#   ./standards/sync.sh --diff NAME  show the full diff for one standard
#   ./standards/sync.sh --pull NAME  overwrite the local copy from its source
#   ./standards/sync.sh --pull-all   overwrite every local copy from its source
#
# One direction only, on purpose. A two-way sync with no conflict resolution
# is how you silently lose an edit. If a standard should live here instead of
# upstream, retire the source and drop its line from .sources.

set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REG="$DIR/.sources"
[ -f "$REG" ] || { echo "no registry at $REG"; exit 1; }

mode="${1:-check}"; target="${2:-}"
drift=0; missing=0; checked=0

while IFS=$'\t' read -r name src; do
  case "$name" in ''|'#'*) continue;; esac
  [ -n "$target" ] && [ "$name" != "$target" ] && continue
  checked=$((checked + 1))
  local_file="$DIR/$name"

  if [ ! -f "$src" ]; then
    echo "MISSING SOURCE  $name"
    echo "                $src"
    missing=$((missing + 1)); continue
  fi

  if diff -q "$local_file" "$src" >/dev/null 2>&1; then
    echo "in sync         $name"
    continue
  fi

  drift=$((drift + 1))
  added=$(diff "$local_file" "$src" | grep -c '^>' || true)
  removed=$(diff "$local_file" "$src" | grep -c '^<' || true)
  echo "DRIFT           $name  (+$added / -$removed lines upstream)"

  case "$mode" in
    --diff)     diff -u "$local_file" "$src" || true ;;
    --pull|--pull-all)
                cp "$src" "$local_file"
                echo "                pulled. local copy now matches source." ;;
  esac
done < "$REG"

[ "$checked" -eq 0 ] && { echo "no standard matched '${target}'"; exit 1; }
echo
echo "$checked checked, $drift drifted, $missing missing."
[ "$drift" -gt 0 ] && [ "$mode" = "check" ] && \
  echo "run: ./standards/sync.sh --diff <name>   to see what changed"
exit 0
