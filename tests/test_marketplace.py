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
    assert "tommy-mode" in names
    assert "long-horizon-swarm" in names
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
    assert "Do not add a `pstack/` sibling to match cursor/plugins" in readme
    assert "Cursor sibling layout for grok-native ports" in readme
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
    for name in (
        "agent-compatibility",
        "cli-for-agent",
        "tommy-mode",
        "long-horizon-swarm",
    ):
        src = by_name[name]["source"]
        if isinstance(src, str):
            path = src
        else:
            path = src.get("path") or ""
        assert path in {f"./{name}", name}
        folder = ROOT / name
        plugin = json.loads((folder / "plugin.json").read_text(encoding="utf-8"))
        assert plugin["name"] == name
        assert plugin["version"] == by_name[name]["version"]
        assert "grokbuild" not in plugin["version"]
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
    tm = (ROOT / "tommy-mode/skills/tommy-mode/SKILL.md").read_text(encoding="utf-8")
    assert "disable-model-invocation: true" in tm
    assert "tommy-ca/grok-build-plugins" not in tm
    assert "plugins/pstack" not in tm
    assert "upstream-cursor-plugins" not in tm
    lhs_root = ROOT / "long-horizon-swarm"
    lhs_plugin = json.loads((lhs_root / "plugin.json").read_text(encoding="utf-8"))
    assert lhs_plugin["version"] == "1.1.0-long-horizon-swarm.0"
    assert lhs_plugin["version"] == by_name["long-horizon-swarm"]["version"]
    assert by_name["long-horizon-swarm"]["source"] == "./long-horizon-swarm"
    assert "agents" not in lhs_plugin
    skill_dirs = sorted(
        p.name for p in (lhs_root / "skills").iterdir() if p.is_dir()
    )
    assert skill_dirs == [
        "coordination-layer",
        "field-guide",
        "long-horizon-swarm",
        "megafile-gate",
        "openspec-intent-flow",
        "ossify-break",
        "planner-worker-split",
        "review-lenses",
    ]
    for name in skill_dirs:
        text = (lhs_root / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
        fm = text.split("---", 2)[1]
        assert "\ndisable-model-invocation: true" in fm
        assert "metadata.cursor" not in fm
    lhs_skill = (
        lhs_root / "skills/long-horizon-swarm/SKILL.md"
    ).read_text(encoding="utf-8")
    assert lhs_skill.lstrip().startswith("---")
    assert "disable-model-invocation: true" in lhs_skill.split("---", 2)[1]
    playbook = (
        lhs_root / "skills/long-horizon-swarm/playbooks/long-horizon-swarm.md"
    )
    assert playbook.is_file()
    lhs_harness = (lhs_root / "HARNESS.md").read_text(encoding="utf-8")
    lhs_readme = (lhs_root / "README.md").read_text(encoding="utf-8")
    lhs_upstream = (lhs_root / "UPSTREAM").read_text(encoding="utf-8")
    overlay_text = "\n".join(
        [lhs_skill, playbook.read_text(encoding="utf-8"), lhs_harness, lhs_readme]
    )
    playbook_text = playbook.read_text(encoding="utf-8")
    assert "spawn_subagent" in overlay_text
    assert "pstack:" in overlay_text
    assert "pstack:feature" in playbook_text
    assert "toml key feature" in playbook_text.replace("`", "")
    for overlay_skill in (
        "planner-worker-split",
        "review-lenses",
        "coordination-layer",
        "megafile-gate",
        "ossify-break",
        "openspec-intent-flow",
        "field-guide",
    ):
        assert overlay_skill in playbook_text
    assert "Before any `spawn_subagent`" in playbook_text
    assert "playbooks/babysit.md" in lhs_skill
    assert "/pr-babysit" in lhs_skill
    assert "missing-poteto-mode" in lhs_skill
    assert ".skills[].name" in lhs_skill
    assert "tommy-ca/pstack --trust" in lhs_skill
    assert "Do not spawn" in lhs_skill
    assert "parent-owned" in overlay_text
    assert "children do not spawn" in overlay_text.lower()
    assert "Depth 1" in overlay_text
    assert "/interrogate" in playbook.read_text(encoding="utf-8")
    assert "openspec-intent-flow" in playbook_text
    assert "field-guide" in playbook_text
    assert "TaskTree" in playbook_text
    assert "1)" in playbook_text and "10)" in playbook_text
    assert "scripts/orch/orch.ts" in lhs_harness or "scripts/orch/orch.ts" in (
        lhs_root / "docs/REQUIRES.md"
    ).read_text(encoding="utf-8")
    assert "Codex" in lhs_harness or "Codex" in (
        lhs_root / "docs/REQUIRES.md"
    ).read_text(encoding="utf-8")
    assert "Do not invoke pstack `scripts/orch/orch.ts`" in playbook_text
    for banned in (
        "chatroom_send",
        "/home/workdir",
        "Harper",
        ".cursor-plugin",
        "the Task tool",
        "GROK-CHAT.md",
        "units.tsv",
        "readonly: true",
        "metadata.cursor",
        "pstack-models.mdc",
        "orchestrate/<",
    ):
        for path in lhs_root.rglob("*"):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            assert banned not in text, f"{path}: {banned}"
    assert (lhs_root / "skills/coordination-layer/SKILL.md").is_file()
    assert not (lhs_root / "skills/long-horizon-swarm-grok-adapter").exists()
    assert not (lhs_root / "GROK-CHAT.md").exists()
    assert not (lhs_root / "rules").exists()
    assert not (lhs_root / "agents").exists()
    assert (lhs_root / "GLOSSARY.md").is_file()
    assert (lhs_root / "docs/REQUIRES.md").is_file()
    assert (lhs_root / "references/handoff-contract.md").is_file()
    assert (lhs_root / "references/openspec-binding.md").is_file()
    assert (lhs_root / "references/standing-orders-template.md").is_file()
    assert "HostStore" in overlay_text
    assert "pstack-long-horizon-swarm-0.1.1.zip" in lhs_upstream
    assert (
        "becdfa7f0cd3a0d3550fb2301da61ffb64e333188e04c66ce67cc7f9e7b4056b"
        in lhs_upstream
    )
    assert "/long-horizon-swarm" in lhs_harness
    assert "none of its own" in lhs_harness
    assert "pstack, then user, then this plugin" in lhs_harness
    assert "Hooks" in lhs_harness
    assert "Commands" in lhs_harness
    assert "long-horizon/" in overlay_text
    assert "orchestrate/<slug>/" not in overlay_text


def test_operator_docs_match_live_inspect() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    ac = (ROOT / "agent-compatibility/README.md").read_text(encoding="utf-8")
    cli = (ROOT / "cli-for-agent/README.md").read_text(encoding="utf-8")
    tm_readme = (ROOT / "tommy-mode/README.md").read_text(encoding="utf-8")
    lhs_readme = (ROOT / "long-horizon-swarm/README.md").read_text(encoding="utf-8")
    spec = (ROOT / "SPEC.md").read_text(encoding="utf-8")
    spec_main = (
        ROOT / "openspec/specs/grok-build-marketplace/spec.md"
    ).read_text(encoding="utf-8")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    for text in (readme, ac, cli, tm_readme, lhs_readme):
        assert "new session" in text
    assert "inspect.agents" in readme
    assert "directory count" in readme
    assert "--available" in readme
    assert "config.toml" in readme
    assert "host shell" in readme
    assert "python3 tests/test_marketplace.py" in agents
    assert "new session" in spec
    assert "inspect.agents" in spec_main


def test_herdr_hooks_sandbox() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    spec = (ROOT / "SPEC.md").read_text(encoding="utf-8")
    profile = (ROOT / ".grok/sandbox.toml").read_text(encoding="utf-8")
    script = (ROOT / "scripts/install-herdr-grok-hooks.sh").read_text(
        encoding="utf-8"
    )
    main = (
        ROOT / "openspec/specs/grok-build-marketplace/spec.md"
    ).read_text(encoding="utf-8")
    assert "herdr integration install grok" in readme
    assert "devbox" in readme
    assert "herdr-install" in readme
    assert "read_write" in readme
    assert "HERDR_SOCKET_PATH" in spec
    assert "Direct global hook write protection" in spec
    assert 'extends = "devbox"' in profile
    assert "[profiles.herdr-install]" in profile
    assert "__GROK_INSIDE_BWRAP" in script
    assert "herdr integration install grok" in script
    assert "herdr-install" in main
    assert "pane.report_agent_session" in main
    assert "Herdr SessionStart tracking does not write hooks" in main


if __name__ == "__main__":
    test_index_exists()
    test_pstack_is_pinned_url()
    test_catalog_does_not_vendor_skills()
    test_readme_install_is_owner_repo()
    test_grok_native_siblings_validate()
    test_operator_docs_match_live_inspect()
    test_herdr_hooks_sandbox()
    print("PASS tests/test_marketplace.py")
