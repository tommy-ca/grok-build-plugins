## Why

Tip `f4dc2ae` ships repo-root `EXTERNAL-LOOP.md` as the Symphony WORKFLOW.md-shaped twin from closed `herdr-agy-workflow-bind` (#24+#25+#26). The **filename** still says EXTERNAL-LOOP while content and upstream Symphony already use **WORKFLOW.md**. Living cites in `long-horizon-swarm/HARNESS.md`, `long-horizon-swarm/README.md`, and `scripts/verify-long-horizon-swarm.sh` assert the old name. Living OpenSpec caps `herdr-agy-workflow-bind` (required), plus `gbp-external-loop-docs` / `lhs-swarm-economics-refresh` where they mandate the live filename, still name `EXTERNAL-LOOP.md` as current SoT. Hard-rename to `WORKFLOW.md` closes the twin-name gap without reminting content, without reminting closed thermos / lhs / herdr-agy archives, and without touching Elixir/LIVE/dual-orch.

## What Changes

- **Wave-4 (this PR):** OpenSpec propose artefacts only under `openspec/changes/workflow-md-rename/`. No product rename. No HARNESS/README/verify-script edits. No remint closed archives.
- **Wave-5 Apply (HOLD until Todd/Horizon go):**
  - Hard-rename repo-root `EXTERNAL-LOOP.md` → `WORKFLOW.md` (git mv; preserve Symphony twin body — Session arms + isolation trinity unchanged).
  - Update living cites: `long-horizon-swarm/HARNESS.md`, `long-horizon-swarm/README.md`, `scripts/verify-long-horizon-swarm.sh` assert (`EXTERNAL-LOOP.md` → `WORKFLOW.md`).
  - **Orchestrators MUST load tip `WORKFLOW.md`** (frontmatter-equivalent + body) before dispatch — Drove continuous tick refuse/hold if missing or missing required keys; Horizon leaf briefs cite tip WORKFLOW.md (Session arms / isolation trinity / lever-first VERIFY from that file); Herd session arms follow herdr→agy as named in tip WORKFLOW.md (not ad-hoc).
  - Merge NEW capability `workflow-md-rename` + MODIFIED deltas for living caps that mandate the live filename.
  - `openspec validate --strict` green; prove rename + cites + orch-load contract; verify script PASS.
  - **OUT OF SCOPE for this gbp git PR (Band B / Drove Apply note):** flip sand-workflow skills (`drove-external-loop`, `fleet-org-raci`, `inner-outer-orch`, `eng-lead-merge-authority`) to say "read tip WORKFLOW.md"; persona/roles-map cite flip — tasks Band B only; Drove/Opus/eggbot own separately (not gbp product files).

## Capabilities

### New Capabilities

- `workflow-md-rename`: Hard-rename repo-root `EXTERNAL-LOOP.md` → `WORKFLOW.md` (content already Symphony twin); update lhs HARNESS/README + verify assert cites; **orchestrators MUST load tip WORKFLOW.md before dispatch** (Drove refuse/hold; Horizon briefs cite; Herd follows named session arms); preserve Session arms Herd→herdr→agy and isolation trinity; OpenSpec living-filename honesty; propose-only Wave-4; Drove sand-workflow "read tip WORKFLOW.md" skill flip = Band B out-of-repo note only.

### Modified Capabilities

- `herdr-agy-workflow-bind`: living SoT filename `EXTERNAL-LOOP.md` → `WORKFLOW.md` (RENAMED + MODIFIED where titles/bodies mandate the live twin path); Session arms + isolation trinity preserved.
- `gbp-external-loop-docs`: only where the live pointer filename is mandated (`Thin EXTERNAL-LOOP.md pointer…` → `WORKFLOW.md`).
- `lhs-swarm-economics-refresh`: only where HARNESS/README / roles-map cite content mandates the live `EXTERNAL-LOOP.md` filename → `WORKFLOW.md`.

## Impact

Wave-4: OpenSpec change folder only. Wave-5 (after Todd/Horizon go): product rename + cite flips in lhs HARNESS/README + verify assert + tip OpenSpec merge + orch-load contract in living OpenSpec. Does **not** remint `thermos-grok-port`, `lhs-swarm-economics-refresh`, or `herdr-agy-workflow-bind` archives. Does **not** rewrite WORKFLOW twin content (rename only). Does **not** land Drove sand-workflow skill / persona / roles-map cite flips in the gbp git PR (Band B Metadata). Does **not** invent LIVE. Does **not** require Elixir Symphony daemon. Dual orch remains forbidden.

## Non-goals

- Remint closed thermos / lhs / herdr-agy archives
- Rewrite WORKFLOW twin body (content already applied under herdr-agy)
- Product rename / HARNESS / README / verify-script edit in the propose PR
- Drove box SoT skill/persona / roles-map cite flip inside this gbp git PR
- Elixir Symphony daemon
- Invent LIVE / LIVE_PASS
- Dual orch ownership
- Clone arena / interrogate
- Ad-hoc Herd session path that ignores tip WORKFLOW.md
- Product orch daemon / Elixir Symphony

## Probe Evidence Record

- Evidence label: `Static`
  - Query: Tip SHA + EXTERNAL-LOOP Symphony twin?
  - Path: tip `f4dc2aee4683837dbe841bb6e7ca30575d67104a` / repo-root `EXTERNAL-LOOP.md`
  - Result summary: HEAD `f4dc2ae` (herdr-agy-workflow-bind archive #26 MERGED). File header: "Symphony WORKFLOW.md twin (gbp)" with frontmatter-equivalent runtime + session arms + isolation trinity. Filename still `EXTERNAL-LOOP.md`.
  - Conclusion: Apply hard-renames to `WORKFLOW.md`; propose must not land the rename.

- Evidence label: `Static`
  - Query: Living product cites of EXTERNAL-LOOP.md?
  - Path: `long-horizon-swarm/HARNESS.md`, `long-horizon-swarm/README.md`, `scripts/verify-long-horizon-swarm.sh`
  - Result summary: HARNESS heading + body cite `EXTERNAL-LOOP.md` (3 hits); README cites repo-root `EXTERNAL-LOOP.md`; verify script `assert "EXTERNAL-LOOP.md" in harness`.
  - Conclusion: Apply flips those cites; root README has no EXTERNAL-LOOP cite.

- Evidence label: `Static`
  - Query: Living OpenSpec filename mandates?
  - Path: `openspec/specs/{herdr-agy-workflow-bind,gbp-external-loop-docs,lhs-swarm-economics-refresh}/spec.md`
  - Result summary: herdr-agy requirement titles/bodies assert `EXTERNAL-LOOP.md` as twin path; gbp thin-pointer requirement mandates repo-root `EXTERNAL-LOOP.md`; lhs fleet-seat bind + roles-map cite string name `EXTERNAL-LOOP.md`.
  - Conclusion: MODIFY (and RENAMED where titles embed the old name) those living caps; box SoT cite flip noted OUT OF SCOPE for gbp git.

- Evidence label: `Static`
  - Query: Act-on refresh — orch must read tip WORKFLOW.md?
  - Path: `/workspace/orchestrate/workflow-md-rename/BRIEF.md` (Act-on refresh)
  - Result summary: Drove load before spawn + refuse/hold on missing keys; Horizon briefs cite tip WORKFLOW.md; Herd follows named herdr→agy; box skills must say "read tip WORKFLOW.md" at Drove Apply.
  - Conclusion: NEW ADDED requirement under `workflow-md-rename`; Drove skill flip = Band B tasks note only (not propose product files).
