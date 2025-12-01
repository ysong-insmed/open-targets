"""Definition for TARGET_DISEASE_ASSOCIATION_EVA nodes: filters Evidence parquet
to eva source to emit germline ClinVar/EVA associations with variant IDs (HGVS,
RS, functional consequence), disease IDs, direction/allelic requirements,
clinical significance, allele origins, cohort phenotypes, confidence/score,
release date, study ID, and target IDs, capturing curated germline variant
evidence in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceAlleleOrigins,
    FieldEvidenceAllelicRequirements,
    FieldEvidenceClinicalSignificances,
    FieldEvidenceCohortPhenotypes,
    FieldEvidenceConfidence,
    FieldEvidenceDirectionOnTrait,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceId,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceReleaseDate,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceStudyId,
    FieldEvidenceTargetFromSourceId,
    FieldEvidenceVariantEffect,
    FieldEvidenceVariantFunctionalConsequenceId,
    FieldEvidenceVariantHgvsId,
    FieldEvidenceVariantId,
    FieldEvidenceVariantRsId,
)

node_target_disease_association_eva: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetEvidence,
        predicate=EqualityExpression(FieldEvidenceSourceId, "eva"),
    ),
    primary_id=FieldEvidenceId,
    label="TARGET_DISEASE_ASSOCIATION_EVA",
    properties=[
        FieldEvidenceAlleleOrigins,
        FieldEvidenceAllelicRequirements,
        FieldEvidenceClinicalSignificances,
        FieldEvidenceCohortPhenotypes,
        FieldEvidenceConfidence,
        FieldEvidenceDirectionOnTrait,
        FieldEvidenceDiseaseFromSource,
        FieldEvidenceDiseaseFromSourceId,
        FieldEvidenceDiseaseFromSourceMappedId,
        FieldEvidenceReleaseDate,
        FieldEvidenceScore,
        FieldEvidenceStudyId,
        FieldEvidenceTargetFromSourceId,
        FieldEvidenceVariantEffect,
        FieldEvidenceVariantFunctionalConsequenceId,
        FieldEvidenceVariantHgvsId,
        FieldEvidenceVariantId,
        FieldEvidenceVariantRsId,
    ],
)
