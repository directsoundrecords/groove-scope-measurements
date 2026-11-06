# GS-2026-0013 — Rega P1 / Rega Carbon — 1 kHz Reference Check

**Measured by Michelangelo Canonico for Direct Sound Records at the AudioReview laboratory.**

The Rega Carbon looked aligned on the Rega P1. The first crosstalk readings told a different story. Groove Scope guided an azimuth adjustment that brought the gap between the two leakage directions down from **10.27 dB to 1.16 dB**. In a separate Groove Scope Studio tracking trial, the same entry-level combination reached **80 µm at 2.5 g**, up from 60 µm at 2.0 g.

Thanks to Mauro Neri, director of *AudioReview*, for making the laboratory session possible.

## Record status

Measured 6 November 2026 at 16:58 local time. The report does not record a timezone. Published 6 November 2026. Record version 0.9.2.

## Playback chain

| Component | Identity |
|---|---|
| Turntable | Rega P1, marked Planar 1 |
| Cartridge | Rega Carbon |
| Phono preamplifier | ART preamp, model unspecified |
| Capture input | USB Audio CODEC, as labelled in the report |

The report title identifies the turntable, cartridge and ART. The capture-device model, tonearm model and reference capture’s tracking force are unspecified. The 2.0 g and 2.5 g settings below apply to the tracking trial.

## Azimuth and channel balance

| 1 kHz metric | As found, measurer’s notes | After adjustment, reference report |
|---|---:|---:|
| Electrical crosstalk, L→R | −33.7 dB | −32.4 dB |
| Electrical crosstalk, R→L | −23.5 dB | −31.2 dB |
| Directional crosstalk difference | 10.27 dB | 1.16 dB |
| Average channel separation | 28.6 dB | 31.8 dB |
| Signal channel balance, L−R | +0.77 dB | +1.04 dB |

With the cartridge apparently square by eye, the right channel was leaking into the left much more than the left was leaking into the right. After adjustment, right-to-left leakage fell by 7.7 dB and left-to-right leakage rose by 1.3 dB, improving average separation by 3.2 dB. The left channel’s signal-level advantage increased slightly, from +0.77 dB to +1.04 dB. The directional gap describes leakage between channels. Signal balance describes the relative output of the two channels.

## Tracking ability

| Tracking force | Reported tracking level |
|---|---:|
| 2.0 g | 60 µm |
| 2.5 g | 80 µm |

The measurer reported a 20 µm gain on the Groove Scope Studio tracking ladder between the two settings. The test record, frequency, pass criterion and trace are unavailable. The result describes this sample and trial. Both tested settings fall within Rega’s specified 2–3 g tracking range for the Carbon. [Rega Carbon specifications](https://www.rega.co.uk/products/carbon)

## Complete reference results

| Metric | Result |
|---|---|
| Playback speed under stylus load | 33.22 RPM |
| Playback speed error | −0.35% vs 33⅓ RPM |
| Settled speed range | 33.11–33.31 RPM |
| Settled speed span | 0.20 RPM |
| DIN-shaped wow & flutter RMS | 0.036% |
| Raw speed variation, unweighted RMS | ±0.176% |
| Raw speed variation, unweighted 2-sigma | ±0.352% |
| Raw wow, unweighted RMS | 0.171% |
| Raw flutter, unweighted RMS | 0.037% |
| Channel balance, L−R | +1.04 dB |
| Average channel separation at 1 kHz | 31.8 dB |
| Electrical crosstalk, L→R | −32.4 dB |
| Electrical crosstalk, R→L | −31.2 dB |
| Directional crosstalk difference | 1.16 dB |
| Total harmonic distortion | Left 1.36%, right 1.95% |
| THD difference, L−R | −0.59 percentage points |
| Second harmonic (H2) | Left −37.4 dB, right −34.3 dB |
| Third harmonic (H3) | Left −63.4 dB, right −53.0 dB |
| Fourth harmonic (H4) | Left −64.1 dB, right −56.7 dB |
| Fifth harmonic (H5) | Left −72.4 dB, right −65.8 dB |
| H2 difference summary | Right 3.1 dB higher |
| H3 difference summary | Right 10.3 dB higher |
| Harmonic reliability | Steady during recording and suitable for setup guidance, per the report |

The tables preserve the reported precision of the individual readings and their differences.

## Rotation Fingerprints

Both speed fingerprints show a trough near the midpoint of the displayed angular scale across eight revolutions. The ±0.29% chart scale shows relative speed deviation, while the report gives DIN-shaped wow and flutter of 0.036% RMS. The relative contributions of the turntable and test record to the recurring pattern were not established. The right channel also shows higher distortion across the captured rotations, consistent with the report’s 1.95% right and 1.36% left THD readings.

The original screenshots cover speed deviation, 1 kHz level modulation, opposite-channel leakage and harmonic distortion. Channel assignments follow the supplied filenames. The angular reference between captures is unspecified.

## Provenance

The PDF documents the adjusted 1 kHz capture. The laboratory location, initial readings, azimuth adjustment and tracking trial come from the measurer’s session account. The physical azimuth angle, anti-skate, loading, alignment geometry, test record and track, repeat count, capture settings and software versions were not recorded. The results describe the playback chain as a whole.

The archived setup photograph is a full-resolution JPEG from the supplied HEIC with embedded metadata stripped. The editorial image is the ImageGen retouch of that photograph, with adjusted lighting and background cleanup. The archived source photograph documents the setup.

## Files

- [Original PDF](report.pdf)
- [Structured JSON](measurement.json)
- [Original fingerprint PNGs](assets/source/)
- [Archived setup photograph](assets/source/hero-original.jpg)
- [Retouched photograph](assets/hero-retouched.png)
- [Image edit prompt](assets/image-edit-prompt.txt)
- [SHA-256 checksums](checksums.sha256)

## Citation

Canonico, Michelangelo. “GS-2026-0013 — Rega P1 / Rega Carbon — 1 kHz Reference Check.” *Groove Scope Measurements*. Direct Sound Records, 2026. CC BY 4.0.

## Changelog

- 0.9.2 — Corrected the publication status to published.
- 0.9.1 — Published the ImageGen retouch as the editorial photograph.
- 0.9.0 — Initial public entry with the reference report, eight Rotation Fingerprints, setup photograph and the measurer’s account of the azimuth and tracking trials.
