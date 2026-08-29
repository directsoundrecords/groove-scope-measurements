# GS-2026-0002 — Ortofon OM10 / Thorens TD160 Super / SME III

**Groove Scope Measurement GS-2026-0002 was conducted by Michelangelo Canonico for Direct Sound Records using Groove Scope.**

This record documents a 1 kHz vinyl playback reference check of a **Thorens TD160 Super**, **SME III** tonearm, **Ortofon OM10** cartridge, and **Perreaux EP2** phono preamplifier.

> **Publication status:** Published as an archival observation on 29 August 2026. Unavailable fields remain explicitly marked `not_recorded`. The source report labels its distortion diagnostics as variable, so those figures are preserved for provenance but are not suitable for setup decisions.

## Identity and provenance

| Field | Value |
|---|---|
| Measurement ID | `GS-2026-0002` |
| Measurement date | 22 July 2026 at 17:58, local time; timezone not recorded |
| Creator / measurer | Michelangelo Canonico |
| Publisher | Direct Sound Records |
| Application | Groove Scope |
| Report label | Groove Scope Reference |
| Input interface label | EVO4 |
| Measurement type | 1 kHz Reference Check |
| Source report | [report.pdf](report.pdf) |
| Structured record | [measurement.json](measurement.json) |

## Playback chain

| Component | Recorded identification |
|---|---|
| Turntable | Thorens TD160 Super |
| Tonearm | SME III |
| Cartridge | Ortofon OM10 |
| Phono preamplifier | Perreaux EP2 |
| Audio interface label | EVO4 |

The source PDF title writes the arm as “SME iII”. The structured record normalizes this to **SME III** while preserving the original source title separately.

## Primary results

| Metric | Result | Role |
|---|---:|---|
| Playback speed | 34.14 RPM | Primary result |
| Playback speed error | +2.41% | Primary result; fast |
| Settled RPM range | 34.06–34.23 RPM | Primary result |
| RPM span | 0.17 RPM | Primary result |
| DIN-shaped wow & flutter | 0.037% | Primary result |
| Raw speed variation RMS | ±0.130% | Unweighted diagnostic |
| Raw speed variation, 2σ | ±0.256% | Unweighted diagnostic |
| Raw wow RMS | 0.121% | Unweighted diagnostic |
| Raw flutter RMS | 0.045% | Unweighted diagnostic |

## Supporting diagnostics

| Metric | Result | Interpretation status |
|---|---:|---|
| Channel balance | +0.82 dB | Diagnostic only |
| Average 1 kHz separation | 26.8 dB | Supporting |
| L→R crosstalk | -24.9 dB | Directional value; repeat |
| R→L crosstalk | -28.7 dB | Directional value; repeat |
| Crosstalk directional difference | 3.83 dB | Directional value; repeat |

## Distortion-quality warning

The report records left/right THD values of 88.00% and 108.73%, but also labels distortion quality as **variable**. It states that phase tracking could not retain enough clean, continuous tone segments for the experimental comparison and advises repeating the capture and checking the record for clicks or dropouts.

For that reason, these distortion and harmonic values are preserved for provenance but classified in the JSON as **not suitable for setup decisions from this capture**.

## Interpretation supplied by Groove Scope

The measurement indicates that playback speed was fast by 2.41%. The report recommends confirming the speed result with another valid capture before correcting the deck and repeating the capture before relying on distortion-related diagnostics.

## Unavailable metadata and publication limitations

- Test record, edition, track, nominal frequency, and record condition
- Cartridge stylus identification and approximate hours
- Tracking force, anti-skate, alignment geometry, and relevant setup notes
- Actual Perreaux EP2 gain/loading settings used
- Audio interface model confirmation and input/gain settings
- Device, operating system, sample rate, bit depth, and channel routing
- Groove Scope application version and analysis-method version
- Measurement location and timezone at city/country level only

Publication makes this historical capture citable while preserving its limits. A repeat capture is still required before confirming the speed result or using distortion-related diagnostics for comparison or adjustment.

## Files and verification

- [Original Groove Scope PDF](report.pdf)
- [Machine-readable JSON](measurement.json)
- [SHA-256 checksums](checksums.sha256)

## Recommended citation

Canonico, Michelangelo. “GS-2026-0002 — Ortofon OM10 / Thorens TD160 Super / SME III — 1 kHz Reference Check.” *Groove Scope Measurements*. Direct Sound Records, 2026. Measurement made with Groove Scope.
