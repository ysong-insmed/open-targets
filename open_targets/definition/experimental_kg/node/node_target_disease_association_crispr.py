"""Definition for TARGET_DISEASE_ASSOCIATION_CRISPR nodes: filters Evidence
parquet to crispr source to emit CRISPR screen associations with disease IDs,
target IDs/symbols, resource score, and score, representing functional genomic
screen evidence in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceResourceScore,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceTargetFromSource,
    FieldEvidenceTargetFromSourceId,
)

node_target_disease_association_crispr: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetEvidence,
        predicate=EqualityExpression(FieldEvidenceSourceId, "crispr"),
    ),
    primary_id=FieldEvidenceId,
    label="TARGET_DISEASE_ASSOCIATION_CRISPR",
    properties=[
        FieldEvidenceDiseaseFromSource,
        FieldEvidenceDiseaseFromSourceMappedId,
        FieldEvidenceResourceScore,
        FieldEvidenceScore,
        FieldEvidenceTargetFromSource,
        FieldEvidenceTargetFromSourceId,
    ],
)
