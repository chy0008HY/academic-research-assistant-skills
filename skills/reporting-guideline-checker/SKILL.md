---
name: reporting-guideline-checker
description: Select and audit research reporting guidelines for manuscripts, protocols, systematic reviews, observational studies, experiments, qualitative studies, mixed methods, prediction models, surveys, and AI studies. Use when checking PRISMA, STROBE, CONSORT, COREQ, SRQR, APA JARS, TRIPOD, CHERRIES, or venue-specific reporting completeness before submission.
---

# Reporting Guideline Checker

## Workflow

1. Identify study design from explicit manuscript evidence. Do not infer a stronger design than reported.
2. Select one primary checklist and only relevant extensions. Read [references/frameworks.md](references/frameworks.md).
3. Record checklist version, official URL, retrieval date, applicability, and target venue requirement.
4. Mark each item `reported`, `partial`, `not_reported`, `not_applicable`, or `unclear` with page or section evidence.
5. Separate missing reporting from flawed methodology. Never label an unreported item as a confirmed error.
6. Produce prioritized revisions and a machine-readable checklist.

## Output Contract

Return study type, selected standard, selection rationale, item-level evidence, major omissions, revision actions, and limitations. Preserve manuscript wording and numbers. Require author confirmation before changing the manuscript.

