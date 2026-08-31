# Agent compatibility (Grok Build)

Grok-native port of Cursor `agent-compatibility`. One slash skill. Four review agents. The scanner is `npx -y agent-compatibility@latest`, not copied into this repo.

```bash
grok plugin marketplace add tommy-ca/grok-build-plugins
grok plugin install agent-compatibility --trust
grok plugin enable agent-compatibility
```

Run marketplace add and enable from a host shell. Nested enable rewrites `~/.grok/config.toml` and hits EROFS even when `__GROK_INSIDE_BWRAP` is unset. After enable, start a **new session**. Spawn `agent-compatibility:startup-review`, not `startup-review`. Live roles are `inspect.agents[]`. `provides.agents` is a directory count.

Then `/check-agent-compatibility`. The parent fans out four children (depth 1). Host map: [`HARNESS.md`](./HARNESS.md).

pstack stays `grok plugin install tommy-ca/pstack --trust`. This plugin is a sibling, not a pstack pack.
