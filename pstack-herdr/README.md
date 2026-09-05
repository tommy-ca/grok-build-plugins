# pstack-herdr

Optional overlay on [tommy-ca/pstack](https://github.com/tommy-ca/pstack): route pstack **implement** roles onto interactive [herdr](https://herdr.dev) agents (default workhorse: `agy`). **Not** a pstack pack and **not** a substitute for arena or interrogate.

## Install

Requires marketplace add (host shell if nested grok hits EROFS on `config.toml`):

```bash
grok plugin marketplace add tommy-ca/grok-build-plugins
grok plugin install pstack-herdr --trust
grok plugin enable pstack-herdr
```

Also install/enable `tommy-ca/pstack` for arena / interrogate / poteto. Start a **new session** after enable.

Copy the default router rule:

```bash
cp "$(dirname "$(grok plugin path pstack-herdr 2>/dev/null || echo ./pstack-herdr)")/references/pstack-herdr-agents.mdc" \
  ~/.cursor/rules/pstack-herdr-agents.mdc
```

(or copy from this folder’s `references/pstack-herdr-agents.mdc`). Edit with the **Setup pstack herdr agents** skill.

## Skills

| Skill | Role |
| --- | --- |
| `herd-with-herdr` | Outside-driver herdr orch + pstack_role resolve |
| `delegate-to-agy` | Interactive agy via herdr; bare `--print` fallback |
| `external-coding-agents` | Meta-orch spawn policy |
| `setup-pstack-herdr-agents` | Edit role→kind map (like `/setup-pstack`) |
| `fleet-roles-map` | Keep fleet / herdr maps updated |

## Philosophy

- `pstack-models.mdc` → LLM models (arena / I1 / judgment)
- `pstack-herdr-agents.mdc` → herdr kinds (implement after Act-on)
- Never N×same herdr kind as fake arena
- Order: arena (local) → Act-on → herdr implement → optional interrogate (local) → prove-it → merge

See `docs/audits/` and `references/pstack-herdr-agents.md`.
