"""Summary: TARGET_DISEASE_ASSOCIATION -> DISEASE object edges.

Definition for HAS_OBJECT edges (target_disease_association -> disease): links
each TARGET_DISEASE_ASSOCIATION node (evidence id) to the DISEASE it references,
binding the disease endpoint of the association in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceDiseaseId,
    FieldEvidenceId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_disease_association_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
        ),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceId,
        target=FieldEvidenceDiseaseId,
        label=EdgeLabel.HAS_OBJECT,
        properties=[],
    )
)
