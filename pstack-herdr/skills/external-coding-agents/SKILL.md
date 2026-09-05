---
name: External coding agents
description: >-
  Use when meta-orchestrating external CLI implement work via Herd/herdr —
  pstack arena/interrogate stay on Cursor Task; herdr after Act-on only; bare
  CLI exception-only.
---
# External coding agents

Use when meta-orchestrating session-sized coding work to external CLI agents — including when pstack would spawn a Cursor Task for an **implement**-shaped role after Act-on. Not a replacement for arena or interrogate.

## Principle

Grok Bot = meta orch. External agent = implement in a worktree. Propose, arena parent, interrogate synthesis, prove-it, and eng-lead merge stay on Grok Bot / Cursor Task.

## Spawn policy

1. Brief [[Herd]] with `pstack_role` → resolve `~/.cursor/rules/pstack-herdr-agents.mdc` → interactive herdr ([Herd with herdr](skill:herd-with-herdr))
2. `local` routes (arena runners, interrogate, hardest, hillclimb, propose, merge, prove-it, …) stay on pstack Task
3. Contested design: **arena first (local)** → Act-on → Herd implement (`arena-implement-arm` / `openspec-apply`) → optional **interrogate (local)** → prove-it → merge
4. Swarm partitions via herdr need **distinct worktrees**
5. Bare CLI only after journaled `fallback` + failed herdr heal
6. Registry ready gate — configure via [Setup pstack herdr agents](skill:setup-pstack-herdr-agents)

## Capability lanes

| Lane | Via | Use | Never |
| --- | --- | --- | --- |
| workhorse | interactive `agy` | feature/swarm/openspec-apply/arena-implement-arm | Fake arena/I1 |
| frontier | when ready | hard implement after Act-on | Pending kinds |
| judgment panels | Cursor Task | arena / interrogate / hardest | Herdr same-kind fan-out |

## Brief shape

```
pstack_role / goal / cwd / branch / constraints / done / evidence path / out
```

## After

Evidence → Prove It Works → eng-lead merge + journal. Herd journals `herd_run` / `fallback`.
