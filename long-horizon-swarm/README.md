# Long-horizon swarm (Grok Build)

Optional overlay on `/poteto-mode` Orchestrate. Standing programs. Spec-as-root. Not a pstack pack. One skill. One playbook. No agents. No hooks.

```bash
grok plugin marketplace add tommy-ca/grok-build-plugins
grok plugin install tommy-ca/pstack --trust
grok --sandbox off plugin enable pstack
grok plugin install long-horizon-swarm --trust
grok --sandbox off plugin enable long-horizon-swarm
```

Run marketplace add and enable from a host shell. Nested enable rewrites `~/.grok/config.toml` and hits EROFS. After enable, start a **new session**.

Then `/poteto-mode`. Then `/long-horizon-swarm`. If poteto-mode is missing, the overlay refuses and names `tommy-ca/pstack --trust`.

pstack stays `grok plugin install tommy-ca/pstack --trust`. This plugin ships no agents. Spawn stays `pstack:<role>`. Live types are `inspect.agents[]`. `provides.agents` is a directory count.
