"""Acquisition definition that acquires nodes of disease cross references."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTargets,
    FieldTargetsDbXrefs,
)
from open_targets.definition.experimental_kg.namespace import Namespace
from open_targets.definition.experimental_kg.target_database_cross_reference_value_expression import (
    target_database_cross_reference_value_expression,
)
from open_targets.definition.helper import get_simple_value_node_definition

node_disease_cross_reference: Final[AcquisitionDefinition[NodeInfo]] = get_simple_value_node_definition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetTargets,
        exploded_field=FieldTargetsDbXrefs,
    ),
    namespace=Namespace.DATABASE_CROSS_REFERENCE,
    value_expression=target_database_cross_reference_value_expression,
    label="DATABASE_CROSS_REFERENCE",
)
