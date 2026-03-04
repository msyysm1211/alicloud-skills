#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys

BLOCK_PATTERNS = {
    "destructive_git_reset": re.compile(r"git\s+reset\s+--hard"),
    "destructive_git_checkout": re.compile(r"git\s+checkout\s+--"),
    "dangerous_rm_root": re.compile(r"rm\s+-rf\s+/(\s|$)"),
    "pipe_to_shell": re.compile(r"curl\b[^\n|]*\|\s*(bash|sh)\b"),
    "disk_format": re.compile(r"\bmkfs\b"),
}


@dataclass(frozen=True)
class RuleAllowance:
    path: str
    rule: str | None
    line: int | None


def parse_allowlist(path: Path) -> set[RuleAllowance]:
    out: set[RuleAllowance] = set()
    if not path.exists():
        return out

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        rule = None
        loc = line
        if "#" in line:
            loc, rule = line.split("#", 1)
            loc = loc.strip()
            rule = rule.strip() or None

        lineno = None
        path_part = loc
        if ":" in loc:
            maybe_path, maybe_line = loc.rsplit(":", 1)
            if maybe_line.isdigit():
                path_part = maybe_path
                lineno = int(maybe_line)

        out.add(RuleAllowance(path=path_part, rule=rule, line=lineno))
    return out


def is_allowed(allow: set[RuleAllowance], rel: str, rule: str, line: int) -> bool:
    for item in allow:
        if item.path != rel:
            continue
        if item.rule is not None and item.rule != rule:
            continue
        if item.line is not None and item.line != line:
            continue
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="skills")
    parser.add_argument("--allowlist", default="scripts/guards/antipattern_allowlist.txt")
    args = parser.parse_args()

    allowlist = parse_allowlist(Path(args.allowlist))

    failures = []
    for path in sorted(Path(args.root).rglob("SKILL.md")):
        rel = path.as_posix()
        text = path.read_text(encoding="utf-8")
        for name, pat in BLOCK_PATTERNS.items():
            for m in pat.finditer(text):
                line_no = text.count("\n", 0, m.start()) + 1
                if is_allowed(allowlist, rel, name, line_no):
                    continue
                failures.append(f"{rel}:{line_no}: matched anti-pattern [{name}]")

    if failures:
        print("Anti-pattern check FAILED:")
        for f in failures:
            print(f"- {f}")
        return 1

    print("Anti-pattern check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
