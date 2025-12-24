from pathlib import Path

from open_targets.data._ftp_client import FTPClient, FTPClientListResult
from open_targets.data.download import get_dataset_download_urls
from open_targets.data.metadata.model import CroissantDatasetModel


def test_get_dataset_download_urls_filters_matches(monkeypatch) -> None:
    path = Path("test/fixture/mock/croissant.json")
    schema = CroissantDatasetModel.model_validate_json(path.read_text(encoding="utf-8"))

    def fake_traverse(self, path: str, depth=None):  # type: ignore[override]
        return FTPClientListResult(
            files=[
                f"{path}/part-00000.parquet",
                f"{path}/notes.txt",
            ],
            dirs=[],
        )

    monkeypatch.setattr(FTPClient, "traverse_directory", fake_traverse)
    urls = get_dataset_download_urls(schema, "association_by_datasource_direct")
    expected_url = (
        "https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/output/"
        "association_by_datasource_direct/part-00000.parquet"
    )
    assert urls == [expected_url]
