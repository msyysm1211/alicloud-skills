#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

from _common import iter_skill_docs

REQUIRED_KEYS = ["display_name", "short_description", "default_prompt"]


def parse_openai_yaml(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    out: dict[str, str] = {}
    for key in REQUIRED_KEYS:
        m = re.search(rf"^\s*{re.escape(key)}:\s*\"?(.*?)\"?\s*$", text, flags=re.MULTILINE)
        if m:
            out[key] = m.group(1).strip()
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="skills")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    failures = []
    warnings = []

    for doc in iter_skill_docs(Path(args.root)):
        skill_dir = doc.path.parent
        rel = doc.path.as_posix()
        yaml_path = skill_dir / "agents" / "openai.yaml"
        if not yaml_path.exists():
            msg = f"{rel}: missing agents/openai.yaml"
            if args.strict:
                failures.append(msg)
            else:
                warnings.append(msg)
            continue

        data = parse_openai_yaml(yaml_path)
        missing = [k for k in REQUIRED_KEYS if not data.get(k)]
        if missing:
            failures.append(f"{yaml_path.as_posix()}: missing keys {missing}")

        name = doc.frontmatter.get("name", skill_dir.name)
        prompt = data.get("default_prompt", "")
        if name and name not in prompt:
            warnings.append(
                f"{yaml_path.as_posix()}: default_prompt does not mention skill name `{name}`"
            )

    for w in warnings:
        print(f"WARN: {w}")

    if failures:
        print("OpenAI YAML check FAILED:")
        for f in failures:
            print(f"- {f}")
        return 1

    print("OpenAI YAML check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
