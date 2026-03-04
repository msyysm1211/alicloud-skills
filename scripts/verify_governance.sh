#!/usr/bin/env bash
set -euo pipefail

bash scripts/guards/run_all.sh --changed-only
python3 -m unittest discover -s tests/guards -p 'test_*.py' -v
before_readme_status="$(git status --porcelain -- README.md README.zh-CN.md README.zh-TW.md)"
python3 scripts/generate_skill_index.py
after_readme_status="$(git status --porcelain -- README.md README.zh-CN.md README.zh-TW.md)"
if [[ "${before_readme_status}" != "${after_readme_status}" ]]; then
  echo "README skill index drift detected after generation. Commit regenerated README files." >&2
  git --no-pager diff -- README.md README.zh-CN.md README.zh-TW.md
  exit 1
fi

go -C apps test ./...
