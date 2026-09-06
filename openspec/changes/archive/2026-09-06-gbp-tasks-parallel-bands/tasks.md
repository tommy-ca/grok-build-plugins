# Tasks: gbp-tasks-parallel-bands

> Schema: intent-driven. Propose atoms → offline verify → **STOP** → Todd-go apply → archive.
> Tip floor: `e3cb0c05b6419e820a1e7d93a374c463059b692d` (`e3cb0c05`). No auto-apply. No product template/skill/SPEC bodies required in Wave-4 beyond OpenSpec artefacts. Never claim parallelism-sync done from propose. P-parallel A with `gbp-herd-fanout-serial-apply`. Soft-after `gbp-openspec-pstack-binding-cite`.

## 0. Preconditions (read-only) — serial gate

- [x] 0.1 Tip SHA Probe: `e3cb0c05b6419e820a1e7d93a374c463059b692d` (≥ floor `e3cb0c05`)
- [x] 0.2 Re-read I1.md, change-ids.md, arena SYNTHESIS + A1–A3, plan, bottlenecks B1/B4, tip tasks template, tip openspec-intent-flow, tip SPEC/marketplace, closed harden archives
- [x] 0.3 Parks held: Drove max_concurrent OUT; B5–B7 park; LIVE_PASS Unavailable; remint harden Dismiss; arena/I1 local; B8 propose gate KEEP
- [x] 0.4 Confirm locked Act-on id `gbp-tasks-parallel-bands` — A1 SPLIT; A2 template+intent-flow(+SPEC); P-parallel A; do not rename without Todd go

## Parallel band A — Propose atoms (Wave-4) — P-parallel

Depends: §0

- [x] A.1 `proposal.md` — Why/What/Capabilities/Impact; Probe Evidence; A1/A2 locks; non-goals (no remint, no Drove caps, no LIVE_PASS) — **P-parallel**
- [x] A.2 `specs/openspec-tasks-parallel-bands/spec.md` — ADDED template Parallel band + N-briefs intent-flow requirements — **P-parallel**
- [x] A.3 `design.md` — A2 home; SPLIT honesty; propose-only Wave-4; no durable ADR — **P-parallel**
- [x] A.4 `adr.md` + `.openspec.yaml` — A1/A2 named; no new repo ADR; schema intent-driven — **P-parallel**

## 1. Validate --strict (offline) — serial gate

Depends: Parallel band A complete

- [x] 1.1 `openspec validate gbp-tasks-parallel-bands --type change --strict` (from worktree) → PASS
- [x] 1.2 Probe honesty: no remint harden; no Drove max_concurrent invent; no LIVE_PASS; no claim tip already has Parallel bands
- [x] 1.3 Confirm Must-nots: no auto-apply; no product PR; B8 KEEP; Soft-after #3 not blocking this propose

## 2. STOP handoff — serial gate

Depends: §1 green

- [x] 2.1 Hand Horizon `openspec/changes/gbp-tasks-parallel-bands/` (+ orch drafts + durable mirror)
- [x] 2.2 Ledger: Wave-4 VALID propose-only; apply gated on Todd go; parallelism-sync done still gated on post-apply Prove bars
- [x] 2.3 **STOP** — no apply; no `openspec apply`; no PR; no push to main

## Parallel band B — Apply (Wave-5; Todd-go) — P-parallel

Depends: Todd go + §1 green + proposal on integration branch

- [x] B.1 Extend `openspec/schemas/intent-driven/templates/tasks.md` with `## Parallel band A/B` + `P-parallel` leaf tags; serial comments for true gates only — **P-parallel**
- [x] B.2 Update `long-horizon-swarm/skills/openspec-intent-flow/SKILL.md` (+ refs as needed) with N-briefs / band apply narrative after tasks; keep propose gate serial — **P-parallel**
- [x] B.3 Add SPEC / docs scenarios for parallel-band acceptance (N-briefs; exclusive worktrees; no Drove caps in gbp text) — **P-parallel**
- [x] B.4 Merge capability delta into tip `openspec/specs/openspec-tasks-parallel-bands/`
- [x] B.5 `openspec validate --all --strict` green after merge
- [x] B.6 **Prove bars Static/Metadata (claim parallelism-sync partial for B4/B1 only if all hold):**
  - [x] P1 tip tasks template has Parallel band A/B + P-parallel convention
  - [x] P2 openspec-intent-flow (+ SPEC) carries N-briefs / band orch language
  - [x] P3 OpenSpec still intent-driven; validate `--strict` green; tip ≥ `e3cb0c05`
  - [x] P4 no remint harden; no Drove max_concurrent in gbp text; no LIVE_PASS; arena local held
  - [x] NOT predicates: Drove quota change; LIVE_PASS; remint harden; N×agy arena — do not invent

## 3. Archive — serial gate

Depends: Parallel band B complete (Todd-go scope that landed) + implementation on integration branch

- [ ] 3.1 `openspec validate gbp-tasks-parallel-bands --type change --strict` still green before archive
- [ ] 3.2 Archive per openspec-git-discipline (from integration after merge)
- [ ] 3.3 Update ledger; reaffirm parks; note B4/B1 Probe status (VERIFIED only if Prove bars held — never invent)
