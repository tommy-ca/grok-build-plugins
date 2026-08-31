## Why

The sibling ports validate and the catalog lists them. The audit still found contract holes. ADR 0001 still says later plugins are url+sha only. The spawn-types spec only names `pstack:how-explorer`. The leftover-token scan skips HARNESS.md. The parent skill omits `spawn_subagent` on three of four children.

## What Changes

- ADR 0001 Decision allows sibling local folders per ADR 0002.
- Spec spawn-types also names `agent-compatibility:<role>`.
- Skill steps 2-4 use full `spawn_subagent` `subagent_type`.
- Tests scan HARNESS.md for Cursor leftover tokens. `reasoning_effort` as a "never send" phrase is allowed only there.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: docs and tests cover sibling spawn types. ADR 0001 matches ADR 0002.

## Impact

`adr/0001-*.md`, `openspec/specs/grok-build-marketplace/spec.md`, `agent-compatibility/skills/check-agent-compatibility/SKILL.md`, `tests/test_marketplace.py`, README if spawn types need a second mention.
