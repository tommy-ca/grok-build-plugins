# Tasks: gbp-external-loop-docs

> Schema: intent-driven. Propose atoms → offline verify → **STOP** → Todd/Horizon-go apply → archive.
> Tip floor: `35c8c6c13b98a61fffab388a23f523090a470a53` (`35c8c6c`). No auto-apply. No product `EXTERNAL-LOOP.md` in propose PR. No remint `thermos-grok-port`. No invent LIVE. No Elixir Symphony daemon. Dual orch forbidden.

## 0. Preconditions (read-only) — serial gate

- [x] 0.1 Tip SHA Probe: `35c8c6c13b98a61fffab388a23f523090a470a53` (≥ floor `35c8c6c`) — thermos archive #17 MERGED
- [x] 0.2 Re-read Todd/room Act-on: rooms-map gbp row + thin EXTERNAL-LOOP.md; research audit; sand-workflow skills; tip has no EXTERNAL-LOOP.md; rooms-map missing gbp room
- [x] 0.3 Parks held: remint thermos-grok-port OUT; LIVE invent OUT; Elixir Symphony daemon OUT; dual orch OUT; second SoT OUT
- [x] 0.4 Confirm locked Act-on id `gbp-external-loop-docs` — prefer over `gbp-symphony-external-loop`; do not rename without Todd go

## Parallel band A — Propose atoms (Wave-4) — P-parallel

Depends: §0

- [x] A.1 `proposal.md` — Why/What/Capabilities/Impact; Probe Evidence; non-goals — **P-parallel**
- [x] A.2 `specs/gbp-external-loop-docs/spec.md` — ADDED EXTERNAL-LOOP.md pointer + rooms-map row honesty — **P-parallel**
- [x] A.3 `design.md` — pointer-not-vendor; split apply ownership; propose-only Wave-4 — **P-parallel**
- [x] A.4 `adr.md` + `.openspec.yaml` — cite 0001–0006; no new repo ADR; schema intent-driven — **P-parallel**

## 1. Validate --strict (offline) — serial gate

Depends: Parallel band A complete

- [x] 1.1 `openspec validate gbp-external-loop-docs --type change --strict` (from worktree) → PASS
- [x] 1.2 Probe honesty: no product EXTERNAL-LOOP.md in propose tree; rooms-map row content named; no thermos remint; no LIVE invent
- [x] 1.3 Confirm Must-nots: no auto-apply; dual orch forbidden; Horizon leaf apply; Drove owns box rooms-map update

## 2. STOP handoff — serial gate

Depends: §1 green

- [x] 2.1 Hand Horizon `openspec/changes/gbp-external-loop-docs/` (+ orch VALID/BRIEF)
- [x] 2.2 Ledger: Wave-4 VALID propose-only; Apply HOLD until Todd/Horizon go
- [x] 2.3 **STOP** — no `openspec apply`; no product EXTERNAL-LOOP.md; no box rooms-map edit from propose executor; do not merge as apply

## Parallel band B — Apply (Wave-5; Todd/Horizon go) — HOLD

Depends: Todd/Horizon go + §1 green

- [x] B.1 Land repo-root `EXTERNAL-LOOP.md` — one-page pointer citing sand-workflow:inner-outer-orch, fleet-org-raci, drove-external-loop, herd-with-herdr + research audit path — **P-parallel (gbp git)**
- [x] B.2 Include Symphony→fleet map (tracker/concurrency/isolation/WORKFLOW/stop) + role names (Drove/Horizon/CAO/Herd/Heavilifter) + dual-orch forbidden + lever-first VERIFY + herd-journal→reconcile + thermos #15→#17 CloudAgent plan-block → Heavilifter recovery — **P-parallel (gbp git)**
- [ ] B.3 Drove/eggbot applies live rooms-map row to `/workspace/fleet-external-agents/rooms-map.md` with exact content: `| 91ada72e-0abc-40f8-bb44-971a584fbdf3 | grok-build-plugins | gbp / thermos / marketplace plugin programs only | Drove, Herd, Horizon, CAO, Heavilifter (+ Planner when seated) | live |` — **Metadata / box SoT (not necessarily gbp git PR)**
- [x] B.4 Merge capability delta into tip `openspec/specs/gbp-external-loop-docs/`
- [x] B.5 `openspec validate gbp-external-loop-docs --type change --strict` (and `--all --strict` as needed) green after merge
- [x] B.6 **Prove bars Metadata/Static (claim external-loop docs done only if all hold):**
  - [x] P1 tip has thin `EXTERNAL-LOOP.md` with required cites + Symphony map + roles
  - [ ] P2 box rooms-map contains the exact gbp row (Metadata)
  - [x] P3 no thermos remint; no LIVE invent; no Elixir daemon; no second SoT skill dump
  - [x] P4 OpenSpec intent-driven; validate `--strict` green; tip ≥ `35c8c6c`
  - [x] NOT predicates: remint thermos-grok-port; invent LIVE; dual orch; propose PR claimed as apply

## 3. Archive — serial gate

Depends: Parallel band B complete + implementation on integration branch

- [ ] 3.1 `openspec validate gbp-external-loop-docs --type change --strict` still green before archive
- [ ] 3.2 Archive per openspec-git-discipline (from integration after merge)
- [ ] 3.3 Update ledger; reaffirm parks; note Prove status (VERIFIED only if Prove bars held — never invent)
