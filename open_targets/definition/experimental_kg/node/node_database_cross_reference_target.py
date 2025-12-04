"""Summary: target cross-reference nodes (hashed ID, normalized value property).

Definition for DATABASE_CROSS_REFERENCE nodes (target xrefs): explodes `dbXrefs`
from the Targets parquet, hashes each string under the `database_cross_reference`
namespace for the primary ID, and writes the raw string to property `value` so
TARGET nodes surface external gene identifiers.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTargets,
    FieldTargetsDbXrefs,
)
from open_targets.definition.experimental_kg.constant import NodeLabel
from open_targets.definition.experimental_kg.expression import (
    database_cross_reference_target_primary_id_expression,
    database_cross_reference_target_value_expression,
)

node_database_cross_reference_target: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetTargets,
        exploded_field=FieldTargetsDbXrefs,
    ),
    primary_id=database_cross_reference_target_primary_id_expression,
    label=NodeLabel.DATABASE_CROSS_REFERENCE,
    properties=[
        ("value", database_cross_reference_target_value_expression),
    ],
)
