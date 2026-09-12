# ADR Review Manifest

- Status: completed
- Review date: 2026-09-12

## Review Summary

ADR review completed for this change. **No new durable ADR.** Thin EXTERNAL-LOOP.md pointer and rooms-map charter-row honesty are documentation / SoT-honesty follow-through. Durable decisions already live in catalog ADRs 0001–0006 (marketplace / sibling layout) and in fleet skills `fleet-org-raci`, `drove-external-loop`, `inner-outer-orch`, `herd-with-herdr`. Cite those; do not mint a gbp ADR that duplicates fleet RACI. No supersession of in-force catalog ADRs.

## In-Force ADRs Reviewed

- `adr/0001-catalog-is-index-not-plugin-monorepo.md`
- `adr/0002-grok-native-sibling-plugins.md`
- `adr/0003-sibling-tags-include-plugin-name.md`
- `adr/0004-semver-not-calver-for-sibling-tags.md`
- `adr/0005-sibling-not-adapter-version.md`
- `adr/0006-cursor-layout-does-not-nest-pstack.md`

## New Durable ADRs Created

- None — no major durable architectural decisions were introduced.

## Arena / Act-on locks named

- Sole NEW Act-on id: **`gbp-external-loop-docs`** (prefer over `gbp-symphony-external-loop`)
- Tip floor: `35c8c6c` (thermos archive #17 MERGED)
- Cite thermos #15→#17 as worked example only — **do not remint** `thermos-grok-port`
- Dual orch forbidden; Horizon leaf apply default; Drove owns rooms-map box update
- No Elixir Symphony daemon unless Todd asks
- No invent LIVE / LIVE_PASS
