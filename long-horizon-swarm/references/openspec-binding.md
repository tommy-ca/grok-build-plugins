# OpenSpec binding

Not a second type system. Each OpenSpec file is an existing overlay artifact.

| On disk | Is |
| --- | --- |
| `openspec/specs/<cap>/spec.md` | living Spec |
| `openspec/changes/<id>/proposal.md` | Spec preamble; capabilities are conceptKeys |
| `openspec/changes/<id>/specs/<cap>/spec.md` | Spec delta (ADDED/MODIFIED/REMOVED) |
| `openspec/changes/<id>/design.md` | program design doc |
| `openspec/changes/<id>/adr.md` | change-local decision |
| `adr/NNNN-*.md` | durable decision |
| `openspec/changes/<id>/tasks.md` | TaskTree leaves; each checkbox is a Unit; `## Parallel band` `P-parallel` leaves allow N-briefs in exclusive worktrees |
| `openspec/config.yaml` | `schema: intent-driven` |
| `long-horizon/<id>/` | overlay extras, not the board |

Each `#### Scenario` becomes one Brief.ACCEPTANCE line. The unit board is orch when bun can run `orch.ts`, else HostStore. After `tasks.md` validates, independent `P-parallel` leaves under Parallel band headings may fan out to N briefs across exclusive worktrees and join on evidence paths.

## OpenSpec × pstack orch compose binding

Fleet design package reference: `/workspace/fleet-external-agents/openspec-pstack-orch/` (README, `design.md`, `specs/orch-binding/spec.md`).

This repository cites the fleet compose binding rather than vendoring the package into `grok-build-plugins`. OpenSpec intent-driven composes with pstack orchestration under three rules:

1. **Propose gated before apply spawn (B8 KEEP)**: OpenSpec proposal, specs, design, adr, and tasks must exist and validate before implementer workers are spawned. Propose remains serial; specs and design may proceed in parallel after proposal.
2. **Parallelism unlocks after tasks**: Once `tasks.md` exists and validates, independent `P-parallel` leaves under `## Parallel band` headings may fan out to N briefs across exclusive worktrees and join on evidence paths.
3. **Exclusive write targets**: Each parallel unit runs in a distinct exclusive worktree (or conceptKey write target). Dual-writing sibling trees is forbidden.

Non-goals and exclusions:
- **No vendor copy**: The `openspec-pstack-orch` package is referenced by path (or mirrored summary), not vendored as a package tree in `grok-build-plugins`.
- **No Drove quota numbers in product text**: Fleet orchestrator `max_concurrent` quotas stay in Drove standing orders / fleet packages, never as gbp catalog product requirements.

