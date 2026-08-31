## Why

Live reload verification scored the catalog well on startup, validation, and docs, then listed operator-doc holes. Sibling READMEs stop at enable. Nested enable hits EROFS even when `__GROK_INSIDE_BWRAP` is unset. `inspect` "enabled" and `provides.agents: 1` mislead. `marketplace list` does not browse sibling names.

## What Changes

- After enable, docs say start a new session.
- Docs say `inspect.agents[]` is the live role list. `provides.agents` is the agents directory count.
- Docs say enable and marketplace add rewrite `config.toml` and hit EROFS from a nested grok even without that bwrap env var. Host shell stays the fix.
- Docs say browse siblings with `grok plugin list --json --available`, not `marketplace list`.
- `AGENTS.md` names `python3 tests/test_marketplace.py` as the catalog check.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: operator docs match grok 1.0.13 inspect, enable, and marketplace CLI.

## Impact

`README.md`, sibling READMEs, `SPEC.md`, `AGENTS.md`, `openspec/specs/grok-build-marketplace/spec.md`, `tests/test_marketplace.py`. Not plugin skill bodies. Not pstack.
