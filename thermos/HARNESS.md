# Grok Build harness for thermos

Host map. grok does not load it as a skill. The parent orchestrator reads it.

## Mapping

| Need | Grok primitive |
|---|---|
| Slash | `/thermos` from `skills/thermos` (also `/thermo-nuclear-review`, `/thermo-nuclear-code-quality-review`) |
| Spawn | `spawn_subagent` with plugin-qualified `thermos:thermo-nuclear-review-subagent` and `thermos:thermo-nuclear-code-quality-review-subagent` |
| Join | `get_command_or_subagent_output` with `task_ids` and `timeout_ms` > 0 |
| Cancel | `kill_command_or_subagent` |
| Parallel | Launch **both** reviewers in **one** message with `background: true` (TUI default is false) |
| Depth | Parent fans out. Reviewer children do not spawn nested agents unless asked. |
| Model | omit `model` to inherit the parent |
| Effort | Never send `reasoning_effort` on spawn. |
| Skill order | pstack, then user, then this plugin |
| Hooks | none. This plugin has no `hooks` key. |
| Commands | none. Do not clone `/thermos` into `commands/` |
| Lever VERIFY | `scripts/verify-thermos.sh` (catalog root) and/or optional `verify-thermos` skill |

## Poteto bind

| Surface | Role |
|---|---|
| arena | Contested port/design forks for thermos packaging or rubric weight |
| interrogate | Post-apply stacked review lens using thermos dual rubrics |
| swarm / long-horizon handoff | Parallel dual-rubric fan-out when a standing program owns the loop |
| lever VERIFY | Named script `scripts/verify-thermos.sh` — falsifiable, not prose-only |

## Not Cursor Task sole API

This harness maps **Grok** primitives (`spawn_subagent`, `get_command_or_subagent_output`, `kill_command_or_subagent`). Cursor Task / `subagent_type` / `run_in_background` are **not** the sole invoke path. Bare stems (`thermo-nuclear-review-subagent`) are unknown — spawn `thermos:<role>`.

Plugin must be in `[plugins].enabled`. Enable from a host shell. Start a new session after enable.
