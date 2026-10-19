---
name: agent-notes
description: Capture, finalize, retrieve, or maintain durable engineering decision Notes. Use before substantial design, simplification, or code review where past decisions may matter, or when durable rationale needs recording; skip routine fixes and local UI changes.
---

# Agent Notes lifecycle

An Agent Note preserves decision rationale that code, tests, and current documentation do not explain. It is not a log of completed tasks. Follow the project's `.agents/notes/AGENTS.md` and `README.md` when present; the project owns its directory layout, format, and checker.

Choose the operation that matches the request:

## Capture

1. Confirm the choice has lasting value: it affects more than a local implementation detail, carries a meaningful trade-off, or prevents a plausible future mistake.
2. Search active Notes for the same feature, mechanism, API, state, compatibility rule, or rejected alternative. Prefer updating or linking the existing owner to creating a duplicate.
3. Choose `proposed`, `implemented`, or `rejected` based on current reality, then use the project's matching template.
4. Record the problem and evidence, decision or proposal, durable contract or invariant, actual alternatives and why they lost, consequences, and status-appropriate acceptance criteria, verification, or reconsideration conditions. Do not invent alternatives, rationale, or checks.
5. Check only notes that could be superseded by this decision. Report full and partial supersession; keep partial records cross-linked.

Do not create a Note for a routine bug fix, mechanical refactor, small local UI change, temporary task plan, or fact already clear in code, tests, or current docs. A substantial simplification audit may surface a Note candidate; its findings or removed-code count alone are not durable decisions.

## Finalize

Finalize only after the requested implementation is complete and relevant verification has run. Rewrite a shipped proposal as present-tense `implemented/` reality: replace proposal/acceptance-plan headings with the actual decision and consequences, and record checks that were run. If only partly implemented, keep it proposed. If declined, mark it rejected and preserve the evidence for that outcome.

## Retrieve

Before a substantial design choice, simplification, or code/PR review where past decisions may constrain the work, search by subsystem, symbol, data source, API, and rejected alternative. Read only the related active Notes and cite their paths in the reasoning. Use Notes to identify expected contracts and invariants, then compare them with current source, tests, and documentation; report mismatches instead of treating a Note alone as proof of current behavior. Archived Notes are historical context, not authority for current behavior.

When writing or updating a Note, preserve its decision rationale and durable contract in concise prose. Omit task chronology, tool-by-tool narration, and facts already clear from the maintained source of truth.

## Maintain

- A new Note triggers a local supersession check, not an automatic sweep of the whole corpus.
- Keep implemented Notes active while they still guide ownership, compatibility, persistence, security, failure behavior, or reintroduction conditions.
- Archive only a completed implemented decision whose rationale no longer guides future work but still has historical value. Keep archived content frozen and repair active inbound links.
- Keep a rejected Note only while it prevents a plausible mistake; remove obsolete proposals from active status.
- Do not use age, word count, or a cleanup quota as the decision rule. Do not archive or delete unrelated Notes during ordinary feature work.

For exact default headings and the maintenance decision table, read [`references/note-format.md`](references/note-format.md) or [`references/retention-policy.md`](references/retention-policy.md) only as needed. If the project has a Note validator, run its documented command after adding or moving a Note. If no checker exists, inspect the required headings and status/folder agreement manually; do not claim an automated check.
