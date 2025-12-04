"""Summary: indirect datatype-level summary association (TARGET -> DISEASE).

Definition for HAS_SUMMARY_ASSOCIATION_BY_DATATYPE_INDIRECT edges: links TARGET
to DISEASE using precomputed indirect summary scores by datatype with
evidenceCount, capturing propagated association strength at datatype level in
the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetAssociationByDatatypeIndirect,
    FieldAssociationByDatatypeIndirectDatatypeId,
    FieldAssociationByDatatypeIndirectDiseaseId,
    FieldAssociationByDatatypeIndirectEvidenceCount,
    FieldAssociationByDatatypeIndirectScore,
    FieldAssociationByDatatypeIndirectTargetId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_has_summary_association_by_datatype_indirect_disease: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetAssociationByDatatypeIndirect,
        ),
        primary_id=NewUuidExpression(),
        source=FieldAssociationByDatatypeIndirectTargetId,
        target=FieldAssociationByDatatypeIndirectDiseaseId,
        label=EdgeLabel.HAS_SUMMARY_ASSOCIATION_BY_DATATYPE_INDIRECT,
        properties=[
            FieldAssociationByDatatypeIndirectDatatypeId,
            FieldAssociationByDatatypeIndirectScore,
            FieldAssociationByDatatypeIndirectEvidenceCount,
        ],
    )
)
