## Context

ADR 0001 kept this repo as a remote index and forbade nesting pstack. Grok 1.0.13 marketplace local source is `{ "type": "local", "path": "./name" }` or a plain path string. Cursor's marketplace uses sibling plugin folders at repo root. Official grok docs show `./plugins/gdrive`. User asked for the Cursor sibling layout.

Selected ports from the cursor/plugins audit at `fd87869`:

- `agent-compatibility` (skills plus four review agents, `npx agent-compatibility`)
- `cli-for-agent` (one skill)

Skipped: team-kit, thermos, ralph, canvases, SDK, orchestrate, create-plugin (bundled `/create-skill`), 50 MCP wrappers.

## Goals / Non-Goals

**Goals:** Two grok-native sibling plugins. pstack stays url+sha. Depth-1 spawn map. Scanner for leftover Cursor tokens.

**Non-Goals:** Copying `cursor/plugins`. Nesting pstack. Plugin hooks. MCP. `commands/` clones.

## Decisions

1. **Sibling dirs at catalog root, not `plugins/`.** User asked Cursor layout. Existing test already forbids a `plugins/` nest (that was the open-pstack footgun). Paths `./agent-compatibility` and `./cli-for-agent`.
2. **pstack remains remote.** ADR 0001's anti-nesting stands. ADR 0002 retires "v1 pstack only".
3. **Spawn types are `agent-compatibility:<role>`.** Parent skill fans out four children. No `model: fast`. No `readonly:` frontmatter. Body says do not edit. `capabilityMode: execute`, `inheritSkills: false`, `effort: medium`.
4. **Do not vendor npm.** Scanner stays `npx -y agent-compatibility@latest`.

## Risks / Trade-offs

- [ADR 0001 v1-only] -> 0002 supersedes that sentence only.
- [User already has `cli-for-agents` as a user skill] -> Plugin slash is `/cli-for-agents`. Skill order is pstack then user then plugin.
- [Four review agents vs depth 1] -> Parent fans out. Children do not spawn.

## Migration Plan

Docs list marketplace add, then install each sibling, then enable. pstack install command does not change.

## Open Questions

None.
