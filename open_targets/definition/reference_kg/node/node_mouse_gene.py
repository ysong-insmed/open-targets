"""Summary: mouse gene orthologs used in model evidence (Ensembl/MGI).

Definition for MOUSE_GENE nodes: scans Mouse Phenotypes parquet to emit mouse
genes (Ensembl/MGI IDs, symbol) used in model annotations, anchoring mouse
orthologs that link targets to in vivo evidence in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionNodeAcquisitionDefinition,
)
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetMousePhenotype,
    FieldMousePhenotypeTargetInModel,
    FieldMousePhenotypeTargetInModelEnsemblId,
    FieldMousePhenotypeTargetInModelMgiId,
)

node_mouse_gene: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetMousePhenotype),
    primary_id=FieldMousePhenotypeTargetInModelEnsemblId,
    label="MOUSE_GENE",
    properties=[
        FieldMousePhenotypeTargetInModel,
        FieldMousePhenotypeTargetInModelMgiId,
    ],
)
