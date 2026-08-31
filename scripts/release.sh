#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [ -n "${__GROK_INSIDE_BWRAP:-}" ]; then
  echo "scripts/release.sh: nested grok cannot write .git/refs/tags. Run from a host shell with grok --sandbox off." >&2
  exit 1
fi
python3 tests/test_release.py

local_names() {
  python3 - <<'PY'
import json
from pathlib import Path

data = json.loads(Path(".grok-plugin/marketplace.json").read_text(encoding="utf-8"))
for plugin in data["plugins"]:
    src = plugin["source"]
    if isinstance(src, str) and src.startswith("./"):
        print(src[2:].rstrip("/"))
PY
}

release_one() {
  local name="$1"
  local dir="./${name}"
  grok plugin validate "${dir}"
  local version tag
  version="$(python3 -c "import json; print(json.load(open('${dir}/plugin.json'))['version'])")"
  tag="v${version}"
  if ! grok --sandbox off plugin tag --push "${dir}"; then
    git rev-parse "refs/tags/${tag}" >/dev/null
    git push origin "refs/tags/${tag}"
  fi
  if gh release view "${tag}" >/dev/null 2>&1; then
    return 0
  fi
  gh release create "${tag}" --generate-notes --verify-tag --latest=false
}

if [ "$#" -gt 1 ]; then
  echo "usage: scripts/release.sh [sibling]" >&2
  exit 1
fi

if [ "$#" -eq 1 ]; then
  name="${1#./}"
  name="${name%/}"
  case "${name}" in
    "" | "." | .. | */*)
      echo "scripts/release.sh: not a local sibling: ${1}" >&2
      exit 1
      ;;
  esac
  found=0
  while IFS= read -r row; do
    if [ "${row}" = "${name}" ]; then
      found=1
    fi
  done < <(local_names)
  if [ "${found}" -ne 1 ]; then
    echo "scripts/release.sh: not a local sibling: ${name}" >&2
    exit 1
  fi
  release_one "${name}"
  exit 0
fi

while IFS= read -r name; do
  release_one "${name}"
done < <(local_names)
