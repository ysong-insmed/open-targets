from pathlib import Path
from typing import Final
from urllib.request import urlopen

from open_targets.config import METADATA_URL
from open_targets.data.metadata.model import CroissantDatasetModel, CroissantFileSetModel

CROISSANT_URL: Final = METADATA_URL


def load_croissant_schema_from_path(path: Path) -> CroissantDatasetModel:
    """Load Croissant schema JSON from a local path."""
    return CroissantDatasetModel.model_validate_json(path.read_text(encoding="utf-8"))


def fetch_open_targets_croissant_schema() -> CroissantDatasetModel:
    """Download Croissant schema JSON from the Open Targets FTP server."""
    with urlopen(METADATA_URL, timeout=30) as response:  # noqa: S310
        json_bytes = response.read()
    return CroissantDatasetModel.model_validate_json(json_bytes)


def extract_croissant_filesets(schema: CroissantDatasetModel) -> list[CroissantFileSetModel]:
    """Extract FileSet entries from a Croissant dataset schema."""
    file_sets: list[CroissantFileSetModel] = []
    for item in schema.distribution:
        if isinstance(item, CroissantFileSetModel):
            file_sets.append(item)
    return file_sets
