# Tasks: workflow-md-rename

> Schema: intent-driven. Propose atoms → offline verify → **STOP** → Todd/Horizon-go apply → archive.
> Tip floor: `f4dc2aee4683837dbe841bb6e7ca30575d67104a` (`f4dc2ae`). No auto-apply. No product `EXTERNAL-LOOP.md` → `WORKFLOW.md` rename in propose PR. No HARNESS/README/verify edits in propose PR. No remint thermos / lhs / herdr-agy archives. No invent LIVE. No Elixir Symphony daemon. Dual orch forbidden. Orch-load contract named in OpenSpec; Drove skill flip = Band B out-of-repo.

## 0. Preconditions (read-only) — serial gate

- [x] 0.1 Tip SHA Probe: `f4dc2aee4683837dbe841bb6e7ca30575d67104a` (≥ floor `f4dc2ae`) — herdr-agy-workflow-bind archive #26 MERGED
- [x] 0.2 Re-read BRIEF + Act-on refresh: hard-rename EXTERNAL-LOOP→WORKFLOW; cite flips; orch MUST load tip WORKFLOW.md before dispatch; Drove Band B skill flip
- [x] 0.3 Parks held: remint thermos/lhs/herdr-agy OUT; LIVE invent OUT; Elixir daemon OUT; dual orch OUT; product rename in propose OUT
- [x] 0.4 Confirm locked Act-on id `workflow-md-rename`; skim tip EXTERNAL-LOOP.md Symphony twin header; living specs filename mandates noted

## Parallel band A — Propose atoms (Wave-4) — P-parallel

Depends: §0

- [x] A.1 `proposal.md` — Why/What/Capabilities/Impact; Probe Evidence; rename + cites + orch-load; non-goals — **P-parallel**
- [x] A.2 `specs/workflow-md-rename/spec.md` — ADDED hard-rename + cite flip + orch-load-before-dispatch + propose-only — **P-parallel**
- [x] A.3 `specs/herdr-agy-workflow-bind/spec.md` — RENAMED + MODIFIED living filename mandates (full blocks) — **P-parallel**
- [x] A.4 `specs/gbp-external-loop-docs/spec.md` + `specs/lhs-swarm-economics-refresh/spec.md` — MODIFIED (+ RENAMED) only where live filename mandated — **P-parallel**
- [x] A.5 `design.md` — hard-rename prefer; orch-load; split apply ownership; propose-only Wave-4 — **P-parallel**
- [x] A.6 `adr.md` + `.openspec.yaml` — cite 0001–0006; no new repo ADR; schema intent-driven — **P-parallel**

## 1. Validate --strict (offline) — serial gate

Depends: Parallel band A complete

- [x] 1.1 `openspec validate workflow-md-rename --type change --strict` (from worktree) → PASS
- [x] 1.2 Probe honesty: no product rename in propose tree; orch-load requirement present; no thermos/lhs/herdr-agy remint; no LIVE invent; Drove skill flip Band B only
- [x] 1.3 Confirm Must-nots: no auto-apply; dual orch forbidden; Horizon leaf apply; no Elixir daemon

## 2. STOP handoff — serial gate

Depends: §1 green

- [x] 2.1 Hand Horizon `openspec/changes/workflow-md-rename/` (+ orch VALID/BRIEF)
- [x] 2.2 Ledger: Wave-4 VALID propose-only; Apply HOLD until Todd/Horizon go
- [x] 2.3 **STOP** — no `openspec apply`; no product rename; no HARNESS/README/verify edit from propose executor; do not merge as apply; do not edit sand-workflow skill bodies from propose

## Parallel band B — Apply (Wave-5; Todd/Horizon go) — APPLY HOLD

Depends: Todd/Horizon go + §1 green

### B-gbp — gbp git Apply (Horizon / Heavilifter) — HOLD

- [x] B.1 **Hard-rename** repo-root `EXTERNAL-LOOP.md` → `WORKFLOW.md` (`git mv`; preserve Symphony twin body — Session arms + isolation trinity unchanged; prefer no redirect stub) — **P-parallel (gbp git)**
- [x] B.2 Flip living cites `EXTERNAL-LOOP.md` → `WORKFLOW.md` in `long-horizon-swarm/HARNESS.md`, `long-horizon-swarm/README.md`, and `scripts/verify-long-horizon-swarm.sh` assert — **P-parallel (gbp git)**
- [x] B.3 Merge capability deltas into tip `openspec/specs/` (`workflow-md-rename` NEW + modified living caps)
- [x] B.4 `openspec validate workflow-md-rename --type change --strict` (and `--all --strict` as needed) green after merge
- [x] B.5 Run `scripts/verify-long-horizon-swarm.sh` → PASS (assert expects WORKFLOW.md)
- [x] B.6 **Prove bars Metadata/Static (claim done only if all hold):**
  - [x] P1 tip `WORKFLOW.md` exists; live `EXTERNAL-LOOP.md` absent (or ADR stub only if later approved — prefer absent)
  - [x] P2 tip WORKFLOW.md retains Symphony twin shape + Session arms Herd→herdr→agy + isolation trinity distinct + Drove tick/concurrency
  - [x] P3 HARNESS/README/verify assert cite `WORKFLOW.md` not `EXTERNAL-LOOP.md`
  - [x] P4 OpenSpec living caps no longer mandate live filename `EXTERNAL-LOOP.md`
  - [x] P5 no thermos/lhs/herdr-agy remint; no LIVE invent; no Elixir daemon; tip ≥ `f4dc2ae`
  - [x] NOT predicates: product rename in propose PR; remint closed archives; invent LIVE; dual orch; propose claimed as apply

### B-drove — Drove Apply / box SoT (out-of-repo; NOT gbp product files) — HOLD / note only

- [ ] B.7 Flip sand-workflow skills to say **read tip WORKFLOW.md** (Drove/Opus/eggbot Metadata):
  - `drove-external-loop`
  - `fleet-org-raci`
  - `inner-outer-orch`
  - `eng-lead-merge-authority`
  - (and persona / roles-map EXTERNAL-LOOP→WORKFLOW cite flip as needed)
- [ ] B.8 **Orchestrator load behaviour (operational):** Drove continuous tick loads tip WORKFLOW.md before spawn and refuse/holds if missing or missing required keys (tracker/polling/workspace/agent/session arms); Horizon briefs cite tip WORKFLOW.md; Herd follows herdr→agy as named in tip WORKFLOW.md — prove via Metadata after skill flip; **not** landed as gbp propose files
- [ ] B.9 Done-claims for B.7/B.8 wait until box SoT lines exist (Metadata verify) — gbp git Apply MAY complete without B.7/B.8

## 3. Archive — serial gate

Depends: Parallel band B-gbp complete + implementation on integration branch (B-drove may trail)

- [x] 3.1 `openspec validate workflow-md-rename --type change --strict` still green before archive
- [x] 3.2 Archive per openspec-git-discipline (from integration after merge)
- [x] 3.3 Update ledger; reaffirm parks; note Prove status + whether Drove Band B Metadata is VERIFIED or still pending

> Archive note (2026-09-12): Drove Band B (B.7–B.9) VERIFIED out-of-repo @ tip `6c197417` / evidence `B-DROVE-WORKFLOW-LOAD-DONE.md`. gbp apply landed `WORKFLOW.md` @ `#28` / `5b2d8f5b`.
