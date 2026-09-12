## Why

Todd asked the room to review/audit team workflows as an **external loop** (OpenAI Symphony class). Horizon audited; the room agreed Act-on: (1) a live `rooms-map` row for the grok-build-plugins room `91ada72e-0abc-40f8-bb44-971a584fbdf3`, and (2) a thin repo-root `EXTERNAL-LOOP.md` in gbp that points at fleet skills — not a second source of truth. Tip `35c8c6c` (thermos archive #17 MERGED) has no `EXTERNAL-LOOP.md` and the gbp room is missing from box SoT `/workspace/fleet-external-agents/rooms-map.md`. Sole NEW Act-on `gbp-external-loop-docs` closes the gap. Do not remint `thermos-grok-port`. Do not invent LIVE. Do not run an Elixir Symphony daemon unless Todd asks.

## What Changes

- **Wave-4 (this PR):** OpenSpec propose artefacts only under `openspec/changes/gbp-external-loop-docs/`. No product `EXTERNAL-LOOP.md` in this PR. No live edit of box `rooms-map.md` from this git PR.
- **Wave-5 Apply (HOLD until Todd/Horizon go):**
  - Land repo-root `EXTERNAL-LOOP.md` — one-page pointer citing fleet skills + Symphony→fleet map + role RACI + thermos #15→#17 worked example.
  - Drove/eggbot applies the live rooms-map row to box SoT `/workspace/fleet-external-agents/rooms-map.md` (Metadata for gbp docs; separate box update for rooms-map).
  - Merge NEW capability into tip `openspec/specs/gbp-external-loop-docs/`; `openspec validate --strict`.

## Capabilities

### New Capabilities

- `gbp-external-loop-docs`: Thin repo-root `EXTERNAL-LOOP.md` pointer (not a second SoT) naming Symphony→fleet map and fleet roles; honesty that Drove/eggbot lands the gbp rooms-map charter row on box SoT; cite sand-workflow skills + Drove Symphony research audit; thermos #15→#17 as CloudAgent plan-block → Heavilifter recovery example.

### Modified Capabilities

- _(none — prefer ADDED under NEW capability only)_

## Impact

Wave-4: OpenSpec change folder only. Wave-5 (after Todd/Horizon go): `EXTERNAL-LOOP.md` at repo root; tip merge of NEW capability; Drove/eggbot updates box `rooms-map.md` with the required gbp row. Does **not** remint `thermos-grok-port`. Does **not** invent LIVE_PASS. Does **not** vendor Symphony / run Elixir daemon. Does **not** duplicate fleet skill bodies into gbp.

## Non-goals

- Second SoT that duplicates sand-workflow skill text
- Elixir Symphony daemon on the box
- Remint closed thermos / parallelism / binding-cite Act-ons
- Invent LIVE / LIVE_PASS
- Dual orch ownership
- Product apply in the propose PR

## Probe Evidence Record

- Evidence label: `Static`
  - Query: Tip has EXTERNAL-LOOP.md?
  - Path: tip `35c8c6c` worktree root
  - Result summary: **Missing** — no `EXTERNAL-LOOP.md`
  - Conclusion: Apply must land the pointer; propose must not.

- Evidence label: `Static` / `Metadata`
  - Query: gbp room in fleet rooms-map?
  - Path: `/workspace/fleet-external-agents/rooms-map.md`
  - Result summary: Live rooms list Eng lead / QStack / Ferro / Fleet meta — **no** row for `91ada72e-0abc-40f8-bb44-971a584fbdf3` / grok-build-plugins
  - Conclusion: Spec SHALL require row content; Drove/eggbot applies to box SoT (not necessarily this git PR).

- Evidence label: `Metadata`
  - Query: Symphony external-loop research + thermos #15→#17
  - Path: `/workspace/fleet-external-agents/audits/2026-09-05-drove-symphony-external-loop-research.md`; tip merges #15 propose → #16 apply → #17 archive
  - Result summary: Research maps Symphony↔Drove; thermos Wave-4/5/archive is the worked CloudAgent plan-block → Heavilifter recovery example under tip `35c8c6c`
  - Conclusion: Cite research + thermos trail in EXTERNAL-LOOP.md; no remint thermos-grok-port.
