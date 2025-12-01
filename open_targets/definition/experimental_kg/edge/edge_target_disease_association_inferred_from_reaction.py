"""Definition for INFERRED_FROM edges (association → reaction): filters Reactome
evidence to link each TARGET_DISEASE_ASSOCIATION node (evidence id) to the
REACTION it was inferred from, capturing reaction-level inference in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceId,
    FieldEvidenceReactionId,
    FieldEvidenceSourceId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_disease_association_inferred_from_reaction: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "reactome"),
        ),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceId,
        target=FieldEvidenceReactionId,
        label=EdgeLabel.INFERRED_FROM,
        properties=[],
    )
)
