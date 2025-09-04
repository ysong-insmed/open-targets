"""Acquisition definition that acquires edges from evidence to diseases."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetInteractionEvidence,
    FieldInteractionEvidenceTargetB,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import target_target_interaction_primary_id_expression

edge_target_has_target_target_interaction_target_b: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetInteractionEvidence),
        primary_id=NewUuidExpression(),
        source=FieldInteractionEvidenceTargetB,
        target=target_target_interaction_primary_id_expression,
        label=EdgeLabel.HAS_TARGET_TARGET_INTERACTION,
        properties=[],
    )
)
