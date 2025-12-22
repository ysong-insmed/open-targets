"""Summary: Reactome reaction nodes (id/name) for pathway inference.

Definition for REACTION nodes: filters Evidence parquet to reactome source to emit
reaction entries (id/name) used in pathway hierarchies and inference edges in the
KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceReactionId,
    FieldEvidenceReactionName,
    FieldEvidenceSourceId,
)

node_reaction: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetEvidence,
        predicate=EqualityExpression(FieldEvidenceSourceId, "reactome"),
    ),
    primary_id=FieldEvidenceReactionId,
    label="REACTION",
    properties=[
        FieldEvidenceReactionName,
    ],
)
