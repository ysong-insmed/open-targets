"""Definition for BELONGS_TO edges: explodes target_class entries to link each
TARGET to its TARGET_CLASSIFICATION node, capturing target grouping in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTargets,
    FieldTargetsId,
    FieldTargetsTargetClass,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import target_classification_primary_id_expression

edge_target_belongs_to_target_classification: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetTargets,
            exploded_field=FieldTargetsTargetClass,
        ),
        primary_id=NewUuidExpression(),
        source=FieldTargetsId,
        target=target_classification_primary_id_expression,
        label=EdgeLabel.BELONGS_TO,
        properties=[],
    )
)
