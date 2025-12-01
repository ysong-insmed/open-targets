"""Definition for TARGET_DISEASE_ASSOCIATION_EUROPEPMC nodes: filters Evidence
parquet to europepmc source to emit text-mined associations with mapped disease
ID, target ID, resource score, and score, capturing literature-derived evidence
in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceResourceScore,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceTargetFromSourceId,
)

node_target_disease_association_europepmc: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetEvidence,
        predicate=EqualityExpression(FieldEvidenceSourceId, "europepmc"),
    ),
    primary_id=FieldEvidenceId,
    label="TARGET_DISEASE_ASSOCIATION_EUROPEPMC",
    properties=[
        FieldEvidenceDiseaseFromSourceMappedId,
        FieldEvidenceResourceScore,
        FieldEvidenceScore,
        FieldEvidenceTargetFromSourceId,
    ],
)
