"""Summary: mouse phenotype terms observed in models (MP IDs/labels).

Definition for MOUSE_PHENOTYPE nodes: scans Mouse Phenotypes parquet to emit
mouse phenotype terms (modelPhenotypeId/label) that mouse models and inference
edges can point to, capturing in vivo phenotype observations in the KG.
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
    FieldMousePhenotypeModelPhenotypeId,
    FieldMousePhenotypeModelPhenotypeLabel,
)

node_mouse_phenotype: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetMousePhenotype),
    primary_id=FieldMousePhenotypeModelPhenotypeId,
    label="MOUSE_PHENOTYPE",
    properties=[
        FieldMousePhenotypeModelPhenotypeLabel,
    ],
)
