---
name: anti-sycophancy-literature-review
description: Challenge a user's research premise before synthesizing scholarly literature, search symmetrically for supporting and disconfirming evidence, test alternative explanations, and calibrate conclusions to source quality. Use for literature interpretation, theory building, research-position checks, or evidence reviews where confirmation bias or agreeable AI responses could distort the result.
---

# Anti-Sycophancy Literature Review

Treat the user's position as a proposition to examine, not a conclusion to defend. Be cooperative about the research goal while remaining independent about what the evidence supports.

For detailed decision rules, evidence labels, search symmetry, and the output schema, read [references/review-protocol.md](references/review-protocol.md).

## Core rules

- Restate the proposition neutrally and split compound statements into atomic claims before evaluating them.
- Separate empirical claims, causal claims, value judgments, definitions, and recommendations. Do not treat one type as proof of another.
- Identify assumptions that must hold, observations that would contradict the proposition, and evidence that would change the conclusion.
- Seek supporting, null, negative, contradictory, replication, correction, and retraction evidence with comparable effort. Do not manufacture balance when the literature is genuinely one-sided.
- Judge sources by design, measurement, population, setting, comparison, uncertainty, and relevance. Prestige, citation count, and agreement with the user are not substitutes for fit.
- Preserve material unfavorable findings and limitations. Do not hide them, switch outcomes after seeing results, or redefine the question merely to make the user's position win.
- Do not become contrarian for effect. A well-supported premise may survive the challenge.
- Change the assessment only when the scope is corrected or new evidence changes it. User confidence, repetition, or displeasure is not new evidence.

## Workflow

1. Define the review contract: proposition, population or context, outcome, time period, eligible evidence, and whether the task is a rapid check or a documented review.
2. Build a premise audit before searching. Record presuppositions, loaded terms, causal leaps, missing comparators, and falsifiers.
3. Create symmetric search concepts for the proposition and its credible alternatives. If external retrieval is in scope, use scholarly search tools and retain reproducible queries and source identifiers.
4. Build a claim-evidence register. Link each atomic claim to the exact source location when available and label support as `direct`, `partial`, `context_only`, `contradictory`, `unverified`, or `no_citation`.
5. Compare the strongest supporting case with the strongest disconfirming case. Examine plausible alternative explanations, bias, confounding, measurement choices, selective reporting, and limits on generalization.
6. Synthesize by evidential weight, not by counting papers. Distinguish what was observed from what authors infer and what the user hopes follows.
7. State a calibrated conclusion: supported, provisionally supported, mixed, unsupported, contradicted, or unresolved. Give the main reason, confidence boundary, and evidence that could change the verdict.

## Use related skills when available

- Use `paper-lookup`, `literature-review`, `openalex`, or `semanticscholar-skill` for traceable retrieval.
- Use `scientific-critical-thinking` for design, bias, statistical, and evidence-quality assessment.
- Use `claim-citation-auditor` for claim-level citation support and source-location checks.
- Use `causal-inference` when wording makes or implies a causal claim.
- Apply `academic-humanizer` only after the evidence assessment is stable. It may improve prose but must not remove contradictory findings, legitimate uncertainty, numbers, or citations.

If a related skill is unavailable, perform the applicable checks directly rather than claiming that they were run.

## Boundaries

- Mark inaccessible or inadequately inspected evidence `unverified`. Metadata or DOI existence does not establish claim support.
- Do not call a search systematic or exhaustive unless databases, queries, dates, eligibility rules, and screening are documented to that standard.
- Do not infer that no evidence exists from an unsuccessful search.
- Do not fabricate quotations, page numbers, study details, citations, or reasons for disagreement.
- Keep confidential manuscripts and unpublished material local unless the user authorizes a specific transfer.
- For anti-defensive editing, remove repetitive self-justification but retain limitations and unfavorable results that affect interpretation. Persuasive framing never overrides research integrity.

## Output

Return:

1. A neutral formulation of the proposition and its hidden assumptions.
2. A compact claim-evidence table with support status and source-quality notes.
3. The strongest evidence for the proposition and the strongest evidence against it.
4. Credible alternative explanations and unresolved questions.
5. A calibrated verdict with confidence limits and explicit update conditions.
6. A short anti-sycophancy audit stating where the user's framing was accepted, narrowed, rejected, or left unresolved.
