# GS-2026-0003 — Audio-Technica AT-OC9XML / Rega P3 / Rega RB330 / Audio Research SP20

**Groove Scope Measurement GS-2026-0003 was conducted by Michelangelo Canonico for Direct Sound Records using Groove Scope.**

This record documents a 1 kHz vinyl playback reference check of a Rega P3, Rega RB330 tonearm, Audio-Technica AT-OC9XML cartridge, Audio Research SP20 preamplifier, and EVO4 input. It preserves the source report, the supplied measurement photograph, and eight app-generated rotation-fingerprint images.

> **Publication status:** Draft — the primary report is preserved and transcribed, but setup, capture, sample, location, and software-version metadata remain incomplete. The report recommends repeating the measurement before using harmonic differences to justify cartridge adjustment.

## Identity and provenance

| Field | Value |
|---|---|
| Measurement ID | `GS-2026-0003` |
| Measurement date | 5 September 2026 at 10:01, local time; timezone not recorded |
| Sample ID | Not recorded |
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
| Tonearm | Rega RB330 |
| Cartridge | Audio-Technica AT-OC9XML |
| Preamplifier | Audio Research SP20 |
| Input interface label | EVO4 |

The task supplied the turntable, tonearm, cartridge, and preamplifier identities. The report supplies the EVO4 input label and the numeric results. No phono gain, cartridge-loading value, test-record detail, tracking force, anti-skate setting, sample rate, or bit depth has been inferred.

## Primary results

| Metric | Result | Role |
|---|---:|---|
| Playback speed | 33.34 RPM | Primary |
| Playback speed error | +0.02% vs 33 1/3 RPM | Primary |
| Settled RPM range | 33.26–33.42 RPM | Primary |
| RPM span | 0.16 RPM | Primary |
| DIN-shaped wow & flutter RMS | 0.030% | Primary |
| Raw speed variation RMS | ±0.144% | Unweighted diagnostic |
| Raw speed variation, 2σ | ±0.287% | Unweighted diagnostic |
| Raw wow RMS | 0.140% | Unweighted diagnostic |
| Raw flutter RMS | 0.033% | Unweighted diagnostic |

## Supporting diagnostics

| Metric | Result | Interpretation status |
|---|---:|---|
| Channel balance | L−R -0.24 dB | Diagnostic |
| Average 1 kHz separation | 31.8 dB | Supporting |
| L→R crosstalk | -30.2 dB | Directional diagnostic |
| R→L crosstalk | -33.5 dB | Directional diagnostic |
| Crosstalk directional difference | 3.27 dB | Directional diagnostic |
| Left-channel THD | 0.29% | Diagnostic; repeat before setup change |
| Right-channel THD | 0.37% | Diagnostic; repeat before setup change |
| L−R THD difference | -0.07 percentage points | Diagnostic |

### Harmonic profile

| Harmonic | Left | Right | L−R difference |
|---|---:|---:|---:|
| H2 | -50.8 dB | -49.0 dB | -1.8 dB |
| H3 | -68.1 dB | -63.3 dB | -4.8 dB |
| H4 | -74.5 dB | -67.8 dB | -6.7 dB |
| H5 | -75.2 dB | -75.5 dB | +0.3 dB |

## Measurement limitation

The source report states that the left channel's third harmonic changed most during recording. Repeat the measurement before using harmonic differences to justify cartridge adjustment.

## Source visual assets

The exact supplied originals are preserved under [`assets/source/`](assets/source/): one HEIC measurement photograph and eight PNG rotation fingerprints covering harmonic distortion, opposite-channel leakage, 1 kHz level modulation, and speed deviation for both channels. Web presentation derivatives are separate from these source files.

## Missing metadata required before final publication

- Sample ID and sample ownership or loan status
- Phono-stage gain and cartridge loading
- Tracking force, anti-skate, alignment, azimuth, and VTA/SRA settings
- Test record, edition, track, and condition
- Audio interface model confirmation and gain settings
- Capture device, sample rate, bit depth, and channel routing
- Groove Scope application version and analysis-method version
- Measurement location and timezone at city/country level only
- Capture repetition count and whether this result is representative

## Files and verification

- [Original Groove Scope PDF](report.pdf)
- [Machine-readable JSON](measurement.json)
- [SHA-256 checksums](checksums.sha256)
- [Original source assets](assets/source/)

## Recommended citation

Canonico, Michelangelo. “GS-2026-0003 — Audio-Technica AT-OC9XML / Rega P3 / Rega RB330 / Audio Research SP20 — 1 kHz Reference Check.” *Groove Scope Measurements*. Direct Sound Records, 2026. Measurement made with Groove Scope.
