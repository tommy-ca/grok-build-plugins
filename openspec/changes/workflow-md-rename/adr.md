# ADR Review Manifest

- Status: completed
- Review date: 2026-09-12

## Review Summary

ADR review completed for this change. **No new durable ADR.** Hard-renaming `EXTERNAL-LOOP.md` → `WORKFLOW.md`, flipping living cites, and requiring orchestrators to load tip `WORKFLOW.md` before dispatch is documentation / SoT-honesty follow-through of Symphony upstream WORKFLOW.md + decisions already live in sand-workflow `drove-external-loop`, `fleet-org-raci`, `inner-outer-orch`, `eng-lead-merge-authority`, `herd-with-herdr`, `delegate-to-agy`, and closed `herdr-agy-workflow-bind`. Catalog ADRs 0001–0006 remain in force for marketplace / sibling layout. Cite those; do not mint a gbp ADR that duplicates fleet WORKFLOW/session-path policy. No supersession of in-force catalog ADRs. No Elixir Symphony daemon ADR. No redirect-stub ADR (prefer hard rename).

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

- Sole NEW Act-on id: **`workflow-md-rename`**
- Tip floor: `f4dc2aee4683837dbe841bb6e7ca30575d67104a` (`f4dc2ae`) — herdr-agy-workflow-bind CLOSED #24+#25+#26
- Cite-only closed: `thermos-grok-port`, `lhs-swarm-economics-refresh`, `herdr-agy-workflow-bind` — **do not remint**
- Dual orch forbidden; Horizon leaf apply default; Drove owns continuous tick + Band B skill flip
- No Elixir Symphony daemon unless Todd/Opus ask
- No invent LIVE / LIVE_PASS
- Isolation trinity + Session arms preserved on rename (content not reminted)
- Orchestrators MUST load tip WORKFLOW.md before dispatch (Drove refuse/hold; Horizon cite; Herd named path)
- Drove sand-workflow "read tip WORKFLOW.md" skill flip = Band B Metadata — **not** gbp propose product files
- Prefer hard rename (no redirect stub unless later ADR)
- **STOP** — propose-only; Apply HOLD until Todd/Horizon go
