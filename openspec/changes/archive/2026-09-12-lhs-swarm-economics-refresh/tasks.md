# Tasks: lhs-swarm-economics-refresh

> Schema: intent-driven. Propose atoms → offline verify → **STOP** → Todd/Horizon-go apply → archive.
> Tip floor: `d03c318c9885b11d07ce5725629874f0e3eb165b` (`d03c318c`). No auto-apply. No product `long-horizon-swarm/` in propose PR. No remint `thermos-grok-port` / `gbp-external-loop-docs`. No clone arena/interrogate. No invent LIVE. Dual orch forbidden.

## 0. Preconditions (read-only) — serial gate

- [x] 0.1 Tip SHA Probe: `d03c318c9885b11d07ce5725629874f0e3eb165b` (≥ floor `d03c318c`) — gbp-external-loop-docs archive #20 MERGED; `EXTERNAL-LOOP.md` present
- [x] 0.2 Re-read Todd/room Act-on: BRIEF.md + WAVE-0-GO; overlay HARNESS/README/playbook/skills; verify script; roles-map + research audit; Cursor blog failure modes
- [x] 0.3 Parks held: remint thermos-grok-port OUT; remint gbp-external-loop-docs OUT; clone arena/interrogate OUT; LIVE invent OUT; Elixir Symphony daemon OUT; dual orch OUT; nest pstack OUT
- [x] 0.4 Confirm locked Act-on id `lhs-swarm-economics-refresh`; SemVer target `1.2.0-long-horizon-swarm.N`; NEW capability only (no marketplace MODIFY)

## Parallel band A — Propose atoms (Wave-4) — P-parallel

Depends: §0

- [x] A.1 `proposal.md` — Why/What/Capabilities/Impact; Probe Evidence; gaps from BRIEF; non-goals — **P-parallel**
- [x] A.2 `specs/lhs-swarm-economics-refresh/spec.md` — ADDED fleet bind, lever-first VERIFY, blog checklist, SemVer+prove, roles-map honesty, propose-only — **P-parallel**
- [x] A.3 `design.md` — C4; refresh map; VERIFY levers; NEW-only; split apply — **P-parallel**
- [x] A.4 `adr.md` + `.openspec.yaml` — cite 0001–0006; SemVer bump decision; no arena clone; schema intent-driven — **P-parallel**

## 1. Validate --strict (offline) — serial gate

Depends: Parallel band A complete

- [x] 1.1 `openspec validate lhs-swarm-economics-refresh --type change --strict` (from worktree) → PASS
- [x] 1.2 Probe honesty: no product overlay/SemVer in propose tree; roles-map cite content named; no thermos / gbp-external-loop-docs remint; no LIVE invent
- [x] 1.3 Confirm Must-nots: no auto-apply; dual orch forbidden; Horizon leaf apply; Drove/eggbot owns box roles-map / persona cites

## 2. STOP handoff — serial gate

Depends: §1 green

- [x] 2.1 Hand Horizon `openspec/changes/lhs-swarm-economics-refresh/` (+ orch VALID/BRIEF)
- [x] 2.2 Ledger: Wave-4 VALID propose-only; Apply HOLD until Todd/Horizon go
- [x] 2.3 **STOP** — no `openspec apply`; no product plugin edits; no box roles-map / persona edit from propose executor; do not merge as apply

## Parallel band B — Apply (Wave-5; Todd/Horizon go) — COMPLETE (Heavilifter gbp + Drove B.6)

Depends: Todd/Horizon go + §1 green

- [x] B.1 Refresh `long-horizon-swarm/HARNESS.md` + `README.md` with EXTERNAL-LOOP fleet seat bind (Planner / Horizon / Drove / CAO / Herd / Heavilifter / Nightly Audit) + dual-orch forbidden; keep Grok primitives — **P-parallel (gbp git)**
- [x] B.2 Refresh playbook + `references/standing-orders-template.md` with blog failure-mode checklist (split-brain, planner contention, merge reconciler, megafiles, ossify, review lenses, Field Guide, model economics) as refuse/stop checks; keep planner≠worker, CostPolicy, Field Guide, review-lenses, megafile-gate, ossify-break, openspec-intent-flow; refuse flat-swarm / dual-board / nested-spawn; arena/interrogate via pstack cite — **P-parallel (gbp git)**
- [x] B.3 Lever-first VERIFY: Brief.VERIFY requires `verify-*` or `scripts/verify-*.sh`; refuse prose-only on non-trivial leaves; handoff records lever path; cite Nightly Audit maintain-verification; no LIVE invent — **P-parallel (gbp git)**
- [x] B.4 Bump SemVer `1.1.0-long-horizon-swarm.0` → `1.2.0-long-horizon-swarm.N` in `plugin.json` and marketplace `plugins[].version`; do not move tags — **P-parallel (gbp git)**
- [x] B.5 Prove `scripts/verify-long-horizon-swarm.sh` green (extend if new assertions needed) + `python3 tests/test_marketplace.py` PASS + `grok plugin validate ./long-horizon-swarm` — **serial after B.1–B.4**
- [x] B.6 Drove/eggbot applies box SoT cite lines to `/workspace/fleet-external-agents/roles-map.md`, `~/.cursor/rules/fleet-roles.mdc`, and personas (Drove, Horizon, Planner, CAO, Herd, Heavilifter, Nightly Audit) with the standing-program overlay block named in spec — **Metadata / box SoT (not necessarily gbp git PR)**
- [x] B.7 Merge capability delta into tip `openspec/specs/lhs-swarm-economics-refresh/`
- [x] B.8 `openspec validate lhs-swarm-economics-refresh --type change --strict` (and `--all --strict` as needed) green after merge
- [x] B.9 **Prove bars Metadata/Static (claim refresh done only if all hold):**
  - [x] P1 HARNESS/README name fleet seats + dual-orch forbidden + Grok primitives remain
  - [x] P2 playbook + standing-orders name the eight blog failure modes as refuse/stop checks
  - [x] P3 Brief.VERIFY / handoff require named lever; prose-only refuse on non-trivial leaves
  - [x] P4 SemVer `1.2.0-long-horizon-swarm.N` on plugin.json + marketplace; verify script + marketplace tests green
  - [x] P5 box roles-map / fleet-roles.mdc / personas contain the standing-program overlay cite (Metadata)
  - [x] P6 keep-list intact; arena/interrogate not cloned; no thermos / gbp-external-loop-docs remint; no LIVE invent
  - [x] P7 OpenSpec intent-driven; validate `--strict` green; tip ≥ `d03c318c`
  - [x] NOT predicates: remint thermos-grok-port; remint gbp-external-loop-docs; clone arena/interrogate; invent LIVE; dual orch; docs-only apply; propose PR claimed as apply

## 3. Archive — serial gate

Depends: Parallel band B complete + implementation on integration branch

- [x] 3.1 `openspec validate lhs-swarm-economics-refresh --type change --strict` still green before archive
- [x] 3.2 Archive per openspec-git-discipline (from integration after merge)
- [x] 3.3 Update ledger; reaffirm parks; note Prove status (VERIFIED only if Prove bars held — never invent)
