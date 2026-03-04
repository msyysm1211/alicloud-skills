#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

from _common import is_external_link, parse_markdown_links


def scan_markdown(root: Path):
    for path in sorted(root.rglob("*.md")):
        yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", action="append", default=["skills"])
    args = parser.parse_args()

    failures = []
    for r in args.root:
        root = Path(r)
        if not root.exists():
            continue
        for md in scan_markdown(root):
            text = md.read_text(encoding="utf-8")
            for link in parse_markdown_links(text):
                link = link.strip()
                if not link or link.startswith("#") or is_external_link(link) or link.startswith("mailto:"):
                    continue
                candidate = (md.parent / link.split("#", 1)[0]).resolve()
                if not candidate.exists():
                    failures.append(f"{md.as_posix()}: broken link -> {link}")

    if failures:
        print("Link check FAILED:")
        for f in failures:
            print(f"- {f}")
        return 1

    print("Link check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
