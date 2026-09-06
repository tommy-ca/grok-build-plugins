# ADR Review Manifest

- Status: completed
- Review date: 2026-09-06

## Review Summary

ADR review completed for this change. No new durable ADR. Syncing tip `herd-with-herdr` toward box Parallel fan-out + `serial_apply` journal is a skill-policy follow-through under the existing pstack-herdr overlay (harden cite-only). Arena locks named: **A1 SPLIT** (this id ∥ `gbp-tasks-parallel-bands`). Honest tip-lag vs box lead is required. No supersession of in-force catalog ADRs 0001–0006.

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

- A1 SPLIT — P-parallel A with `gbp-tasks-parallel-bands`
- B3 — tip LAGS box; sync into plugin sibling; do not claim tip already patched
- Soft-after — binding cite is a separate Act-on (`gbp-openspec-pstack-binding-cite`)
