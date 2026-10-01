# GS-2026-0007 — Goldring 2100 / Micro Seiki DQX-500 — 1 kHz Reference Check

**Measured by Michelangelo Canonico for Direct Sound Records using Groove Scope.**

The 22:17 Micro Seiki DQX-500 capture measured 33.33 RPM (−0.01%) with 0.032% DIN-shaped wow and flutter RMS. Average separation was 20.1 dB at 1 kHz and channel balance was −0.54 dB. THD was 1.72% left and 2.15% right. The report recommends a repeat because the right-channel third harmonic changed most during recording.

## Record status and identity

Public archive entry, status **draft**: setup and software metadata remain incomplete. Measured 1 October 2026 at 22:17 local time; timezone not recorded. Record version 0.9.1.

The measurer confirmed this later capture used the Micro Seiki DQX-500, Goldring 2100, Audio Research SP20 and EVO4. These setup identities were supplied after publication; the source PDF itself does not name the turntable or cartridge and leaves the input field blank. The equipment photograph is reused from the earlier GS-2026-0004 session, so it remains illustrative rather than capture-specific evidence.

## Complete results

| Metric | Result |
|---|---|
| Playback speed under stylus load | 33.33 RPM |
| Playback speed error | −0.01% vs 33⅓ RPM |
| Settled speed range | 33.24–33.42 RPM |
| Settled speed span | 0.18 RPM |
| DIN-shaped wow & flutter RMS | 0.032% |
| Raw speed variation RMS | ±0.169% |
| Raw speed variation, 2-sigma | ±0.338% |
| Raw wow RMS | 0.163% |
| Raw flutter RMS | 0.040% |
| Channel balance, L−R | −0.54 dB |
| Average channel separation at 1 kHz | 20.1 dB |
| Electrical crosstalk, L→R | −21.6 dB |
| Electrical crosstalk, R→L | −18.6 dB |
| Crosstalk directional difference | 2.95 dB |
| Total harmonic distortion | Left 1.72%; right 2.15% |
| THD difference, L−R | −0.43 percentage points (source report) |
| Second harmonic (H2) | Left −35.4 dB; right −33.4 dB |
| Third harmonic (H3) | Left −54.7 dB; right −59.1 dB |
| Fourth harmonic (H4) | Left −71.6 dB; right −61.6 dB |
| Fifth harmonic (H5) | Left −74.9 dB; right −69.4 dB |
| H2 difference summary | Right 2.0 dB higher (source report) |
| H3 difference summary | Left 4.4 dB higher (source report) |
| Harmonic reliability | Right-channel H3 changed most; repeat before cartridge setup changes. |

Differences are transcribed exactly as reported. They may differ from subtraction of rounded channel values.

## Rotation fingerprints

Eight supplied screenshots show L/R views of speed deviation, 1 kHz level modulation, opposite-channel leakage and harmonic distortion over eight rotations. L/R labels follow the supplied pair order; the screenshots themselves do not show channel labels. Original PNGs are preserved unedited.

## Interpretation and next comparison

The speed fingerprints show a recurring broad rise and fall. The report says the right-channel third harmonic changed most during recording and advises a repeat before changing cartridge setup. The plots alone do not identify a mechanical cause.

## Setup and provenance

The PDF input field is blank. The measurer supplied the cartridge, preamplifier and interface identities separately. Tonearm, stylus, test record and track, loading, tracking force, alignment, anti-skate, capture settings and software versions were not supplied for this capture. The previously supplied DQX-500 photograph and editorial hero are reused for context; they are not capture-specific evidence. No raw test-record audio is published.

## Files

- [Original PDF report](report.pdf)
- [Structured JSON](measurement.json)
- [Source photograph and screenshots](assets/source/)
- [Illustrative hero reused from GS-2026-0004](assets/hero-retouched.png)
- [Hero provenance note](assets/image-edit-prompt.txt)
- [SHA-256 checksums](checksums.sha256)

## Citation

Canonico, Michelangelo. “GS-2026-0007 — Goldring 2100 / Micro Seiki DQX-500 — 1 kHz Reference Check.” *Groove Scope Measurements*. Direct Sound Records, 2026. CC BY 4.0.

## Changelog

- 0.9.1 — Added measurer-confirmed Goldring 2100, Audio Research SP20 and EVO4 setup identities.
- 0.9.0 — Initial public entry for the 22:17 capture with source PDF, eight supplied fingerprints and an illustrative DQX-500 hero.
