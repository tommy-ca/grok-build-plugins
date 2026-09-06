# ADR Review Manifest

- Status: completed
- Review date: 2026-09-06

## Review Summary

ADR review completed for this change. No new durable ADR. Parallel band / P-parallel convention in the intent-driven tasks template and openspec-intent-flow narrative is tactical markup under the existing intent-driven schema (A2 home). Arena locks named: **A1 SPLIT**, **A2 template + openspec-intent-flow (+ SPEC)**. Soft-after binding cite is a separate Act-on. No supersession of in-force catalog ADRs 0001–0006.

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

- A1 SPLIT — this id ∥ `gbp-herd-fanout-serial-apply` (P-parallel A)
- A2 convention home — template + openspec-intent-flow (+ SPEC); not tommy-mode; not herdr-only
- Soft-after — `gbp-openspec-pstack-binding-cite` after band language exists
