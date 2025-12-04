"""Summary: direct datatype-level summary association (TARGET -> DISEASE).

Definition for HAS_SUMMARY_ASSOCIATION_BY_DATATYPE_DIRECT edges: links TARGET to
DISEASE using precomputed direct summary scores by datatype with evidenceCount,
capturing direct association strength aggregated at datatype level in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetAssociationByDatatypeDirect,
    FieldAssociationByDatatypeDirectDatatypeId,
    FieldAssociationByDatatypeDirectDiseaseId,
    FieldAssociationByDatatypeDirectEvidenceCount,
    FieldAssociationByDatatypeDirectScore,
    FieldAssociationByDatatypeDirectTargetId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_has_summary_association_by_datatype_direct_disease: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetAssociationByDatatypeDirect,
        ),
        primary_id=NewUuidExpression(),
        source=FieldAssociationByDatatypeDirectTargetId,
        target=FieldAssociationByDatatypeDirectDiseaseId,
        label=EdgeLabel.HAS_SUMMARY_ASSOCIATION_BY_DATATYPE_DIRECT,
        properties=[
            FieldAssociationByDatatypeDirectDatatypeId,
            FieldAssociationByDatatypeDirectScore,
            FieldAssociationByDatatypeDirectEvidenceCount,
        ],
    )
)
