from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / ".grok-plugin" / "marketplace.json"


def local_plugins() -> list[tuple[str, Path, dict]]:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    out = []
    for plugin in data["plugins"]:
        src = plugin["source"]
        if isinstance(src, str) and src.startswith("./"):
            name = src[2:].rstrip("/")
            folder = ROOT / name
            manifest = json.loads((folder / "plugin.json").read_text(encoding="utf-8"))
            out.append((name, folder, manifest))
        elif isinstance(src, dict) and src.get("source") == "url":
            continue
        else:
            raise AssertionError(f"unexpected source for {plugin['name']}: {src}")
    return out


def test_no_root_plugin_json() -> None:
    assert not (ROOT / "plugin.json").exists()


def test_local_versions_are_unique_and_named() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    by_name = {p["name"]: p for p in data["plugins"]}
    versions = []
    for name, folder, manifest in local_plugins():
        version = manifest["version"]
        assert re.fullmatch(rf"\d+\.\d+\.\d+-{re.escape(name)}\.\d+", version), version
        assert re.fullmatch(r"\d{4}\.\d{1,2}\.\d{1,2}", version) is None
        assert by_name[name]["version"] == version
        versions.append(version)
    assert len(versions) == len(set(versions)), versions
    assert {name for name, _, _ in local_plugins()} == {
        "agent-compatibility",
        "cli-for-agent",
        "tommy-mode",
    }
    pstack = by_name["pstack"]["source"]
    assert pstack.get("source") == "url"


def test_release_script_host_sandbox_and_dual_writer() -> None:
    script = (ROOT / "scripts/release.sh").read_text(encoding="utf-8")
    assert "grok --sandbox off plugin tag --push" in script
    assert "git push origin" in script
    assert "gh release view" in script
    assert "gh release create" in script
    assert "--verify-tag" in script
    assert "--latest=false" in script
    assert "__GROK_INSIDE_BWRAP" in script
    assert "--force" not in script


def test_github_release_workflow_on_version_tags() -> None:
    wf = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
    assert "v*" in wf
    assert "gh release view" in wf
    assert "gh release create" in wf
    assert "--verify-tag" in wf
    assert "--latest=false" in wf
    assert "contents: write" in wf
    assert "grok plugin tag" not in wf
    assert "workflow_dispatch" not in wf
    assert "test_marketplace.py" not in wf


if __name__ == "__main__":
    test_no_root_plugin_json()
    test_local_versions_are_unique_and_named()
    test_release_script_host_sandbox_and_dual_writer()
    test_github_release_workflow_on_version_tags()
    print("PASS tests/test_release.py")
