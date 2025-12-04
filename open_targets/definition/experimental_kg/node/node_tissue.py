"""Summary: tissue concepts (id/name) for CRISPR cell line context.

Definition for TISSUE nodes: explodes CRISPR evidence cell line tissues from the
Evidence parquet (sourceId==crispr) to emit tissue concepts (id/name) used as
anatomical context for cell lines in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceDiseaseCellLines,
    FieldEvidenceDiseaseCellLinesElementTissue,
    FieldEvidenceDiseaseCellLinesElementTissueId,
    FieldEvidenceSourceId,
)

node_tissue: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetEvidence,
        exploded_field=FieldEvidenceDiseaseCellLines,
        predicate=EqualityExpression(FieldEvidenceSourceId, "crispr"),
    ),
    primary_id=FieldEvidenceDiseaseCellLinesElementTissueId,
    label="TISSUE",
    properties=[
        FieldEvidenceDiseaseCellLinesElementTissue,
    ],
)
