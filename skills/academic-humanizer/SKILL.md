---
name: academic-humanizer
description: |
  Improve the clarity and voice of AI-assisted academic writing (papers, theses, rebuttals) and
  funding proposals: preserve scholarly conventions, match claims to evidence, and match the
  author's own voice. It never changes a number, result, or citation, and it is not for evading
  AI-use disclosure. Use when editing AI-assisted academic prose or grant proposals.
---

# Academic Humanizer

For upstream source, license, and local adaptations, read [references/provenance.md](references/provenance.md).

Improve the clarity and voice of AI-assisted academic writing while keeping the precise,
evidence-bound voice that scholarship requires and matching the author's own style. Preserve every
number, result, and citation. Do not use this tool to evade AI-use disclosure.

## When to use

Use for papers, theses, abstracts, related work, rebuttals, and funding proposals. Do not inject
opinion, humor, or casual first-person personality into a manuscript. Neutral and precise is the
appropriate human voice for technical and academic writing.

## Core principle

Academic writing already has a correct human voice: neutral, precise, and evidence-bound. Remove
formulaic AI patterns without casualizing the text. Every claim must earn its number, figure, table,
or citation, and no verb may be stronger than its evidence.

## Process

1. Read the manuscript, target venue, and any author writing sample.
2. Audit before editing: identify patterns, locations, proposed fixes, and empirical claims whose
   evidence is absent or too weak.
3. Rewrite without changing structure or meaning. Preserve all citations, numbers, equations,
   results, and legitimate hedging.
4. Return the revised text and a short change report. Confirm that no number, equation, result, or
   citation was altered.

## General AI-writing patterns

Remove or revise:

- Inflated significance such as “pivotal”, “groundbreaking”, or “revolutionary”.
- Superficial participial endings that claim insight without evidence.
- Promotional or figurative language such as “rich tapestry” or “vibrant landscape”.
- Vague attributions such as “experts argue” without a citation.
- Formulaic vocabulary used as filler: delve, underscore, intricate, tapestry, testament,
  landscape, pivotal, showcase, foster, leverage, realm, seamless.
- Copula avoidance such as “serves as” where “is” is clearer.
- “Not only X but also Y” padding and artificial lists of three.
- Cycling synonyms for the same technical referent.
- Filler such as “it is worth noting that” and “in order to”.
- Clause-stacked sentences longer than roughly 30 words when they contain several subordinate ideas.
- Repetitive em dashes; recast with commas, colons, parentheses, or separate sentences.

## Academic-specific checks

### Match verbs to evidence

Empirical studies provide evidence; they rarely prove universal truths. Flag “prove”, “establish”,
“confirm”, “guarantee”, and “significantly” when the text does not provide the relevant design,
test, number, or scope.

### Replace significance hype

Replace “paves the way”, “opens new avenues”, “sheds light on”, “bridges the gap”, and similar
phrases with the specific problem, comparison, limitation, or contribution.

### Replace empty scale words

Replace “extensive”, “comprehensive”, “numerous”, “various”, and “a wide range” with actual counts,
datasets, methods, or conditions when the evidence is supplied. Never invent the missing count.

### Remove novelty padding

Do not repeat “novel”, “for the first time”, or “to the best of our knowledge”. State the exact
difference from prior research and cite it.

### Remove formulaic openings

Avoid “In recent years…”, “With the rapid development of…”, and generic “Despite recent advances…”
openers. Begin with the concrete empirical or theoretical problem.

### Control connective overuse

Do not begin consecutive sentences with Moreover, Furthermore, Additionally, and In particular.
Let the logical relation or paragraph structure carry the transition.

### Make contributions specific

Each contribution must name a method, result, dataset, boundary condition, or released artifact.
Do not use “novel method”, “extensive experiments”, and “strong results” as contribution items.

### Avoid citation dumping

Identify the one or two works that matter most and explain their relation to the current claim.
Preserve all existing citations unless the author explicitly authorizes changes.

### Preserve legitimate hedging

Keep “suggests”, “is consistent with”, “may indicate”, “appears to”, and “we hypothesize” when the
design or evidence is uncertain. Never strengthen “suggests” to “proves”. Passive voice is acceptable
when the actor is irrelevant. First-person plural “we” is standard scholarly usage.

### Protect technical content

Formal definitions, named methods, metrics, technical terms, equations, symbols, cite keys, numbers,
and results must remain verbatim unless the author supplies a correction.

## Claim–evidence discipline

For every empirical claim, ask:

1. Is it supported by a number, figure, table, quoted finding, or citation in the supplied material?
2. Does the verb match the study design and strength of evidence?
3. Is the scope limited to the actual sample, datasets, period, context, and measures?
4. Is a causal statement supported by a design capable of causal identification?

If evidence is missing, add a visible evidence-needed marker or soften the claim. Never invent a
number, citation, comparison, source, dataset, participant characteristic, result, or limitation.

## Voice and venue matching

When the author supplies prior writing, identify sentence rhythm, connective habits, preferred
hedging, paragraph openings, notation, terminology, and recurring phrasing. Match these traits without
copying distinctive passages. Also match the target venue's register. Without a sample, default to
clear, precise, venue-appropriate prose rather than casual “humanized” prose.

For this research assistant, preserve Traditional Chinese when the draft uses Traditional Chinese.
Do not convert terminology to Simplified Chinese. Maintain consistent translations for constructs,
methods, journal names, and statistical terms throughout a manuscript.

## Output

Return:

1. The revised passage with the same factual content and citation coverage.
2. A short change report listing removed patterns, softened overclaims, evidence pointers added, and
   voice or venue adjustments.
3. A preservation statement confirming that numbers, equations, results, and citations were not altered.
