# Agent compatibility (Grok Build)

Grok-native port of Cursor `agent-compatibility`. One slash skill. Four review agents. The scanner is `npx -y agent-compatibility@latest`, not copied into this repo.

```bash
grok plugin marketplace add tommy-ca/grok-build-plugins
grok plugin install agent-compatibility --trust
grok plugin enable agent-compatibility
```

Run marketplace add and enable from a host shell. Enable rewrites `~/.grok/config.toml` and hits EROFS inside the agent sandbox. After enable, spawn `agent-compatibility:startup-review`, not `startup-review`.

Then `/check-agent-compatibility`. The parent fans out four children (depth 1). Host map: [`HARNESS.md`](./HARNESS.md).

pstack stays `grok plugin install tommy-ca/pstack --trust`. This plugin is a sibling, not a pstack pack.
