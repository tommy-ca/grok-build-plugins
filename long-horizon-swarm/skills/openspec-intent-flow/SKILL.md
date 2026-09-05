---
name: openspec-intent-flow
description: >
  Bind OpenSpec intent-driven artifacts onto the long-horizon swarm overlay.
  Use when a program should run proposal → specs/design → adr → tasks → apply → archive,
  or when the user names OpenSpec, /opsx, or intent-driven flows.
disable-model-invocation: true
---

# OpenSpec intent-driven flow

OpenSpec is the on-disk spec language. The swarm overlay is the execution engine. This skill binds them. It does not invent types. It does not replace poteto-mode.

Builds on **long-horizon-swarm**, **planner-worker-split**, **field-guide**, **review-lenses**, and **show-me-your-work**.

## When

- User names OpenSpec, `/opsx:*`, intent-driven, spec-driven, or "agree before you build".
- The long-horizon overlay is active and a Spec artifact would otherwise be a free-form spec blob.
- The work is a program with observable behaviour and decisions that should survive the change.

Not for a one-line bug-fix. That stays on Bug fix.

## Disk

If `openspec/config.yaml` is missing, write:

```yaml
schema: intent-driven
```

Then use this layout. Do not invent a twin.

```
openspec/specs/<capability>/spec.md
openspec/changes/<change>/proposal.md
openspec/changes/<change>/specs/<capability>/spec.md
openspec/changes/<change>/design.md
openspec/changes/<change>/adr.md
openspec/changes/<change>/tasks.md
adr/NNNN-<slug>.md
long-horizon/<change>/
```

The change id is the overlay program id and the TaskTree root id. `long-horizon/<change>/` holds extras and, when bun can run `orch.ts`, the orch unit store. HostStore is the board only when orch cannot run.

## Gates

```
explore? -> proposal -> (specs || design) -> adr -> tasks -> apply -> archive
```

Refuse to spawn workers until `tasks.md` exists and `adr.md` is present. specs and design may proceed in parallel after proposal.

## Binding

Read `references/openspec-binding.md` in this plugin. Short form:

- capability kebab-case = `conceptKey`
- each `#### Scenario` = one Brief.ACCEPTANCE line
- each `tasks.md` checkbox = one Unit
- `design.md` = program DesignDoc
- `long-horizon/<id>/design-docs/<conceptKey>.md` = per-key DesignDoc
- adr.md row = show-me-your-work row
- archive = Close step + merge deltas into `openspec/specs/` + Field Guide curate

## Commands as playbook steps, not a second router

| User says | Do |
| --- | --- |
| `/opsx:explore` or "explore first" | Investigation / how / prototype. No files. |
| `/opsx:propose` | Write proposal.md, then specs + design, then adr, then tasks. Stop for review unless the user said apply too. |
| `/opsx:apply` | Long-horizon-swarm scale/drain/land, one Unit per checkbox. |
| `/opsx:update` | Revise change-folder artifacts from Field Guide surprises. Never edit `openspec/specs/` here. |
| `/opsx:verify` | Review-lenses + ledger on the selected board at the current SHA. |
| `/opsx:sync` or `/opsx:archive` | Merge deltas into truth specs, move change to archive, encode lessons. |

If the OpenSpec CLI is on PATH, prefer `openspec status --change <id>` and `openspec archive <id>` over hand-merging. If it is not, merge by the delta headers and record `cli: absent` in the trail.

## Git discipline

Proposal artifacts land on the integration branch before apply starts. Apply runs in exclusive worktrees. Archive waits until implementation is on the integration branch. This is **sequence-verifiable-units** plus `playbooks/shipping.md`, not a new VCS.

## Planner vs worker

Planner writes proposal, specs, design, adr, tasks, Field Guide index. Worker implements one checkbox. Worker may append a Field Guide surprise. Worker may not edit proposal, design, adr, or `openspec/specs/`.
