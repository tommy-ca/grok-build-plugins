# Tasks: thermos-grok-port

> Schema: intent-driven. Propose atoms → offline verify → **STOP** → Todd/Horizon-go apply → archive.
> Tip floor: `e3cb096cb2d68fefbb1629358e83ee4b69473180` (`e3cb096c`). Propose-only Wave-4. No auto-apply. No product `thermos/` in propose PR. No nest pstack. No invent LIVE_PASS. No remint closed gbp #1–#14.

## 0. Preconditions (read-only) — serial gate

- [x] 0.1 Tip SHA Probe: `e3cb096cb2d68fefbb1629358e83ee4b69473180` (≥ floor `e3cb096c`)
- [x] 0.2 Re-read BRIEF.md, WAVE-0-GO.md, tip-audit, inventory thermos-source + gbp-catalog, PORT-SCOPE, ADRs 0001–0006, sibling HARNESS patterns (`tommy-mode/`, `long-horizon-swarm/`)
- [x] 0.3 Parks held: no pstack nest; no Cursor-only Task sole path; docs-only reject; no LIVE_PASS; no remint closed leaves
- [x] 0.4 Confirm locked Act-on id `thermos-grok-port`; plugin id/dir `thermos`; full poteto bind — do not rename without Todd go

## Parallel band A — Propose atoms (Wave-4) — P-parallel

Depends: §0

- [x] A.1 `proposal.md` — Why/What/Capabilities/Impact; Probe Evidence Static/Metadata; non-goals — **P-parallel**
- [x] A.2 `specs/thermos-grok-port/spec.md` — ADDED R-THERMOS-01..04 — **P-parallel**
- [x] A.3 `specs/grok-build-marketplace/spec.md` — light MODIFY (+ ADDED thermos sibling) with full-body copies — **P-parallel**
- [x] A.4 `design.md` — C4; port map; poteto surfaces; VERIFY levers — **P-parallel**
- [x] A.5 `adr.md` + `.openspec.yaml` — cite 0001–0006; A1/A2/A3; schema intent-driven — **P-parallel**

## 1. Validate --strict (offline) — serial gate

Depends: Parallel band A complete

- [x] 1.1 `openspec validate thermos-grok-port --type change --strict` (from worktree) → MUST PASS
- [x] 1.2 Probe honesty: propose-only; no product thermos/ in PR; no LIVE_PASS; no remint closed leaves
- [x] 1.3 Confirm Must-nots: no nest pstack; no Cursor Task sole path; docs-only reject at apply

## 2. STOP handoff — serial gate

Depends: §1 green

- [x] 2.1 Open propose PR (OpenSpec artefacts only); title/body per brief; do **not** merge
- [x] 2.2 Hand Horizon `openspec/changes/thermos-grok-port/` + PR URL; write `wave-4/VALID.md`
- [x] 2.3 **STOP** — Apply HOLD until Todd/Horizon go; no `openspec apply`; no land `thermos/` product; no push to main

## Parallel band B — Apply (Wave-5; HOLD) — P-parallel

Depends: Todd/Horizon go + §1 green

- [x] B.1 Land `thermos/` sibling: `plugin.json`, README, `HARNESS.md`, `skills/` (thermos + both rubrics), `agents/` adapted from upstream — **P-parallel**
- [x] B.2 Marketplace entry `./thermos` + SemVer `MAJOR.MINOR.PATCH-thermos.N` (plugin.json == marketplace version) — **P-parallel**
- [x] B.3 Lever VERIFY: `scripts/verify-thermos.sh` and/or `verify-thermos` skill + skill smoke receipts — **P-parallel**
- [x] B.4 Update catalog README/SPEC/tests sibling sets; reject docs-only without installable surfaces
- [x] B.5 Merge capability deltas into tip `openspec/specs/`; `openspec validate --all --strict` green
- [x] B.6 **Prove bars (claim VERIFIED only if all hold):**
  - [x] P1 `grok plugin validate` (or repo equivalent) green on `thermos/`
  - [x] P2 skill smoke: orchestrator + both rubrics load; HARNESS names Grok spawn/join
  - [x] P3 poteto surfaces named; lever VERIFY rerunnable
  - [x] P4 marketplace + SemVer `-thermos.N`; no pstack nest; ADRs 0001–0006 held
  - [x] NOT predicates: Cursor Task sole API; docs-only; LIVE_PASS invent; remint closed gbp leaves

## 3. Archive — serial gate

Depends: Parallel band B complete + implementation on integration branch

- [ ] 3.1 `openspec validate thermos-grok-port --type change --strict` still green before archive
- [ ] 3.2 Archive per openspec-git-discipline (from integration after merge)
- [ ] 3.3 Update ledger; reaffirm parks; note Prove status (VERIFIED only if Prove bars held — never invent)
