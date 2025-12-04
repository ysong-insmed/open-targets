"""Summary: Gene Ontology term nodes for functional annotation.

Definition for GO_TERM nodes: scans the GO parquet to emit Gene Ontology terms
with IDs and names, providing functional annotation entities that targets and
pathways can link to in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetGo,
    FieldGoId,
    FieldGoName,
)

node_go_term: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetGo),
    primary_id=FieldGoId,
    label="GO_TERM",
    properties=[
        FieldGoName,
    ],
)
