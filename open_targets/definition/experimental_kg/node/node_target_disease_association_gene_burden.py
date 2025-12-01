"""Definition for TARGET_DISEASE_ASSOCIATION_GENE_BURDEN nodes: filters Evidence
parquet to gene_burden source to emit rare-variant burden associations with
beta/OR stats, p-values, ancestry/cohort info, allelic requirements, disease/
target IDs, study metadata, and scores, capturing burden-test genetic evidence
in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceAllelicRequirements,
    FieldEvidenceAncestry,
    FieldEvidenceAncestryId,
    FieldEvidenceBeta,
    FieldEvidenceBetaConfidenceIntervalLower,
    FieldEvidenceBetaConfidenceIntervalUpper,
    FieldEvidenceCohortId,
    FieldEvidenceDirectionOnTrait,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceId,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceOddsRatio,
    FieldEvidenceOddsRatioConfidenceIntervalLower,
    FieldEvidenceOddsRatioConfidenceIntervalUpper,
    FieldEvidenceProjectId,
    FieldEvidencePValueExponent,
    FieldEvidencePValueMantissa,
    FieldEvidenceReleaseVersion,
    FieldEvidenceResourceScore,
    FieldEvidenceScore,
    FieldEvidenceSex,
    FieldEvidenceSourceId,
    FieldEvidenceStatisticalMethod,
    FieldEvidenceStatisticalMethodOverview,
    FieldEvidenceStudyCases,
    FieldEvidenceStudyCasesWithQualifyingVariants,
    FieldEvidenceStudySampleSize,
    FieldEvidenceTargetFromSourceId,
    FieldEvidenceVariantEffect,
)

node_target_disease_association_gene_burden: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "gene_burden"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_GENE_BURDEN",
        properties=[
            FieldEvidenceAllelicRequirements,
            FieldEvidenceAncestry,
            FieldEvidenceAncestryId,
            FieldEvidenceBeta,
            FieldEvidenceBetaConfidenceIntervalLower,
            FieldEvidenceBetaConfidenceIntervalUpper,
            FieldEvidenceCohortId,
            FieldEvidenceDirectionOnTrait,
            FieldEvidenceDiseaseFromSource,
            FieldEvidenceDiseaseFromSourceId,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceOddsRatio,
            FieldEvidenceOddsRatioConfidenceIntervalLower,
            FieldEvidenceOddsRatioConfidenceIntervalUpper,
            FieldEvidencePValueExponent,
            FieldEvidencePValueMantissa,
            FieldEvidenceProjectId,
            FieldEvidenceReleaseVersion,
            FieldEvidenceResourceScore,
            FieldEvidenceScore,
            FieldEvidenceSex,
            FieldEvidenceStatisticalMethod,
            FieldEvidenceStatisticalMethodOverview,
            FieldEvidenceStudyCases,
            FieldEvidenceStudyCasesWithQualifyingVariants,
            FieldEvidenceStudySampleSize,
            FieldEvidenceTargetFromSourceId,
            FieldEvidenceVariantEffect,
        ],
    )
)
