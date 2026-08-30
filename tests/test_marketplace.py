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
    assert [p["name"] for p in plugins] == ["pstack"]
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
            ["git", "-C", str(sibling), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        assert src["sha"] == got.stdout.strip()


def test_catalog_does_not_vendor_skills() -> None:
    assert not (ROOT / "skills").exists()
    assert not (ROOT / "plugins").exists()


def test_readme_install_is_owner_repo() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "grok plugin install tommy-ca/pstack --trust" in readme
    assert "xAI Official already publishes a plugin named `pstack`" in readme
    assert "grok plugin install pstack --trust" not in readme
    assert "many sibling folders" not in readme
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
    delta = (
        ROOT
        / "openspec/changes/grok-build-plugins-marketplace/specs/grok-build-marketplace/spec.md"
    )
    assert delta.is_file()
    assert "## ADDED Requirements" in delta.read_text(encoding="utf-8")
    enable_delta = (
        ROOT
        / "openspec/changes/pstack-enable-spawn-docs/specs/grok-build-marketplace/spec.md"
    )
    assert enable_delta.is_file()
    assert "pstack:how-explorer" in enable_delta.read_text(encoding="utf-8")


if __name__ == "__main__":
    test_index_exists()
    test_pstack_is_pinned_url()
    test_catalog_does_not_vendor_skills()
    test_readme_install_is_owner_repo()
    print("PASS tests/test_marketplace.py")
