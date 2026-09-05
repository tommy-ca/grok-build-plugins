---
name: long-horizon-swarm
description: >
  Overlay on poteto-mode Orchestrate for standing programs, swarm economics,
  and spec-as-root. Use for /long-horizon-swarm or a program the user will leave.
  Does not replace swarm or Orchestrate.
disable-model-invocation: true
---

# Long-horizon swarm

Optional overlay on `/poteto-mode` Orchestrate. One skill. One playbook. No agents.

## Start

Start multi-step work with a todolist. First item is to read `/poteto-mode` Principles and pstack `HARNESS.md`. Copy Orchestrate steps in verbatim. Then copy `playbooks/long-horizon-swarm.md` overlay gates.

OverlayGate is refuse or run. Missing poteto-mode cannot look like a run.

## Refuse

Stop. Do not spawn.

- **missing-poteto-mode.** Run `grok inspect --json`. If `poteto-mode` is missing from `.skills[].name`, refuse. Tell the operator to run `grok plugin install tommy-ca/pstack --trust`, enable pstack from a host shell, then start a new session. Do not invent a router.
- **one-session.** One agent fits the budget. Route to Autonomous run.
- **flat-swarm.** Coverage matrix with no spec. Route to `/swarm`.
- **second-board.** Ask wants a playbook-local units board. HostStore is Orchestrate durable-state by name.
- **nested-spawn.** A child that would call `spawn_subagent`. Recurse is parent-owned units.
- **openspec-incomplete.** `adr.md` or `tasks.md` missing. OpenSpec is mandatory. No blob spec fallback.
- **shared-write-target.** Two live units share a ConceptKey or exclusive path.

Do not copy pstack leaves into this plugin.

## What this adds

Playbook gates plus drain extras. Spec-as-root. Planner vs worker CostPolicy. Field Guide. Stacked review. Megafile 800. Ossify as one licensed patch.

## What this reuses

Call pstack leaves by name. Orchestrate playbook. `/swarm`. arena. interrogate. architect. show-me-your-work. `playbooks/shipping.md`. `playbooks/babysit.md`. Do not route babysit to `/pr-babysit`.

## Spawn

Parent only. Depth 1. Recurse is parent-owned units. Children do not spawn.

```
spawn_subagent
  prompt: Brief
  description: <3-5 words>
  subagent_type: pstack:<role>
  background: true
  isolation: worktree
  model: <toml slug or omit>
```

Do not send extra spawn fields. Isolation `none` only when the unit needs this machine. Do not combine `cwd` with `isolation: worktree`.

Worker `pstack:feature` (or matching playbook role). Verifier `pstack:independent-verifier`. Reconciler `pstack:poteto-agent` (conflicts and design only). Planner is this session.

CostPolicy reads `~/.grok/pstack-models.toml`. Absent file sends `grok-4.6` (omit if rejected). Missing key, inherit-parent, or auto omits `model`.

## Stores

CatalogEntry is name `long-horizon-swarm`, version `1.0.0-long-horizon-swarm.0`, source `./long-horizon-swarm`.

Three stores.

- HostStore. Orchestrate durable-state by name. The board.
- OverlayWorkspace. `long-horizon/<id>/` in the target repo. Field Guide and spend.tsv. Not the board.
- OpenSpecChange. `openspec/changes/<id>/`. Spec pipeline. Not the board.

## Glossary

| Name | Meaning |
|---|---|
| planner | this parent session. Never product code. |
| worker | `pstack:<role>` implementer of one checkbox |
| verifier | `pstack:independent-verifier` |
| Field Guide | stigmergy under `long-horizon/<id>/field-guide/` |
| conceptKey | OpenSpec capability kebab |
| SpendRow | tsv row on every drain. tokens may be unknown |
| review lenses | default output-only plus codebase-only. interrogate is one lens |
| arena, interrogate, orchestrate | pstack names. Not copied here |
