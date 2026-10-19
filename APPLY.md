# Apply Agent Notes Kit to a project

Use this file when a user gives an agent this repository URL and asks to apply the workflow to the current project.

## Guard the target project

1. Identify the target repository root and read its existing root and subtree `AGENTS.md` files, `.agents/notes/README.md`, and Note-related Skills.
2. Inspect `git status --short` and existing Note files. Preserve all pre-existing edits, untracked files, Notes, templates, and local policies.
3. Do not clone this kit inside the target repository as a nested repository or submodule. Use its contents as source files.

## Project installation

Merge these components into the target project:

- `.agents/skills/agent-notes/` into the target's `.agents/skills/agent-notes/`.
- `.agents/notes/AGENTS.md` and `.agents/notes/README.md` into the target Notes folder, preserving its current rules and vocabulary.
- `.agents/notes/templates/` only for missing lifecycle templates; never replace existing templates without comparing them.
- `.agents/notes/verify_format.py` if the target has no compatible Note validator.
- The applicable conditional Note workflow rules from this repo's root `AGENTS.md` into the target root instructions. Preserve the project's existing rules; this Note workflow does not depend on installing separate audit, review, or prose Skills.

If the target already has a Note schema, validator, lifecycle folders, or same-name Skill, stop before overwriting it. Compare the two designs and report the exact conflict and a merge proposal.

Do not create a Note during installation. Do not move, archive, or delete existing Notes. Do not change product code, build configuration, or CI unless the user separately requests those changes.

After merging, run the target's documented checker. If it uses this kit's checker, run `python3 .agents/notes/verify_format.py` from the target project root. Report the exact files changed, check result, and any remaining manual merge.

## Global Codex installation

Only when the user asks for a global Skill, install the single directory `.agents/skills/agent-notes/` into `~/.codex/skills/agent-notes/` or `$CODEX_HOME/skills/agent-notes/`. Keep project Notes, templates, and project rules in each repository. Do not copy project-specific Notes into global storage.

For Codex, the built-in `$skill-installer` can install this Skill directly from:

```text
https://github.com/fish5257/agent-notes-kit/tree/main/.agents/skills/agent-notes
```

## Root AGENTS triggers

Use the conditional rules in this repository's root `AGENTS.md` as the source for project-level routing. Merge the applicable bullets into the target project's root `AGENTS.md`; do not replace its existing instructions.
