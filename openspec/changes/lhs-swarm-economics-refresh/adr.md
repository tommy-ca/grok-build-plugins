# ADR Review Manifest

- Status: completed
- Review date: 2026-09-12

## Review Summary

ADR review completed for this change. **No new durable ADR.** Fleet-seat bind, lever-first VERIFY, and a blog failure-mode checklist are overlay refresh / SoT-honesty follow-through. Durable decisions already live in catalog ADRs 0001–0006 (marketplace / sibling layout / SemVer / no pstack nest) and in fleet skills `fleet-org-raci`, `drove-external-loop`, `inner-outer-orch`, plus landed `EXTERNAL-LOOP.md`. Cite those; do not mint a gbp ADR that duplicates fleet RACI or remints thermos / gbp-external-loop-docs. No supersession of in-force catalog ADRs.

## In-Force ADRs Reviewed

- `adr/0001-catalog-is-index-not-plugin-monorepo.md`
- `adr/0002-grok-native-sibling-plugins.md`
- `adr/0003-sibling-tags-include-plugin-name.md`
- `adr/0004-semver-not-calver-for-sibling-tags.md`
- `adr/0005-sibling-not-adapter-version.md`
- `adr/0006-cursor-layout-does-not-nest-pstack.md`

## SemVer bump decision

- From: `1.1.0-long-horizon-swarm.0`
- To: `1.2.0-long-horizon-swarm.N` (N at apply; first land typically `0`)
- Why MINOR not PATCH: fleet bind + lever-first VERIFY contract + falsifiable failure-mode checklist are new overlay capabilities, not a docs patch.
- Why not MAJOR: no break of existing spawn/orch/HostStore / keep-list behaviour.
- Grammar: ADR 0003–0005 — `MAJOR.MINOR.PATCH-long-horizon-swarm.N`; not CalVer; not `-grokbuild.N`; do not move tags.
- Marketplace listing already exists; uniqueness already required — no MODIFY of `grok-build-marketplace`.

## Arena / Act-on locks named

- Sole NEW Act-on id: **`lhs-swarm-economics-refresh`**
- Tip floor: `d03c318c` (gbp-external-loop-docs archive #20 MERGED)
- Do **not** remint `thermos-grok-port` or `gbp-external-loop-docs`
- Do **not** clone arena or interrogate into this plugin — cite pstack
- Dual orch forbidden; Horizon leaf apply default; Drove owns box roles-map / persona cites
- No Elixir Symphony daemon unless Todd asks
- No invent LIVE / LIVE_PASS
- Plugin ships no agents unless a later ADR says so; spawn stays `pstack:<role>`

## New Durable ADRs Created

- None — no major durable architectural decisions were introduced.
