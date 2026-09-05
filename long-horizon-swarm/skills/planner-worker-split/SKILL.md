---
name: planner-worker-split
description: Bind planner vs worker roles and cost policy onto an existing pstack run. Use when a long-horizon overlay is active or when spend must be explicit.
disable-model-invocation: true
---

# Planner / worker split

Context isolation is the scaling mechanism. Planners keep high-level context and never implement. Workers keep narrow context and never plan.

## Bindings

Read `~/.grok/pstack-models.toml` per pstack `resolve-model.md`. Planner is this parent session. Worker `pstack:feature` (or the matching playbook role) uses toml key `feature`. Verifier `pstack:independent-verifier`. Reconciler `pstack:poteto-agent`. Short coverage inside a leaf uses `/swarm` and toml key `swarm-workers`.

Absent toml sends `grok-4.6` (omit if rejected). Missing key, inherit-parent, or auto omits `model`. Single-family stacked review records `family: same-degraded`.

## Invariants

- A planner that wants to edit product code publishes a worker task instead.
- A worker that wants to change scope writes BLOCKED and stops. It does not replan.
- `conceptKey` is unique among running and pending subtrees.
- Spend rows go to `long-horizon/<id>/spend.tsv` at drain: ts, role, model, tokens, usd, agent_count, unit_id.
- Tokens may be unknown. Still record model and role so mixes stay auditable.
- Recurse is parent-owned units. Children do not call `spawn_subagent`.

## When to apply

Orchestrate, autopilot-*, figure-it-out programs, and any user request that names long-horizon swarm or model economics. Not for a single swarm skill coverage matrix.
