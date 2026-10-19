# AGENTS.md — Agent Notes Kit

- Keep this repository focused on reusable decision-note workflows; do not add product-specific contracts here.
- For durable architecture, API, state, persistence, compatibility, or security decisions in this repo, use `$agent-notes` to retrieve related Notes before choosing an approach.
- Only create or finalize a Note after implementation and relevant verification, and only when the decision rationale is not already explained by source, tests, or current documentation. Routine fixes and mechanical edits do not need Notes.
- After adding or moving an active Note, run `python3 .agents/notes/verify_format.py` and report the result.
- When delegating work that creates or maintains Notes, specify the `$agent-notes` operation and require a scoped supersession report.
