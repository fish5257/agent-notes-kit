# Default Agent Note format

Use the project's own format when it exists. This is the template default.

## Header and location

Use `.agents/notes/{proposed,implemented,rejected}/YYYY-MM-DD-topic.md`. Start every file with:

```markdown
# Agent Note: <title>

Status: <proposed | implemented | rejected — reason>
```

The folder and `Status:` must agree. Use a short date-prefixed filename; keep exact enforcement in the repository validator rather than in this reference.

## Lifecycle sections

`proposed/`:

```markdown
## Problem
## Proposal
## Alternatives considered
## Acceptance criteria
## Risks
```

`implemented/`:

```markdown
## Problem
## Decision
## Alternatives considered
## Consequences
## Verification
```

`rejected/`:

```markdown
## Problem
## Proposal
## Alternatives considered
## Reconsider if
```

`Alternatives considered` contains only reasons supported by the available record. An implemented Note describes what shipped in present tense; verification lists actual evidence, not a plan.
