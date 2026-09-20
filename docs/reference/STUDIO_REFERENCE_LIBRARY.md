# Groove Scope Studio Reference Library

The Studio Reference Library is an application-support presentation of the canonical Groove Scope measurement records. It is not a second measurement database and does not replace the public Groove Scope catalogue or individual measurement pages.

## Endpoints

- Web preview: `https://measurements.directsoundrecords.com/groove-scope/studio/`
- Application feed: `https://measurements.directsoundrecords.com/groove-scope/studio/catalog.json`

The feed is a static HTTPS JSON file suitable for `URLSession`. It requires no authentication, cookies, or JavaScript. A native client should retain its last successfully decoded catalogue and replace it only after a new response passes schema decoding and application validation.

## Generation

Run:

```sh
python3 tools/build_studio_reference.py
python3 tools/validate_studio_catalog.py
```

The generator reads every `measurements/GS-*/measurement.json` record, applies the explicit status policy in `data/studio/reference-library-policy.json`, and writes `docs/groove-scope/studio/catalog.json`. The web preview reads that same generated feed.

The existing public catalogue is deliberately outside this generator. No existing public page is rewritten when the Studio feed is built.

## Feed versioning

`schema_version` is the API contract version. Additive, backward-compatible fields increment its minor version; renamed, removed, or semantically changed fields require a major version. `catalogue_version` is a stable digest of the canonical source records and allows an app cache to detect content changes. `generated_at` records the build time.

Each measurement provides stable identity, canonical status, dates, titles, summary, top-level absolute `hero_image_url` and `card_image_url` fields, structured image metadata, authoritative measurement and technical-record URLs, structured setup components, and a flexible `headline_metrics` array. Metrics use an identifier, display label, numeric value, unit, and the canonical classification when one exists. Measurement types are not required to expose the same metrics.

Unknown canonical values remain explicit component states such as `not_recorded` and `not_confirmed`; the generator does not guess them. Manufacturer and model remain `null` until the canonical schema provides those values separately.

## Status policy

Visibility is configured in `data/studio/reference-library-policy.json`. The initial policy includes `draft` and `published` records because the existing public Groove Scope catalogue already exposes the current draft. `superseded` and `withdrawn` records are excluded. The canonical `publication_status` is always retained in the feed and is never silently promoted.

## Images

The high-resolution hero URL reuses the existing processed measurement photograph. The generator creates a 1200 × 675 card crop under `docs/groove-scope/studio/images/` when it is absent. It uses ImageMagick when available or macOS `sips` as a fallback. Source photography remains under the canonical measurement record; manufacturer catalogue photography and synthetic product renders are not used.

## Component indexes

`components.cartridges`, `components.turntables`, `components.tonearms`, and `components.phono_stages` are generated from visible measurement records. Each entry is an index into documented systems containing that component, not an isolated component specification.

## Static hosting and access

The repository's GitHub Pages site serves the committed `docs/` directory. JSON files are served directly as static resources. Browser CORS headers are controlled by GitHub Pages; native `URLSession` is not subject to browser CORS enforcement. No server-side dependency is introduced.
