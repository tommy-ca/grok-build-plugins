# Long-horizon swarm (Grok Build)

Optional overlay on `/poteto-mode` Orchestrate. Standing programs. Spec-as-root. TaskTree. Not a pstack pack. Overlay skills plus one playbook. No agents. No hooks.

```bash
grok plugin marketplace add tommy-ca/grok-build-plugins
grok plugin install tommy-ca/pstack --trust
grok --sandbox off plugin enable pstack
grok plugin install long-horizon-swarm --trust
grok --sandbox off plugin enable long-horizon-swarm
```

Run marketplace add and enable from a host shell. Nested enable rewrites `~/.grok/config.toml` and hits EROFS. After enable, start a **new session**.

Then `/poteto-mode`. Then `/long-horizon-swarm`. If poteto-mode is missing, the overlay refuses and names `tommy-ca/pstack --trust`.

## Who runs a standing program?

Fleet seat bind (Planner / Horizon / Drove / CAO / Herd / Heavilifter / Nightly Audit) lives in [`HARNESS.md`](./HARNESS.md) and cites repo-root `EXTERNAL-LOOP.md`. **Dual orch forbidden** — one orch owner per brief. Heavilifter is prove-it / recovery / worktree, not primary fan-out. Herd is session herdr after Act-on, not CAO scale.

Overlay skills: `long-horizon-swarm`, `field-guide`, `planner-worker-split`, `review-lenses`, `coordination-layer`, `megafile-gate`, `ossify-break`, `openspec-intent-flow`.

pstack stays `grok plugin install tommy-ca/pstack --trust`. This plugin ships no agents. Spawn stays `pstack:<role>`. Live types are `inspect.agents[]`. `provides.agents` is a directory count. Arena and interrogate stay pstack cites — not cloned here.
