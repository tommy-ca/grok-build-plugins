## 1. File contracts (TDD)

- [x] 1.1 Fail then pass `tests/test_release.py`: unique `MAJOR.MINOR.PATCH-<name>.N` versions, marketplace equality, no root `plugin.json`, script has `grok --sandbox off plugin tag --push`, `git push origin`, `gh release view`, `--verify-tag`, `--latest=false`, no `--force`. Workflow on `v*` has no grok and no `workflow_dispatch`.

## 2. Versions and writers

- [x] 2.1 Set sibling `plugin.json` and marketplace versions to `1.0.0-<name>.0`.
- [x] 2.2 Add `scripts/release.sh` and `.github/workflows/release.yml`.
- [x] 2.3 Update README, SPEC, live marketplace spec, ADR 0003. Extend `tests/test_marketplace.py` so marketplace version equals each local `plugin.json`.

## 3. Prove and archive

- [ ] 3.1 Land writers on `origin/main`. From a host shell run `./scripts/release.sh`. Confirm tags, GitHub Releases, and a non-empty `gh run list --workflow=release.yml`.
- [ ] 3.2 `openspec validate catalog-sibling-release-tag --type change --strict` then archive after implementation is on `main`.
