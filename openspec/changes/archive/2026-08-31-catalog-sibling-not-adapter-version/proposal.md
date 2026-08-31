## Why

This catalog is many local plugins in one git tag namespace. Shared `1.0.0-grokbuild.0` collided on `v1.0.0-grokbuild.0`. pstack's `-grokbuild.N` is adapter lineage in a single-plugin repo. Specs name the sibling grammar but do not say "do not copy pstack's grokbuild token onto locals." A later agent could unify and reintroduce the collision.

## What Changes

- Specs say local siblings MUST remain `MAJOR.MINOR.PATCH-<plugin-name>.N`.
- Local siblings MUST NOT use `-grokbuild.N`.
- The marketplace pstack row MAY copy pstack's grokbuild version for display. That row stays url+sha and is not a catalog tag.
- Tests reject `grokbuild` on local `plugin.json` versions. No retag. No version bump.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: local sibling identity is plugin name, not pstack's grokbuild adapter token.

## Impact

Live marketplace spec, ADR 0005, `tests/test_release.py`, README, SPEC. Not existing git tags. Not tommy-ca/pstack's tag namespace.
