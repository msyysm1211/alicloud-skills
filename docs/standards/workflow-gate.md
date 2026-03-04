# Cross-Skill Workflow Gate (prepare -> validate -> deploy)

## State Machine

1. `prepare`
- Create `output/workflow/<ticket>/plan.md`.
- Status -> `Prepared`.

2. `validate`
- Run governance checks, guard tests, index generation, Go tests.
- Verify generated files are committed.
- Status -> `Validated`.

3. `deploy`
- Allowed only when status is `Validated`.
- Generate deploy summary.
- Status -> `DeployReady`.

## Local Commands

```bash
bash scripts/workflow_prepare.sh <ticket>
bash scripts/workflow_validate.sh <ticket>
bash scripts/workflow_deploy.sh <ticket>
```
