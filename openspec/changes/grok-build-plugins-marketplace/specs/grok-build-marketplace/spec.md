## ADDED Requirements

### Requirement: Catalog lists pstack without copying the skill tree

Feature: grok-build-marketplace
Rule: tommy-ca/pstack is the plugin source of truth

The marketplace MUST list a plugin named `pstack` whose source is a git URL of `https://github.com/tommy-ca/pstack.git` pinned to a full 40-hex sha. It MUST NOT rsync `skills/` into a second copy.

#### Scenario: Pin is recorded

- **GIVEN** a published marketplace index
- **WHEN** provenance is inspected
- **THEN** the pstack entry includes a 40-character lowercase hex git sha

### Requirement: Documented install is owner/repo

Feature: grok-build-marketplace
Rule: Bare pstack is not the default while xAI Official lists the Cursor wrap

Shipped docs MUST use `grok plugin install tommy-ca/pstack --trust`. They MUST warn that xAI Official already names `pstack` from `cursor/plugins`.

#### Scenario: Bare pstack name is not the documented default

- **GIVEN** xAI Official lists a plugin named `pstack` sourced from `cursor/plugins`
- **WHEN** shipped catalog docs name the install command
- **THEN** they use owner/repo `tommy-ca/pstack`
- **AND** they warn that bare `pstack` can resolve to the Cursor wrap

### Requirement: v1 catalog is pstack only

Feature: grok-build-marketplace
Rule: Optional Cursor siblings stay optional

`cursor-team-kit` and `make-bot-ui` MUST NOT be required Grok plugins.

#### Scenario: v1 catalog is pstack only

- **GIVEN** the v1 marketplace index
- **WHEN** plugins[] is read
- **THEN** the only installable plugin is `pstack`
