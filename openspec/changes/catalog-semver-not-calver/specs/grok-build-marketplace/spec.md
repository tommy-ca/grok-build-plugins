## ADDED Requirements

### Requirement: Sibling versions are SemVer identity, not calendar uniqueness

Feature: grok-build-marketplace
Rule: uniqueness is plugin name in one git tag namespace

Local sibling versions MUST remain `MAJOR.MINOR.PATCH-<plugin-name>.N` (SemVer 2.0 prerelease used as namespace). They MUST NOT be calendar-only (`YYYY.MM.DD`, `YYYY.MM.MICRO`) and MUST NOT use a date as the uniqueness key. Two siblings shipping the same day MUST still have distinct versions. Ship day belongs in GitHub Release notes. Existing tags MUST NOT be moved.

#### Scenario: date is not uniqueness

- **GIVEN** two local siblings
- **WHEN** both would ship on the same calendar day
- **THEN** their `plugin.json` versions still differ by plugin name
- **AND** neither version is a date-only CalVer string
