# audio technica — 1 kHz Reference Check

Measurement ID: GS-2026-0020

Status: **Withdrawn** on 17 November 2026 at the publisher’s request. Removed from the public website; original source files and numerical results are retained for transparency.

Measured by zorro. Published by Direct Sound Records.

la misura ha riportato un imbalance lieve che ho potuto rilevare grazie all'app

## Setup

- turntable: rega
- tonearm: rega
- cartridge: audio technica
- stylus: microlinear
- phono stage: no
- test record: ortofon
- test record track: not\_recorded
- vertical tracking force g: 2
- anti skate setting: 2
- alignment geometry: manuale
- cartridge loading: not\_recorded
- phono gain db: not\_recorded
- audio interface reported label: USB-Audio - USB Audio CODEC
- audio interface full model: behringer
- sample rate hz: 48000

## Measurement recap

### RPM and speed variation

| Metric | Result |
|---|---|
| Average RPM | 33.30 RPM |
| Error vs nominal | -0.09% |
| Left-track RPM | 33.31 RPM |
| Right-track RPM | 33.30 RPM |
| Left wow / flutter RMS | 0.129% / 0.037% |
| Right wow / flutter RMS | 0.133% / 0.033% |

Raw, unweighted RMS estimates split at 4 Hz; not a DIN/IEC weighted-peak rating.
### Electrical crosstalk

| Metric | Result |
|---|---|
| Left → right | -28.0 dB |
| Right → left | -34.6 dB |
| Directional difference | 6.6 dB |
| Reference-level difference | 0.8 dB |
| Internal input boost | +11.0 dB |

More negative leakage means better separation. Keep interface gain unchanged between tracks.
### Azimuth indication

| Metric | Result |
|---|---|
| Comparison | Left → right leakage is higher |
| Suggested check | Trial: tilt right viewed from the front, then remeasure |

A 2 dB difference is a follow-up cue, not a cartridge tolerance. Confirm routing and track selection; make only small trial changes and repeat both captures.
### Left-track harmonic profile

| Metric | Result |
|---|---|
| THD (harmonics 2–5) | 0.40% |
| 2nd harmonic | -49.2 dBc |
| 3rd harmonic | -56.4 dBc |
| 4th harmonic | -60.6 dBc |
| 5th harmonic | -63.3 dBc |

Harmonics are relative to the expected main-channel 1 kHz fundamental.
### Right-track harmonic profile

| Metric | Result |
|---|---|
| THD (harmonics 2–5) | 0.75% |
| 2nd harmonic | -42.8 dBc |
| 3rd harmonic | -56.2 dBc |
| 4th harmonic | -60.0 dBc |
| 5th harmonic | -63.3 dBc |

Harmonics are relative to the expected main-channel 1 kHz fundamental.

## Source and reuse

[Saved capture](capture.json), [structured record](measurement.json), [checksums](checksums.sha256). Capture and exporter versions are separate. No raw audio is published.

Licence: CC BY 4.0.
