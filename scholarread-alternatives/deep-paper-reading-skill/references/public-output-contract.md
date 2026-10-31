# Public Output Contract

This reference documents the public output shape for `deep-paper-reading-skill`.

Keep this contract simple and auditable. It should help another agent produce consistent files without exposing private scoring weights or prompt chains.

## Required files

- `deep_reading_report.md`
- `claim_evidence_matrix.md`
- `figure_table_review.md`
- `advisor_questions.md`
- `verification_checklist.md`
- `handoff_to_group_meeting.md`
- `handoff_to_group_meeting.json`

## Required distinctions

Every report must distinguish:

- author-stated claim;
- evidence shown in the provided material;
- reader inference;
- original-paper verification needed.

## Support labels

Use qualitative labels only:

- `Strongly supported`
- `Partially supported`
- `Weakly supported`
- `Unclear from provided material`

Do not include numeric weights, hidden thresholds, or private chain-of-thought instructions.
