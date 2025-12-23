"""Module providing functions to download Open Targets data."""

from fnmatch import fnmatch
from pathlib import PurePosixPath
from urllib.parse import urlparse

from open_targets.data._ftp_client import FTPClient
from open_targets.data.metadata.model import CroissantDatasetModel, CroissantFileObjectModel, CroissantFileSetModel

FTP_LOCATION_ID = "ftp-location"


def extract_croissant_filesets(schema: CroissantDatasetModel) -> list[CroissantFileSetModel]:
    """Extract FileSet entries from a Croissant dataset schema."""
    return [item for item in schema.distribution if isinstance(item, CroissantFileSetModel)]


def find_dataset_fileset(schema: CroissantDatasetModel, dataset_name: str) -> CroissantFileSetModel:
    """Return the FileSet that matches a dataset name."""
    for file_set in extract_croissant_filesets(schema):
        if file_set.includes.startswith(f"{dataset_name}/"):
            return file_set
    msg = f"No FileSet found for dataset: {dataset_name}"
    raise ValueError(msg)


def get_ftp_base_url(schema: CroissantDatasetModel) -> str:
    """Return the FTP base URL from Croissant metadata."""
    for item in schema.distribution:
        if isinstance(item, CroissantFileObjectModel) and item.id == FTP_LOCATION_ID and item.content_url:
            return item.content_url.rstrip("/")
    msg = "Croissant metadata is missing ftp-location contentUrl"
    raise ValueError(msg)


def get_dataset_download_urls(schema: CroissantDatasetModel, dataset_name: str) -> list[str]:
    """Get a list of download URLs of all files in a dataset."""
    file_set = find_dataset_fileset(schema, dataset_name)
    base_url = get_ftp_base_url(schema)
    parsed = urlparse(base_url)
    if not parsed.netloc or not parsed.path:
        msg = f"Invalid FTP base URL: {base_url}"
        raise ValueError(msg)

    includes_path = PurePosixPath(file_set.includes)
    directory_path = PurePosixPath(parsed.path) / includes_path.parent
    discovered_files = FTPClient(parsed.netloc).traverse_directory(str(directory_path)).files
    pattern = str(PurePosixPath(parsed.path) / includes_path)
    return [f"https://{parsed.netloc}{file_path}" for file_path in discovered_files if fnmatch(file_path, pattern)]
