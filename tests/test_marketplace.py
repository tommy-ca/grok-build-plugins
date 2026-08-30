"""Drive the shipped marketplace index (not a reimplementation of grok)."""

from __future__ import annotations

import json
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


def test_catalog_does_not_vendor_skills() -> None:
    assert not (ROOT / "skills").exists()
    assert not (ROOT / "plugins" / "pstack" / "skills").exists()


def test_readme_install_is_owner_repo() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "grok plugin install tommy-ca/pstack --trust" in readme
    assert "cursor/plugins" in readme
    install_pstack = "grok plugin install pstack --trust"
    assert install_pstack not in readme
    assert "many plugin folders" not in readme
    assert "index + `plugins/pstack`" not in readme


if __name__ == "__main__":
    test_index_exists()
    test_pstack_is_pinned_url()
    test_catalog_does_not_vendor_skills()
    test_readme_install_is_owner_repo()
    print("PASS tests/test_marketplace.py")
