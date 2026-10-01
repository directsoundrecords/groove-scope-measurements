# GS-2026-0004 — Goldring 2100 / Micro Seiki DQX-500

**Measured by Michelangelo Canonico for Direct Sound Records using Groove Scope.**

The Micro Seiki DQX-500 / Goldring 2100 capture measured 33.36 RPM (+0.09%) with 0.032% DIN-shaped wow and flutter RMS. Average separation was 21.8 dB at 1 kHz and channel balance was +0.32 dB. Harmonic levels were steady during the recording, with THD of 1.37% left and 1.97% right.

## Record status and identity

Public archive entry, status **draft**: setup and software metadata remain incomplete. Measured 1 October 2026 at 13:56 local time; timezone not recorded. Record version 0.9.0.

The report title is “Micro Seiki QRP500 - Goldring 2100”. The measurer confirmed DQX, matching the DQX-500 badge in the supplied photograph. The public record uses **Micro Seiki DQX-500**; the original PDF is preserved unchanged. The cartridge is Goldring 2100. Input is recorded as **USB Audio CODEC**; the full interface model and phono stage are unconfirmed.

## Complete results

| Metric | Result |
|---|---|
| Playback speed under stylus load | 33.36 RPM |
| Playback speed error | +0.09% vs 33⅓ RPM |
| Settled speed range | 33.27–33.46 RPM |
| Settled speed span | 0.19 RPM |
| DIN-shaped wow & flutter RMS | 0.032% |
| Raw speed variation RMS | ±0.163% |
| Raw speed variation, 2-sigma | ±0.325% |
| Raw wow RMS | 0.159% |
| Raw flutter RMS | 0.033% |
| Channel balance, L−R | +0.32 dB |
| Average channel separation at 1 kHz | 21.8 dB |
| Electrical crosstalk, L→R | −22.4 dB |
| Electrical crosstalk, R→L | −21.3 dB |
| Crosstalk directional difference | 1.13 dB |
| Total harmonic distortion | Left 1.37%; right 1.97% |
| THD difference, L−R | −0.61 percentage points (source report) |
| Second harmonic (H2) | Left −37.5 dB; right −34.2 dB |
| Third harmonic (H3) | Left −51.1 dB; right −50.6 dB |
| Fourth harmonic (H4) | Left −65.6 dB; right −57.5 dB |
| Fifth harmonic (H5) | Left −75.2 dB; right −67.6 dB |
| H2 difference summary | Right 3.2 dB higher (source report) |
| H3 difference summary | Right 0.6 dB higher (source report) |
| Harmonic reliability | Steady during recording. Suitable for setup guidance. |

Differences are transcribed exactly as reported. They may differ from subtraction of rounded channel values.

## Rotation fingerprints

Eight supplied screenshots show speed deviation, 1 kHz level modulation, opposite-channel leakage and harmonic distortion across eight rotations. The speed plots show a recurring once-per-rotation pattern. Both channels share an alignment label of R +140°. The screenshots alone do not identify a mechanical cause. L/R assignments follow the supplied pair order; leakage directions are explicit in the source screenshots.

## Interpretation and next comparison

Steady harmonic levels during this capture provide useful context for the measured channel differences. A repeat capture with unchanged settings can show whether the rotational pattern and the higher right-channel THD persist. These are in-system observations; no manufacturer specification or audibility comparison is claimed.

## Setup and provenance

Tonearm model, phono stage, interface model, loading, tracking force, anti-skate, alignment, test-record identity/track, gain, capture format, software and analysis-method versions, sample ownership, location and repeat count were not supplied. Missing values remain `not_recorded` or `not_confirmed` in the structured record.

The original PDF, HEIC and eight PNGs are preserved. The hero photograph is cosmetically retouched using built-in imagegen for background removal, colour and studio lighting; it is an editorial illustration of the supplied equipment. Measurement images remain unretouched. No raw test-record audio is published.

## Files

- [Original PDF report](report.pdf)
- [Structured JSON](measurement.json)
- [Source photographs and screenshots](assets/source/)
- [Retouched hero](assets/hero-retouched.png)
- [Image-edit prompt](assets/image-edit-prompt.txt)
- [SHA-256 checksums](checksums.sha256)

## Citation

Canonico, Michelangelo. “GS-2026-0004 — Goldring 2100 / Micro Seiki DQX-500 — 1 kHz Reference Check.” *Groove Scope Measurements*. Direct Sound Records, 2026. CC BY 4.0.

## Changelog

- 0.9.0 — Initial public archive entry with report transcription, original assets, rotation fingerprints and retouched hero.
