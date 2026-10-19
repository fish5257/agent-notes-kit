# AGENTS.md — Agent Notes Kit

- Keep this repository focused on reusable decision-note workflows; do not add product-specific contracts here.
- For durable architecture, API, state, persistence, compatibility, or security decisions in this repo, use `$agent-notes` to retrieve related Notes before choosing an approach.
- After a substantial simplification audit, use `$agent-notes` Capture only when it surfaces durable decision rationale that code, tests, and current docs do not explain; audit findings or removed-code counts alone are not Notes.
- Before a substantial code or PR review where past choices may constrain correctness or compatibility, use `$agent-notes` Retrieve and cite related active Note paths. Compare recorded contracts with current evidence and report mismatches.
- When writing or updating a Note, preserve the problem, decision or proposal, durable contract, actual alternatives and reasons, consequences, and status-appropriate evidence. Keep it concise and omit task chronology.
- Capture only durable rationale not fully expressed in source, tests, or current docs. Keep an open decision `proposed`; finalize it as `implemented` or `rejected` only after delivery or evaluation and relevant evidence. Routine fixes and mechanical edits do not need Notes.
- After adding or moving an active Note, run `python3 .agents/notes/verify_format.py` and report the result.
- When delegating work that creates or maintains Notes, specify the `$agent-notes` operation and require a scoped supersession report.
