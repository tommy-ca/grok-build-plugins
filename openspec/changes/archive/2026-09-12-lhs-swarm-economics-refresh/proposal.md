## Why

Todd asked the room to audit `long-horizon-swarm` against Cursor swarm economics (Wilson Lin, Jul 2026) plus poteto arena/interrogate/lever and fleet EXTERNAL-LOOP seats. Tip `d03c318c` already ships a strong overlay (planner≠worker + CostPolicy, Field Guide, review-lenses, megafile-gate, ossify-break, openspec-intent-flow, refuse flat-swarm/dual-board/nested-spawn). Gaps remain: HARNESS/README are still Grok-CLI spawn-centric (no Drove/Horizon/CAO/Herd/Heavilifter bind), Brief.VERIFY/handoff allow prose-only proof, blog failure modes are not a falsifiable playbook/standing-orders checklist, SemVer is still `1.1.0-long-horizon-swarm.0`, and fleet roles-map/personas do not cite overlay skills when a standing program is armed. Sole NEW Act-on `lhs-swarm-economics-refresh` closes those gaps. Do not remint `thermos-grok-port` or `gbp-external-loop-docs`. Do not clone arena/interrogate into this plugin.

## What Changes

- **Wave-4 (this PR):** OpenSpec propose artefacts only under `openspec/changes/lhs-swarm-economics-refresh/`. No product `long-horizon-swarm/` edits. No marketplace SemVer bump. No box roles-map / persona edits from this git PR.
- **Wave-5 Apply (HOLD until Todd/Horizon go):**
  - Refresh HARNESS/README/playbook/standing-orders/handoff-contract with fleet seat bind + lever-first VERIFY + blog failure-mode checklist.
  - Bump SemVer `1.1.0-long-horizon-swarm.0` → `1.2.0-long-horizon-swarm.N` (N chosen at apply; first land typically `.0`) in `plugin.json` and marketplace `plugins[].version`.
  - Prove `scripts/verify-long-horizon-swarm.sh` green + `python3 tests/test_marketplace.py` PASS.
  - Drove/eggbot applies fleet roles-map / `fleet-roles.mdc` / persona cite lines on box SoT (split like rooms-map).
  - Merge NEW capability into tip `openspec/specs/lhs-swarm-economics-refresh/`; `openspec validate --strict`.

## Capabilities

### New Capabilities

- `lhs-swarm-economics-refresh`: Refresh long-horizon-swarm overlay with EXTERNAL-LOOP fleet bind, lever-first VERIFY, blog failure-mode checklist, SemVer `1.2.0-long-horizon-swarm.N`, prove lever, and box SoT roles-map/persona cite honesty. Keep existing overlay invariants. Arena/interrogate stay pstack cites.

### Modified Capabilities

- _(none — marketplace already lists `long-horizon-swarm` and already requires unique `MAJOR.MINOR.PATCH-<plugin-name>.N`; the SemVer bump is apply-time product identity, not a listing-behaviour change)_

## Impact

Wave-4: OpenSpec change folder only. Wave-5 (after Todd/Horizon go): overlay HARNESS/playbook/skills/references + SemVer + verify script/marketplace tests; tip merge of NEW capability; Drove/eggbot updates box `roles-map.md` / `fleet-roles.mdc` / personas. Does **not** remint `thermos-grok-port` or `gbp-external-loop-docs`. Does **not** clone arena/interrogate. Does **not** invent LIVE_PASS. Does **not** nest under pstack. Docs-only without installable skill/HARNESS/lever deltas → reject at apply.

## Non-goals

- Remint `thermos-grok-port` or `gbp-external-loop-docs`
- Clone arena / interrogate into this plugin (cite pstack)
- Nest under pstack / invent Cursor VCS / Elixir Symphony daemon
- Invent LIVE / LIVE_PASS
- Dual orch / flat-swarm / dual-board / nested-spawn
- Product plugin edits or SemVer bump in the propose PR
- Marketplace MODIFY (listing already exists; uniqueness grammar already in force)
- Docs-only apply without HARNESS / playbook / lever deltas

## Probe Evidence Record

- Evidence label: `Static`
  - Query: Tip SHA and EXTERNAL-LOOP.md present?
  - Path: `/workspace/verify/grok-build-plugins` @ `d03c318c9885b11d07ce5725629874f0e3eb165b`
  - Result summary: HEAD `d03c318` — Merge PR #20 gbp-external-loop-docs archive; repo-root `EXTERNAL-LOOP.md` present (roles + lever-first VERIFY + dual-orch forbidden).
  - Conclusion: Tip floor held; cite EXTERNAL-LOOP, do not remint that Act-on.

- Evidence label: `Static`
  - Query: Overlay version + HARNESS/README fleet bind?
  - Path: `long-horizon-swarm/plugin.json`, `HARNESS.md`, `README.md`
  - Result summary: version `1.1.0-long-horizon-swarm.0`. HARNESS is Grok-CLI spawn/join/orch/worktree only — no Drove/Horizon/CAO/Herd/Heavilifter seats. README is install + overlay skill list; no fleet bind.
  - Conclusion: Apply must refresh HARNESS/README with EXTERNAL-LOOP seat map; propose must not.

- Evidence label: `Static`
  - Query: Brief.VERIFY / handoff lever-first?
  - Path: playbook step 5; `references/handoff-contract.md`; `references/standing-orders-template.md` #7
  - Result summary: Brief lists a VERIFY field but does not require `verify-*` or `scripts/verify-*.sh`. Handoff Verification is an enum (`live-ui-verified` / `unit-test-verified` / `type-check-only` / `not-verified`) with no lever path. Standing-order 7 says "real artifact" but not a named lever.
  - Conclusion: Lever-first VERIFY is a real gap; refuse prose-only on non-trivial leaves.

- Evidence label: `Static`
  - Query: Blog failure modes as falsifiable checklist?
  - Path: playbook "Article loop" table; overlay skills field-guide / review-lenses / megafile-gate / ossify-break / planner-worker-split / coordination-layer
  - Result summary: Article loop maps 9 blog steps onto playbook steps. Skills already implement planner≠worker, Field Guide, review-lenses, megafile-gate, ossify-break, reconciler. No single playbook/standing-orders checklist that treats split-brain, planner contention, merge reconciler, megafiles, ossify, review lenses, Field Guide, and model economics as named refuse/stop checks.
  - Conclusion: Keep the skills; add a falsifiable checklist. Cite https://cursor.com/blog/agent-swarm-model-economics (Wilson Lin, Jul 2026).

- Evidence label: `Static`
  - Query: Prove lever present?
  - Path: `scripts/verify-long-horizon-swarm.sh`; `.grok-plugin/marketplace.json` long-horizon-swarm row
  - Result summary: Verify script exists (marketplace functions + `test_release.py` + `grok plugin validate` + orch probe). Marketplace row version `1.1.0-long-horizon-swarm.0`.
  - Conclusion: Apply must bump SemVer and keep the lever green; extend the script if new HARNESS/checklist assertions are needed.

- Evidence label: `Metadata`
  - Query: Fleet roles-map / personas cite overlay skills?
  - Path: `/workspace/fleet-external-agents/roles-map.md`; `~/.cursor/rules/fleet-roles.mdc`; research `/workspace/fleet-external-agents/audits/2026-09-05-drove-symphony-external-loop-research.md`
  - Result summary: roles-map (2026-09-06) maps keys (Drove = long-horizon-swarm/swarm-orch/nonstop-swarm; Horizon = eng-orch/long-horizon) and RACI, but does not cite overlay skill names or lever-first VERIFY. `fleet-roles.mdc` matches. Research audit already lists lever-first VERIFY + standing-orders + arena/I1-on-pstack as Drove gaps.
  - Conclusion: Spec requires exact cite lines; Drove/eggbot applies box SoT (not this gbp propose PR).

- Evidence label: `Static`
  - Query: Keep-list still present? Arena/interrogate cloned?
  - Path: `long-horizon-swarm/skills/`; playbook refuse; GLOSSARY
  - Result summary: Overlay ships field-guide, planner-worker-split, review-lenses, coordination-layer, megafile-gate, ossify-break, openspec-intent-flow. Refuse includes flat-swarm, second-board/dual-write, nested-spawn. GLOSSARY: arena/interrogate are pstack leaves, not shipped. No `agents/` in plugin.json.
  - Conclusion: Keep invariants; do not clone arena/interrogate; no agents unless a later ADR says so.
