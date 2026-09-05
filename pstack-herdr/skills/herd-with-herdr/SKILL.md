---
name: Herd with herdr
description: >-
  Use when routing or orchestrating external agents through herdr as the pstack
  implement router — arena/interrogate stay on Cursor Task (local); herdr after
  Act-on only; interactive default; not for propose or eng-lead merge.
---
# Herd with herdr

Use when a Grok Bot (especially [[Herd]]) **routes, monitors, and orchestrates** external coding agents through **herdr** — including as the **pstack agent router** (task/role → herdr kind). Pair with [External coding agents](skill:external-coding-agents), [Delegate to agy](skill:delegate-to-agy), and [Setup pstack herdr agents](skill:setup-pstack-herdr-agents).

## Install

`mise use -g herdr` — fleet box **0.8.2**. Opus owns upgrades/PATH/hooks. Binary authority: `herdr --help` / `herdr agent` (never invent flags).

## Standing policy (Todd 2026-09-05)

**herdr is the answer** for monitor + orch of *implement* agents. Interactive herdr is default and allowed. Bare CLI `--print` is exception-only.

## Pstack philosophy (arena / interrogate)

Herd is **not** a substitute for poteto arena or interrogate.

| Concern | Owner | Router |
| --- | --- | --- |
| Arena Frame→Fan→Cross-judge→Pick→Graft→Verify | Horizon / poteto on Cursor Task | `pstack-models` + `arena runners` = **local** |
| Interrogate multi-model review | Horizon / poteto (readonly Tasks) | `interrogate reviewers` = **local** |
| Session-sized implement after Act-on | Herd → herdr | `openspec-apply` / `feature` / `arena-implement-arm` / `swarm workers` → ready kind |
| Prove It Works / eng-lead merge / OpenSpec propose | Heavilifter / Horizon / Planner | **local** |

**Anti-patterns (Act-on from 2026-09-05 arena/I1 audit):**

- Do not spawn N×`agy` and call it an arena — adversarial/generation diversity needs **model** (or true multi-kind) diversity
- Do not route `arena runners`, `arena cross-judge pool`, or `interrogate reviewers` to herdr
- Do not run cross-judge or I1 synthesis inside Herd
- Contested design order: arena (local) → Act-on → Herd implement → optional interrogate (local) → prove-it → merge
- Swarm via herdr: **one worktree or output path per arm** (separate-before-serializing)

## Pstack agent router

| Map | Path |
| --- | --- |
| Task/role → herdr kind | `~/.cursor/rules/pstack-herdr-agents.mdc` |
| Twin | `references/pstack-herdr-agents.md` |
| Role → model | `~/.cursor/rules/pstack-models.mdc` — judgment only |
| Ready gate | `references/registry.example.md (or operator registry)` |

### Resolve

1. Read `pstack_role` from the brief. Default `openspec-apply` only for explicit session-apply briefs; else ask caller once.
2. Look up `pstack-herdr-agents.mdc`.
3. `local` | `pstack-task` | `inherit-parent` → **do not spawn**; return `routed: local` with reason.
4. Kind list → first **ready** kind (or one pane per ready entry for true multi-kind swarm/arena-*implement* fan-out only). Skip pending. Never fake diversity with duplicate same-kind panes for judgment panels.
5. Configure with [Setup pstack herdr agents](skill:setup-pstack-herdr-agents).

### Brief contract

```
pstack_role: <key>
goal / cwd|worktree / branch / constraints / done / evidence path / out
# swarm: one brief per arm, distinct worktree
```

Return: `routed_kind`, agent name, evidence path — or `routed: local`.

## Outside-driver

Ignore upstream `HERDR_ENV=1` gate. Never bare `herdr` TUI for discovery; never `server stop` unless Opus/Todd.

## Role split

Herd = route + herdr orch + journal. Horizon/Heavilifter = prove-it + merge (+ arena/I1 parent). Opus = install. herdr agent = implement only.

## Lifecycle truth

`working` / `idle` / `done` / `blocked` / `unknown` — idle/done ≠ task-complete without evidence file. CLI read does not mark seen — `agent focus` when needed. Prefer `recent-unwrapped`.

## Interactive orch loop (after route resolve)

0. `herdr status` / `agent list` / heal via Opus before bare fallback  
1. Topology: reuse or `workspace create` / `pane split` `--cwd` `--no-focus`; JSON ids  
2. `herdr agent start <name> --kind <routed> --pane <id>`  
3. `herdr agent prompt … --wait --timeout` multi-turn; blocked → inspect → `send-keys`  
4. Evidence → journal `herd_run` → hand Heavilifter/Horizon (`pstack_role`, kind, path)  
5. Fallback: journal `fallback` → one bare `--print` → heal → return interactive  

## Safety / anti-jobs

One writer per worktree; no LIVE_PASS; no Mainnet dials; arena before contested spawn graphs; interrogate before herd-wide kill; no product code / propose / merge / desk spam. Blocked → Secretary TLDR.
