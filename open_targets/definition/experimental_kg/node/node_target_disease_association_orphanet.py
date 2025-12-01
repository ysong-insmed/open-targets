"""Definition for TARGET_DISEASE_ASSOCIATION_ORPHANET nodes: filters Evidence
parquet to orphanet source to emit rare disease associations with disease IDs,
direction on trait, allelic requirements, variant functional consequence,
confidence/score, allele origins, target IDs, capturing Orphanet curation in the
KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceAlleleOrigins,
    FieldEvidenceConfidence,
    FieldEvidenceDirectionOnTrait,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceId,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceTargetFromSource,
    FieldEvidenceTargetFromSourceId,
    FieldEvidenceVariantEffect,
    FieldEvidenceVariantFunctionalConsequenceId,
)

node_target_disease_association_orphanet: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetEvidence,
        predicate=EqualityExpression(FieldEvidenceSourceId, "orphanet"),
    ),
    primary_id=FieldEvidenceId,
    label="TARGET_DISEASE_ASSOCIATION_ORPHANET",
    properties=[
        FieldEvidenceAlleleOrigins,
        FieldEvidenceConfidence,
        FieldEvidenceDirectionOnTrait,
        FieldEvidenceDiseaseFromSource,
        FieldEvidenceDiseaseFromSourceId,
        FieldEvidenceDiseaseFromSourceMappedId,
        FieldEvidenceScore,
        FieldEvidenceTargetFromSource,
        FieldEvidenceTargetFromSourceId,
        FieldEvidenceVariantEffect,
        FieldEvidenceVariantFunctionalConsequenceId,
    ],
)
