# GS-2026-0016 — AVID Reference Ruby / AVID Acutus / Nexus — 1 kHz Reference Check

**Measured by Michelangelo Canonico for Direct Sound Records using Groove Scope Studio.**

The AVID Reference Ruby, Acutus and Nexus chain delivered **37.6 dB average channel separation at 1 kHz**, with the left output **0.43 dB** above the right. In a separate Groove Scope Studio tracking capture, both 90 µm and 100 µm were rated clean. The 80 µm band stands out for its sharp rise in distortion and much weaker test tone.

## Record status

The 1 kHz reference capture was made on 8 November 2026 at 17:32 local time. The tracking capture was made at 17:26 the same day. The reports do not record a timezone. Published 9 November 2026. Record version 1.0.0.

## Playback chain

| Component | Identity |
|---|---|
| Turntable | AVID Acutus |
| Tonearm | AVID Nexus |
| Cartridge | AVID Reference Ruby |
| Phono preamplifier | ART preamp, model unspecified |
| Capture input | USB Audio CODEC, as labelled in both reports |

Tracking force, anti-skate, alignment geometry, cartridge loading, test-record identity and track, repeat count and software versions were not recorded. The tracking report separately identifies its DSP analysis version and capture settings.

## Complete 1 kHz reference results

| Metric | Result |
|---|---|
| Playback speed under stylus load | 33.20 RPM |
| Playback speed error | −0.39% vs 33⅓ RPM |
| Settled speed range | 33.07–33.31 RPM |
| Settled speed span | 0.24 RPM |
| DIN-shaped wow & flutter RMS | 0.059% |
| Raw speed variation, unweighted RMS | ±0.210% |
| Raw speed variation, unweighted 2-sigma | ±0.420% |
| Raw wow, unweighted RMS | 0.199% |
| Raw flutter, unweighted RMS | 0.061% |
| Channel balance, L−R | +0.43 dB |
| Average channel separation at 1 kHz | 37.6 dB |
| Electrical crosstalk, L→R | −39.7 dB |
| Electrical crosstalk, R→L | −35.5 dB |
| Directional crosstalk difference | 4.27 dB |
| Total harmonic distortion | Left 0.59%, right 0.64% |
| THD difference, L−R | −0.05 percentage points |
| Second harmonic (H2) | Left −44.7 dB, right −43.9 dB |
| Third harmonic (H3) | Left −66.6 dB, right −64.0 dB |
| Fourth harmonic (H4) | Left −70.6 dB, right −64.9 dB |
| Fifth harmonic (H5) | Left −71.3 dB, right −68.7 dB |
| H2 difference summary | Right 0.7 dB higher |
| H3 difference summary | Right 2.6 dB higher |

The table preserves the reported precision of the individual readings and their differences. Separation and distortion describe the cartridge in this playback and capture chain.

## Tracking ability

| Band | Stored THD | Left THD | Right THD | Balance (L−R) | Report evaluation |
|---|---:|---:|---:|---:|---|
| 50 µm | 0.402% | 0.40169% | 0.21493% | +0.392 dB | Clean |
| 60 µm | 0.589% | 0.58943% | 0.31536% | +0.084 dB | Clean |
| 70 µm | 0.595% | 0.59521% | 0.38103% | −0.067 dB | Clean |
| 80 µm | 28.526% | 24.70041% | 28.52627% | −21.304 dB | Severe |
| 90 µm | 0.652% | 0.65234% | 0.44435% | +0.797 dB | Clean |
| 100 µm | 0.744% | 0.74373% | 0.44493% | +0.064 dB | Clean |

The report lists **100 µm as the highest passed band and 80 µm as the first failed band**. At 80 µm, the fitted fundamental was −106.268 dBFS left and −84.955 dBFS right. The extracted interval lasted 0.800 seconds and yielded five retained windows per channel, compared with 31 windows per channel at every other band. The measurer suspects a local test-record imperfection given the clean 90 µm and 100 µm bands. The cause remains open.

Groove Scope Studio captured the tracking test through the direct interface in stereo at 48 kHz. The report retained the original ladder evaluations and lists the breakdown thresholds as uncalibrated, with affected channels and anti-skate adjustment direction undetermined. [Original tracking-ability report](tracking-ability-report.pdf)

## Reference capture reliability

The 1 kHz report notes that the right channel’s third harmonic changed most during recording and calls for a repeat capture before changing the cartridge setup. For the directional crosstalk difference, it advises checking routing and gain before repeating. If the difference persists, it points to the General Reference Level and 1 kHz channel suite in Groove Scope Studio with the matching test records.

## Rotation Fingerprints

The eight original screenshots cover speed deviation, 1 kHz level modulation, opposite-channel leakage and harmonic distortion. Channel assignments follow the supplied filenames. The angular reference between captures is unspecified.

## Provenance

The two original PDFs document separate reference and tracking captures. The playback chain and the possible explanation for the 80 µm tracking anomaly come from the measurer’s account.

The archived photograph is a full-resolution 5712 × 4284 JPEG from the supplied HEIC with embedded metadata stripped. The editorial version uses the built-in ImageGen edit to straighten and brighten the composition, soften glare and simplify the background.

## Files

- [Original 1 kHz reference report](report.pdf)
- [Original tracking-ability report](tracking-ability-report.pdf)
- [Structured JSON](measurement.json)
- [Original fingerprint PNGs](assets/source/)
- [Archived photograph](assets/source/hero-original.jpg)
- [Retouched photograph](assets/hero-retouched.png)
- [Image edit prompt](assets/image-edit-prompt.txt)
- [SHA-256 checksums](checksums.sha256)

## Citation

Canonico, Michelangelo. “GS-2026-0016 — AVID Reference Ruby / AVID Acutus / Nexus — 1 kHz Reference Check.” *Groove Scope Measurements*. Direct Sound Records, 2026. CC BY 4.0.

## Changelog

- 1.0.0 — Initial publication with the two original reports, eight Rotation Fingerprints, photograph and the measurer’s session account.
