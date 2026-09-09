# Review protocol

Use this protocol when a literature interpretation could be distorted by confirmation bias, motivated framing, or pressure to validate the user's position.

## Premise audit

Record the proposition in a form that could be false. Then identify:

- atomic empirical and causal claims;
- ambiguous or evaluative terms;
- assumed population, setting, comparator, mechanism, and time horizon;
- omitted alternatives;
- the result that would count against each claim;
- the evidence that would materially change the assessment.

If the proposition is normative, evaluate its empirical premises separately from its value judgment.

## Symmetric retrieval

Derive searches from concepts rather than from the user's preferred conclusion. Include appropriate variants for:

- the proposed relationship or mechanism;
- null, negative, contradictory, or heterogeneous findings;
- plausible rival mechanisms and confounders;
- replication, preregistration, correction, expression of concern, and retraction;
- broader or narrower populations that test generalizability.

Symmetry means comparable opportunity for relevant evidence to be found. It does not require equal numbers of sources on both sides. Record query strings, databases, dates, filters, and screening rules when the task is a documented review.

## Claim-support labels

| Label | Decision rule |
|---|---|
| `direct` | The source examines the same substantive relationship with sufficiently aligned constructs, population, context, and direction. |
| `partial` | The source supports only part of the claim or a narrower population, mechanism, direction, or scope. |
| `context_only` | The source supplies background but does not test or document the claim. |
| `contradictory` | The source reports a materially different, null, or opposite result relevant to the claim. |
| `unverified` | The relevant text, method, result, or exact source location has not been inspected adequately. |
| `no_citation` | A checkable empirical or historical claim has no supporting source. |

Assess source identity separately from support. A valid citation can still be irrelevant, indirect, or contradictory.

## Evidence comparison

For each important source, record:

- source identifier and exact relevant location;
- study design and whether it can answer the stated question;
- population, setting, sample size when known, exposure or intervention, comparator, and outcome;
- direction, magnitude, and uncertainty of the relevant result;
- measurement validity, attrition, confounding, multiplicity, selective reporting, and conflicts of interest when material;
- directness and support label;
- correction, retraction, or replication status when known.

Do not use a numerical vote count when studies are not sufficiently comparable. Explain why apparently conflicting results may differ before choosing a side.

## Pressure resistance check

Before finalizing, ask:

1. Did the analysis accept any premise merely because the user stated it confidently?
2. Were search terms or inclusion rules tilted toward the preferred answer?
3. Was an unfavorable study held to a stricter standard than a favorable one?
4. Were null results, boundary conditions, or alternative explanations omitted from the synthesis?
5. Did the conclusion become stronger than the designs and measurements allow?
6. Would the verdict remain the same if the user's preferred conclusion were reversed?

Correct any asymmetry found. Do not insert performative disagreement when no asymmetry exists.

## Verdict scale

- `supported`: convergent, sufficiently direct evidence supports the proposition within a stated scope.
- `provisionally supported`: the balance supports it, but important uncertainty or limited directness remains.
- `mixed`: credible evidence differs by method, population, setting, or outcome.
- `unsupported`: available evidence does not establish the proposition; this is not proof of its negation.
- `contradicted`: sufficiently direct evidence materially opposes the proposition.
- `unresolved`: source access, quantity, quality, or comparability is inadequate for a directional conclusion.

State confidence qualitatively and explain its basis. Do not generate precise probabilities unless a defensible model or synthesis supplies them.

## Compact output schema

```text
Proposition:
Scope:
Assumptions and falsifiers:

Claim | Best source/location | Design and fit | Direction | Support label | Main limitation

Strongest supporting case:
Strongest disconfirming case:
Alternative explanations:
Unresolved questions:
Verdict and confidence boundary:
What would change the verdict:
Anti-sycophancy audit:
```
