# GS-2026-0001 — 1 kHz Reference Check

**Groove Scope Measurement GS-2026-0001 was conducted by Michelangelo Canonico for Direct Sound Records using Groove Scope.**

This record documents a 1 kHz vinyl playback reference check covering playback speed, rotational stability, DIN-weighted wow and flutter, channel balance, crosstalk, distortion, harmonic character, and relative residual noise.

> **Publication status:** Draft — the turntable, external power supply, cartridge, stylus profile, and phono preamplifier have now been identified. The actual phono loading, test-record details, capture format, Groove Scope version, and analysis-method version still need confirmation before this record is promoted to `published`.

## Identity and provenance

| Field | Value |
|---|---|
| Measurement ID | `GS-2026-0001` |
| Measurement date | 12 July 2026 at 22:04, local time; timezone not recorded |
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
| Turntable | Rega P3 |
| External turntable power supply | Rega Neo PSU MK2 |
| Tonearm | Rega RB330 |
| Cartridge | Audio-Technica AT-OC9XML moving-coil cartridge |
| Stylus profile | Nude Microlinear diamond |
| Phono preamplifier | Audio Research SP20 integrated phono stage |
| Actual phono loading used | Not yet confirmed |

## Primary results

| Metric | Result | Role |
|---|---:|---|
| Settled test-tone frequency | 992.88 Hz | Stable primary result |
| Playback speed error | -0.71% | Stable primary result |
| Calculated speed | 33.10 RPM | Stable primary result |
| Settled RPM range | 32.63–33.55 RPM | Stable primary result |
| RPM span | 0.93 RPM | Stable primary result |
| DIN-weighted wow & flutter | 0.045% | Stable primary result |
| Raw speed variation RMS | ±0.358% | Unweighted diagnostic |
| Raw speed variation, 2σ | ±0.716% | Unweighted diagnostic |
| Raw wow RMS | 0.186% | Unweighted diagnostic |
| Raw flutter RMS | 0.287% | Unweighted diagnostic |

The Groove Scope report states that playback speed was slow by 0.71% and that DIN-weighted wow and flutter was low at 0.045% for this capture.

## Supporting diagnostics

| Metric | Result | Interpretation status |
|---|---:|---|
| Channel balance | -0.63 dB | Diagnostic only; repeat before alignment changes |
| Average 1 kHz separation | 30.4 dB | Supporting |
| L→R crosstalk | -27.7 dB | Directional value; repeat |
| R→L crosstalk | -33.1 dB | Directional value; repeat |
| Crosstalk directional difference | 5.40 dB | Directional value; repeat |
| Left-channel THD | 0.37% | Diagnostic only |
| Right-channel THD | 0.34% | Diagnostic only |
| L−R THD difference | +0.03 percentage points | Diagnostic only |
| Combined 1 kHz THD | 0.31% | Supporting |
| Relative residual noise | 14.8 dB | Diagnostic only; not an A-weighted bench-noise value |

### Harmonic profile

| Harmonic | Left | Right | L−R difference |
|---|---:|---:|---:|
| H2 | -48.7 dB | -49.7 dB | +0.9 dB |
| H3 | -64.4 dB | -63.2 dB | -1.2 dB |
| H4 | -72.5 dB | -70.5 dB | -2.0 dB |
| H5 | -79.6 dB | -82.0 dB | +2.4 dB |

The report treats the harmonic differences as diagnostic because they are isolated or change direction. It recommends acting only when the same multi-harmonic pattern repeats across valid captures.

## Interpretation supplied by Groove Scope

Playback speed and rotational stability were measured consistently during this capture. Channel-specific distortion, harmonic, balance, and directional 1 kHz measurements require repetition before mechanical adjustment.

The report recommends confirming the speed result with another valid capture and correcting the deck speed only if the same error repeats. It also advises repeating variable diagnostics before adjusting anti-skate, zenith, azimuth, VTA, or VTF.

## Missing metadata required before final publication

- Cartridge hours of use
- Tracking force and anti-skate setting
- Alignment geometry and relevant setup notes
- Actual Audio Research SP20 phono loading used for the capture
- Test record, edition, track, nominal frequency, and record condition
- Audio interface model confirmation and input/gain settings
- Device, operating system, sample rate, bit depth, and channel routing
- Groove Scope application version and analysis-method version
- Capture repetition count and whether this result is representative
- Measurement location and timezone at city/country level only

Unknown values are explicitly preserved as `not_recorded` in the JSON record. This is deliberate: an honest blank is more useful than a beautifully formatted invention.

## Files and verification

- [Original Groove Scope PDF](report.pdf)
- [Machine-readable JSON](measurement.json)
- [SHA-256 checksums](checksums.sha256)

## Recommended citation

Canonico, Michelangelo. “GS-2026-0001 — 1 kHz Reference Check.” *Groove Scope Measurements*. Direct Sound Records, 2026. Measurement made with Groove Scope.
