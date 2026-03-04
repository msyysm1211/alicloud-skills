#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Dict, List, Sequence, Set, Tuple

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
OUTPUT_PATH_RE = re.compile(r"output/([a-z0-9][a-z0-9-]*)/")


@dataclass
class SkillDoc:
    path: Path
    text: str
    frontmatter: Dict[str, str]


def iter_skill_docs(root: Path) -> List[SkillDoc]:
    docs: List[SkillDoc] = []
    for path in sorted(root.rglob("SKILL.md")):
        text = path.read_text(encoding="utf-8")
        docs.append(SkillDoc(path=path, text=text, frontmatter=parse_frontmatter(text)))
    return docs


def parse_frontmatter(text: str) -> Dict[str, str]:
    m = FRONTMATTER_RE.search(text)
    if not m:
        return {}
    data: Dict[str, str] = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip().strip('"').strip("'")
    return data


def parse_markdown_links(text: str) -> List[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def is_external_link(link: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", link))


def check_required_sections(text: str, required: Sequence[str]) -> Tuple[bool, List[str]]:
    missing = []
    lower_text = text.lower()
    for section in required:
        if f"## {section.lower()}" not in lower_text:
            missing.append(section)
    return (len(missing) == 0, missing)


def load_migrated_skills(path: Path) -> Set[str]:
    if not path.exists():
        return set()
    out: Set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        out.add(line)
    return out


def expected_output_slug(doc: SkillDoc) -> str:
    return doc.frontmatter.get("name") or doc.path.parent.name


def mentioned_output_slugs(text: str) -> Set[str]:
    return set(OUTPUT_PATH_RE.findall(text))
