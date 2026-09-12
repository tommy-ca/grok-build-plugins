## Why

Todd + Horizon Act-on REFRESH + WAVE-0 GO: **rewrite** gbp repo-root `EXTERNAL-LOOP.md` as the in-repo Symphony-class **WORKFLOW.md twin** — not a thin cite-only patch. Upstream [Symphony WORKFLOW.md](https://openai-symphony.mintlify.app/setup/workflow-file) combines YAML frontmatter (runtime) + Markdown body (agent/orch contract). Tip `4c126d8e` already ships a thin pointer from archived `gbp-external-loop-docs`, but it lacks (1) a frontmatter-equivalent runtime block (tracker/board, polling/tick, workspace isolation, `max_concurrent=5`+backpressure, hooks/observability), (2) a Markdown body contract (eligibility, dispatch, reconcile, retry/stall, handoff VERIFIED|human_review|quota, lever-first VERIFY), and (3) Session arms Herd→herdr→agy (herdr default; bare `agy --print` exception-only + fallback journal) with CAO=scale and Heavilifter=recovery. Drove B1 Session arms already VERIFIED on box SoT skills — **do not remint**. Personas B1 VERIFIED — do not remint. Closed thermos / gbp-external-loop-docs / lhs-swarm-economics-refresh are cite-only. Sole NEW Act-on `herdr-agy-workflow-bind` closes the WORKFLOW twin gap. Map Symphony SPEC — **do not clone Elixir daemon**.

## What Changes

- **Wave-4 (this PR):** OpenSpec propose artefacts only under `openspec/changes/herdr-agy-workflow-bind/`. No product `EXTERNAL-LOOP.md` rewrite in this PR. No HARNESS rewrite. No box sand-workflow remint. No persona remint.
- **Wave-5 Apply (HOLD until Todd/Horizon go):**
  - **Rewrite** repo-root `EXTERNAL-LOOP.md` to Symphony WORKFLOW.md-shaped sections:
    1. YAML frontmatter-equivalent runtime (YAML fenced block **or** equivalent table): tracker/board, polling/tick, workspace/isolation, agent concurrency (`max_concurrent` default 5 + CPU/mem backpressure), hooks (optional), observability (approvals / herd journals).
    2. Markdown body = agent/orch contract: eligibility, dispatch, reconcile, retry/stall, handoff states (`VERIFIED` | `human_review` | quota exhausted), lever-first VERIFY.
    3. Session implement/PR-review path: Herd → [Herd with herdr] + [Delegate to agy] (herdr default; bare `agy --print` exception-only + fallback journal); CAO = scale fan-out; Heavilifter = recovery; dual orch forbidden.
    4. Cite sand-workflow SoT + research audit; do **not** vendor skill bodies; no Elixir Symphony daemon.
  - Optional light `long-horizon-swarm/HARNESS.md` cross-cite to session path (do **not** clone arena).
  - Box SoT Session arms = separate Drove/Opus/eggbot apply (already VERIFIED B1) — like rooms-map; do not remint personas B1.
  - Merge NEW capability into tip `openspec/specs/herdr-agy-workflow-bind/`; `openspec validate --strict`.
  - Prove: tip EXTERNAL-LOOP is WORKFLOW-shaped **and** contains herdr→agy default; verify/marketplace scripts still green if touched.

## Capabilities

### New Capabilities

- `herdr-agy-workflow-bind`: Rewrite `EXTERNAL-LOOP.md` as Symphony WORKFLOW.md-shaped gbp twin (frontmatter-equivalent runtime + Markdown body contract) including Herd→herdr→agy session arms (bare `agy --print` exception-only + fallback journal); cite sand-workflow SoT + research audit; honesty that box SoT Session arms are Drove/Opus/eggbot (already VERIFIED); optional light HARNESS cross-cite; no remint closed archives / personas B1; no Elixir daemon.

### Modified Capabilities

- _(none — prefer ADDED under NEW capability only; living `gbp-external-loop-docs` stays cite-only; do not full-body MODIFY)_

## Impact

Wave-4: OpenSpec change folder only. Wave-5 (after Todd/Horizon go): rewrite `EXTERNAL-LOOP.md` (+ optional HARNESS one-liner); tip merge of NEW capability; box SoT skill Session arms remain Drove/Opus/eggbot SoT (already green). Does **not** remint `thermos-grok-port`, `gbp-external-loop-docs`, or `lhs-swarm-economics-refresh`. Does **not** remint personas B1. Does **not** vendor Symphony / run Elixir daemon. Does **not** duplicate fleet skill bodies into gbp. Does **not** treat Herd as CAO-scale N-arm fan-out.

## Non-goals

- Thin-only cite patch that omits WORKFLOW frontmatter-equivalent + body contract
- Remint closed thermos / gbp-external-loop-docs / lhs-swarm-economics-refresh archives
- Remint personas B1 or Drove B1 skill Session arms (already VERIFIED — cite only)
- Second SoT that vendors sand-workflow skill bodies / Liquid Codex prompt clone
- Elixir Symphony daemon on the box
- Invent LIVE / LIVE_PASS
- Dual orch ownership
- Clone arena / interrogate into lhs HARNESS
- Product EXTERNAL-LOOP.md / HARNESS edit in the propose PR
- MODIFY living `gbp-external-loop-docs` (NEW capability owns the rewrite)

## Probe Evidence Record

- Evidence label: `Static`
  - Query: Tip SHA + EXTERNAL-LOOP WORKFLOW shape + herdr→agy?
  - Path: tip `4c126d8e3b6413fe0e868c3e3c88f8e99a7e15c0` / repo-root `EXTERNAL-LOOP.md`
  - Result summary: HEAD `4c126d8` (lhs archive #23 MERGED). File is a thin pointer (Cite / Symphony→fleet map / Roles / Contracts / worked example / MUST-NOT). **Missing:** YAML frontmatter-equivalent runtime block; body contract sections (eligibility/dispatch/reconcile/retry/stall/handoff); `delegate-to-agy` cite; herdr→agy default; bare `agy --print` exception + fallback journal.
  - Conclusion: Apply must **rewrite** EXTERNAL-LOOP to WORKFLOW.md shape including session arms; propose must not land the product file.

- Evidence label: `Static`
  - Query: HARNESS session path?
  - Path: `long-horizon-swarm/HARNESS.md` @ tip
  - Result summary: Fleet seats table names Herd = session herdr pane; no herdr→agy / delegate-to-agy / bare-print exception. Optional light cross-cite only; do not clone arena.
  - Conclusion: Optional apply task.

- Evidence label: `Metadata`
  - Query: Box SoT Session arms (Drove B1)?
  - Path: `/home/box/sand-data/workflows/{fleet-org-raci,inner-outer-orch,eng-lead-merge-authority,fleet-roles-map}/SKILL.md`
  - Result summary: Each has `## Session arms (herdr → agy) — 2026-09-12` (herdr default; bare `agy --print` exception-only + fallback journal). Orch spend.tsv: Drove B1 VERIFIED.
  - Conclusion: Document as separate box SoT apply (already done); do not remint from gbp PR; do not remint personas B1.

- Evidence label: `Metadata`
  - Query: Symphony WORKFLOW.md upstream + research twin
  - Path: https://openai-symphony.mintlify.app/setup/workflow-file ; `/workspace/fleet-external-agents/audits/2026-09-05-drove-symphony-external-loop-research.md`
  - Result summary: Upstream = YAML frontmatter (`tracker`, `polling`, `workspace`, `agent`, `hooks`, `observability`, …) + Markdown body prompt/contract. Research maps Symphony↔Drove; gap #3 was WORKFLOW/standing-orders contract; gap #7 no Elixir daemon unless Todd asks.
  - Conclusion: Apply rewrite maps keys to fleet surfaces; cite research; no Elixir daemon; no Liquid Codex clone required.
