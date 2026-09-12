## Purpose
Rewrite repo-root EXTERNAL-LOOP.md as Symphony WORKFLOW.md-shaped twin (frontmatter-equivalent runtime + Markdown body contract) binding Herd→herdr→agy session arms, isolation trinity (CAO cloud VM / Herd herdr pane+kind=agy / Heavilifter on-box worktree), and Drove-owned tick/concurrency — without reminting thermos / gbp-external-loop-docs / lhs, without vendoring skill bodies, and without an Elixir Symphony daemon.

## Requirements
### Requirement: WORKFLOW.md is Symphony WORKFLOW.md-shaped twin

Feature: herdr-agy-workflow-bind
Rule: Frontmatter-equivalent runtime + Markdown body contract; map not clone Elixir

After apply of `workflow-md-rename`, tommy-ca/grok-build-plugins repo-root `WORKFLOW.md` MUST be the in-repo **Symphony-class WORKFLOW.md twin** (cite https://openai-symphony.mintlify.app/setup/workflow-file and `/workspace/fleet-external-agents/audits/2026-09-05-drove-symphony-external-loop-research.md`). The live twin path MUST be `WORKFLOW.md` (hard-renamed from historical `EXTERNAL-LOOP.md`). The file MUST include both of the following sections (YAML fenced block preferred for runtime, or an equivalent keyed Markdown table that is machine-scannable):

**1. Frontmatter-equivalent runtime** — MUST name at least:

| Runtime key | Fleet mapping (MUST state) |
| --- | --- |
| tracker / board | boards / `long-horizon/*` + OpenSpec tasks |
| polling / tick | **Drove** owns continuous tick when brief has goal+quota+TaskTree (Horizon = single-change OpenSpec apply/merge only — not the continuous tick) |
| workspace / isolation | **Isolation trinity — distinct, do not collapse:** (1) **CAO** = cloud VM (scale fan-out); (2) **Herd session** = herdr pane + `kind=agy` (session implement/PR-review); (3) **Heavilifter** = on-box worktree recovery (prove-it / when cloud blocked — not primary N-arm fan-out) |
| agent concurrency | **Drove**-owned `max_concurrent` default **5** + CPU/mem backpressure (Herd fills herdr slots under that policy; CAO scale is separate cloud concurrency) |
| hooks | optional (may be named absent / N/A) |
| observability | approvals journal + herd-journal (stalls/fallbacks) |

**2. Markdown body = agent/orch contract** — MUST cover:

- eligibility (when a unit may be dispatched)
- dispatch (who/how implement arms start)
- reconcile (outer tick / evidence join)
- retry / stall (heal → journal → restart or handoff)
- handoff states: `VERIFIED` | `human_review` | quota exhausted
- lever-first VERIFY (Brief.VERIFY cites a lever script or verify-* skill; refuse prose-only on non-trivial leaves)

The twin MUST remain a **pointer/index**, not a second SoT: it MUST cite sand-workflow skill ids (at minimum `inner-outer-orch`, `fleet-org-raci`, `drove-external-loop`, `herd-with-herdr`, `delegate-to-agy`) and MUST NOT vendor full skill bodies, MUST NOT require an Elixir Symphony daemon, MUST NOT invent LIVE/LIVE_PASS, and MUST NOT remint closed `thermos-grok-port`, `gbp-external-loop-docs`, or `lhs-swarm-economics-refresh`. Cite living `gbp-external-loop-docs` as prior pointer Act-on — the twin content was rewritten under `herdr-agy-workflow-bind`; the live filename is now owned by `workflow-md-rename`.

#### Scenario: Frontmatter-equivalent runtime keys present

- **GIVEN** tip after `workflow-md-rename` applies
- **WHEN** an operator opens repo-root `WORKFLOW.md`
- **THEN** a YAML fenced block or equivalent keyed table names tracker/board, polling/tick, workspace/isolation, max_concurrent default 5 + backpressure, hooks (optional), and observability (approvals/herd journals)
- **AND** fleet mappings for those keys are stated
- **AND** polling/tick + concurrency are owned by Drove (Horizon is not the continuous tick)
- **AND** isolation lists the trinity as three distinct surfaces (CAO cloud VM; Herd herdr pane + kind=agy; Heavilifter on-box worktree recovery) without collapsing them into one path

#### Scenario: Body contract covers orch loop

- **GIVEN** `WORKFLOW.md` after apply
- **WHEN** the Markdown body (agent/orch contract) is read
- **THEN** eligibility, dispatch, reconcile, and retry/stall are named
- **AND** handoff states include VERIFIED, human_review, and quota exhausted
- **AND** lever-first VERIFY is required

#### Scenario: Twin cites SoT and refuses Elixir/LIVE/remint

- **GIVEN** `WORKFLOW.md` after apply
- **WHEN** SoT and must-nots are checked
- **THEN** sand-workflow ids including herd-with-herdr and delegate-to-agy are cited
- **AND** the Drove Symphony research audit path is cited
- **AND** full skill bodies are not vendored
- **AND** no Elixir Symphony daemon is required
- **AND** LIVE/LIVE_PASS is not invented
- **AND** closed thermos / gbp-external-loop-docs / lhs archives are not reminted

#### Scenario: Propose PR does not land product rewrite

- **GIVEN** Wave-4 propose-only artefacts for `workflow-md-rename`
- **WHEN** the propose PR is reviewed
- **THEN** product `EXTERNAL-LOOP.md` is still present and unrenamed in that PR
- **AND** product `WORKFLOW.md` is absent from that PR
- **AND** apply tasks remain HOLD until Todd/Horizon go

### Requirement: Session arms Herd → herdr → agy on the WORKFLOW twin

Feature: herdr-agy-workflow-bind
Rule: herdr default session path; bare agy --print exception-only + fallback journal

Repo-root `WORKFLOW.md` MUST bind the **session implement / PR-review path** as:

- **Herd** owns session-sized interactive orch after Act-on / tasks exist
- Default path: [Herd with herdr](sand-workflow:herd-with-herdr) → [Delegate to agy](sand-workflow:delegate-to-agy) (interactive agy via herdr)
- Bare `agy --print` is **exception-only** (herdr down or prompt still stalled after heal) and MUST journal `fallback` / `fallback_used` first via [Herd failure journal](sand-workflow:herd-failure-journal)
- **CAO** = default parallel *scale* fan-out isolation = **cloud VM** (distinct from herdr pane and on-box worktree); do not treat Herd as the N-arm scale path
- **Herd session isolation** = **herdr pane + `kind=agy`** (interactive session implement/PR-review); not a cloud VM and not a Heavilifter worktree
- **Heavilifter** = prove-it / session recovery isolation = **on-box worktree** when cloud blocked — **not** primary N-arm fan-out; not a herdr pane substitute for scale
- **Drove** owns continuous tick + concurrency/`max_concurrent` reconcile; Horizon owns single-change apply/merge only
- **Dual orch forbidden** — exactly one orch owner per brief (Horizon leaf XOR Drove continuous tick)
- Isolation trinity MUST remain **distinct** — MUST NOT collapse CAO / Herd / Heavilifter into one isolation path

#### Scenario: Session path names herdr default and agy cite

- **GIVEN** `WORKFLOW.md` after apply
- **WHEN** session implement / PR-review guidance is read
- **THEN** Herd → herdr → agy is the default session path
- **AND** sand-workflow `herd-with-herdr` and `delegate-to-agy` are cited
- **AND** bare `agy --print` is stated as exception-only with fallback journal first
- **AND** CAO is named for scale fan-out on cloud VM
- **AND** Herd session isolation is herdr pane + kind=agy
- **AND** Heavilifter is named for on-box worktree recovery
- **AND** the three isolation surfaces are distinct (not collapsed)
- **AND** Drove owns tick/concurrency; dual orch is forbidden

#### Scenario: Isolation trinity stays distinct

- **GIVEN** `WORKFLOW.md` after apply
- **WHEN** workspace/isolation guidance is read
- **THEN** CAO = cloud VM is stated as scale isolation
- **AND** Herd session = herdr pane + kind=agy is stated as session isolation
- **AND** Heavilifter = on-box worktree recovery is stated as recovery isolation
- **AND** no prose collapses the three into a single interchangeable path
- **AND** continuous tick and max_concurrent policy are attributed to Drove

### Requirement: Optional HARNESS light cross-cite only

Feature: herdr-agy-workflow-bind
Rule: Do not clone arena; WORKFLOW.md remains session-path SoT twin

Apply MAY add or keep a light cross-cite in `long-horizon-swarm/HARNESS.md` pointing operators at `WORKFLOW.md` session arms (Herd→herdr→agy). Apply MUST NOT clone arena/interrogate into the plugin, MUST NOT vendor sand-workflow bodies into HARNESS, and MUST NOT treat the optional cite as a second WORKFLOW twin. If `WORKFLOW.md` alone satisfies session-path discoverability, the HARNESS cite MAY be skipped. After `workflow-md-rename` apply, any live HARNESS cite MUST name `WORKFLOW.md` (not `EXTERNAL-LOOP.md`).

#### Scenario: Optional cite does not clone arena

- **GIVEN** Wave-5 apply for `workflow-md-rename` (or a later HARNESS cite refresh)
- **WHEN** HARNESS is considered for a session-path cross-cite
- **THEN** any edit is a light cite to `WORKFLOW.md` / session arms only
- **OR** the cite is skipped as optional
- **AND** arena/interrogate are not cloned into long-horizon-swarm
- **AND** live cites do not assert path `EXTERNAL-LOOP.md`

## Requirements
- FROM: `### Requirement: EXTERNAL-LOOP.md is Symphony WORKFLOW.md-shaped twin`
- TO: `### Requirement: WORKFLOW.md is Symphony WORKFLOW.md-shaped twin`
