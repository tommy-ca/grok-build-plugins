# ADR Review Manifest

- Status: completed
- Review date: 2026-09-06

## Review Summary

ADR review completed for this change. No new durable ADR. Citing fleet openspec-pstack-orch compose in gbp SPEC/docs/LHS is documentation follow-through; durable compose decisions live in the fleet package. Arena locks named: **A3 Soft-after** (`gbp-openspec-pstack-binding-cite`); no vendor; no Drove quotas. Depends Soft-after on **A2/A1** band language from `gbp-tasks-parallel-bands` (and herd fan-out). No supersession of in-force catalog ADRs 0001–0006.

## In-Force ADRs Reviewed

- `adr/0001-catalog-is-index-not-plugin-monorepo.md`
- `adr/0002-grok-native-sibling-plugins.md`
- `adr/0003-sibling-tags-include-plugin-name.md`
- `adr/0004-semver-not-calver-for-sibling-tags.md`
- `adr/0005-sibling-not-adapter-version.md`
- `adr/0006-cursor-layout-does-not-nest-pstack.md`

## New Durable ADRs Created

- None - no major durable architectural decisions were introduced.

## Arena / Act-on locks named

- A3 Soft-after binding cite — this id
- Soft-after A after `gbp-tasks-parallel-bands` (+ preferably `gbp-herd-fanout-serial-apply`)
- B8 propose gate KEEP — compose, don't delete
- Drove max_concurrent — OUT of gbp product text
