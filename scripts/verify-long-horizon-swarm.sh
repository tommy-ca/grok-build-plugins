#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

python3 - <<'PY'
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(".").resolve()
LHS = ROOT / "long-horizon-swarm"
INDEX = ROOT / ".grok-plugin" / "marketplace.json"
VERSION = "1.2.0-long-horizon-swarm.0"

# --- Static: SemVer + marketplace identity ---
plugin = json.loads((LHS / "plugin.json").read_text(encoding="utf-8"))
assert plugin["name"] == "long-horizon-swarm"
assert plugin["version"] == VERSION, plugin["version"]
data = json.loads(INDEX.read_text(encoding="utf-8"))
by_name = {p["name"]: p for p in data["plugins"]}
assert by_name["long-horizon-swarm"]["version"] == VERSION
assert by_name["long-horizon-swarm"]["source"] == "./long-horizon-swarm"
assert "agents" not in plugin

# --- Static: fleet seats / dual-orch / Grok primitives ---
harness = (LHS / "HARNESS.md").read_text(encoding="utf-8")
readme = (LHS / "README.md").read_text(encoding="utf-8")
for seat in (
    "Planner",
    "Horizon",
    "Drove",
    "CAO",
    "Herd",
    "Heavilifter",
    "Nightly Audit",
):
    assert seat in harness, seat
assert "WORKFLOW.md" in harness
assert "Dual orch forbidden" in harness or "dual orch forbidden" in harness.lower()
assert "spawn_subagent" in harness or "pstack:<role>" in harness
assert "pstack:" in harness
assert "worktree" in harness.lower()
assert "orch" in harness.lower()
assert "Join" in harness and "Cancel" in harness
assert "none of its own" in harness
# README points at fleet bind
assert "HARNESS.md" in readme or "fleet" in readme.lower()
assert "Dual orch forbidden" in readme or "dual orch" in readme.lower()
assert "ships no agents" in readme or "No agents" in readme

# --- Static: blog failure-mode checklist ---
playbook = (
    LHS / "skills/long-horizon-swarm/playbooks/long-horizon-swarm.md"
).read_text(encoding="utf-8")
standing = (LHS / "references/standing-orders-template.md").read_text(encoding="utf-8")
for mode in (
    "split-brain",
    "planner contention",
    "merge reconciler",
    "megafiles",
    "ossify",
    "review lenses",
    "Field Guide",
    "model economics",
):
    assert mode in playbook, f"playbook missing {mode}"
    assert mode in standing, f"standing missing {mode}"
assert "cursor.com/blog/agent-swarm-model-economics" in playbook
assert "cursor.com/blog/agent-swarm-model-economics" in standing
for keep in (
    "planner",
    "CostPolicy",
    "field-guide",
    "review-lenses",
    "megafile-gate",
    "ossify-break",
    "openspec-intent-flow",
    "flat-swarm",
    "nested-spawn",
):
    assert keep.lower() in (playbook + standing).lower() or keep in playbook or keep in standing, keep
assert "dual-board" in standing or "second-board" in standing
# arena/interrogate not cloned
assert not (LHS / "skills/arena").exists()
assert not (LHS / "skills/interrogate").exists()

# --- Static: lever-first VERIFY ---
handoff = (LHS / "references/handoff-contract.md").read_text(encoding="utf-8")
assert "verify-*" in standing or "verify-*" in playbook
assert "scripts/verify-" in standing or "scripts/verify-" in playbook
assert "prose-only" in standing.lower() or "prose-only" in playbook.lower()
assert "lever:" in handoff.lower() or "lever path" in handoff.lower()
assert "PASS" in handoff and "FAIL" in handoff and "INCONCLUSIVE" in handoff
assert "Nightly Audit" in standing or "maintain-verification" in standing
# Refuse inventing LIVE — prohibition may name the token; ban positive invent claims
for blob, label in ((playbook, "playbook"), (standing, "standing"), (handoff, "handoff")):
    assert "do not invent LIVE" in blob.lower() or "not invent LIVE" in blob or "LIVE" in blob and "invent" in blob.lower(), label
    assert "LIVE_PASS as" not in blob and "claim LIVE_PASS" not in blob

print(f"PASS static fleet/checklist/VERIFY/SemVer version={VERSION}")

# marketplace helper functions (same as before)
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

# grok validate if present; else structural fail-closed (thermos pattern)
python3 - <<'PY'
import shutil
import subprocess
from pathlib import Path

lhs = Path("long-horizon-swarm").resolve()
grok = shutil.which("grok")
if grok:
    proc = subprocess.run(
        ["grok", "plugin", "validate", str(lhs)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr or proc.stdout
    print("GROK_VALIDATE_PASS")
else:
    # structural already asserted above (plugin.json, skills, no hooks/commands)
    print("GROK_VALIDATE_SKIPPED grok CLI missing — structural checks fail-closed above")
PY

find_orch() {
  if [ -n "${PSTACK_ORCH:-}" ] && [ -f "${PSTACK_ORCH}" ]; then
    printf '%s\n' "${PSTACK_ORCH}"
    return 0
  fi
  local d f
  for d in "${HOME}/.grok/installed-plugins"/pstack-* ../pstack ../../pstack ../../../pstack /workspace/verify/pstack; do
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
