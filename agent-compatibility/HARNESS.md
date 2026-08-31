# Grok Build harness for agent-compatibility

Host map for this plugin. grok does not load it as a skill. The parent skill reads it.

## Mapping

| Need | Grok primitive |
|---|---|
| Slash | `/check-agent-compatibility` from `skills/` |
| Spawn | `spawn_subagent` with `prompt`, `description` (3-5 words), `subagent_type` `agent-compatibility:<role>` |
| Roles | `compatibility-scan-review`, `startup-review`, `validation-review`, `docs-reliability-review` |
| Depth | `MAX_SUBAGENT_DEPTH` 1. This parent fans out. Children do not spawn. |
| Background | `background: true` (TUI default is false) |
| Join | `get_command_or_subagent_output` with `task_ids` and `timeout_ms` > 0 |
| Cancel | `kill_command_or_subagent` |
| Resume | `resume_from` same `subagent_type`. **gap** for this skill. |
| Model | omit `model` to inherit the parent |
| Effort | agent frontmatter `effort`. Never send `reasoning_effort` on spawn. |
| Tool policy | agent `capabilityMode: execute` (shell allowed, no file edits). Body says do not edit. Not grok `read-only` (that mode has no shell, so no `npx`). |
| Isolation | `none` unless the child must not touch the writer tree |
| Todos | `todo_write`. **gap** for this skill. |
| Ask the human | `ask_user_question`. **gap** for this skill. |
| Overnight | `/loop` → `scheduler_create`. **gap** for this skill. |
| Watch | `monitor`. **gap** for this skill. |
| Skill order | pstack, then user, then this plugin |
| Workflows | Not a plugin field. **gap**. |
| Hooks | none. This plugin has no `hooks` key. |

Bare role names are unknown. Spawn `agent-compatibility:startup-review`, not `startup-review`.

Plugin must be in `[plugins].enabled`. Enable from a host shell.
