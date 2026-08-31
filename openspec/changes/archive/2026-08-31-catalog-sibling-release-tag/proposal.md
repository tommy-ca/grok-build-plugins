## Why

Catalog siblings all ship `1.0.0-grokbuild.0`. `grok plugin tag --dry-run` on each folder would create the same git tag. The catalog root is not a plugin, so `grok plugin tag .` fails. pstack already has a proven dual-writer train. This catalog has no tags, no workflow, and no unique versions.

## What Changes

- Local sibling versions become `1.0.0-<plugin-name>.0` and stay unique. Marketplace `version` matches `plugin.json`.
- `scripts/release.sh` tags local siblings with `grok --sandbox off plugin tag --push`, git-pushes a local-only tag, then `gh release view` or `gh release create --verify-tag --latest=false`. Optional sibling argument. No args walks every local marketplace row. pstack is never tagged here.
- `.github/workflows/release.yml` on `v*` does the same Release step. No grok. No `workflow_dispatch`.
- Docs name the command and the version scheme.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: local sibling versions are unique and include the plugin name. Catalog tags those versions. pstack stays a sha pin.

## Impact

Sibling `plugin.json` files, `.grok-plugin/marketplace.json`, `scripts/release.sh`, `tests/test_release.py`, `tests/test_marketplace.py`, `.github/workflows/release.yml`, README, SPEC, live marketplace spec, ADR 0003. Not tommy-ca/pstack. Not a catalog-root `plugin.json`.
