from pathlib import Path

from open_targets.data.metadata.model import CroissantDatasetModel


def test_croissant_dataset_model() -> None:
    path = Path("test/fixture/mock/croissant.json")
    schema = CroissantDatasetModel.model_validate_json(path.read_text(encoding="utf-8"))
    assert schema.record_set
