#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

from _common import expected_output_slug, iter_skill_docs, load_migrated_skills, mentioned_output_slugs


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
        expected = expected_output_slug(doc)
        slugs = mentioned_output_slugs(doc.text)
        if not slugs:
            continue

        wrong = sorted(s for s in slugs if s != expected)
        if not wrong:
            continue

        msg = f"{rel}: expected output/{expected}/ but found output paths for {wrong}"
        if args.strict_migrated_only and rel not in migrated:
            warnings.append(msg)
        else:
            failures.append(msg)

    for w in warnings:
        print(f"WARN: {w}")

    if failures:
        print("Output path check FAILED:")
        for f in failures:
            print(f"- {f}")
        return 1

    print("Output path check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
