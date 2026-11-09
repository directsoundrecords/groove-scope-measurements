# GS-2026-0017 — Ortofon 2M Bronze — 1 kHz Reference Check

**Measured by Michelangelo Canonico for Direct Sound Records using Groove Scope.**

The Ortofon 2M Bronze averaged **32.2 dB of separation at 1 kHz** on a vintage Thorens TD 160 Super with an SME III tonearm. The final capture showed a **1.72 dB** difference between crosstalk directions and a left-minus-right output balance of **+0.44 dB**. Playback averaged **33.30 RPM** with **0.028% DIN-shaped wow and flutter RMS**.

## Setup adjustments

The measurer observed an initial 5.86 dB imbalance before adjusting azimuth. The measurer also adjusted anti-skate and reported a significant improvement after that step. The initial imbalance metric was unspecified, and the final report separately lists output balance and the difference between crosstalk directions. The source PDF documents the final capture.

## Record status

Measured 6 November 2026 at 22:03 local time. The report does not record a timezone. Published 9 November 2026. Record version 1.0.0.

## Playback chain

| Component | Identity |
|---|---|
| Turntable | Thorens TD 160 Super |
| Tonearm | SME III |
| Cartridge | Ortofon 2M Bronze |
| Phono stage | ART preamp |

The exact ART model, capture input, tracking force, final azimuth and anti-skate settings, loading, test record and track, capture settings and software versions were not recorded.

## Complete reference results

| Metric | Result |
|---|---|
| Playback speed under stylus load | 33.30 RPM |
| Playback speed error | −0.11% vs 33⅓ RPM |
| Settled speed range | 33.22–33.37 RPM |
| Settled speed span | 0.15 RPM |
| DIN-shaped wow and flutter RMS | 0.028% |
| Raw speed variation, unweighted RMS | ±0.138% |
| Raw speed variation, unweighted 2-sigma | ±0.276% |
| Raw wow, unweighted RMS | 0.134% |
| Raw flutter, unweighted RMS | 0.032% |
| Channel balance, L−R | +0.44 dB |
| Average channel separation at 1 kHz | 32.2 dB |
| Electrical crosstalk, L→R | −33.0 dB |
| Electrical crosstalk, R→L | −31.3 dB |
| Directional crosstalk difference | 1.72 dB |
| Total harmonic distortion | Left 1.23%, right 1.26% |
| THD difference, L−R | −0.03 percentage points |
| Second harmonic (H2) | Left −38.6 dB, right −38.5 dB |
| Third harmonic (H3) | Left −49.7 dB, right −50.1 dB |
| Fourth harmonic (H4) | Left −57.4 dB, right −58.8 dB |
| Fifth harmonic (H5) | Left −68.3 dB, right −66.4 dB |
| H2 difference summary | Right 0.1 dB higher |
| H3 difference summary | Left 0.5 dB higher |

The table preserves the report’s precision for the individual readings and differences. The report found that left-channel total distortion changed most during the capture and recommends repeating the measurement before using the distortion results to guide further cartridge setup changes.

## Rotation Fingerprints

Both speed fingerprints show a recurring faster section near the start and end of the displayed angle and a slower section near the middle of each of the eight rotations. The colour scale spans ±0.21% relative speed deviation. The cause of the recurring speed pattern was not established.

The right-channel leakage fingerprint shows stronger leakage in the first rotation than in later rotations. The left-channel distortion fingerprint shows a more pronounced rise on the second rotation. Channel assignments follow the supplied filenames. The angular reference between captures is unspecified.

## Provenance

The original PDF documents the final 1 kHz capture. The initial imbalance and adjustment observations come from the measurer’s session account. The results describe the playback chain as a whole.

The archived setup photograph is a full-resolution 4032 × 3024 JPEG from the supplied HEIC with embedded metadata stripped. The separate ImageGen edit adjusts lighting and white balance, reduces glare and cleans up dust.

## Files

- [Original PDF](report.pdf)
- [Structured JSON](measurement.json)
- [Original fingerprint PNGs](assets/source/)
- [Archived setup photograph](assets/source/hero-original.jpg)
- [Retouched photograph](assets/hero-retouched.png)
- [Image edit prompt](assets/image-edit-prompt.txt)
- [SHA-256 checksums](checksums.sha256)

## Citation

Canonico, Michelangelo. “GS-2026-0017 — Ortofon 2M Bronze — 1 kHz Reference Check.” *Groove Scope Measurements*. Direct Sound Records, 2026. CC BY 4.0.

## Changelog

- 1.0.0 — Initial publication with the reference report, eight Rotation Fingerprints, setup photograph and the measurer’s account of the azimuth and anti-skate adjustments.
