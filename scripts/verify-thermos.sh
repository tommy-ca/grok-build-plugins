#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

python3 - <<'PY'
from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(".").resolve()
THERMOS = ROOT / "thermos"
INDEX = ROOT / ".grok-plugin" / "marketplace.json"
VERSION = "1.0.0-thermos.0"

FORBIDDEN = (
    ".cursor-plugin",
    "the Task tool",
    "AskQuestion",
    "readonly: true",
    "capability_mode",
    "reasoning_effort",
)

assert THERMOS.is_dir(), THERMOS
plugin = json.loads((THERMOS / "plugin.json").read_text(encoding="utf-8"))
assert plugin["name"] == "thermos"
assert plugin["version"] == VERSION, plugin["version"]
assert "skills" in plugin and "agents" in plugin
assert "hooks" not in plugin and "commands" not in plugin and "mcpServers" not in plugin

data = json.loads(INDEX.read_text(encoding="utf-8"))
by_name = {p["name"]: p for p in data["plugins"]}
assert "thermos" in by_name, sorted(by_name)
assert by_name["thermos"]["version"] == plugin["version"]
assert by_name["thermos"]["source"] == "./thermos"

for skill in (
    "thermos",
    "thermo-nuclear-review",
    "thermo-nuclear-code-quality-review",
):
    assert (THERMOS / "skills" / skill / "SKILL.md").is_file(), skill

for agent in (
    "thermo-nuclear-review-subagent.md",
    "thermo-nuclear-code-quality-review-subagent.md",
):
    assert (THERMOS / "agents" / agent).is_file(), agent

harness = (THERMOS / "HARNESS.md").read_text(encoding="utf-8")
assert "spawn_subagent" in harness
assert "get_command_or_subagent_output" in harness
assert "kill_command_or_subagent" in harness
assert "thermos:" in harness
assert "scripts/verify-thermos.sh" in harness
assert "arena" in harness.lower()
assert "interrogate" in harness.lower()

orch = (THERMOS / "skills/thermos/SKILL.md").read_text(encoding="utf-8")
assert "spawn_subagent" in orch
assert "get_command_or_subagent_output" in orch
assert "thermo-nuclear-review" in orch
assert "thermo-nuclear-code-quality-review" in orch
assert "disable-model-invocation: true" in orch.split("---", 2)[1]

assert not (THERMOS / ".cursor-plugin").exists()
assert not (THERMOS / "hooks").exists()
assert not (THERMOS / "commands").exists()

for path in THERMOS.rglob("*"):
    if not path.is_file():
        continue
    if path.suffix not in {".md", ".json"}:
        continue
    text = path.read_text(encoding="utf-8")
    skip = set()
    if path.name in {"HARNESS.md", "UPSTREAM"}:
        skip.add("reasoning_effort")
    for token in FORBIDDEN:
        if token in skip:
            continue
        assert token not in text, f"{path}: {token}"

# Agents must not claim Task subagent sole path
for agent_path in (THERMOS / "agents").glob("*.md"):
    text = agent_path.read_text(encoding="utf-8")
    assert "You are a **Task subagent**" not in text
    assert "You are a Task subagent" not in text
    assert "thermos:" in text or "spawn_subagent" in text

grok = shutil.which("grok")
if grok:
    proc = subprocess.run(
        ["grok", "plugin", "validate", str(THERMOS)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr or proc.stdout
    print("GROK_VALIDATE_PASS")
else:
    print("GROK_VALIDATE_SKIPPED grok CLI missing — structural checks fail-closed above")

print(f"PASS verify-thermos.sh version={VERSION}")
PY
