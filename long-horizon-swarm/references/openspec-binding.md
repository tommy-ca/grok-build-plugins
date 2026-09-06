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
