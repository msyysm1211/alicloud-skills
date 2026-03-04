#!/usr/bin/env bash
set -euo pipefail

CHANGED_ONLY=0
if [[ "${1:-}" == "--changed-only" ]]; then
  CHANGED_ONLY=1
fi

python3 scripts/guards/check_frontmatter.py --root skills
python3 scripts/guards/check_template_sections.py --root skills --strict-migrated-only
python3 scripts/guards/check_output_paths.py --root skills --strict-migrated-only
python3 scripts/guards/check_openai_yaml.py --root skills
python3 scripts/guards/check_links.py --root skills --root docs
python3 scripts/guards/check_antipatterns.py --root skills
python3 scripts/guards/check_skill_test_coverage.py --skills skills --tests tests --stage legacy

if [[ ${CHANGED_ONLY} -eq 1 ]]; then
  mapfile -t changed_skill_dirs < <(git diff --name-only -- 'skills/**/SKILL.md' | xargs -r -n1 dirname | sort -u)
  for skill_dir in "${changed_skill_dirs[@]}"; do
    python3 scripts/quick_validate.py "${skill_dir}"
  done
fi
