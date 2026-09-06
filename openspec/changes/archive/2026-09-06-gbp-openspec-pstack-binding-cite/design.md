## Context

Tip floor `e3cb0c05`. Fleet openspec-pstack-orch package exists and is authoritative for compose. Tip SPEC/LHS lack cite (S8). A3 Soft-after Act-on preferred over folding into tasks Act-on. #1/#2 supply Parallel band + herd fan-out language this Soft-after points at.

## Goals / Non-Goals

**Goals:** Cite compose (propose gated; parallel after tasks; exclusive worktrees) in SPEC/docs/LHS; Soft-after honesty; keep B8.

**Non-Goals:** Vendor package; invent Drove max_concurrent; remint harden; LIVE_PASS; fold-only (demoted); auto-apply; claim sync done from propose.

## Decisions

1. **NEW capability `openspec-pstack-binding-cite`.** Cite surface is distinct Soft-after deliverable.
2. **Cite path, don't vendor.** Point at `/workspace/fleet-external-agents/openspec-pstack-orch/` (+ README/design/orch-binding spec). Optional short LHS mirror summary OK if it links back.
3. **Soft-after A.** Ordered after #1 (required band language) and preferably #2; propose may land in same Wave-4 batch.
4. **Exclude Drove quotas from gbp text.** Fleet quotas stay in Drove standing orders / fleet package — not gbp product REQUIREMENTS.
5. **No new durable ADR.** Binding philosophy already lives in the fleet package; gbp only cites.
6. **Propose-only Wave-4.** Cite/docs land Wave-5 after Todd go.

## Risks / Trade-offs

- [Cite bitrots if fleet path moves] -> Prefer package-relative name `openspec-pstack-orch` plus path; update on path churn.
- [Operators treat Soft-after as optional forever] -> I1 Prove bar #4 requires cite for parallelism-sync done gate.
- [Fold pressure to delete Soft-after id] -> A3 Soft-after preferred; fold demoted unless Todd go.

## Migration Plan

Propose Soft-after artefacts on worktree. Validate `--strict`. Mirror orch+durable. STOP. Wave-5 after #1/#2 land (or Todd-authorized docs-only): add cites, merge capability, re-validate, archive. No tag move. No vendor copy.

## Open Questions

None that block propose. Exact cite home (SPEC.md vs intent-flow references vs both) is Wave-5 author choice within the requirement.
