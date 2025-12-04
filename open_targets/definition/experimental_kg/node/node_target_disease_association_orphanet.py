"""Summary: Orphanet expert-curated rare disease gene-disease assertions.

Definition for TARGET_DISEASE_ASSOCIATION_ORPHANET nodes: filters Evidence
parquet to orphanet rare-disease curation. Orphanet experts review clinical
genetics for rare diseases and assert gene-disease links, noting allele origins,
allelic requirements, direction on trait, and functional consequence. Records
keep disease/target IDs, confidence, and scores. Inference: rare disease cases
-> expert curation of causal gene -> recorded as curated rare-disease evidence in
the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceAlleleOrigins,
    FieldEvidenceAllelicRequirements,
    FieldEvidenceDirectionOnTrait,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceId,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceTargetFromSourceId,
    FieldEvidenceVariantFunctionalConsequenceId,
)

node_target_disease_association_orphanet: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "orphanet"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_ORPHANET",
        properties=[
            FieldEvidenceAlleleOrigins,
            FieldEvidenceAllelicRequirements,
            FieldEvidenceDirectionOnTrait,
            FieldEvidenceDiseaseFromSource,
            FieldEvidenceDiseaseFromSourceId,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceScore,
            FieldEvidenceTargetFromSourceId,
            FieldEvidenceVariantFunctionalConsequenceId,
        ],
    )
)
