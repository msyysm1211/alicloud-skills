#!/usr/bin/env bash
set -euo pipefail

TICKET="${1:-manual}"
DIR="output/workflow/${TICKET}"
STATUS_FILE="${DIR}/status.txt"

if [[ ! -f "${STATUS_FILE}" ]]; then
  echo "Missing status file. Run prepare and validate first." >&2
  exit 1
fi

if ! grep -q "Validated" "${STATUS_FILE}"; then
  echo "Deploy blocked: status is not Validated (current: $(cat "${STATUS_FILE}"))" >&2
  exit 1
fi

cat > "${DIR}/deploy.md" <<MD
# Deploy Summary (${TICKET})

status: DeployReady

actions:
- Governance checks passed in validate stage.
- Ready for PR merge/release.

rollback:
- Revert this ticket's commits.
MD

echo "DeployReady" > "${STATUS_FILE}"
echo "Deploy summary generated: ${DIR}/deploy.md"
