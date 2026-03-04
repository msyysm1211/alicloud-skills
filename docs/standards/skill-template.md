# SKILL.md Template (Skill-Creator Aligned)

This template is the minimum standard for new or migrated skills in this repository.

## Frontmatter (required)

```yaml
---
name: <skill-name-kebab-case>
description: <one-line trigger sentence with explicit "Use when ...">
---
```

Rules:
- Keep frontmatter minimal: only `name` and `description`.
- Put trigger logic in `description` (not in a separate "When to use" body section).

## Body Template (required sections for migrated skills)

```markdown
# <Skill Title>

## Validation
- Provide one minimal executable command.
- Write validation evidence to `output/<skill-name>/`.

## Output And Evidence
- Define artifact path and what evidence must be saved.

## Workflow
- Keep actionable operational steps.

## References
- Keep local references and official sources.
```

## Migration Scope in This Iteration

See `docs/standards/migrated-skills.txt`.

## Migration Notes

- Do not remove existing domain knowledge sections.
- Add required sections with minimal, executable validation commands first.
- Keep SKILL body concise; move deep details to `references/` as needed.
