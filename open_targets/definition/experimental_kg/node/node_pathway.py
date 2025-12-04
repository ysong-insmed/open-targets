"""Summary: Reactome pathway nodes (ids/labels) for hierarchy/annotation.

Definition for PATHWAY nodes: scans the Reactome parquet to emit pathway terms
with IDs and labels, forming the pathway hierarchy and annotation targets for
proteins/associations in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetReactome,
    FieldReactomeId,
    FieldReactomeLabel,
)

node_pathway: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetReactome),
    primary_id=FieldReactomeId,
    label="PATHWAY",
    properties=[
        FieldReactomeLabel,
    ],
)
