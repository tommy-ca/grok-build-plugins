#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

python3 - <<'PY'
import tests.test_marketplace as t

t.test_index_exists()
t.test_catalog_does_not_vendor_skills()
t.test_readme_install_is_owner_repo()
t.test_grok_native_siblings_validate()
t.test_operator_docs_match_live_inspect()
t.test_herdr_hooks_sandbox()
print("PASS overlay marketplace functions")
PY
python3 tests/test_release.py
grok plugin validate ./long-horizon-swarm

find_orch() {
  if [ -n "${PSTACK_ORCH:-}" ] && [ -f "${PSTACK_ORCH}" ]; then
    printf '%s\n' "${PSTACK_ORCH}"
    return 0
  fi
  local d f
  for d in "${HOME}/.grok/installed-plugins"/pstack-* ../pstack; do
    f="${d}/skills/poteto-mode/scripts/orch/orch.ts"
    if [ -f "${f}" ]; then
      printf '%s\n' "${f}"
      return 0
    fi
  done
  return 1
}

if command -v bun >/dev/null 2>&1; then
  RUNNER=(bun)
elif command -v node >/dev/null 2>&1; then
  RUNNER=(node)
else
  printf 'ORCH_SKIPPED no bun or node (Grok chat case)\n'
  exit 0
fi

if ! orch="$(find_orch)"; then
  printf 'ORCH_SKIPPED pstack orch.ts not found\n' >&2
  exit 1
fi

store="$(mktemp -d "${TMPDIR:-/tmp}/lhs-orch.XXXXXX")"
cleanup() { rm -rf "${store}"; }
trap cleanup EXIT

"${RUNNER[@]}" "${orch}" --store "${store}" init
test -f "${store}/frontier.json"
test -f "${store}/ledger.tsv"
printf 'ORCH_RAN runner=%s store=%s\n' "${RUNNER[0]}" "${store}"
