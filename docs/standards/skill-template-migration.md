# SKILL Template Migration Notes (2026-03-03)

## Goal

Align representative skills with `skill-creator` principles:
- minimal frontmatter (`name`, `description`)
- explicit validation command
- explicit output/evidence contract

## Mandatory Additions in This Batch

- `## Validation`
- `## Output And Evidence`
- migration scope source: `docs/standards/migrated-skills.txt`

## Strategy

1. Keep existing capability and workflow content unchanged.
2. Add validation commands that are executable in local environments.
3. Require evidence under `output/<skill-name>/`.
4. Enforce strict checks only for migrated skills in this batch.

## Rollback

- Revert only files in this migration batch.
- `scripts/guards/` checks are isolated and can be disabled independently.
