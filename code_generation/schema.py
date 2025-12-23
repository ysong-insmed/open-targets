"""Functions for generating the schema.py file from Croissant JSON."""

from dataclasses import dataclass
from typing import Any

from pydantic.alias_generators import to_pascal, to_snake

from open_targets.data.metadata import fetch_open_targets_croissant_schema
from open_targets.data.metadata.model import CroissantFieldModel, OpenTargetsDatasetFieldType
from open_targets.data.schema_base import Dataset, Field, ScalarField, SequenceField, StructField

CLASS_PREFIX_DATASET = "Dataset"
CLASS_PREFIX_FIELD = "Field"
FIELD_ATTRIBUTE_PREFIX = "f_"
ELEMENT_FIELD_NAME = "element"

SCALAR_TYPE_MAP: dict[str, OpenTargetsDatasetFieldType] = {
    "sc:Text": OpenTargetsDatasetFieldType.STRING,
    "sc:Boolean": OpenTargetsDatasetFieldType.BOOLEAN,
    "sc:Integer": OpenTargetsDatasetFieldType.INTEGER,
    "sc:Float": OpenTargetsDatasetFieldType.FLOAT,
    "sc:Number": OpenTargetsDatasetFieldType.FLOAT,
    "sc:Date": OpenTargetsDatasetFieldType.DATE,
}


@dataclass(frozen=True)
class FieldInfo:
    """Intermediate representation of a field in Croissant JSON."""

    name: str
    data_type: OpenTargetsDatasetFieldType
    sub_fields: list["FieldInfo"]
    element: "FieldInfo | None" = None


@dataclass(frozen=True)
class LateAttribute:
    """Key and value of a class attribute that is not immediately assigned."""

    name: str
    type: str
    value: str


@dataclass(frozen=True)
class PrefixedClassName:
    """A class name with a prefix."""

    prefix: str
    name: str

    def __str__(self) -> str:
        return f"{self.prefix}{self.name}"


@dataclass(frozen=True)
class ClassInfo:
    """Information about a class to be generated."""

    name: PrefixedClassName
    late_attributes: list[LateAttribute]
    dependants: list["ClassInfo"]
    inherit_from: str


@dataclass(frozen=True)
class FieldsHandlerResult:
    """Result of handling child fields."""

    class_infos: list[ClassInfo]
    fields_attribute: LateAttribute
    field_attributes: list[LateAttribute]


def quote(s: str) -> str:
    """Add quotes around a string."""
    return f'"{s}"'


def map_croissant_data_type(data_type: str | None) -> OpenTargetsDatasetFieldType:
    """Map Croissant data types to OpenTargetsDatasetFieldType."""
    if data_type is None:
        msg = "Missing dataType for scalar field"
        raise ValueError(msg)
    if data_type not in SCALAR_TYPE_MAP:
        msg = f"Unsupported dataType: {data_type}"
        raise ValueError(msg)
    return SCALAR_TYPE_MAP[data_type]


def build_field_info(field: CroissantFieldModel) -> FieldInfo:
    """Build FieldInfo from Croissant field model."""
    sub_fields = [build_field_info(sub) for sub in field.sub_field]
    if field.repeated:
        if sub_fields:
            element = FieldInfo(
                name=ELEMENT_FIELD_NAME,
                data_type=OpenTargetsDatasetFieldType.STRUCT,
                sub_fields=sub_fields,
            )
        else:
            element = FieldInfo(
                name=ELEMENT_FIELD_NAME,
                data_type=map_croissant_data_type(field.data_type),
                sub_fields=[],
            )
        return FieldInfo(name=field.name, data_type=OpenTargetsDatasetFieldType.ARRAY, sub_fields=[], element=element)
    if sub_fields:
        return FieldInfo(name=field.name, data_type=OpenTargetsDatasetFieldType.STRUCT, sub_fields=sub_fields)
    return FieldInfo(name=field.name, data_type=map_croissant_data_type(field.data_type), sub_fields=[])


def recursive_handle_fields(fields: list[FieldInfo], owner_path: list[PrefixedClassName]) -> FieldsHandlerResult:
    """Generate and sort attributes and class information for fields."""
    field_class_infos: list[ClassInfo] = []
    field_attributes: list[LateAttribute] = []

    for field in fields:
        field_class_info = recursive_get_field_class_info(field, owner_path)
        field_class_infos.append(field_class_info)
        field_attributes.append(
            LateAttribute(
                name=f"{FIELD_ATTRIBUTE_PREFIX}{to_snake(field.name)}",
                type=f"Final[type[{quote(str(field_class_info.name))}]]",
                value=str(field_class_info.name),
            ),
        )

    field_class_infos = sorted(field_class_infos, key=lambda i: str(i.name))
    fields_attribute = LateAttribute(
        name="fields",
        type=f"Final[Sequence[type[{Field.__name__}]]]",
        value=f"[{', '.join(str(i.name) for i in field_class_infos)}]",
    )
    field_attributes = sorted(field_attributes, key=lambda i: i.name)

    return FieldsHandlerResult(
        class_infos=field_class_infos,
        fields_attribute=fields_attribute,
        field_attributes=field_attributes,
    )


def recursive_get_field_class_info(field: FieldInfo, owner_path: list[PrefixedClassName]) -> ClassInfo:
    """Convert a FieldInfo to a ClassInfo."""
    dataset_class_name = owner_path[0]
    owner_class_name = owner_path[-1]
    normalised_name = to_pascal(to_snake(field.name))
    field_class_name = PrefixedClassName(CLASS_PREFIX_FIELD, owner_class_name.name + normalised_name)
    field_path = [*owner_path, field_class_name]

    attributes = [
        LateAttribute("name", "Final[str]", quote(field.name)),
        LateAttribute(
            name="data_type",
            type=f"Final[{OpenTargetsDatasetFieldType.__name__}]",
            value=f"{OpenTargetsDatasetFieldType.__name__}.{field.data_type.name}",
        ),
        LateAttribute("dataset", f"Final[type[{Dataset.__name__}]]", str(dataset_class_name)),
        LateAttribute(
            "path",
            f"Final[Sequence[type[{Dataset.__name__}] | type[{Field.__name__}]]]",
            f"[{', '.join(str(i) for i in field_path)}]",
        ),
    ]

    dependants: list[ClassInfo] = []
    if field.data_type == OpenTargetsDatasetFieldType.STRUCT:
        result = recursive_handle_fields(field.sub_fields, field_path)
        dependants.extend(result.class_infos)
        attributes.append(result.fields_attribute)
        attributes.extend(result.field_attributes)
        inherit_from = StructField.__name__
    elif field.data_type == OpenTargetsDatasetFieldType.ARRAY:
        if field.element is None:
            msg = f"Array field {field.name} is missing element info"
            raise ValueError(msg)
        element_class_info = recursive_get_field_class_info(field.element, field_path)
        dependants.append(element_class_info)
        attributes.append(
            LateAttribute(
                name="element",
                type=f"Final[type[{quote(str(element_class_info.name))}]]",
                value=str(element_class_info.name),
            ),
        )
        inherit_from = SequenceField.__name__
    else:
        inherit_from = ScalarField.__name__

    return ClassInfo(
        name=field_class_name,
        late_attributes=attributes,
        dependants=dependants,
        inherit_from=inherit_from,
    )


def flatten_class_infos(class_infos: list[ClassInfo]) -> list[ClassInfo]:
    """Flatten nested class infos for deterministic output."""
    flattened: list[ClassInfo] = []

    def visit(info: ClassInfo) -> None:
        flattened.append(info)
        for dependant in sorted(info.dependants, key=lambda i: str(i.name)):
            visit(dependant)

    for info in sorted(class_infos, key=lambda i: str(i.name)):
        visit(info)
    return flattened


def create_schema_render_context() -> dict[str, Any]:
    """Return a jinja context for the schema.py file."""
    schema = fetch_open_targets_croissant_schema()

    class_infos: list[ClassInfo] = []

    for record_set in schema.record_set:
        dataset_class_name = PrefixedClassName(CLASS_PREFIX_DATASET, to_pascal(to_snake(record_set.name)))
        attributes = [LateAttribute(name="id", type="Final[str]", value=quote(record_set.name))]
        dependants: list[ClassInfo] = []

        fields = [build_field_info(field) for field in record_set.field]
        result = recursive_handle_fields(fields, [dataset_class_name])
        dependants.extend(result.class_infos)
        attributes.append(result.fields_attribute)
        attributes.extend(result.field_attributes)

        class_infos.append(
            ClassInfo(
                name=dataset_class_name,
                late_attributes=attributes,
                dependants=dependants,
                inherit_from=Dataset.__name__,
            ),
        )

    return {"class_infos": flatten_class_infos(class_infos)}
