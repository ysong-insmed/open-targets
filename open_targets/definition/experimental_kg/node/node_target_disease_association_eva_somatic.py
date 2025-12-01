"""Definition for TARGET_DISEASE_ASSOCIATION_EVA_SOMATIC nodes: filters Evidence
parquet to eva_somatic source to emit somatic variant associations with variant
IDs (HGVS, RS, functional consequence), disease IDs, direction/allelic
requirements, clinical significance, allele origins, cohort phenotypes,
confidence/score, release date, study ID, and target IDs, capturing somatic
variant evidence in the KG."""

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

node_target_disease_association_eva_somatic: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "eva_somatic"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_EVA_SOMATIC",
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
)
