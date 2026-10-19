#!/usr/bin/env python3
"""Check active Agent Note structure and lifecycle/status agreement."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = {
    "proposed": ("Problem", "Proposal", "Alternatives considered", "Acceptance criteria", "Risks"),
    "implemented": ("Problem", "Decision", "Alternatives considered", "Consequences"),
    "rejected": ("Problem", "Proposal", "Alternatives considered", "Reconsider if"),
}
STATUS = {
    "proposed": re.compile(r"^Status: proposed$"),
    "implemented": re.compile(r"^Status: implemented$"),
    "rejected": re.compile(r"^Status: rejected — .+$"),
}
BANNED_IMPLEMENTED = {"Proposal", "Plan", "Migration plan", "Acceptance criteria"}


def prose_lines(text: str) -> list[str]:
    lines = text.splitlines()
    result: list[str] = []
    in_fence = False
    for line in lines:
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            result.append(line)
    return result


def check(path: Path, lifecycle: str) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    rel = path.as_posix()
    if not lines or not lines[0].startswith("# Agent Note: ") or len(lines[0]) <= len("# Agent Note: "):
        errors.append(f"{rel}: line 1 must be '# Agent Note: <title>'")
    if len(lines) < 4 or lines[1] != "" or lines[3] != "":
        errors.append(f"{rel}: lines 2 and 4 must be blank")
    if len(lines) < 3 or not STATUS[lifecycle].fullmatch(lines[2]):
        errors.append(f"{rel}: line 3 status must match lifecycle '{lifecycle}'")

    prose = prose_lines("\n".join(lines))
    status_lines = [line for line in prose if line.startswith("Status:")]
    if status_lines != ([lines[2]] if len(lines) >= 3 else []):
        errors.append(f"{rel}: the header must contain the only Status line")

    headings = [line[3:].strip() for line in prose if line.startswith("## ")]
    required = REQUIRED[lifecycle]
    if not headings or headings[0] != "Problem":
        errors.append(f"{rel}: the first section must be '## Problem'")
    for heading in required:
        if heading not in headings:
            errors.append(f"{rel}: missing '## {heading}'")
    if lifecycle == "implemented":
        for heading in sorted(BANNED_IMPLEMENTED.intersection(headings)):
            errors.append(f"{rel}: implemented Notes must not retain proposal heading '## {heading}'")
    return errors


def main() -> int:
    notes_root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd() / ".agents/notes"
    if not notes_root.is_dir():
        print(f"agent-notes-format: notes directory not found: {notes_root}", file=sys.stderr)
        return 2

    notes = [
        (path, lifecycle)
        for lifecycle in REQUIRED
        for path in sorted((notes_root / lifecycle).rglob("*.md"))
        if path.is_file()
    ]
    errors: list[str] = []
    for path, lifecycle in notes:
        try:
            errors.extend(check(path, lifecycle))
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path}: cannot read note: {exc}")

    if errors:
        print("agent-notes-format: violations found:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"agent-notes-format: {len(notes)} active Note(s) conform to the format")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
