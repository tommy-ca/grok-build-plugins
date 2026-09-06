## Why

Tip `e3cb0c05` ships intent-driven OpenSpec with a serial-only `tasks.md` template (`## 1.` / `## 2.` numbered groups). Fleet bottleneck B4: total-order sections hide independent leaves, so Horizon/Drove cannot spawn N briefs for P-parallel apply. LHS `openspec-intent-flow` allows specs∥design after proposal but lacks N-briefs / parallel-band apply narrative (B1). Arena A2 locks convention home = template + openspec-intent-flow (+ SPEC scenarios) — not tommy-mode, not herdr-only. Without Parallel band markup, TaskTree fan-out stays under-armed even when paths do not conflict.

## What Changes

- Extend `openspec/schemas/intent-driven/templates/tasks.md` with `## Parallel band A/B` headings and `P-parallel` leaf tags; keep numbered serial sections only for true gates (validate → STOP → Todd-go apply → archive).
- Add openspec-intent-flow (+ SPEC) narrative: after `tasks.md` exists, Horizon/Drove MAY spawn N briefs for P-parallel leaves (one exclusive worktree each); Soft-after / true-gate leaves stay serial.
- Land SPEC/OpenSpec acceptance scenarios for parallel-band markup and N-briefs orch language — docs/SPEC, **not** Drove `max_concurrent` caps.
- Wave-4 = OpenSpec artefacts only — product template/skill/SPEC bodies land Wave-5 after Todd go.

## Capabilities

### New Capabilities

- `openspec-tasks-parallel-bands`: Intent-driven tasks template Parallel band A/B + P-parallel leaf convention; openspec-intent-flow N-briefs / band apply narrative; SPEC scenarios for band acceptance; serial only for true gates; no Drove caps; no remint harden.

### Modified Capabilities

- _(none — prefer ADDED under new capability; tip `grok-build-marketplace` remains cite-only soft fuel for marketplace/herdr overlay context)_

## Impact

OpenSpec propose artefacts only in Wave-4. Wave-5 apply (after Todd go) edits tip `openspec/schemas/intent-driven/templates/tasks.md`, `long-horizon-swarm/skills/openspec-intent-flow/SKILL.md` (+ optional binding refs), and repo `SPEC.md` / marketplace docs scenarios for N-briefs / band acceptance. Merges NEW capability into tip `openspec/specs/openspec-tasks-parallel-bands/`. Does **not** remint `fix-release-test-herdr-set` / `openspec-marketplace-pstack-herdr`. Does **not** invent Drove `max_concurrent` / LIVE_PASS. Soft-before Soft-after binding cite (`gbp-openspec-pstack-binding-cite`). P-parallel A with `gbp-herd-fanout-serial-apply` (independent write targets).

## Probe Evidence Record

- Evidence label: `Static`
  - Query: Tip tasks.md template Parallel band / P-parallel
  - Path: `openspec/schemas/intent-driven/templates/tasks.md`
  - Command: tip @ `e3cb0c05` — serial-only `## 1.` / `## 2.` groups; Parallel band / P-parallel MISSING (S4 / B4)
  - Result summary: Template gap confirmed.
  - Conclusion: Act-on #1 primary mint surface = template.

- Evidence label: `Static` / `Metadata`
  - Query: openspec-intent-flow N-briefs / band apply; SPEC parallel-band
  - Path: `long-horizon-swarm/skills/openspec-intent-flow/SKILL.md`; repo `SPEC.md`; `openspec/specs/grok-build-marketplace/spec.md`
  - Result summary: specs∥design OK; N-briefs / band apply MISSING (S6/S7 / B1); marketplace herdr overlay present without parallel-band scenarios.
  - Conclusion: Graft A2 home into #1 (template + intent-flow + SPEC).

- Evidence label: `Metadata`
  - Query: Arena A1–A3 + I1 Act-on lock
  - Path: `arena/SYNTHESIS.md`; `i1/I1.md`; `i1/change-ids.md`
  - Result summary: A1 SPLIT; A2 template+intent-flow(+SPEC); Act-on `gbp-tasks-parallel-bands` LOCKED P-parallel A.
  - Conclusion: Propose locked id; Soft-after #3; no mega Act-on; no remint harden.
