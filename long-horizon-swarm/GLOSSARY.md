# Overlay glossary

One name per concept. Article words where the article named them. pstack skill names where pstack already shipped them.

| Canonical | Also heard | Do not use |
| --- | --- | --- |
| planner | coordinator (root planner only) | lead agent, boss |
| worker | builder (when the brief is specified) | implementer-agent |
| verifier | judge | reviewer-bot |
| reconciler | neutral resolver | merge-bot |
| Field Guide | field-guide/ | notes/, memory.md |
| design doc | DesignDoc, design-docs/<conceptKey>.md | architecture.md blob |
| review lenses | review-lenses | vibe check |
| arena | pstack arena | arena-view |
| interrogate | pstack interrogate | interrogate-view |
| TaskTree | task tree | TaskGraph type |
| OrchStore | pstack orch.ts under long-horizon/<id>/ | second board |
| HostStore | Orchestrate durable-state when orch cannot run | second board |
| Brief | orchestrate brief | prompt.txt |
| openspec-intent-flow | OpenSpec binding | openspec-intent |
| coordination-layer | git adapter | coordination (spec id) |
| long-horizon-swarm | overlay playbook | article-loop playbook |

## Install names

Skills that ship in this plugin under `skills/`:

- long-horizon-swarm
- field-guide
- planner-worker-split
- review-lenses
- coordination-layer
- megafile-gate
- ossify-break
- openspec-intent-flow

Not shipped: grok-chat adapter, Cursor rules.

pstack leaves called by reference, not copied: arena, interrogate, swarm, architect, how, why.

## Sources

- Article: planner, worker, Field Guide, design docs, review lenses, reconciler
- pstack: arena, interrogate, poteto-mode, Orchestrate HostStore
- This plugin: the skill names in `skills/`
