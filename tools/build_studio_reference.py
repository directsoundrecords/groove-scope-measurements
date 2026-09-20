#!/usr/bin/env python3
"""Generate the application-facing Groove Scope Studio Reference Library feed."""
from studio_catalog import build_catalog, write_catalog


if __name__ == "__main__":
    catalog = build_catalog()
    write_catalog(catalog)
    print(
        f"Built Studio Reference Library {catalog['catalogue_version']} "
        f"with {catalog['measurement_count']} measurement(s)."
    )
