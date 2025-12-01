"""Definition for SUBJECT_OF edges (target → target_disease_association): links
each TARGET to its reified TARGET_DISEASE_ASSOCIATION node (evidence id) from
the Evidence parquet, binding the target endpoint of the association in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceId,
    FieldEvidenceTargetId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_subject_of_target_disease_association: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
        ),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceTargetId,
        target=FieldEvidenceId,
        label=EdgeLabel.SUBJECT_OF,
        properties=[],
    )
)
