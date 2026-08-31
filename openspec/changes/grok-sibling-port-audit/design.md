## Context

Audit of HEAD `4020137`. Validate and tests pass. Isolated install in the prior turn loaded four `agent-compatibility:` roles. Remaining holes are contract text, not packaging.

## Goals / Non-Goals

**Goals:** Align ADR 0001 with 0002. Spec and tests lock sibling spawn types. Parent skill names `spawn_subagent` on every child. Scanner covers HARNESS.md for Cursor leftovers.

**Non-Goals:** Re-porting skills. plugin-index.json. Installing into this session's grok.

## Decisions

1. **No new ADR.** Edit 0001 Decision so later plugins may be a sibling folder with a local path, per 0002.
2. **Tighten the existing spawn-types requirement** instead of a new spec name.
3. **HARNESS scan.** Forbid `model: fast`, `readonly: true`, `AskQuestion`, `the Task tool`, `.cursor-plugin` in HARNESS.md. Allow `reasoning_effort` only as the documented never-send line.

## Risks / Trade-offs

- [ADR 0001 history] -> Status stays accepted. 0002 still supersedes v1-only.

## Migration Plan

Docs and tests. No reinstall.

## Open Questions

None.
