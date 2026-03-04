#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    out: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Quickly validate one skill folder")
    parser.add_argument("skill_dir")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        print(f"FAILED: missing {skill_md}")
        return 1

    fm = parse_frontmatter(skill_md)
    failures = []

    name = fm.get("name", "")
    desc = fm.get("description", "")
    if not name:
        failures.append("frontmatter missing name")
    elif not NAME_RE.match(name):
        failures.append(f"invalid skill name: {name}")
    if not desc:
        failures.append("frontmatter missing description")

    if not (skill_dir / "agents" / "openai.yaml").exists():
        failures.append("missing agents/openai.yaml")

    text = skill_md.read_text(encoding="utf-8")
    for section in ("## Validation", "## Output And Evidence"):
        if section not in text:
            failures.append(f"missing required section {section}")

    if failures:
        print("Quick validate FAILED:")
        for f in failures:
            print(f"- {f}")
        return 1

    print(f"Quick validate passed: {skill_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
