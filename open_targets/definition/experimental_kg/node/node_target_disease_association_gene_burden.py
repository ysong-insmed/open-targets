"""Summary: rare-variant burden tests linking genes to disease/traits.

Definition for TARGET_DISEASE_ASSOCIATION_GENE_BURDEN nodes: filters Evidence
parquet to gene_burden source to emit rare-variant burden associations. Burden
tests collapse many rare variants in a gene into a single burden score and test
carriers vs non-carriers for disease/trait difference. Arrow logic: sequence rare
variants -> collapse into burden score -> regress burden against phenotype ->
significant beta/OR/p-value -> link gene to disease. Records store regression
effects, p-values, ancestry/cohort info, allelic requirements, and study metadata.
The KG captures these gene-wide rare-variant signals rather than single-variant
hits."""

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
