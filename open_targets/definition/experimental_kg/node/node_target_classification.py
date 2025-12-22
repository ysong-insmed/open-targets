"""Summary: target classification nodes (label/level) grouping targets.

Definition for TARGET_CLASSIFICATION nodes: explodes target_class entries from
the Targets parquet to emit classification terms (label/level) that group targets
for categorization and navigation in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTargets,
    FieldTargetsTargetClass,
    FieldTargetsTargetClassElementLabel,
    FieldTargetsTargetClassElementLevel,
)
from open_targets.definition.experimental_kg.expression import target_classification_primary_id_expression

node_target_classification: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetTargets,
        exploded_field=FieldTargetsTargetClass,
    ),
    primary_id=target_classification_primary_id_expression,
    label="TARGET_CLASSIFICATION",
    properties=[
        FieldTargetsTargetClassElementLabel,
        FieldTargetsTargetClassElementLevel,
    ],
)
