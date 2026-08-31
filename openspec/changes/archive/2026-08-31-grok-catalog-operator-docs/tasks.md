## 1. Tests first

- [x] 1.1 Fail then pass. README and sibling READMEs name a new session after enable, `inspect.agents`, directory count, `--available`, and EROFS without requiring the bwrap env var. `AGENTS.md` names `python3 tests/test_marketplace.py`.

## 2. Docs

- [x] 2.1 Update README, SPEC, sibling READMEs, and add `AGENTS.md`.

## 3. Prove

- [x] 3.1 `python3 tests/test_marketplace.py`. `openspec validate grok-catalog-operator-docs --type change --strict`.
