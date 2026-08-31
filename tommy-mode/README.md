# Tommy mode (Grok Build)

Standalone overlay on `/poteto-mode`. Not a pstack pack. One skill. No agents. No hooks.

```bash
grok plugin marketplace add tommy-ca/grok-build-plugins
grok plugin install tommy-mode --trust
grok --sandbox off plugin enable tommy-mode
```

Run marketplace add and enable from a host shell. Nested enable rewrites `~/.grok/config.toml` and hits EROFS. After enable, start a **new session**.

Then `/tommy-mode`. If a user copy exists at `~/.grok/skills/tommy-mode`, remove it so this plugin is the only load.

pstack stays `grok plugin install tommy-ca/pstack --trust`.
