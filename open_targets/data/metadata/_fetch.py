from urllib.request import urlopen

from open_targets.config import METADATA_URL
from open_targets.data.metadata.model import CroissantDatasetModel


def fetch_open_targets_croissant_schema() -> CroissantDatasetModel:
    """Download Croissant schema JSON from the Open Targets FTP server."""
    with urlopen(METADATA_URL, timeout=30) as response:  # noqa: S310
        json_bytes = response.read()
    return CroissantDatasetModel.model_validate_json(json_bytes)
