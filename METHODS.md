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

Historical captures made before this publication policy was established may be published as archival observations when unavailable fields are explicitly recorded as `not_recorded`, the source report and provenance are preserved, and the record clearly limits any result that requires repetition or missing context. Such publication makes the observation citable; it does not upgrade incomplete diagnostics into reference-quality evidence.

## Repetition and interpretation

Speed and rotational-stability results may be stable within a capture, while channel-specific distortion, harmonic, balance, and directional crosstalk measurements can vary. The classification supplied by Groove Scope must be retained in the record, and variable diagnostics should be repeated before mechanical adjustment.

## Raw audio

Raw audio is not included by default. Derived data, metadata, short visualisations, and generated reports are generally sufficient for public comparison. Do not publish audio copied from a commercial test record unless the necessary rights or permission are confirmed.

## Corrections

Corrections should be made through a documented commit. The commit message should name the measurement ID and the reason, for example:

`Correct cartridge loading metadata for GS-2026-0001`

Numerical values transcribed from a report should only be changed when the source report was transcribed incorrectly. If the algorithm itself changes, preserve the original and publish a new analysis version.
