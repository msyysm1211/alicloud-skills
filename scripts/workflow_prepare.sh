#!/usr/bin/env bash
set -euo pipefail

TICKET="${1:-manual}"
DIR="output/workflow/${TICKET}"
mkdir -p "${DIR}"

cat > "${DIR}/plan.md" <<PLAN
# Change Plan (${TICKET})

status: Prepared

## Scope
- Skill governance checks and representative skill migration.

## Risks
- Legacy skills outside migration scope may remain inconsistent.

## Rollback
- Revert changed files in this ticket only.
PLAN

echo "Prepared" > "${DIR}/status.txt"
echo "Created ${DIR}/plan.md"
