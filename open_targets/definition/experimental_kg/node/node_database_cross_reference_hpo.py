"""Acquisition definition that acquires nodes of disease cross references."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetHpo,
    FieldHpoDbXRefs,
    FieldHpoDbXRefsElement,
)
from open_targets.definition.experimental_kg.namespace import Namespace
from open_targets.definition.helper import get_simple_value_node_definition

node_disease_cross_reference: Final[AcquisitionDefinition[NodeInfo]] = get_simple_value_node_definition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetHpo,
        exploded_field=FieldHpoDbXRefs,
    ),
    namespace=Namespace.DATABASE_CROSS_REFERENCE,
    value_expression=FieldHpoDbXRefsElement,
    label="DATABASE_CROSS_REFERENCE",
)
