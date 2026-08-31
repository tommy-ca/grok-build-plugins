## 1. Tests first

- [x] 1.1 Fail then pass. Marketplace lists `./tommy-mode`. `grok plugin validate` on that dir. Skill has `disable-model-invocation`. No hooks or `commands/`.

## 2. Plugin

- [x] 2.1 Add `tommy-mode/` plugin.json, skill, README, HARNESS. Update marketplace, README, SPEC, main spec.

## 3. Prove

- [x] 3.1 `python3 tests/test_marketplace.py`. `openspec validate tommy-mode-plugin --type change --strict`.
