## Why

The catalog is pstack-only. Two grok-native siblings earned a port: agent-compatibility and cli-for-agent. Operators need them as installable plugins next to the pstack index entry, not as a vendored cursor/plugins tree and not nested as `plugins/pstack`.

## What Changes

- Cursor-style sibling plugin dirs at catalog root: `agent-compatibility/`, `cli-for-agent/`.
- `.grok-plugin/marketplace.json` keeps pstack as pinned `url` plus sha. Adds local sources `./agent-compatibility` and `./cli-for-agent`.
- Grok-native `plugin.json` (14 parsed fields). Skills and agents. No `commands/`, no `hooks`, no MCP.
- Host map on agent-compatibility for depth-1 `spawn_subagent` types `agent-compatibility:<role>`.
- Tests lock validate, leftover Cursor tokens, and "pstack stays remote".
- ADR 0002. v1 pstack-only is retired. pstack still is not copied into this repo.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: index lists pstack (remote pin) plus grok-native sibling plugins. It MUST NOT nest `plugins/pstack` or vendor `cursor/plugins`.

## Impact

`.grok-plugin/marketplace.json`, `README.md`, `SPEC.md`, `tests/test_marketplace.py`, `adr/0002-*.md`, `agent-compatibility/`, `cli-for-agent/`. Not `tommy-ca/pstack`.
