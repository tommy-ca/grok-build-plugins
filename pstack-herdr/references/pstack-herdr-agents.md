# pstack → herdr agent map

Twin of `~/.cursor/rules/pstack-herdr-agents.mdc`. Same idea as `pstack-models.mdc` (role → model), but **role/task → herdr agent kind**.

## Two routers (do not conflate)

| Map | Routes | Consumer | Philosophy |
| --- | --- | --- | --- |
| `pstack-models.mdc` | role → LLM model | Cursor `Task` / poteto | Model diversity for arena / interrogate / judgment |
| `pstack-herdr-agents.mdc` | role/task → herdr kind | [[Herd]] | Session-sized *implement* after Act-on |
| `fleet-roles.mdc` | fleet job → bot/CLI | meta orch | Who owns the desk |

## Arena / interrogate contract

1. **Arena** (Frame→Fan→Cross-judge→Pick→Graft→Verify) runs on **Cursor Task models** (`arena runners` / `cross-judge` = `local`). Never N×same herdr kind.
2. After Act-on, **implement the base** may brief Herd with `pstack_role: arena-implement-arm` (or `openspec-apply` / `feature`) → interactive herdr in a **dedicated worktree**.
3. **Interrogate** reviewers stay `local`. Herd does not synthesize adversarial verdicts. After herdr evidence, Horizon/Heavilifter may run interrogate then prove-it then merge.
4. **Swarm workers** may route to herdr only with **one worktree (or output path) per arm**.

## How Herd routes

1. Brief includes `pstack_role`.
2. Look up mdc; `local` → hand back; kind → registry ready check → [Herd with herdr](skill:herd-with-herdr).
3. Comma lists = preference or true multi-kind fan-out when ready — skip pending; no fake diversity.

## Current defaults (post arena/I1 audit 2026-09-05)

| Keys | Route |
| --- | --- |
| feature, refactoring, bug-fix, perf-issue, swarm workers, openspec-apply, session-apply, arena-implement-arm | `agy` |
| hardest tasks, hillclimb, judgment/how/why/reflect, arena runners, cross-judge, architect, interrogate, propose, merge, prove-it | `local` |

## Edit

[Setup pstack herdr agents](skill:setup-pstack-herdr-agents). Never write pending registry kinds as live routes.

## Audit

`docs/audits/2026-09-05-pstack-herdr-router-arena-i1.md`
