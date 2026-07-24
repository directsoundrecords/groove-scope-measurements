# Measurement schema

`measurement.schema.json` defines the minimum structure for Groove Scope public measurement records.

The schema is intentionally permissive in version 1.0.0 because Groove Scope is still evolving. Stable identity, provenance, status, version, setup, result, and licensing fields are required, while measurement-specific result objects may expand.

## Versioning rules

- Increase the **patch** number for clarifications that do not change field meaning.
- Increase the **minor** number when adding backward-compatible fields.
- Increase the **major** number when changing or removing existing field meanings.
- Each measurement stores the schema version used when that record was published.
