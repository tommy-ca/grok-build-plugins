# Tasks: <!-- change-id -->

> Schema: intent-driven. Serial gates for validate / STOP / apply authority / archive. Parallel bands for independent concurrent leaves.

## 0. Preconditions (read-only) — serial gate

<!-- True gate: serialize before propose band -->
- [ ] 0.1 <!-- Precondition check / tip probe -->

## Parallel band A — Propose atoms — P-parallel

<!-- Independent propose leaves may run concurrently; tag with P-parallel -->
- [ ] A.1 <!-- Independent proposal leaf --> — **P-parallel**
- [ ] A.2 <!-- Independent spec/design leaf --> — **P-parallel**

## 1. Validate --strict (offline) — serial gate

<!-- True gate: serialize before STOP / handoff -->
- [ ] 1.1 `openspec validate <change-id> --type change --strict` → PASS

## 2. STOP handoff — serial gate

<!-- True gate: STOP for review / Todd-go authority before apply -->
- [ ] 2.1 Hand off propose artifacts
- [ ] 2.2 **STOP** — no apply; await Todd-go apply authority

## Parallel band B — Apply (Todd-go) — P-parallel

<!-- Independent apply leaves; tag with P-parallel -->
<!-- Soft-after leaves marked Soft-after; do not force fake total order with unrelated P-parallel leaves -->
<!-- No Drove max_concurrent quota numbers invented here -->
- [ ] B.1 <!-- Independent apply leaf --> — **P-parallel**
- [ ] B.2 <!-- Independent apply leaf --> — **P-parallel**
- [ ] B.3 <!-- Dependent or sequenced apply leaf --> — Soft-after B.1

## 3. Archive — serial gate

<!-- True gate: serialize after implementation lands on integration branch -->
- [ ] 3.1 `openspec validate <change-id> --type change --strict`
- [ ] 3.2 Archive change
