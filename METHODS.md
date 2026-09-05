# Publication and measurement policy

## Purpose

Groove Scope Measurements is a curated public archive created by Michelangelo Canonico and Direct Sound Records. Its purpose is to document real playback-system measurements in a transparent and reusable form, not to manufacture league tables from incomparable systems.

## Record identity

Every session receives an immutable identifier in the form `GS-YYYY-NNNN`. The identifier never changes, even if metadata is corrected. A corrected record receives a new `record_version` and an explanatory changelog entry.

## Publication status

- `draft`: data preserved, but required metadata or verification is incomplete.
- `published`: required metadata and provenance checks are complete.
- `superseded`: a later analysis or corrected record replaces the interpretation; the old record remains available.
- `withdrawn`: retained for transparency but excluded from normal comparison because of a documented validity problem.

## Software and method changes

Groove Scope may change its calculations, filters, confidence rules, labels, report layout, or supported tests. Every future record should store both:

- `application_version`: the user-facing Groove Scope release;
- `analysis_method_version`: the internal version of the relevant measurement algorithm.

A later application version must not silently rewrite a historical result. Reanalysis should create a new analysis record or a new record version while preserving the original PDF and values.

## Minimum metadata for a published record

A final public record should identify the turntable, tonearm, cartridge/stylus, tracking force, anti-skate, alignment, phono stage, cartridge loading, test record and track, interface and gain, sample rate, Groove Scope version, analysis-method version, measurement date, and repeat count.

When information is genuinely unavailable, use `not_recorded`. Never infer a model or setting merely because it seems likely.

## Measurement-chain presentation

Published pages show verified hardware in signal order on one continuous horizontal line. On narrow screens, the line remains intact and becomes horizontally scrollable rather than wrapping into rows.

Include a preamplifier or phono stage only when its identity is explicitly supplied or present in the source evidence. If a different measurement method bypasses that component, or its identity is not verified, omit the component from the visual chain rather than inventing a placeholder. The same rule applies to every optional stage, so future chains may contain different numbers of elements without changing the presentation pattern.

## Editorial review summaries

Every measurement page should use its highlighted editorial panel to summarise the review, not to lead with a warning or defensive disclaimer. Begin with the strongest relevant measured outcomes, explain what the combined evidence says about the playback chain, and give the reader a constructive next comparison when the data contains variation or tension.

Keep the tone positive, neutral, and evidence-led. Do not hide contradictions, reliability classifications, or missing context; retain those details in the technical record and diagnostic labels. In the review summary, present them as useful context or an opportunity to extend the measurement rather than as a reason to dismiss the result. Avoid unsupported product claims, rankings, or audibility conclusions.

When a review compares a measured result with an external benchmark, use a primary source such as the manufacturer's current manual or an applicable published standard and link it directly. Compare the same metric, frequency, unit, and channel convention. Name the component most clearly illuminated by the result—for example, cartridge separation and output balance—while identifying the value as an in-system measurement when the full playback chain contributes to it.

## Repetition and interpretation

Speed and rotational-stability results may be stable within a capture, while channel-specific distortion, harmonic, balance, and directional crosstalk measurements can vary. The classification supplied by Groove Scope must be retained in the record, and variable diagnostics should be repeated before mechanical adjustment.

## Raw audio

Raw audio is not included by default. Derived data, metadata, short visualisations, and generated reports are generally sufficient for public comparison. Do not publish audio copied from a commercial test record unless the necessary rights or permission are confirmed.

## Corrections

Corrections should be made through a documented commit. The commit message should name the measurement ID and the reason, for example:

`Correct cartridge loading metadata for GS-YYYY-NNNN`

Numerical values transcribed from a report should only be changed when the source report was transcribed incorrectly. If the algorithm itself changes, preserve the original and publish a new analysis version.
