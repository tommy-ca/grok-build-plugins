# External loop — Symphony WORKFLOW.md twin (gbp)

In-repo **WORKFLOW.md twin** for tommy-ca/grok-build-plugins. **Map, not clone** of Elixir Symphony. Pointer/index — **not** a second SoT. Cite sand-workflow skills; do not vendor skill bodies.

Upstream: https://openai-symphony.mintlify.app/setup/workflow-file  
Research: `/workspace/fleet-external-agents/audits/2026-09-05-drove-symphony-external-loop-research.md`

---
tracker:
  board: boards / long-horizon/* + OpenSpec tasks
polling:
  tick: Drove continuous tick when brief has goal+quota+TaskTree
  horizon: single-change OpenSpec apply/merge only (not continuous tick)
workspace:
  isolation_trinity:
    CAO: cloud VM (scale fan-out)
    Herd_session: herdr pane + kind=agy (session implement / PR-review)
    Heavilifter: on-box worktree recovery (prove-it / when cloud blocked — not primary N-arm fan-out)
agent:
  max_concurrent: 5
  backpressure: CPU/mem (Drove-owned concurrency policy)
hooks: optional / N/A
observability:
  - approvals journal
  - herd-journal (stalls / fallbacks)
---

## Cite (SoT)

| Skill / audit | Id / path |
| --- | --- |
| Inner outer orch | [Inner outer orch](sand-workflow:inner-outer-orch) |
| Fleet org RACI | [Fleet org RACI](sand-workflow:fleet-org-raci) |
| Drove external loop | [Drove external loop](sand-workflow:drove-external-loop) |
| Herd with herdr | [Herd with herdr](sand-workflow:herd-with-herdr) |
| Delegate to agy | [Delegate to agy](sand-workflow:delegate-to-agy) |
| Herd failure journal | [Herd failure journal](sand-workflow:herd-failure-journal) |
| Research twin | `/workspace/fleet-external-agents/audits/2026-09-05-drove-symphony-external-loop-research.md` |

Living prior pointer Act-on: `gbp-external-loop-docs` (cite only — this file is rewritten under NEW capability `herdr-agy-workflow-bind`, without MODIFY of that living spec).

## Agent / orch contract

### Eligibility

A unit may be dispatched when:

- Brief (or OpenSpec change) has **goal + quota + TaskTree** (Drove continuous tick), **or** a locked Act-on / tasks band for a single-change leaf (Horizon apply)
- Isolation surface is exclusive for the conceptKey (no dual orch; no nested child spawn as whole program)
- VERIFY names a **lever** (script path or `verify-*` skill) for non-trivial leaves — prose-only VERIFY is refused

### Dispatch

| Arm | Who | How / isolation |
| --- | --- | --- |
| Scale fan-out | **CAO** | Cloud VM — default parallel implement |
| Session implement / PR-review | **Herd** | herdr pane + `kind=agy` via [Herd with herdr](sand-workflow:herd-with-herdr) → [Delegate to agy](sand-workflow:delegate-to-agy) |
| Recovery / prove-it | **Heavilifter** | On-box worktree when cloud blocked — **not** primary N-arm fan-out |

**Drove** owns continuous tick + `max_concurrent` (default **5**) + CPU/mem backpressure. Herd fills herdr slots under that policy; CAO scale uses separate cloud concurrency. **Horizon** owns single-change OpenSpec apply/merge only.

### Reconcile

Outer tick (Drove) joins evidence: boards / OpenSpec tasks / HostStore / herd-journal. Stalls and fallbacks append [Herd failure journal](sand-workflow:herd-failure-journal); Drove reconciles restart vs handoff. Horizon reconciles leaf merge bars only — not the continuous loop.

### Retry / stall

1. Heal in place (same isolation surface) when safe  
2. Journal `stall` / `fallback` / `fallback_used` via herd-failure-journal  
3. Restart under Drove tick **or** hand off (see below)  
4. Do **not** normalize bare `agy --print` as the default recovery path

### Handoff

Terminal / stop states for the external loop:

| State | Meaning |
| --- | --- |
| `VERIFIED` | Prove bars held; eng-lead / merge authority satisfied |
| `human_review` | Orch stops; eng-lead / Todd review (not product VERIFIED) |
| quota exhausted | Stop on spend / wall / max_units / max_concurrent — do not invent LIVE |

### Lever-first VERIFY

Brief.VERIFY MUST cite a lever script or `verify-*` skill. Refuse prose-only VERIFY on non-trivial leaves. Prefer build-the-lever / prove-it over N×agy fake arena.

## Session arms (Herd → herdr → agy)

Default **session** path after Act-on / tasks exist:

1. **Herd** owns session-sized interactive orch  
2. [Herd with herdr](sand-workflow:herd-with-herdr) → [Delegate to agy](sand-workflow:delegate-to-agy) (interactive agy via herdr; herdr default)  
3. Bare `agy --print` is **exception-only** (herdr down or prompt still stalled after heal) — MUST journal fallback via [Herd failure journal](sand-workflow:herd-failure-journal) **first**  
4. **CAO** = scale on **cloud VM** (not herdr pane; not Heavilifter worktree)  
5. **Herd session isolation** = **herdr pane + `kind=agy`** (not cloud VM; not Heavilifter worktree)  
6. **Heavilifter** = **on-box worktree** recovery / prove-it when cloud blocked — not a herdr pane substitute for scale  
7. **Dual orch forbidden** — exactly one orch owner per brief (Horizon leaf XOR Drove continuous tick)  
8. **Isolation trinity stays distinct** — do not collapse CAO / Herd / Heavilifter into one path

### Box SoT honesty (cite-only; no remint)

Session arms are **already VERIFIED** on box SoT under `/home/box/sand-data/workflows/` for:

- `fleet-org-raci`
- `inner-outer-orch`
- `eng-lead-merge-authority`
- `fleet-roles-map`

**Drove / Opus / eggbot** own those skill bodies. This gbp twin **cites** them — does **not** remint skill bodies or personas B1 (herdr-agy-pr-review-lane already VERIFIED).

## Roles (quick map)

| Role | Duty |
| --- | --- |
| **Drove** | Continuous tick when goal+quota+TaskTree; owns `max_concurrent` + backpressure |
| **Horizon** | Single-change OpenSpec apply/merge (no dual orch with Drove) |
| **CAO** | Default parallel implement — **cloud VM** scale fan-out |
| **Herd** | Session herdr after Act-on — **herdr pane + kind=agy** |
| **Heavilifter** | Prove-it / recovery — **on-box worktree** when cloud blocked |

## Worked example

`thermos-grok-port` #15 propose → #16 apply → #17 archive @ tip floor `35c8c6c` / close `35c8c6c1`: CloudAgent plan-block → Heavilifter on-box recovery worktree → prove (`verify-thermos`) → eng-lead merge. Cite only — do not remint.

## MUST-NOT

- Elixir Symphony daemon (unless Todd/Opus ask)
- Invent LIVE / LIVE_PASS
- Remint `thermos-grok-port`, `gbp-external-loop-docs`, or `lhs-swarm-economics-refresh`
- Vendor full sand-workflow skill bodies here
- Collapse isolation trinity (CAO / Herd / Heavilifter)
- Dual orch (Horizon + Drove on the same brief)
- Thin-only cite regress (omit frontmatter-equivalent runtime or body contract)
