"""Summary: direct datasource-level summary association (TARGET -> DISEASE).

Definition for HAS_SUMMARY_ASSOCIATION_BY_DATASOURCE_DIRECT edges: uses
precomputed direct association summary parquet to link each TARGET to a DISEASE
with datasource/datatype IDs, score, and evidenceCount, capturing direct source-
level association strength in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetAssociationByDatasourceDirect,
    FieldAssociationByDatasourceDirectDatasourceId,
    FieldAssociationByDatasourceDirectDatatypeId,
    FieldAssociationByDatasourceDirectDiseaseId,
    FieldAssociationByDatasourceDirectEvidenceCount,
    FieldAssociationByDatasourceDirectScore,
    FieldAssociationByDatasourceDirectTargetId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_has_summary_association_by_datasource_direct_disease: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetAssociationByDatasourceDirect,
        ),
        primary_id=NewUuidExpression(),
        source=FieldAssociationByDatasourceDirectTargetId,
        target=FieldAssociationByDatasourceDirectDiseaseId,
        label=EdgeLabel.HAS_SUMMARY_ASSOCIATION_BY_DATASOURCE_DIRECT,
        properties=[
            FieldAssociationByDatasourceDirectDatatypeId,
            FieldAssociationByDatasourceDirectDatasourceId,
            FieldAssociationByDatasourceDirectScore,
            FieldAssociationByDatasourceDirectEvidenceCount,
        ],
    )
)
