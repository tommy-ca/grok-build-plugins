---
name: Fleet roles map
description: >-
  Use when assigning work by fleet role or editing pstack→herdr / fleet maps —
  keep maps updated like pstack-models; arena/I1 stay local on the herdr router.
---
# Fleet roles map

Use when assigning work by fleet role or editing pstack→herdr / fleet role maps — keep always-applied maps updated like pstack-models.

## Sources

1. `~/.cursor/rules/fleet-roles.mdc` + `references/roles-map.example.md (optional)`
2. `~/.cursor/rules/pstack-herdr-agents.mdc` + `references/pstack-herdr-agents.md`
3. `~/.cursor/rules/pstack-models.mdc`
4. `references/registry.example.md (or operator registry)`
5. Philosophy audit: `docs/audits/2026-09-05-pstack-herdr-router-arena-i1.md`

## Two routers

| Map | Routes | Consumer |
| --- | --- | --- |
| pstack-models | role → LLM | Cursor Task / arena / I1 |
| pstack-herdr-agents | role → herdr kind | Herd implement only |
| fleet-roles | job → bot/CLI | meta orch |

Arena/interrogate keys stay `local` on the herdr map. Edit herdr routes with [Setup pstack herdr agents](skill:setup-pstack-herdr-agents).

## Anti-jobs

Do not invent agents; do not point herdr routes at pending CLIs; do not map arena runners or interrogate reviewers to a single herdr kind.
