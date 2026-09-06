## Context

Tip floor `e3cb0c05b6419e820a1e7d93a374c463059b692d`. Intent-driven schema present; active changes empty (harden archived #8). Template `openspec/schemas/intent-driven/templates/tasks.md` is serial-only. Fleet audit B4/B1 + Arena A2 lock template + openspec-intent-flow (+ SPEC) as convention home. Sibling Act-on `gbp-herd-fanout-serial-apply` owns herdr runtime fan-out (∥ write target). Soft-after `gbp-openspec-pstack-binding-cite` cites fleet openspec-pstack-orch compose once band language exists.

## Goals / Non-Goals

**Goals:** Mint Parallel band A/B + P-parallel in the intent-driven tasks template; add N-briefs / band narrative to openspec-intent-flow (+ SPEC acceptance scenarios); keep true gates serial; preserve B8 propose gate.

**Non-Goals:** Remint harden ids; invent Drove `max_concurrent`; LIVE_PASS / Mainnet dials; tommy-mode as primary home; herdr-only as markup home; auto-apply; claim parallelism-sync done from propose; vendor openspec-pstack-orch; rewrite arena/I1 off local.

## Decisions

1. **NEW capability `openspec-tasks-parallel-bands`.** Prefer ADDED under new capability over MODIFIED `grok-build-marketplace` (marketplace overlay stays cite-only soft fuel).
2. **A2 home = template + intent-flow (+ SPEC).** Graft B1/B4 into this Act-on; do not create a thin A2-home sibling id.
3. **P-parallel A with herd Act-on.** Independent paths (template/LHS vs `pstack-herdr/.../SKILL.md`); propose drafts may land in parallel; apply still exclusive per worktree.
4. **Serial only for true gates.** validate → STOP → Todd-go → archive; Soft-after marked, not fake-ordered with unrelated leaves.
5. **No new durable ADR.** Convention markup is tactical follow-through on existing intent-driven schema + fleet binding philosophy; Soft-after cite owns binding pointer.
6. **Propose-only Wave-4.** Product bodies (template/skill/SPEC edits) land Wave-5 after Todd go.

## Risks / Trade-offs

- [Authors ignore new template headings] -> SPEC scenarios + intent-flow narrative + archive merge make acceptance checkable; Prove bars post-apply.
- [Soft-after binding cites language before #1 lands] -> Soft-after A ordered after #1/#2; docs-only parallel allowed only once band language exists.
- [Drove operators read N-briefs as gbp quota change] -> Explicit non-goal: no max_concurrent invent in gbp text.

## Migration Plan

Propose on worktree branch from tip. Validate `--strict`. Mirror orch+durable. STOP for Todd-go. Wave-5: edit template + intent-flow (+ SPEC), merge capability into `openspec/specs/`, re-validate, archive after land. No tag move.

## Open Questions

None that block propose. tommy-mode parallel surface remains Defer (A2).
