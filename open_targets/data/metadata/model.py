"""Data models for Open Targets Croissant metadata."""

from enum import Enum
from typing import Literal, TypeAlias

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class Key(str, Enum):
    """Key for a Croissant metadata entry."""

    ID = "@id"
    TYPE = "@type"
    CONTENT_URL = "contentUrl"
    RECORD_SET = "recordSet"


class ConfiguredBaseModel(BaseModel):
    """Base model with shared configuration."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="ignore",
        frozen=True,
    )


class OpenTargetsDatasetFieldType(str, Enum):
    """Data type of a dataset field derived from Croissant JSON."""

    BOOLEAN = "boolean"
    INTEGER = "integer"
    FLOAT = "float"
    STRING = "string"
    DATE = "date"
    ARRAY = "array"
    STRUCT = "struct"


class CroissantFieldModel(ConfiguredBaseModel):
    """Data model of a field in a Croissant record set."""

    name: str
    description: str | None = None
    data_type: str | None = None
    repeated: bool = False
    sub_field: list["CroissantFieldModel"] = Field(default_factory=list)


class CroissantRecordSetModel(ConfiguredBaseModel):
    """Data model of a Croissant record set."""

    id: str | None = Field(default=None, alias=Key.ID.value)
    name: str
    description: str | None = None
    field: list[CroissantFieldModel] = Field(default_factory=list)


class CroissantFileSetModel(ConfiguredBaseModel):
    """Data model of a Croissant FileSet entry."""

    type: Literal["cr:FileSet"] = Field(alias=Key.TYPE.value)
    id: str = Field(alias=Key.ID.value)
    name: str | None = None
    description: str | None = None
    includes: str
    encoding_format: str | None = None


class CroissantFileObjectModel(ConfiguredBaseModel):
    """Data model of a Croissant FileObject entry."""

    type: Literal["cr:FileObject"] = Field(alias=Key.TYPE.value)
    id: str = Field(alias=Key.ID.value)
    name: str | None = None
    description: str | None = None
    content_url: str | None = Field(default=None, alias=Key.CONTENT_URL.value)
    encoding_format: str | None = None


CroissantDistributionModel: TypeAlias = CroissantFileSetModel | CroissantFileObjectModel


class CroissantDatasetModel(ConfiguredBaseModel):
    """Top-level Croissant dataset model."""

    record_set: list[CroissantRecordSetModel] = Field(default_factory=list)
    distribution: list[CroissantDistributionModel] = Field(default_factory=list)


CroissantFieldModel.model_rebuild()
CroissantDatasetModel.model_rebuild()
