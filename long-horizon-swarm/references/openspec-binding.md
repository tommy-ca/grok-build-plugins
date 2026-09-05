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
| `openspec/changes/<id>/tasks.md` | TaskTree leaves; each checkbox is a Unit |
| `openspec/config.yaml` | `schema: intent-driven` |
| `long-horizon/<id>/` | overlay extras, not the board |

Each `#### Scenario` becomes one Brief.ACCEPTANCE line. HostStore stays the board.
