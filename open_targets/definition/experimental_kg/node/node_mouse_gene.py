"""Definition for MOUSE_GENE nodes: scans Mouse Phenotypes parquet to emit mouse
genes (Ensembl/MGI IDs, symbol) used in model annotations, anchoring mouse
orthologs that link targets to in vivo evidence in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionNodeAcquisitionDefinition,
)
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetMousePhenotypes,
    FieldMousePhenotypesTargetInModel,
    FieldMousePhenotypesTargetInModelEnsemblId,
    FieldMousePhenotypesTargetInModelMgiId,
)

node_mouse_gene: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetMousePhenotypes),
    primary_id=FieldMousePhenotypesTargetInModelEnsemblId,
    label="MOUSE_GENE",
    properties=[
        FieldMousePhenotypesTargetInModel,
        FieldMousePhenotypesTargetInModelMgiId,
    ],
)
