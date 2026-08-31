## Why

`tommy-mode` lives as a user skill under `~/.grok/skills/`. That recouples personal overlay with the host profile and keeps it out of the marketplace. pstack must not ship it. The catalog already hosts grok-native siblings.

## What Changes

- Sibling plugin `tommy-mode/` with one skill, grok `plugin.json`, no `commands/`, no hooks, no agents.
- Marketplace local source `./tommy-mode`.
- Tests lock validate and "pstack stays remote."
- Catalog README lists the sibling.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: local sibling `tommy-mode` besides `agent-compatibility` and `cli-for-agent`. pstack stays a remote pin.

## Impact

`tommy-mode/`, `.grok-plugin/marketplace.json`, `README.md`, `SPEC.md`, `tests/test_marketplace.py`, main spec. Not `tommy-ca/pstack`.
