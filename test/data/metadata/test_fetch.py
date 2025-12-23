from pathlib import Path

from open_targets.data.metadata import extract_croissant_filesets, load_croissant_schema_from_path


def test_extract_croissant_filesets() -> None:
    schema = load_croissant_schema_from_path(Path("test/fixture/mock/croissant.json"))
    file_sets = extract_croissant_filesets(schema)
    assert any(file_set.includes.startswith("association_by_datasource_direct/") for file_set in file_sets)
