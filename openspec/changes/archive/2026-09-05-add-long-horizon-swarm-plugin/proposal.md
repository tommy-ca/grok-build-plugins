## Why

Zip `pstack-long-horizon-swarm-0.1.1` is a Cursor overlay plus a Grok-chat adapter. It is not a Grok Build plugin. Long-horizon planner and worker behavior should be an optional catalog sibling on top of enabled pstack. It must not live in `tommy-ca/pstack`. It must not nest `pstack/` here.

## What Changes

- Sibling plugin `long-horizon-swarm/` with one skill, one playbook, grok `plugin.json`, `HARNESS.md`. No `commands/`, no hooks, no agents.
- Marketplace local source `./long-horizon-swarm`. Version `1.0.0-long-horizon-swarm.0`.
- Tests lock validate, sibling name set, and leftover Cursor or Grok-chat tokens.
- Catalog README and SPEC list the sibling.
- Overlay calls pstack leaves by name. It refuses if poteto-mode is missing.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: local sibling `long-horizon-swarm` besides `agent-compatibility`, `cli-for-agent`, and `tommy-mode`. pstack stays a remote pin. The sibling is an optional overlay on pstack, not a pstack pack.

## Impact

`long-horizon-swarm/`, `.grok-plugin/marketplace.json`, `README.md`, `SPEC.md`, `tests/test_marketplace.py`, `tests/test_release.py`, main spec. Not `tommy-ca/pstack`.
