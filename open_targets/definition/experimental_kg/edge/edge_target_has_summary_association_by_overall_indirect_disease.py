"""Summary: overall indirect summary association (TARGET -> DISEASE).

Definition for HAS_SUMMARY_ASSOCIATION_BY_OVERALL_INDIRECT edges: links TARGET to
DISEASE using precomputed overall indirect summary scores with evidenceCount,
capturing propagated aggregate association strength across all sources in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetAssociationByOverallIndirect,
    FieldAssociationByOverallIndirectDiseaseId,
    FieldAssociationByOverallIndirectEvidenceCount,
    FieldAssociationByOverallIndirectScore,
    FieldAssociationByOverallIndirectTargetId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_has_summary_association_by_overall_indirect_disease: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetAssociationByOverallIndirect,
        ),
        primary_id=NewUuidExpression(),
        source=FieldAssociationByOverallIndirectTargetId,
        target=FieldAssociationByOverallIndirectDiseaseId,
        label=EdgeLabel.HAS_SUMMARY_ASSOCIATION_BY_OVERALL_INDIRECT,
        properties=[
            FieldAssociationByOverallIndirectScore,
            FieldAssociationByOverallIndirectEvidenceCount,
        ],
    )
)
