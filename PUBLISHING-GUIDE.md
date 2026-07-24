# Publishing guide

This guide assumes the intended GitHub organisation is `DirectSoundRecords` and the repository is `groove-scope-measurements`. GitHub account and organisation names are case-insensitive in URLs, but the displayed capitalisation may differ.

## Before uploading

1. Confirm that the GitHub organisation name `DirectSoundRecords` is available. If you use a different owner name, replace every occurrence of `DirectSoundRecords` and `directsoundrecords.github.io` in this repository before enabling GitHub Pages.
2. Complete the missing setup fields in `measurements/GS-2026-0001/measurement.json` and its `README.md`.
3. Add the Groove Scope application version and analysis-method version.
4. Change `publication_status` from `draft` to `published`, change `record_version` to `1.0.0`, add `date_published`, and update `data/index.csv` only after the metadata is complete.
5. Recreate `checksums.sha256` after any file changes.

## Create the Direct Sound Records organisation

Using a GitHub organisation is recommended because the archive belongs to a long-term brand rather than one personal account. Michelangelo Canonico should remain clearly named as creator, lead measurer, and organisation owner.

Suggested organisation profile:

- **Name:** Direct Sound Records
- **Handle:** `DirectSoundRecords`
- **Description:** `Direct Sound Records develops reference audio recordings, measurement research, Groove Scope and Resonance Lab.`
- **Website:** `https://directsoundrecords.com/`
- **Location:** `London–Rome`

## Create the repository

- **Owner:** DirectSoundRecords
- **Repository name:** `groove-scope-measurements`
- **Description:** `Open vinyl playback measurements created with Groove Scope by Michelangelo Canonico and Direct Sound Records.`
- **Visibility:** Public
- Do **not** initialise it with another README, licence, or `.gitignore`, because this package already contains those files.

## Upload using the browser

1. Open the empty repository.
2. Select **Add file → Upload files**.
3. Unzip the starter package on your Mac.
4. Open the `groove-scope-measurements` folder and drag **all files and folders inside it** into the GitHub upload area. Do not upload the outer ZIP file.
5. Use the commit message: `Publish Groove Scope measurement GS-2026-0001`.
6. Commit directly to the `main` branch for this first publication.

## Repository settings

### About section

Add these topics:

`groove-scope`, `direct-sound-records`, `michelangelo-canonico`, `resonance-lab`, `vinyl`, `turntable`, `cartridge`, `audio-measurement`, `wow-and-flutter`, `crosstalk`, `distortion`, `dataset`

Set the website field to the GitHub Pages URL after Pages is enabled.

### GitHub Pages

1. Open **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Choose branch `main` and folder `/docs`.
4. Save.
5. Wait for the deployment and open the published URL.
6. Confirm that `sitemap.xml`, `robots.txt`, and `llms.txt` also load from the Pages site. The `llms.txt` file is an optional emerging convention, not a guarantee of AI indexing.

Expected URL if the organisation is `DirectSoundRecords`:

`https://directsoundrecords.github.io/groove-scope-measurements/`

### Social preview

Upload a 1280 × 640 pixel social image that includes:

- Direct Sound Records logo
- Groove Scope Measurements
- “Open vinyl playback measurement archive”
- Michelangelo Canonico

Avoid filling the image with small numerical results; the preview needs to remain readable on mobile.

### Citation

GitHub will detect `CITATION.cff` on the default branch and display a **Cite this repository** control. Confirm that the author is Michelangelo Canonico, the type is Dataset, and the repository URL is correct.

### First release

Create a GitHub Release after the record is complete:

- **Tag:** `v1.0.0`
- **Release title:** `Groove Scope Measurements v1.0.0 — First public record`
- **Release text:** `First public release of the Direct Sound Records Groove Scope measurement archive, including GS-2026-0001.`

Attach no duplicate files unless needed; GitHub automatically provides source archives. Later, connecting releases to Zenodo can create citable DOI-backed snapshots.

## Link the archive from Direct Sound Records

Create a page at a stable website address, ideally:

`https://directsoundrecords.com/apps/groove-scope-measurements/`

That page should contain original explanatory text, not merely an embedded GitHub frame. Include:

- the full names Direct Sound Records, Michelangelo Canonico, Groove Scope, and Resonance Lab;
- a concise description of what is measured;
- a visible link to the GitHub repository and GitHub Pages archive;
- the latest measurement IDs;
- a short methodology and limitations statement;
- Dataset JSON-LD structured data;
- a canonical URL and inclusion in the website sitemap.

Cross-linking the official website and GitHub helps search systems understand that the dataset, apps, person, and organisation are related entities.

## Future measurement workflow

For each new measurement:

1. Create the next immutable ID, for example `GS-2026-0002`.
2. Copy the previous measurement folder as a structural template, not as a source of values.
3. Replace every value and metadata field from the new session.
4. Preserve the original Groove Scope report as `report.pdf`.
5. Export or transcribe the structured JSON.
6. Add a human-readable `README.md` with context and limitations.
7. Add the row to `data/index.csv`.
8. Recalculate checksums.
9. Validate JSON against the schema.
10. Commit with a precise message, such as `Add GS-2026-0002 — [cartridge and test name]`.
11. Update the GitHub Pages index.
12. Create periodic releases rather than a release for every tiny correction.

## When external submissions open

Do not accept anonymous PDFs dropped into the repository. Use a structured submission form and moderation process. Require complete setup metadata, app and method versions, original report, repetition information, contributor identity or stable pseudonym, permission to publish, and agreement to the licence. Mark records as `community_submitted` and distinguish them from `direct_sound_records_reference` measurements.
