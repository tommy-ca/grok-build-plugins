## 0. Propose gate (this wave)

- [x] 0.1 Write proposal, specs, design, adr, and tasks for `fix-release-test-herdr-set`.
- [x] 0.2 `openspec validate fix-release-test-herdr-set --type change --strict` PASS.
- [x] 0.3 Offline verify artefacts (paths, tip SHA, no C1, no product apply). **STOP** — no apply this turn.

## 1. Apply (Wave-5 — requires Todd-go)

- [x] 1.1 After Todd-go: update `tests/test_release.py` expected local set to include `pstack-herdr` beside `agent-compatibility`, `cli-for-agent`, `tommy-mode`, and `long-horizon-swarm`.
- [x] 1.2 Run `python3 tests/test_release.py` → PASS.
- [x] 1.3 Merge OpenSpec delta for version/identity GIVENs when applying this change (or confirm identical text already on tip from ordered apply).
- [x] 1.4 `openspec validate fix-release-test-herdr-set --type change --strict` PASS on the apply branch.

## 2. Archive (after apply + Todd/eng-lead go)

- [ ] 2.1 Archive only after apply is done, lever green, and validate `--strict` still PASS.
- [ ] 2.2 Do not archive while propose-only or before Todd-go apply authority.
