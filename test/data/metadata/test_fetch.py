from pathlib import Path

from open_targets.data.download import extract_croissant_filesets
from open_targets.data.metadata.model import CroissantDatasetModel


def test_extract_croissant_filesets() -> None:
    path = Path("test/fixture/mock/croissant.json")
    schema = CroissantDatasetModel.model_validate_json(path.read_text(encoding="utf-8"))
    file_sets = extract_croissant_filesets(schema)
    assert any(file_set.includes.startswith("association_by_datasource_direct/") for file_set in file_sets)
