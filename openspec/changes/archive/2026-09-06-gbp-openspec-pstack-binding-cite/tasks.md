# Tasks: gbp-openspec-pstack-binding-cite

> Schema: intent-driven. Propose atoms → offline verify → **STOP** → Todd-go apply → archive.
> Tip floor: `e3cb0c05b6419e820a1e7d93a374c463059b692d` (`e3cb0c05`). Soft-after A after #1/#2. No auto-apply. No vendor openspec-pstack-orch. No Drove quotas in gbp text. Never claim parallelism-sync done from propose.

## 0. Preconditions (read-only) — serial gate

- [x] 0.1 Tip SHA Probe: `e3cb0c05b6419e820a1e7d93a374c463059b692d` (≥ floor `e3cb0c05`)
- [x] 0.2 Re-read I1.md, change-ids.md, arena A3 + SYNTHESIS, plan, fleet openspec-pstack-orch README/design/orch-binding, tip SPEC + openspec-intent-flow cite gap
- [x] 0.3 Parks held: Drove max_concurrent OUT; LIVE_PASS Unavailable; remint harden Dismiss; no vendor; B8 KEEP
- [x] 0.4 Confirm locked Soft-after Act-on id `gbp-openspec-pstack-binding-cite` — A3 Soft-after; do not rename without Todd go

## Parallel band A — Propose atoms (Wave-4; Soft-after ready once #1/#2 band language in propose set) — P-parallel

Depends: §0 (Soft-after: band language present in sibling proposes)

- [x] A.1 `proposal.md` — Why/What/Capabilities/Impact; Soft-after honesty; non-goals (no vendor, no Drove caps) — **P-parallel**
- [x] A.2 `specs/openspec-pstack-binding-cite/spec.md` — ADDED cite compose + Soft-after ordering requirements — **P-parallel**
- [x] A.3 `design.md` — cite-not-vendor; Soft-after A; propose-only Wave-4 — **P-parallel**
- [x] A.4 `adr.md` + `.openspec.yaml` — A3 Soft-after named; no new repo ADR; schema intent-driven — **P-parallel**

## 1. Validate --strict (offline) — serial gate

Depends: Parallel band A complete

- [x] 1.1 `openspec validate gbp-openspec-pstack-binding-cite --type change --strict` (from worktree) → PASS
- [x] 1.2 Probe honesty: Soft-after stated; no vendor; no Drove max_concurrent invent; no LIVE_PASS; no remint harden
- [x] 1.3 Confirm Must-nots: no auto-apply; B8 KEEP; no claim sync done from propose

## 2. STOP handoff — serial gate

Depends: §1 green

- [x] 2.1 Hand Horizon `openspec/changes/gbp-openspec-pstack-binding-cite/` (+ orch drafts + durable mirror)
- [x] 2.2 Ledger: Wave-4 VALID propose-only Soft-after; apply gated on Todd go (+ Soft-after after #1/#2 land unless Todd authorizes docs-only earlier)
- [x] 2.3 **STOP** — no apply; no `openspec apply`; no PR; no push to main

## Parallel band B — Apply (Wave-5; Todd-go Soft-after) — P-parallel

Depends: Todd go + §1 green + Soft-after readiness (#1 band language on integration, preferably #2 too)

- [x] B.1 Add cite in tip `SPEC.md` and/or openspec-intent-flow references pointing at openspec-pstack-orch compose — **P-parallel**
- [x] B.2 Document three rules: propose gated; parallel after tasks/Parallel bands; exclusive worktrees — **P-parallel**
- [x] B.3 Explicitly exclude Drove quota numbers and vendor copy from gbp cite text — **P-parallel**
- [x] B.4 Merge capability delta into tip `openspec/specs/openspec-pstack-binding-cite/`
- [x] B.5 `openspec validate --all --strict` green after merge
- [x] B.6 **Prove bars Metadata/Static (claim binding cite only if all hold):**
  - [x] P1 tip SPEC/docs/LHS cites openspec-pstack-orch compose (or mirrored summary)
  - [x] P2 three compose rules present; B8 KEEP
  - [x] P3 no vendor tree; no Drove max_concurrent in gbp text; no LIVE_PASS; no remint harden
  - [x] P4 OpenSpec intent-driven; validate `--strict` green; tip ≥ `e3cb0c05`
  - [x] NOT predicates: Drove quota change; vendor package; LIVE_PASS; remint harden

## 3. Archive — serial gate

Depends: Parallel band B complete (Todd-go Soft-after scope that landed) + implementation on integration branch

- [ ] 3.1 `openspec validate gbp-openspec-pstack-binding-cite --type change --strict` still green before archive
- [ ] 3.2 Archive per openspec-git-discipline (from integration after merge)
- [ ] 3.3 Update ledger; reaffirm parks; note binding-cite Prove status (VERIFIED only if Prove bars held — never invent)
