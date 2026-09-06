# Tasks: gbp-herd-fanout-serial-apply

> Schema: intent-driven. Propose atoms → offline verify → **STOP** → Todd-go apply → archive.
> Tip floor: `e3cb0c05b6419e820a1e7d93a374c463059b692d` (`e3cb0c05`). No auto-apply. No product skill body required in Wave-4 beyond OpenSpec artefacts. Tip LAGS box — do not claim tip already patched. P-parallel A with `gbp-tasks-parallel-bands`. Soft-after `gbp-openspec-pstack-binding-cite`.

## 0. Preconditions (read-only) — serial gate

- [x] 0.1 Tip SHA Probe: `e3cb0c05b6419e820a1e7d93a374c463059b692d` (≥ floor `e3cb0c05`)
- [x] 0.2 Re-read I1.md, change-ids.md, arena SYNTHESIS + A1, plan, bottlenecks B3, tip herd-with-herdr, box herd-with-herdr cite fuel, closed harden archives
- [x] 0.3 Parks held: B6 pending kinds; Drove max_concurrent OUT; LIVE_PASS Unavailable; remint harden Dismiss; arena/I1 local; B8 KEEP
- [x] 0.4 Confirm locked Act-on id `gbp-herd-fanout-serial-apply` — A1 SPLIT; P-parallel A (∥ #1); do not rename without Todd go

## Parallel band A — Propose atoms (Wave-4) — P-parallel

Depends: §0

- [x] A.1 `proposal.md` — Why/What/Capabilities/Impact; Probe tip-lag honesty; non-goals — **P-parallel**
- [x] A.2 `specs/herd-fanout-serial-apply/spec.md` — ADDED fan-out default + serial_apply journal requirements — **P-parallel**
- [x] A.3 `design.md` — box cite fuel; tip plugin SoT after apply; propose-only Wave-4 — **P-parallel**
- [x] A.4 `adr.md` + `.openspec.yaml` — A1 SPLIT named; no new repo ADR; schema intent-driven — **P-parallel**

## 1. Validate --strict (offline) — serial gate

Depends: Parallel band A complete

- [x] 1.1 `openspec validate gbp-herd-fanout-serial-apply --type change --strict` (from worktree) → PASS
- [x] 1.2 Probe honesty: tip LAGS box stated; no claim tip already patched; no remint harden; no pending kinds invent; no Drove caps; no LIVE_PASS
- [x] 1.3 Confirm Must-nots: no auto-apply; no N×agy fake arena; arena/I1 local held

## 2. STOP handoff — serial gate

Depends: §1 green

- [x] 2.1 Hand Horizon `openspec/changes/gbp-herd-fanout-serial-apply/` (+ orch drafts + durable mirror)
- [x] 2.2 Ledger: Wave-4 VALID propose-only; apply gated on Todd go; B3 Prove bar post-apply only
- [x] 2.3 **STOP** — no apply; no `openspec apply`; no PR; no push to main

## Parallel band B — Apply (Wave-5; Todd-go) — P-parallel

Depends: Todd go + §1 green + proposal on integration branch

- [x] B.1 Patch tip `pstack-herdr/skills/herd-with-herdr/SKILL.md` toward box: Parallel fan-out default for N parallel-band briefs — **P-parallel**
- [x] B.2 Add journal `class: serial_apply` when choosing one (one brief | true gate | slot starved) — **P-parallel**
- [x] B.3 Preserve arena/I1/prove-it local anti-patterns; no N×agy fake arena; no pending kinds as live routes — **P-parallel**
- [x] B.4 Merge capability delta into tip `openspec/specs/herd-fanout-serial-apply/`
- [x] B.5 `openspec validate --all --strict` green after merge
- [x] B.6 **Prove bars Static (claim B3 partial only if all hold):**
  - [x] P1 tip herd-with-herdr has Parallel fan-out default + serial_apply journal
  - [x] P2 tip docs/propose language no longer claims lag as already patched
  - [x] P3 OpenSpec intent-driven; validate `--strict` green; tip ≥ `e3cb0c05`
  - [x] P4 no remint harden; no Drove caps; no LIVE_PASS; arena local held; pending kinds still park
  - [x] NOT predicates: Drove quota; LIVE_PASS; remint harden; N×agy arena; invent pending kinds

## 3. Archive — serial gate

Depends: Parallel band B complete (Todd-go scope that landed) + implementation on integration branch

- [ ] 3.1 `openspec validate gbp-herd-fanout-serial-apply --type change --strict` still green before archive
- [ ] 3.2 Archive per openspec-git-discipline (from integration after merge)
- [ ] 3.3 Update ledger; reaffirm parks; note B3 Probe status (VERIFIED only if Prove bars held — never invent)
