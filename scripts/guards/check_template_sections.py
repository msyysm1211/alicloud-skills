#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

from _common import check_required_sections, iter_skill_docs, load_migrated_skills

REQUIRED_SECTIONS = [
    "Validation",
    "Output And Evidence",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="skills")
    parser.add_argument("--strict-migrated-only", action="store_true")
    parser.add_argument("--migrated-list", default="docs/standards/migrated-skills.txt")
    args = parser.parse_args()

    migrated = load_migrated_skills(Path(args.migrated_list))

    failures = []
    warnings = []

    for doc in iter_skill_docs(Path(args.root)):
        rel = doc.path.as_posix()
        ok, missing = check_required_sections(doc.text, REQUIRED_SECTIONS)
        if ok:
            continue

        if args.strict_migrated_only and rel not in migrated:
            warnings.append(f"{rel}: missing sections {missing}")
            continue

        failures.append(f"{rel}: missing sections {missing}")

    for w in warnings:
        print(f"WARN: {w}")

    if failures:
        print("Template section check FAILED:")
        for f in failures:
            print(f"- {f}")
        return 1

    print("Template section check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
