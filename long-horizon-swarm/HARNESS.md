# Grok Build harness for long-horizon-swarm

Host map. grok does not load it as a skill.

## Fleet seats (cite WORKFLOW.md)

Standing-program overlay roles bind to fleet seats per repo-root `WORKFLOW.md` (sand-workflow seats; do not remint `gbp-external-loop-docs`; do not vendor sand-workflow skill bodies):

| Overlay need | Fleet seat |
|---|---|
| Propose / plan-with-code / OpenSpec artefacts | **Planner** |
| Single-change OpenSpec apply/merge | **Horizon** |
| Continuous tick (goal + quota + TaskTree) | **Drove** |
| Default parallel implement (cloud fan-out) | **CAO** (Cloud Agent Orchestrator) |
| Session herdr pane after Act-on (interactive arms; not CAO scale) | **Herd** |
| Prove-it / session recovery / on-box worktree when cloud blocked — **not** primary N-arm fan-out | **Heavilifter** |
| Verification cadence / maintain-verification | **Nightly Audit** (Nightly Audit Engineer) |

**Dual orch forbidden.** Exactly one orch owner per brief (Horizon leaf apply/merge XOR Drove continuous tick — never both).

**Session arms:** default Herd→herdr→agy per repo-root `WORKFLOW.md` (cite [Herd with herdr](sand-workflow:herd-with-herdr) + [Delegate to agy](sand-workflow:delegate-to-agy); do not clone arena/interrogate here).

## Grok primitives

| Need | Grok primitive |
|---|---|
| Slash | `/long-horizon-swarm` plus overlay skills `/field-guide`, `/review-lenses`, `/openspec-intent-flow` |
| Spawn | none of its own. Overlay uses `pstack:<role>` from the pstack plugin |
| Skill order | pstack, then user, then this plugin |
| Hooks | none |
| Commands | none. Do not clone `/long-horizon-swarm` into `commands/` |
| Durable board | If `bun` or `node` can run pstack `skills/poteto-mode/scripts/orch/orch.ts`, `orch init --store long-horizon/<id>` is the overlay unit store. If neither exists (Grok chat sandbox), skip orch and use HostStore plus extras only |
| Join | `get_command_or_subagent_output` with `task_ids` and `timeout_ms` > 0 |
| Cancel | `kill_command_or_subagent` |
| Overnight | Orchestrate heartbeat. `/loop` then `scheduler_create`. Watch with `monitor` |
| Isolation | `worktree` unless the unit needs this machine. Do not combine `cwd` with `isolation: worktree` |
