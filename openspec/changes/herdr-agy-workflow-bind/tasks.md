# Tasks: herdr-agy-workflow-bind

> Schema: intent-driven. Propose atoms → offline verify → **STOP** → Todd/Horizon-go apply → archive.
> Tip floor: `4c126d8e3b6413fe0e868c3e3c88f8e99a7e15c0` (`4c126d8e`). No auto-apply. No product `EXTERNAL-LOOP.md` rewrite in propose PR. No remint thermos / gbp-external-loop-docs / lhs. No remint personas B1 / Drove B1 skills. No invent LIVE. No Elixir Symphony daemon. Dual orch forbidden. **STOP thin-only cite** — Apply rewrites WORKFLOW.md-shaped EXTERNAL-LOOP.

## 0. Preconditions (read-only) — serial gate

- [x] 0.1 Tip SHA Probe: `4c126d8e3b6413fe0e868c3e3c88f8e99a7e15c0` (≥ floor `4c126d8e`) — lhs archive #23 MERGED
- [x] 0.2 Re-read BRIEF + Horizon REFRESH: Symphony WORKFLOW.md-shaped EXTERNAL-LOOP (frontmatter-equivalent + body contract + session arms); research audit; upstream workflow-file docs
- [x] 0.3 Parks held: remint thermos/gbp-external-loop-docs/lhs OUT; personas B1 remint OUT; Drove B1 skill remint OUT; LIVE invent OUT; Elixir daemon OUT; dual orch OUT; thin-only cite OUT
- [x] 0.4 Confirm locked Act-on id `herdr-agy-workflow-bind`; NEW capability only (no MODIFY living gbp-external-loop-docs)

## Parallel band A — Propose atoms (Wave-4) — P-parallel

Depends: §0

- [x] A.1 `proposal.md` — Why/What/Capabilities/Impact; Probe Evidence; WORKFLOW rewrite (not thin-only); non-goals — **P-parallel**
- [x] A.2 `specs/herdr-agy-workflow-bind/spec.md` — ADDED WORKFLOW-shaped EXTERNAL-LOOP + session arms + box SoT honesty + optional HARNESS — **P-parallel**
- [x] A.3 `design.md` — map-not-clone Symphony; rewrite decisions; split apply ownership; propose-only Wave-4 — **P-parallel**
- [x] A.4 `adr.md` + `.openspec.yaml` — cite 0001–0006; no new repo ADR; schema intent-driven — **P-parallel**

## 1. Validate --strict (offline) — serial gate

Depends: Parallel band A complete

- [x] 1.1 `openspec validate herdr-agy-workflow-bind --type change --strict` (from worktree) → PASS
- [x] 1.2 Probe honesty: no product EXTERNAL-LOOP rewrite in propose tree; WORKFLOW keys + session arms named in spec; no thermos/lhs/gbp-external-loop-docs remint; no LIVE invent; Drove B1 cite-only
- [x] 1.3 Confirm Must-nots: no auto-apply; dual orch forbidden; Horizon leaf apply; Drove/Opus/eggbot own box skill SoT; no Elixir daemon

## 2. STOP handoff — serial gate

Depends: §1 green

- [x] 2.1 Hand Horizon `openspec/changes/herdr-agy-workflow-bind/` (+ orch VALID/BRIEF)
- [x] 2.2 Ledger: Wave-4 VALID propose-only; Apply HOLD until Todd/Horizon go
- [x] 2.3 **STOP** — no `openspec apply`; no product EXTERNAL-LOOP rewrite; no box skill remint from propose executor; do not merge as apply

## Parallel band B — Apply (Wave-5; Todd/Horizon go) — HOLD

Depends: Todd/Horizon go + §1 green

- [ ] B.1 **Rewrite** repo-root `EXTERNAL-LOOP.md` to Symphony WORKFLOW.md shape:
  - Frontmatter-equivalent runtime (YAML block or keyed table): tracker/board, polling/tick, workspace/isolation, `max_concurrent` default 5 + backpressure, hooks optional, observability (approvals/herd journals)
  - Markdown body contract: eligibility, dispatch, reconcile, retry/stall, handoff VERIFIED|human_review|quota, lever-first VERIFY
  - Session arms: Herd→herdr→agy (cite herd-with-herdr + delegate-to-agy; bare `agy --print` exception-only + fallback journal); CAO=scale; Heavilifter=recovery; dual orch forbidden
  - Cite sand-workflow SoT + research audit; do not vendor skill bodies; no Elixir daemon
  - Keep prior useful cites (thermos #15→#17 worked example; rooms-map honesty if still relevant) without reminting closed Act-ons — **P-parallel (gbp git)**
- [ ] B.2 Optional light `long-horizon-swarm/HARNESS.md` cross-cite to EXTERNAL-LOOP session path — do **not** clone arena — **P-parallel (gbp git; optional)**
- [ ] B.3 Box SoT Session arms: Drove/Opus/eggbot — **already VERIFIED B1** — Metadata cite-only; do **not** remint skill bodies or personas B1 from gbp — **Metadata / box SoT**
- [ ] B.4 Merge capability delta into tip `openspec/specs/herdr-agy-workflow-bind/`
- [ ] B.5 `openspec validate herdr-agy-workflow-bind --type change --strict` (and `--all --strict` as needed) green after merge
- [ ] B.6 If verify / marketplace scripts touched, keep them green; else leave untouched (marketplace unaffected)
- [ ] B.7 **Prove bars Metadata/Static (claim done only if all hold):**
  - [ ] P1 tip `EXTERNAL-LOOP.md` is WORKFLOW-shaped (frontmatter-equivalent runtime keys + body contract sections present)
  - [ ] P2 tip `EXTERNAL-LOOP.md` contains herdr→agy default session path + bare-print exception + herd-with-herdr + delegate-to-agy cites
  - [ ] P3 Drove B1 skills already green (cite-only); personas B1 not reminted
  - [ ] P4 no thermos/lhs/gbp-external-loop-docs remint; no LIVE invent; no Elixir daemon; no skill-body dump
  - [ ] P5 OpenSpec intent-driven; validate `--strict` green; tip ≥ `4c126d8e`; verify scripts green if touched
  - [ ] NOT predicates: thin-only cite regress; remint closed archives; invent LIVE; dual orch; propose PR claimed as apply

## 3. Archive — serial gate

Depends: Parallel band B complete + implementation on integration branch

- [ ] 3.1 `openspec validate herdr-agy-workflow-bind --type change --strict` still green before archive
- [ ] 3.2 Archive per openspec-git-discipline (from integration after merge)
- [ ] 3.3 Update ledger; reaffirm parks; note Prove status (VERIFIED only if Prove bars held — never invent)
