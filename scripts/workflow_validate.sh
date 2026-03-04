#!/usr/bin/env bash
set -euo pipefail

TICKET="${1:-manual}"
DIR="output/workflow/${TICKET}"
STATUS_FILE="${DIR}/status.txt"

if [[ ! -f "${STATUS_FILE}" ]]; then
  echo "Missing status file. Run workflow_prepare.sh first." >&2
  exit 1
fi

if ! grep -q "Prepared\|Validated" "${STATUS_FILE}"; then
  echo "Invalid status. Current: $(cat "${STATUS_FILE}")" >&2
  exit 1
fi

mkdir -p "${DIR}"
LOG="${DIR}/validate.log"
: > "${LOG}"

run_cmd() {
  echo "$ $*" | tee -a "${LOG}"
  "$@" 2>&1 | tee -a "${LOG}"
}

run_cmd bash scripts/guards/run_all.sh --changed-only
run_cmd python3 -m unittest discover -s tests/guards -p 'test_*.py' -v
before_readme_status="$(git status --porcelain -- README.md README.zh-CN.md README.zh-TW.md)"
run_cmd python3 scripts/generate_skill_index.py
after_readme_status="$(git status --porcelain -- README.md README.zh-CN.md README.zh-TW.md)"
if [[ "${before_readme_status}" != "${after_readme_status}" ]]; then
  echo "README skill index drift detected after generation. Commit regenerated README files." >&2
  git --no-pager diff -- README.md README.zh-CN.md README.zh-TW.md | tee -a "${LOG}"
  exit 1
fi
run_cmd go -C apps test ./...

echo "Validated" > "${STATUS_FILE}"

cat > "${DIR}/validate.md" <<MD
# Validate Report (${TICKET})

status: Validated

- log: ${LOG}
MD

echo "Validation complete: ${DIR}/validate.md"
