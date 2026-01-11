"""Summary: Ensembl target gene nodes (symbol/name/biotype/functions).

Definition for TARGET nodes: scans the Targets parquet to emit Ensembl gene
targets with symbol, name, biotype, and function descriptions as the core
target entities used across drug, association, and annotation edges in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionNodeAcquisitionDefinition,
)
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetTarget,
    FieldTargetApprovedName,
    FieldTargetApprovedSymbol,
    FieldTargetBiotype,
    FieldTargetFunctionDescriptions,
    FieldTargetId,
)

node_target: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetTarget),
    primary_id=FieldTargetId,
    label="TARGET",
    properties=[
        FieldTargetApprovedSymbol,
        FieldTargetBiotype,
        FieldTargetApprovedName,
        FieldTargetFunctionDescriptions,
    ],
)
