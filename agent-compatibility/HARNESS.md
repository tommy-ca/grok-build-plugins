# Grok Build harness for agent-compatibility

Host map for this plugin. grok does not load it as a skill. The parent skill reads it.

## Mapping

| Need | Grok primitive |
|---|---|
| Slash | `/check-agent-compatibility` from `skills/` |
| Spawn | `spawn_subagent` `subagent_type` `agent-compatibility:<role>` |
| Roles | `compatibility-scan-review`, `startup-review`, `validation-review`, `docs-reliability-review` |
| Depth | `MAX_SUBAGENT_DEPTH` 1. This parent fans out. Children do not spawn. |
| Background | `background: true` then join with `get_command_or_subagent_output` |
| Model | omit to inherit, or `grok-4.6` if the file is absent |
| Effort | agent frontmatter `effort`. Never send `reasoning_effort` on spawn. |
| Read-only | body rule. Not a spawn field. |
| Isolation | `none` unless the child must not touch the writer tree |

Bare role names are unknown. Spawn `agent-compatibility:startup-review`, not `startup-review`.

Plugin must be in `[plugins].enabled`. Enable from a host shell.
