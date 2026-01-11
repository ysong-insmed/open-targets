"""Summary: overall direct summary association (TARGET -> DISEASE).

Definition for HAS_SUMMARY_ASSOCIATION_BY_OVERALL_DIRECT edges: links TARGET to
DISEASE using precomputed overall direct summary scores with evidenceCount,
capturing direct aggregate association strength across all sources in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetAssociationOverallDirect,
    FieldAssociationOverallDirectDiseaseId,
    FieldAssociationOverallDirectEvidenceCount,
    FieldAssociationOverallDirectScore,
    FieldAssociationOverallDirectTargetId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_target_has_summary_association_by_overall_direct_disease: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetAssociationOverallDirect,
        ),
        primary_id=NewUuidExpression(),
        source=FieldAssociationOverallDirectTargetId,
        target=FieldAssociationOverallDirectDiseaseId,
        label=EdgeLabel.HAS_SUMMARY_ASSOCIATION_BY_OVERALL_DIRECT,
        properties=[
            FieldAssociationOverallDirectScore,
            FieldAssociationOverallDirectEvidenceCount,
        ],
    )
)
