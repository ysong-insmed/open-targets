from pathlib import Path

from open_targets.data._ftp_client import FTPClient, FTPClientListResult
from open_targets.data.download import get_dataset_download_urls
from open_targets.data.metadata import load_croissant_schema_from_path


def test_get_dataset_download_urls_filters_matches(monkeypatch) -> None:
    schema = load_croissant_schema_from_path(Path("test/fixture/mock/croissant.json"))

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
