## Why

cursor/plugins ships MIT **thermos**: dual-rubric thermo-nuclear review (bug/security + code-quality) with a parallel orchestrator skill and two Task subagents. Tip `tommy-ca/grok-build-plugins` @ `e3cb096c` has **no** `thermos/` sibling, no marketplace row, and no OpenSpec Act-on for the port. Operators either stay on Cursor Task APIs or invent a nest under pstack — both violate catalog ADRs 0001–0006 and the poteto bind (arena / interrogate / swarm handoff / lever VERIFY). Sole NEW Act-on `thermos-grok-port` fills the gap. Do not remint closed gbp leaves (#1–#14 cite-only).

## What Changes

- **Wave-4 (this PR):** OpenSpec propose artefacts only under `openspec/changes/thermos-grok-port/`. No product `thermos/` tree. No marketplace edit in this PR.
- **Wave-5 Apply (HOLD until Todd/Horizon go):** Land sibling `thermos/` (plugin.json, README, HARNESS.md, skills/, agents/) adapted from upstream; marketplace `./thermos` + SemVer `MAJOR.MINOR.PATCH-thermos.N`; lever VERIFY scripts/receipts + skill smoke; then validate `--strict` + archive.
- Rewrite orchestration invoke path to **Grok/poteto primitives** (not Cursor `Task` / `subagent_type` / `run_in_background` as the sole API).
- Poteto bind: arena, interrogate, swarm/long-horizon handoff surface, **falsifiable lever VERIFY**.

## Capabilities

### New Capabilities

- `thermos-grok-port`: Grok-native sibling plugin `thermos/` porting dual-rubric + orchestrator from cursor/plugins thermos; HARNESS maps Grok spawn/join; poteto arena/interrogate/swarm/lever VERIFY; marketplace + SemVer `-thermos.N`; no pstack nest; no Cursor-only Task recipes as sole path.

### Modified Capabilities

- `grok-build-marketplace`: list local sibling `thermos` (`./thermos`) beside existing siblings; keep catalog-is-index; full-body MODIFY of sibling-list / version-list / pstack-not-sibling requirements only as required for listing. Prefer ADDED thermos overlay/port requirement under marketplace when apply lands the row.

## Impact

Wave-4: OpenSpec change folder only. Wave-5 (after Todd/Horizon go): `thermos/`, `.grok-plugin/marketplace.json`, catalog README/SPEC/tests as needed, tip merge of NEW capability + marketplace delta. Does **not** nest under `tommy-ca/pstack` or `plugins/pstack`. Does **not** remint closed gbp Act-ons. Does **not** invent LIVE_PASS. Docs-only without installable plugin surfaces → reject at apply.

## Non-goals

- Nest thermos inside pstack / `plugins/pstack`
- Cursor-only Task / `subagent_type` / `run_in_background` as the **sole** invoke path
- Docs-only PR without installable surfaces
- Invent LIVE_PASS / ferro / qstack bleed
- Remint closed gbp leaves (#1–#14)
- Auto-apply or land `thermos/` product in the propose PR

## Probe Evidence Record

- Evidence label: `Static`
  - Query: thermos sibling / marketplace / OpenSpec change on tip
  - Path: tip `e3cb096cb2d68fefbb1629358e83ee4b69473180`; `.grok-plugin/marketplace.json`; `openspec/changes/`
  - Result summary: `thermos/` ABSENT; marketplace row ABSENT; active thermos* change ABSENT; tip = gbp #14 archive MERGED
  - Conclusion: NEW Act-on required; gap real

- Evidence label: `Metadata`
  - Query: Upstream thermos surfaces + ADRs
  - Path: `https://github.com/cursor/plugins/tree/main/thermos`; `adr/0001`–`0006`; inventory `thermos-source.md` / `PORT-SCOPE.md`
  - Result summary: skills×3 + agents×2; MIT; dual-rubric parallel then synthesize; catalog ADRs lock sibling-at-root + SemVer `-thermos.N` + no pstack nest
  - Conclusion: Port map + poteto bind locked (A1 id `thermos`, A2 full poteto, A3 NEW Act-on)
