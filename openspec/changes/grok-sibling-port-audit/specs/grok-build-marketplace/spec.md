## ADDED Requirements

None.

## MODIFIED Requirements

### Requirement: Spawn types are plugin-qualified

Feature: grok-build-marketplace
Rule: grok 1.0.13 names plugin-qualified roles

Shipped catalog docs MUST say pstack playbooks spawn `pstack:<role-key>` (`pstack:how-explorer`). They MUST say agent-compatibility children are `agent-compatibility:<role>` (`agent-compatibility:startup-review`). They MUST say bare stems are unknown even after enable.

#### Scenario: Docs name the live spawn type

- **GIVEN** pstack is enabled
- **WHEN** catalog docs describe subagents
- **THEN** they use `pstack:how-explorer`
- **AND** they do not claim the bare stem is a live type

#### Scenario: sibling docs name qualified review roles

- **GIVEN** shipped catalog README
- **WHEN** an operator enables agent-compatibility
- **THEN** docs name `agent-compatibility:startup-review`
- **AND** they say not to spawn `startup-review`

## REMOVED Requirements

None.

## RENAMED Requirements

None.
