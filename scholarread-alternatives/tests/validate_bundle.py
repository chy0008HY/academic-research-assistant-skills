#!/usr/bin/env python3
"""Validate the isolated ScholarRead alternatives bundle without network access."""

from __future__ import annotations

import json
import re
from pathlib import Path


BUNDLE = Path(__file__).resolve().parents[1]

SNAPSHOTS = {
    "paper-reading": {
        "name": "paper-reading",
        "required": ("LICENSE", "NOTICE.md"),
    },
    "academic-paper-review": {
        "name": "academic-paper-review",
        "required": ("LICENSE",),
    },
    "deep-paper-reading-skill": {
        "name": "deep-paper-reading-skill",
        "required": ("LICENSE",),
    },
}


def frontmatter_name(skill_file: Path) -> str:
    text = skill_file.read_text(encoding="utf-8-sig")
    if not text.startswith("---"):
        raise AssertionError(f"missing YAML frontmatter: {skill_file}")
    match = re.search(r"(?m)^name:\s*[\"']?([^\"'\n]+)", text)
    if not match:
        raise AssertionError(f"missing frontmatter name: {skill_file}")
    return match.group(1).strip()


def main() -> None:
    assert (BUNDLE / "README.md").is_file()
    assert (BUNDLE / "SOURCES.md").is_file()

    for directory, metadata in SNAPSHOTS.items():
        root = BUNDLE / directory
        skill_file = root / "SKILL.md"
        assert skill_file.is_file(), f"missing {skill_file}"
        actual_name = frontmatter_name(skill_file)
        assert actual_name == metadata["name"], (
            f"unexpected skill name in {skill_file}: {actual_name!r}"
        )
        for required in metadata["required"]:
            assert (root / required).is_file(), f"missing {root / required}"

    descriptor_dir = BUNDLE / "scholarly-deep-research"
    descriptor = json.loads((descriptor_dir / "upstream.json").read_text(encoding="utf-8"))
    assert descriptor["redistributed"] is False
    assert descriptor["license"] is None
    assert re.fullmatch(r"[0-9a-f]{40}", descriptor["revision"])
    assert not (descriptor_dir / "SKILL.md").exists(), (
        "unlicensed upstream source must not be redistributed"
    )

    print("PASS: ScholarRead alternatives bundle structure and license guards are valid")


if __name__ == "__main__":
    main()
