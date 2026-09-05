## 0. Propose gate (this wave)

- [x] 0.1 Write proposal, specs, design, adr, and tasks for `openspec-marketplace-pstack-herdr`.
- [x] 0.2 `openspec validate openspec-marketplace-pstack-herdr --type change --strict` PASS.
- [x] 0.3 Offline verify artefacts (paths, tip SHA, EXTEND-only, no C1, no product apply). **STOP** — no apply this turn.

## 1. Apply (Wave-5 — requires Todd-go; soft-after #1)

- [ ] 1.1 Prefer `fix-release-test-herdr-set` lever green first (`python3 tests/test_release.py` PASS).
- [ ] 1.2 After Todd-go: apply this change’s OpenSpec delta into the intent-driven pipeline (keep capability `grok-build-marketplace` only; no companion spec).
- [ ] 1.3 Confirm catalog-list scenarios name `./pstack-herdr` and overlay requirement mirrors SPEC (arena/I1/prove-it local; implement after Act-on; anti N×agy).
- [ ] 1.4 `openspec validate openspec-marketplace-pstack-herdr --type change --strict` PASS on the apply branch.
- [ ] 1.5 `openspec validate --all --strict` PASS after merge/archive path is ready.

## 2. Archive (after apply + Todd/eng-lead go)

- [ ] 2.1 Archive only after apply is done and validate `--strict` PASS.
- [ ] 2.2 Do not archive while propose-only or before Todd-go apply authority.
- [ ] 2.3 Do not invent LIVE herdr kinds or touch C1 in this archive.
