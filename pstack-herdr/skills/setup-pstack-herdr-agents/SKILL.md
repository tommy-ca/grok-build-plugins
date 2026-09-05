---
name: Setup pstack herdr agents
description: >-
  Use when configuring pstack task/role → herdr agent routing after arena/I1
  philosophy — like setup-pstack for models; keep arena/interrogate local;
  implement arms may use ready herdr kinds.
---
# Setup pstack herdr agents

Use when configuring which **herdr agent kinds** pstack task/roles route to — the Herd implement-router map, analogous to `/setup-pstack` for models. Also for "configure pstack herdr", "task to agent mapper", or post-arena/I1 route changes.

## Sources

| Layer | Path |
| --- | --- |
| Always-applied rule | `~/.cursor/rules/pstack-herdr-agents.mdc` |
| Twin | `references/pstack-herdr-agents.md` |
| Ready gate | `references/registry.example.md (or operator registry)` |
| Models (do not conflate) | `~/.cursor/rules/pstack-models.mdc` |
| Philosophy audit | `docs/audits/2026-09-05-pstack-herdr-router-arena-i1.md` |

## Invariants (do not violate)

1. `arena runners`, `arena cross-judge pool`, `interrogate reviewers`, `architect runners` stay **`local`** until true multi-kind diversity exists — never N×same kind as fake arena/I1
2. `hardest tasks`, `hillclimb`, judgment/how/why/reflect, `openspec-propose`, `eng-lead-merge`, `prove-it` stay **`local`**
3. Implement keys (`feature`, `openspec-apply`, `swarm workers`, `arena-implement-arm`, …) may point at ready herdr kinds
4. Every real kind on the map must be registry **ready**

## Steps

1. Detect ready herdr kinds from registry  
2. Load current mdc (or defaults above)  
3. Show every role key → route; confirm changes (widget when consequential)  
4. Validate ready-only + invariants  
5. Overwrite mdc + twin; keep labels aligned with poteto / pstack-models  
6. Confirm to operator; point at [Herd with herdr](skill:herd-with-herdr)
