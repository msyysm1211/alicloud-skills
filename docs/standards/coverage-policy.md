# Skill Test Coverage Policy

Coverage stages for `scripts/guards/check_skill_test_coverage.py`:

- `legacy`: 0.49 (current baseline)
- `bronze`: 0.60
- `silver`: 0.75
- `gold`: 0.90

Usage:

```bash
python3 scripts/guards/check_skill_test_coverage.py --stage legacy
python3 scripts/guards/check_skill_test_coverage.py --stage bronze
```

Recommended rollout:

1. Keep CI on `legacy` until missing tests are added.
2. Raise to `bronze` after ratio >= 0.60.
3. Raise to `silver` and `gold` with migration milestones.
