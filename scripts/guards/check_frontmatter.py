#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

from _common import iter_skill_docs

REQUIRED = ["name", "description"]
ALLOWED = set(REQUIRED)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="skills")
    parser.add_argument("--strict-no-extra", action="store_true", default=True)
    args = parser.parse_args()

    failures = []
    for doc in iter_skill_docs(Path(args.root)):
        fm = doc.frontmatter
        rel = doc.path.as_posix()

        missing = [k for k in REQUIRED if not fm.get(k)]
        if missing:
            failures.append(f"{rel}: missing required frontmatter {missing}")

        if args.strict_no_extra:
            extras = [k for k in fm.keys() if k not in ALLOWED]
            if extras:
                failures.append(f"{rel}: unsupported frontmatter keys {extras}")

    if failures:
        print("Frontmatter check FAILED:")
        for f in failures:
            print(f"- {f}")
        return 1

    print(f"Frontmatter check passed ({len(iter_skill_docs(Path(args.root)))} skills scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
