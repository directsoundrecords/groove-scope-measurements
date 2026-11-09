# GS-2026-0011 — Audio-Technica VM95SH — 1 kHz Reference Check

**Measured by Michelangelo Canonico for Direct Sound Records using Groove Scope.**

Groove Scope made it easy to improve the azimuth from a much poorer starting point. After adjustment, this setup measured 17.7 dB average channel separation at 1 kHz. The Audio-Technica VM95SH had a bent cantilever, which limits the cartridge readings to this compromised specimen. The Thorens averaged 33.29 RPM, and both speed fingerprints showed a pattern that repeated each turn and warrants further investigation.

## Record status

Measured 5 November 2026 at 12:08 local time. The report does not record a timezone. Published 5 November 2026. Record version 0.9.3.

## Playback chain

| Component | Identity |
|---|---|
| Turntable | Thorens TD 160 Super |
| Tonearm | SME III |
| Cartridge | Audio-Technica VM95SH, with a bent cantilever |
| Phono preamplifier | ART preamp, model unspecified |

The report title identifies the hardware and its input field is blank. The cantilever condition comes from the measurer’s session account. Tracking force, loading, anti-skate, alignment geometry, test record and track, capture settings, and software versions were not recorded.

## Complete results

| Metric | Result |
|---|---|
| Playback speed under stylus load | 33.29 RPM |
| Playback speed error | −0.12% vs 33⅓ RPM |
| Settled speed range | 33.23–33.36 RPM |
| Settled speed span | 0.13 RPM |
| DIN-shaped wow & flutter RMS | 0.030% |
| Raw speed variation, unweighted RMS | ±0.108% |
| Raw speed variation, unweighted 2-sigma | ±0.216% |
| Raw wow, unweighted RMS | 0.101% |
| Raw flutter, unweighted RMS | 0.037% |
| Channel balance, L−R | +2.90 dB |
| Average channel separation at 1 kHz | 17.7 dB |
| Electrical crosstalk, L→R | −18.4 dB |
| Electrical crosstalk, R→L | −17.0 dB |
| Directional crosstalk difference | 1.45 dB |
| Total harmonic distortion | Left 1.37%, right 1.26% |
| THD difference, L−R | +0.11 percentage points |
| Second harmonic (H2) | Left −37.3 dB, right −38.1 dB |
| Third harmonic (H3) | Left −68.1 dB, right −59.5 dB |
| Fourth harmonic (H4) | Left −76.5 dB, right −72.0 dB |
| Fifth harmonic (H5) | Left −75.2 dB, right −71.6 dB |
| H2 difference summary | Left 0.8 dB higher |
| H3 difference summary | Right 8.6 dB higher |
| Harmonic reliability | Steady during recording and suitable for setup guidance, per the report |

The table preserves the source report’s precision for both the individual channel values and the reported differences.

## Azimuth and channel balance

The starting azimuth was substantially worse by the measurer’s account. Groove Scope made the adjustment straightforward, but the supplied capture documents only the final readings. There is no recorded initial value or physical angle for a numerical comparison.

After adjustment, the two directions of crosstalk differed by 1.45 dB. The left channel’s signal level was 2.90 dB higher than the right, a separate measurement. The report flags that level difference for a repeat capture after checking routing and gain.

## Rotation Fingerprints

Both speed fingerprints show a slower portion and a faster portion recurring at similar relative angles over eight revolutions. The repeatable pattern is a reason to investigate the Thorens’ rotation further. Its mechanical cause remains open.

The eight supplied screenshots cover speed deviation, 1 kHz level modulation, opposite-channel leakage and harmonic distortion. Left and right assignments follow the supplied filenames. The screenshots do not specify how the relative angles align across channels.

## SME III trackability

A separate article will cover the ultra-low-mass SME III’s excellent 90 µm trackability result measured with Groove Scope Studio.

## Provenance

The PDF supplies the numerical results. The measurer supplies the bent-cantilever diagnosis, the azimuth adjustment history and the separate trackability observation. The results reflect the captured playback chain as a whole. The individual contributions of the cartridge, tonearm, turntable, test record and electronics were not isolated.

The archived source photo is a metadata-stripped JPEG export of the supplied HEIC with its original framing and tone. ImageGen was used to preview a subtle tonal grade, which was applied to the source pixels to preserve the original hardware detail and framing. The eight original fingerprint PNGs are preserved.

No raw test-record audio is published.

## Files

- [Original PDF](report.pdf)
- [Structured JSON](measurement.json)
- [Original fingerprint PNGs and source photograph](assets/source/)
- [Retouched photograph](assets/hero-retouched.png)
- [Image edit prompt](assets/image-edit-prompt.txt)
- [SHA-256 checksums](checksums.sha256)

## Citation

Canonico, Michelangelo. “GS-2026-0011 — Audio-Technica VM95SH — 1 kHz Reference Check.” *Groove Scope Measurements*. Direct Sound Records, 2026. CC BY 4.0.

## Changelog

- 0.9.3 — Standardised the measurement title around the cartridge name.
- 0.9.2 — Corrected the publication status to published.
- 0.9.1 — Replaced the left-channel speed fingerprint with the supplied cropped image.
- 0.9.0 — Initial public entry with the source report, eight Rotation Fingerprints, the setup photograph and the measurer’s account.
