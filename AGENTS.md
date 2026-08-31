# grok-build-plugins

Marketplace catalog. Not an application. Do not expect a one-command app startup, CI, or a linter.

## Check

```bash
python3 tests/test_marketplace.py
python3 tests/test_release.py
```

`test_marketplace.py` also runs `grok plugin validate` on local sibling folders. `test_release.py` is file-text. It is what Actions runs.

## Install

Host shell for marketplace add and enable. Nested grok cannot rewrite `~/.grok/config.toml` (EROFS). After enable, start a new session. Spawn `agent-compatibility:startup-review`, not `startup-review`. pstack stays `grok plugin install tommy-ca/pstack --trust`.
