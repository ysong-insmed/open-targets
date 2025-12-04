"""Summary: TARGET -> TARGET_TARGET_INTERACTION edges (participant A).

Definition for HAS_TARGET_TARGET_INTERACTION edges (target A): links a TARGET to
a TARGET_TARGET_INTERACTION node using participant A from interaction evidence
(where participant B is present), enabling traversal from the target to the
interaction record in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression, NotExpression
from open_targets.data.schema import (
    DatasetInteractionEvidence,
    FieldInteractionEvidenceTargetA,
    FieldInteractionEvidenceTargetB,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import target_target_interaction_primary_id_expression

edge_target_has_target_target_interaction_target_a: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetInteractionEvidence,
            # Only target B could be NULL
            predicate=NotExpression(EqualityExpression(FieldInteractionEvidenceTargetB, None)),
        ),
        primary_id=NewUuidExpression(),
        source=FieldInteractionEvidenceTargetA,
        target=target_target_interaction_primary_id_expression,
        label=EdgeLabel.HAS_TARGET_TARGET_INTERACTION,
        properties=[],
    )
)
