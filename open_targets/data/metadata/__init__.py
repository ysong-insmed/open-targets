"""Open Targets Platform metadata retrieval."""

from open_targets.data.metadata._fetch import (
    extract_croissant_filesets,
    fetch_open_targets_croissant_schema,
    load_croissant_schema_from_path,
)

__all__ = [
    "extract_croissant_filesets",
    "fetch_open_targets_croissant_schema",
    "load_croissant_schema_from_path",
]
