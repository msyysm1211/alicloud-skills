#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

STAGE_MIN = {
    "legacy": 0.49,
    "bronze": 0.60,
    "silver": 0.75,
    "gold": 0.90,
}


def stem_from_skill(path: Path) -> str:
    return path.parent.name


def stem_from_test(path: Path) -> str:
    p = path.parent.name
    return p[:-5] if p.endswith("-test") else p


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skills", default="skills")
    parser.add_argument("--tests", default="tests")
    parser.add_argument("--min", type=float, default=None)
    parser.add_argument("--stage", choices=sorted(STAGE_MIN.keys()), default="legacy")
    args = parser.parse_args()

    min_ratio = args.min if args.min is not None else STAGE_MIN[args.stage]

    skill_stems = {stem_from_skill(p) for p in sorted(Path(args.skills).rglob("SKILL.md"))}
    tested_stems = {stem_from_test(p) for p in sorted(Path(args.tests).rglob("SKILL.md"))}

    covered = sorted(skill_stems & tested_stems)
    missing = sorted(skill_stems - tested_stems)
    ratio = (len(covered) / len(skill_stems)) if skill_stems else 1.0

    print(
        f"skills={len(skill_stems)} tests={len(tested_stems)} covered={len(covered)} "
        f"ratio={ratio:.4f} stage={args.stage} min={min_ratio:.2f}"
    )
    if missing:
        print("Missing tests for:")
        for m in missing:
            print(f"- {m}")

    if ratio + 1e-9 < min_ratio:
        print(f"Coverage check FAILED: ratio {ratio:.4f} < min {min_ratio:.4f}")
        return 1

    print("Coverage check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
