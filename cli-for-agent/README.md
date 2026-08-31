# CLI for agents (Grok Build)

Grok-native port of the Cursor `cli-for-agent` skill. One skill. No agents. No hooks.

```bash
grok plugin marketplace add tommy-ca/grok-build-plugins
grok plugin install cli-for-agent --trust
grok plugin enable cli-for-agent
```

Run marketplace add and enable from a host shell. Enable rewrites `~/.grok/config.toml` and hits EROFS inside the agent sandbox.

Then `/cli-for-agents` when you design or review a CLI for agents.

pstack stays `grok plugin install tommy-ca/pstack --trust`. This plugin is a sibling, not a pstack pack.
