# GS-2026-0006 — Transfiguration Orpheus / Micro Seiki RX-5000 / SME V

**Measured by Michelangelo Canonico for Direct Sound Records using Groove Scope.**

The Micro Seiki RX-5000 / SME V / Transfiguration Orpheus capture measured 33.51 RPM (+0.52%) with 0.031% DIN-shaped wow and flutter RMS. Average separation was 19.5 dB at 1 kHz, channel balance was −0.35 dB, and THD was 0.87% left and 1.18% right. The report classified harmonic levels as steady during this capture.

## Record status and identity

Public archive entry, status **draft**: some setup and software metadata remain incomplete. Measured 26 September 2026 at 16:24 local time; timezone not recorded. Record version 0.9.0. The PDF title is “Transfiguration Orpheus”; the measurer identified the turntable, tonearm, cartridge and EVO4 interface. The original PDF does not record an input name.

| Component | Identification |
|---|---|
| Turntable | Micro Seiki RX-5000 |
| Tonearm | SME V |
| Cartridge | Transfiguration Orpheus |
| Audio interface | EVO4 (measurer supplied) |

## Complete results

| Metric | Result |
|---|---|
| Playback speed under stylus load | 33.51 RPM |
| Playback speed error | +0.52% vs 33⅓ RPM |
| Settled speed range | 33.42–33.58 RPM |
| Settled speed span | 0.16 RPM |
| DIN-shaped wow & flutter RMS | 0.031% |
| Raw speed variation RMS | ±0.136% |
| Raw speed variation, 2-sigma | ±0.271% |
| Raw wow RMS | 0.129% |
| Raw flutter RMS | 0.039% |
| Channel balance, L−R | −0.35 dB |
| Average channel separation at 1 kHz | 19.5 dB |
| Electrical crosstalk, L→R | −19.1 dB |
| Electrical crosstalk, R→L | −19.8 dB |
| Crosstalk directional difference | 0.64 dB |
| Total harmonic distortion | Left 0.87%; right 1.18% |
| THD difference, L−R | −0.31 percentage points (source report) |
| Second harmonic (H2) | Left −41.3 dB; right −38.6 dB |
| Third harmonic (H3) | Left −60.1 dB; right −61.7 dB |
| Fourth harmonic (H4) | Left −75.2 dB; right −77.1 dB |
| Fifth harmonic (H5) | Left −73.3 dB; right −73.9 dB |
| H2 difference summary | Right 2.7 dB higher (source report) |
| H3 difference summary | Left 1.6 dB higher (source report) |
| Harmonic reliability | Steady during recording. Suitable for setup guidance. |

Differences retain the report's precision and may differ from subtraction of rounded channel values.

## Rotation fingerprints

Eight supplied screenshots cover speed deviation, 1 kHz level modulation, opposite-channel leakage and harmonic distortion across eight rotations for each channel. Left/right assignments follow the supplied pair order because the screenshots themselves have no visible channel labels. The speed plots show a recurring once-per-rotation pattern, and the level and distortion patterns differ between the two supplied channel views. These plots alone do not establish a physical cause.

## Interpretation and next comparison

The report describes harmonic levels as steady within this capture, which makes them useful setup context. A repeated session with the same record, track and settings can test whether the reported +0.52% mean speed offset and the channel-specific fingerprint patterns persist. The values describe this playback chain and recording; they are not manufacturer specifications.

## Setup and provenance

Tracking force, anti-skate, alignment, phono stage, cartridge loading, test-record identity and track, gain, capture format, software and analysis-method versions, sample ownership, location and repeat count were not supplied. These remain `not_recorded` in the JSON. The PDF, original HEIC and eight graph PNGs are preserved. A separate editorial hero was cosmetically retouched; measurement screenshots are unretouched. No raw test-record audio is published.

## Files

- [Original PDF report](report.pdf)
- [Structured JSON](measurement.json)
- [Original photograph and screenshots](assets/source/)
- [Editorial hero](assets/hero-retouched.png)
- [Image-edit description](assets/image-edit-prompt.txt)
- [SHA-256 checksums](checksums.sha256)

## Citation

Canonico, Michelangelo. “GS-2026-0006 — Transfiguration Orpheus / Micro Seiki RX-5000 / SME V — 1 kHz Reference Check.” *Groove Scope Measurements*. Direct Sound Records, 2026. CC BY 4.0.

## Changelog

- 0.9.0 — Initial public archive entry with report transcription, supplied setup identities, eight rotation fingerprints and original assets.
