# Academic Research Assistant Skills

Nineteen Agent Skills selected or created for the Academic Research Assistant workflow: nine traceable upstream snapshots and ten project-authored 4.7–4.10 research-rigor skills.

## Included skills

| Skill | Upstream | Purpose |
|---|---|---|
| `openalex` | `yy/claude-scholar` | Literature and bibliometric search through OpenAlex |
| `doi-bibtex` | `yy/claude-scholar` | Retrieve BibTeX records from DOI identifiers |
| `check-refs` | `yy/claude-scholar` | Validate manuscript references against scholarly databases |
| `semanticscholar-skill` | `Agents365-ai/semanticscholar-skill` | Semantic Scholar search and citation-graph traversal |
| `scientific-critical-thinking` | `K-Dense-AI/scientific-agent-skills` | Evidence-bounded scientific reasoning |
| `peer-review` | `K-Dense-AI/scientific-agent-skills` | Structured scholarly peer review |
| `paper-lookup` | `K-Dense-AI/scientific-agent-skills` | Multi-database scholarly paper lookup |
| `literature-review` | `K-Dense-AI/scientific-agent-skills` | Systematic literature review workflow |
| `statistical-analysis` | `K-Dense-AI/scientific-agent-skills` | Statistical analysis and reporting workflow |

## Project-authored 4.7–4.10 skills

| Phase | Skill | Purpose |
|---|---|---|
| 4.7 | `reporting-guideline-checker` | Select and audit design-appropriate reporting guidelines |
| 4.7 | `claim-citation-auditor` | Check whether cited evidence supports manuscript claims |
| 4.8 | `research-design-measurement` | Align questions, constructs, sampling and measurement quality |
| 4.8 | `causal-inference` | Audit estimands, identification assumptions and causal language |
| 4.8 | `qualitative-mixed-methods` | Audit qualitative rigor and mixed-method integration |
| 4.9 | `research-data-quality` | Build data dictionaries and research-data quality gates |
| 4.9 | `reproducibility-open-science` | Record preregistration, provenance and reproducibility manifests |
| 4.10 | `journal-fit-submission` | Evaluate venue fit from official, dated policies |
| 4.10 | `publication-ethics-ai-compliance` | Audit publication ethics and AI disclosure requirements |
| 4.10 | `submission-package-builder` | Assemble and cross-check human-approved submission packages |

These ten skills were created for this research assistant. They are evidence-bounded: they do not guarantee acceptance, invent study evidence, certify compliance, or submit manuscripts automatically.

## Installation

Install a skill by pointing Codex's `skill-installer` at its directory in this repository. For example:

```text
$skill-installer install https://github.com/chy0008HY/academic-research-assistant-skills/tree/main/skills/openalex
```

Restart Codex or start a new turn after installation so the newly installed skills are discovered.

## Provenance

This repository is a redistribution snapshot, not the canonical upstream source. See [UPSTREAM.md](UPSTREAM.md) for source revisions and update guidance. Preserve upstream notices and review every skill and script before use. Some skills call third-party APIs or require separate credentials and dependencies.

## Licensing

The bundled work remains subject to its upstream license and any per-skill metadata. Copies of the upstream repository licenses are included under [`THIRD_PARTY_LICENSES/`](THIRD_PARTY_LICENSES/). No additional license is asserted over upstream content.
