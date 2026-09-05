## 1. Tests first

- [x] 1.1 Fail then pass. Marketplace lists `./long-horizon-swarm`. `grok plugin validate` on that dir. Skill has `disable-model-invocation`. No hooks or `commands/`. Playbook names `spawn_subagent` and `pstack:`. Texts do not name `orch init` or `chatroom_send`.

## 2. Plugin

- [x] 2.1 Add `long-horizon-swarm/` plugin.json, skill, playbook, README, HARNESS, LICENSE, UPSTREAM. Update marketplace, README, SPEC, main spec, both test files.

## 3. Prove

- [x] 3.1 `python3 tests/test_marketplace.py`. `python3 tests/test_release.py`. `openspec validate add-long-horizon-swarm-plugin --type change --strict`.
