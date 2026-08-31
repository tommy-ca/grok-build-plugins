# Grok Build harness for cli-for-agent

Host map. grok does not load it as a skill.

| Need | Grok primitive |
|---|---|
| Slash | `/cli-for-agents` |
| Spawn | none. This plugin has no agents. |
| Skill order | pstack, then user, then this plugin. Qualified name is `cli-for-agent:cli-for-agents` if the slash collides. |
| Hooks | none |
