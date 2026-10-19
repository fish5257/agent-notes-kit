# Agent Notes instructions

- Notes are durable decision records, not task logs. Do not create one for a routine fix, local UI adjustment, or fact already carried by code, tests, or existing documentation.
- Before adding a Note, search active Notes for the same decision, mechanism, API, state, or rejected alternative. Update the existing owner where possible.
- Every new Note triggers a scoped supersession check. Classify direct full and partial supersession; cross-link partial supersession. Do not turn this check into an unrelated corpus cleanup.
- Keep alternatives grounded in evidence; never invent a rationale that the record cannot support.
- `proposed/` means not fully shipped. After implementation and relevant verification, rewrite it as present-tense `implemented/`; if declined, mark `rejected/` with the reason.
- Archive only a completed implemented decision whose rationale no longer guides current work but still has historical value. Rejected Notes stay only while they prevent a plausible mistake. Archived Notes are frozen and never current authority.
- Read the relevant Note before a substantial design choice or review. Search by feature, symbol, and mechanism; do not load the whole Notes tree for a narrow task.
- Run `python3 .agents/notes/verify_format.py` after adding or moving a Note. It checks active Note structure and lifecycle folder/status agreement; it does not validate the technical decision.
