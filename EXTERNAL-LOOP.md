# External loop (Symphony-class) — pointer

Thin index for tommy-ca/grok-build-plugins. **Not** a second source of truth.

## Cite (SoT)

| Skill / audit | Id / path |
| --- | --- |
| Inner outer orch | [Inner outer orch](sand-workflow:inner-outer-orch) |
| Fleet org RACI | [Fleet org RACI](sand-workflow:fleet-org-raci) |
| Drove external loop | [Drove external loop](sand-workflow:drove-external-loop) |
| Herd with herdr | [Herd with herdr](sand-workflow:herd-with-herdr) |
| Research twin | `/workspace/fleet-external-agents/audits/2026-09-05-drove-symphony-external-loop-research.md` |

## Symphony → fleet map

| Symphony | Fleet |
| --- | --- |
| tracker poll | boards / `long-horizon/*` + OpenSpec tasks |
| concurrency slot | `max_concurrent` (default 5) + CPU/mem backpressure |
| isolation | CAO cloud VM / Heavilifter worktree / herdr pane |
| WORKFLOW.md | brief + standing-orders |
| stop | VERIFIED \| `human_review` \| quota exhausted |

## Roles

| Role | Duty |
| --- | --- |
| **Drove** | Continuous tick only when brief has goal+quota+TaskTree |
| **Horizon** | Single-change OpenSpec apply/merge (no dual orch with Drove) |
| **CAO** | Default parallel implement (cloud fan-out) |
| **Herd** | Session herdr after Act-on (interactive arms; not scale fan-out) |
| **Heavilifter** | Prove-it / session recovery / on-box worktree when cloud blocked — **not** primary N-arm fan-out |

**Dual orch forbidden.** One orch owner per brief.

## Contracts

- **Lever-first VERIFY** — briefs cite a lever script or verify-* skill; refuse prose-only VERIFY on non-trivial leaves.
- **Herd-journal → Drove reconcile** — stalls/fallbacks append herd-journal; outer tick reconciles.

## Worked example

`thermos-grok-port` #15 propose → #16 apply → #17 archive @ tip floor `35c8c6c` / close `35c8c6c1`: CloudAgent plan-block → Heavilifter on-box recovery worktree → prove (`verify-thermos`) → eng-lead merge. Cite only — do not remint.

## MUST-NOT

- Elixir Symphony daemon (unless Todd/Opus ask)
- Invent LIVE / LIVE_PASS
- Remint `thermos-grok-port` or closed gbp Act-ons
- Vendor full sand-workflow skill bodies here
