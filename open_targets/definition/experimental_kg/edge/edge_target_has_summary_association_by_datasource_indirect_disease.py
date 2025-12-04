"""Summary: indirect datasource-level summary association (TARGET -> DISEASE).

Definition for HAS_SUMMARY_ASSOCIATION_BY_DATASOURCE_INDIRECT edges: uses
precomputed indirect association summary parquet to link TARGET to DISEASE with
datasource/datatype IDs, score, and evidenceCount, capturing ontology-propagated
source-level association strength in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetAssociationByDatasourceIndirect,
    FieldAssociationByDatasourceIndirectDatasourceId,
    FieldAssociationByDatasourceIndirectDatatypeId,
    FieldAssociationByDatasourceIndirectDiseaseId,
    FieldAssociationByDatasourceIndirectEvidenceCount,
    FieldAssociationByDatasourceIndirectScore,
    FieldAssociationByDatasourceIndirectTargetId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_has_summary_association_by_datasource_indirect_disease: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetAssociationByDatasourceIndirect,
        ),
        primary_id=NewUuidExpression(),
        source=FieldAssociationByDatasourceIndirectTargetId,
        target=FieldAssociationByDatasourceIndirectDiseaseId,
        label=EdgeLabel.HAS_SUMMARY_ASSOCIATION_BY_DATASOURCE_INDIRECT,
        properties=[
            FieldAssociationByDatasourceIndirectDatatypeId,
            FieldAssociationByDatasourceIndirectDatasourceId,
            FieldAssociationByDatasourceIndirectScore,
            FieldAssociationByDatasourceIndirectEvidenceCount,
        ],
    )
)
