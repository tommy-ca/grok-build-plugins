# Grok Build harness for long-horizon-swarm

Host map. grok does not load it as a skill.

| Need | Grok primitive |
|---|---|
| Slash | `/long-horizon-swarm` plus overlay skills `/field-guide`, `/review-lenses`, `/openspec-intent-flow` |
| Spawn | none of its own. Overlay uses `pstack:<role>` from the pstack plugin |
| Skill order | pstack, then user, then this plugin |
| Hooks | none |
| Commands | none. Do not clone `/long-horizon-swarm` into `commands/` |
| Durable board | Grok HostStore (canonical task and agent state). Do not invoke pstack `scripts/orch/orch.ts`. That CLI, including `orch init`, is Codex compatibility only |
| Join | `get_command_or_subagent_output` with `task_ids` and `timeout_ms` > 0 |
| Cancel | `kill_command_or_subagent` |
| Overnight | Orchestrate heartbeat. `/loop` then `scheduler_create`. Watch with `monitor` |
| Isolation | `worktree` unless the unit needs this machine. Do not combine `cwd` with `isolation: worktree` |
