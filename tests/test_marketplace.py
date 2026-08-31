"""Drive the shipped marketplace index (not a reimplementation of grok)."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / ".grok-plugin" / "marketplace.json"


def test_index_exists() -> None:
    assert INDEX.is_file(), INDEX


def test_pstack_is_pinned_url() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    assert data["name"] == "grok-build-plugins"
    plugins = data["plugins"]
    names = [p["name"] for p in plugins]
    assert names[0] == "pstack"
    assert "agent-compatibility" in names
    assert "cli-for-agent" in names
    src = plugins[0]["source"]
    assert src.get("source") == "url"
    assert src["url"] == "https://github.com/tommy-ca/pstack.git"
    assert len(src["sha"]) == 40
    assert all(c in "0123456789abcdef" for c in src["sha"])
    assert plugins[0]["version"].count("-grokbuild.") == 1
    sibling = ROOT.parent / "pstack"
    plugin_json = sibling / "plugin.json"
    if plugin_json.is_file():
        want_ver = json.loads(plugin_json.read_text(encoding="utf-8"))["version"]
        assert plugins[0]["version"] == want_ver
        got = subprocess.run(
            ["git", "-C", str(sibling), "rev-parse", "origin/main"],
            check=True,
            capture_output=True,
            text=True,
        )
        assert src["sha"] == got.stdout.strip()


def test_catalog_does_not_vendor_skills() -> None:
    assert not (ROOT / "skills").exists()
    assert not (ROOT / "plugins").exists()
    adr = ROOT / "adr/0001-catalog-is-index-not-plugin-monorepo.md"
    assert adr.is_file()
    text = adr.read_text(encoding="utf-8")
    assert "url" in text
    assert "plugins/pstack" in text
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Do not nest tommy-ca/pstack as `plugins/pstack`" in readme
    assert not (ROOT / "pstack").exists()


def test_readme_install_is_owner_repo() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "grok plugin install tommy-ca/pstack --trust" in readme
    assert "xAI Official already publishes a plugin named `pstack`" in readme
    assert "grok plugin install pstack --trust" not in readme
    assert "rev-parse origin/main" in readme
    assert "EROFS" in readme
    assert "config.toml" in readme
    assert "host shell" in readme
    assert "grok plugin enable pstack" in readme
    assert "grok --sandbox off plugin enable pstack" in readme
    assert "pstack:how-explorer" in readme
    assert "sync-from-upstream.py" in readme
    spec = (ROOT / "SPEC.md").read_text(encoding="utf-8")
    assert "tommy-ca/pstack --trust" in spec
    assert "EROFS" in spec
    assert "grok plugin enable pstack" in spec
    assert "pstack:how-explorer" in spec
    spec_main = (
        ROOT / "openspec/specs/grok-build-marketplace/spec.md"
    )
    assert spec_main.is_file()
    text = spec_main.read_text(encoding="utf-8")
    assert "## Requirements" in text
    assert "pstack:how-explorer" in text
    assert "agent-compatibility" in text
    assert "./agent-compatibility" in text
    assert "agent-compatibility:startup-review" in text
    assert "agent-compatibility:startup-review" in readme
    adr1 = (ROOT / "adr/0001-catalog-is-index-not-plugin-monorepo.md").read_text(
        encoding="utf-8"
    )
    assert "sibling" in adr1.lower() or "local path" in adr1.lower()


FORBIDDEN = (
    "model: fast",
    "readonly: true",
    "readonly:true",
    "AskQuestion",
    "the Task tool",
    "capability_mode",
    "reasoning_effort",
    ".cursor-plugin",
)


def test_grok_native_siblings_validate() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    by_name = {p["name"]: p for p in data["plugins"]}
    for name in ("agent-compatibility", "cli-for-agent"):
        src = by_name[name]["source"]
        if isinstance(src, str):
            path = src
        else:
            path = src.get("path") or ""
        assert path in {f"./{name}", name}
        folder = ROOT / name
        plugin = json.loads((folder / "plugin.json").read_text(encoding="utf-8"))
        assert plugin["name"] == name
        assert "skills" in plugin
        assert "hooks" not in plugin
        assert "commands" not in plugin
        assert "mcpServers" not in plugin
        assert not (folder / "commands").exists()
        assert not (folder / "hooks").exists()
        assert not (folder / ".mcp.json").exists()
        assert not (folder / ".cursor-plugin").exists()
        proc = subprocess.run(
            ["grok", "plugin", "validate", str(folder)],
            capture_output=True,
            text=True,
            check=False,
        )
        assert proc.returncode == 0, proc.stderr or proc.stdout
        for path in folder.rglob("*"):
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
    ac_skill = (
        ROOT / "agent-compatibility/skills/check-agent-compatibility/SKILL.md"
    ).read_text(encoding="utf-8")
    assert "spawn_subagent" in ac_skill
    assert "MAX_SUBAGENT_DEPTH" in ac_skill
    assert "background: true" in ac_skill
    assert "task_ids" in ac_skill
    assert "timeout_ms" in ac_skill
    assert "Launch `" not in ac_skill
    for role in (
        "compatibility-scan-review",
        "startup-review",
        "validation-review",
        "docs-reliability-review",
    ):
        assert f"agent-compatibility:{role}" in ac_skill
    harness = ROOT / "agent-compatibility/HARNESS.md"
    assert harness.is_file()
    harness_text = harness.read_text(encoding="utf-8")
    assert "gap" in harness_text
    assert "capabilityMode: execute" in harness_text
    upstream = (ROOT / "agent-compatibility/UPSTREAM").read_text(encoding="utf-8")
    assert "fd878692de15a3069c21c8f429eb0b9f2fe178fa" in upstream
    assert (ROOT / "cli-for-agent/HARNESS.md").is_file()
    assert "cli-for-agent:cli-for-agents" in (
        ROOT / "cli-for-agent/README.md"
    ).read_text(encoding="utf-8")
    assert (ROOT / "adr/0002-grok-native-sibling-plugins.md").is_file()


if __name__ == "__main__":
    test_index_exists()
    test_pstack_is_pinned_url()
    test_catalog_does_not_vendor_skills()
    test_readme_install_is_owner_repo()
    test_grok_native_siblings_validate()
    print("PASS tests/test_marketplace.py")
