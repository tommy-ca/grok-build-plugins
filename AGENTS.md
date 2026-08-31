# grok-build-plugins

Marketplace catalog. Not an application. Do not expect a one-command app startup, CI, or a linter.

## Check

```bash
python3 tests/test_marketplace.py
```

That script also runs `grok plugin validate` on `./agent-compatibility` and `./cli-for-agent`.

## Install

Host shell for marketplace add and enable. Nested grok cannot rewrite `~/.grok/config.toml` (EROFS). After enable, start a new session. Spawn `agent-compatibility:startup-review`, not `startup-review`. pstack stays `grok plugin install tommy-ca/pstack --trust`.
