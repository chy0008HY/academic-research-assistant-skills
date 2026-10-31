# ScholarRead alternatives bundle

This new, isolated folder groups four public academic-reading skills without changing the repository's existing `skills/` collection.

## Contents

| Directory | Upstream skill | Integration | License |
|---|---|---|---|
| `paper-reading/` | `techdou/paper-reading` | Reviewed source snapshot | Apache-2.0 |
| `scholarly-deep-research/` | `Tw6249/scholarly-deep-research` | Pinned upstream install descriptor; source is not redistributed here | No license declared upstream |
| `academic-paper-review/` | `bytedance/deer-flow/skills/public/academic-paper-review` | Reviewed source snapshot | MIT (repository license) |
| `deep-paper-reading-skill/` | `Zero-stargazer/deep-paper-reading-skill/skills/deep-paper-reading-skill` | Reviewed source snapshot | MIT |

Exact reviewed revisions and license evidence are recorded in [SOURCES.md](SOURCES.md).

## Install with Codex

Install the three redistributed snapshots independently:

```text
$skill-installer install https://github.com/chy0008HY/academic-research-assistant-skills/tree/main/scholarread-alternatives/paper-reading
$skill-installer install https://github.com/chy0008HY/academic-research-assistant-skills/tree/main/scholarread-alternatives/academic-paper-review
$skill-installer install https://github.com/chy0008HY/academic-research-assistant-skills/tree/main/scholarread-alternatives/deep-paper-reading-skill
```

`scholarly-deep-research` does not currently declare a license. To avoid republishing code without permission, install its reviewed revision directly from the upstream repository:

```text
$skill-installer install https://github.com/Tw6249/scholarly-deep-research/tree/4a77b32c753a1a2789bfdb80e0a41ef74b709df9
```

Start a new Codex turn after installation so the skills are discovered. Review the skill instructions and scripts before use; some workflows make network requests or need separate API credentials.

## Validation

Run the bundle checks from the repository root:

```text
python scholarread-alternatives/tests/validate_bundle.py
```

The validator checks the three redistributed skill packages, required license/notice files, frontmatter names, and the pinned metadata for the non-redistributed skill.
