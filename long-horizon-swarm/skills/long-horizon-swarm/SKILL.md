---
name: long-horizon-swarm
description: >
  Overlay entry for spec-as-root planner/worker trees. Use for /long-horizon-swarm,
  long-horizon swarm, swarm economics, or a standing program the user will leave.
  Routes through poteto-mode and the Orchestrate playbook. Does not replace swarm or Orchestrate.
disable-model-invocation: true
---

# Long-horizon swarm

Entry skill for the overlay. Read `playbooks/long-horizon-swarm.md` beside this file and copy its steps into the todolist after Orchestrate.

If poteto-mode is already active, match that playbook. If not, read poteto-mode Principles and pstack `HARNESS.md` first, then this playbook.

OverlayGate is refuse or run. Missing poteto-mode cannot look like a run.

## Refuse

Stop. Do not spawn.

- **missing-poteto-mode.** Run `grok inspect --json`. If `poteto-mode` is missing from `.skills[].name`, refuse. Tell the operator to run `grok plugin install tommy-ca/pstack --trust`, enable pstack from a host shell, then start a new session. Do not invent a router.
- **one-session.** One agent fits the budget. Route to Autonomous run.
- **flat-swarm.** Coverage matrix with no spec. Route to `/swarm`.
- **second-board.** Ask wants a playbook-local units board or Grok `orch init`. HostStore is Orchestrate durable-state by name.
- **dual-write.** Ask wants HostStore and pstack `scripts/orch` both as the board. Pick HostStore. Codex orch stays on the Codex map.
- **nested-spawn.** A child that would call `spawn_subagent`. Recurse is parent-owned units.
- **openspec-incomplete.** `adr.md` or `tasks.md` missing. OpenSpec is mandatory.
- **shared-write-target.** Two live units share a ConceptKey or exclusive path.

Do not copy pstack leaves into this plugin. Do not rewrite poteto-mode. Do not implement a custom VCS. Do not clone arena or interrogate.

## What this adds

- Spec artifact as the root prompt (**openspec-intent-flow**)
- planner ≠ worker with CostPolicy (**planner-worker-split**)
- Field Guide injection (**field-guide**)
- DesignDoc per conceptKey under `long-horizon/<id>/design-docs/`
- Review lenses stack (**review-lenses**)
- SpendRow per drain
- CoordinationLayer drain hooks (**coordination-layer**, **megafile-gate**, **ossify-break**)

## What this reuses

Call pstack leaves by name. Orchestrate playbook. `/swarm`. arena. interrogate. architect. show-me-your-work. `playbooks/shipping.md`. `playbooks/babysit.md`. session-pickup. pause-safely. Do not route babysit to `/pr-babysit`.

## Spawn

Parent only. Depth 1. Recurse is parent-owned units. Children do not spawn.

```
spawn_subagent
  prompt: Brief
  description: <3-5 words>
  subagent_type: pstack:<role>
  background: true
  isolation: worktree
  model: <toml key for that role, or grok-4.6, omit if inherit-parent>
```

Do not send extra spawn fields. Isolation `none` only when the unit needs this machine. Do not combine `cwd` with `isolation: worktree`.

Worker `pstack:feature` (toml key `feature`). Verifier `pstack:independent-verifier`. Reconciler `pstack:poteto-agent`. Planner is this session.

## Stores

CatalogEntry is name `long-horizon-swarm`, version `1.1.0-long-horizon-swarm.0`, source `./long-horizon-swarm`.

Three stores.

- HostStore. Orchestrate durable-state by name. The board.
- OverlayWorkspace. `long-horizon/<id>/`. Field Guide, spend.tsv, handoffs, design-docs. Not the board.
- OpenSpecChange. `openspec/changes/<id>/`. Spec pipeline. Not the board.
