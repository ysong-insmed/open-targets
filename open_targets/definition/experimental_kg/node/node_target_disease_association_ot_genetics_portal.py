"""Summary: GWAS fine-mapping + L2G causal gene assignments (OT Genetics).

Definition for TARGET_DISEASE_ASSOCIATION_OT_GENETICS_PORTAL nodes: filters
Evidence parquet to ot_genetics_portal GWAS/L2G results. OT Genetics finds
GWAS-significant loci, fine-maps variants, and runs the Locus2Gene model to
estimate the causal gene (L2G > 0.05). Records keep p-values, beta/OR and CIs,
variant/consequence IDs (RS/id/QTL), direction on trait, project/publication
info, disease/target IDs, and resource/score. Inference: GWAS locus → fine-mapping
→ L2G causal gene probability → gene–disease link recorded as genetics-based
causal inference in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceBeta,
    FieldEvidenceBetaConfidenceIntervalLower,
    FieldEvidenceBetaConfidenceIntervalUpper,
    FieldEvidenceDirectionOnTrait,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceOddsRatio,
    FieldEvidenceOddsRatioConfidenceIntervalLower,
    FieldEvidenceOddsRatioConfidenceIntervalUpper,
    FieldEvidenceProjectId,
    FieldEvidencePublicationFirstAuthor,
    FieldEvidencePublicationYear,
    FieldEvidencePValueExponent,
    FieldEvidencePValueMantissa,
    FieldEvidenceResourceScore,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceStudyId,
    FieldEvidenceStudySampleSize,
    FieldEvidenceTargetFromSourceId,
    FieldEvidenceVariantEffect,
    FieldEvidenceVariantFunctionalConsequenceFromQtlId,
    FieldEvidenceVariantFunctionalConsequenceId,
    FieldEvidenceVariantId,
    FieldEvidenceVariantRsId,
)

node_target_disease_association_ot_genetics_portal: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "ot_genetics_portal"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_OT_GENETICS_PORTAL",
        properties=[
            FieldEvidenceBeta,
            FieldEvidenceBetaConfidenceIntervalLower,
            FieldEvidenceBetaConfidenceIntervalUpper,
            FieldEvidenceDirectionOnTrait,
            FieldEvidenceDiseaseFromSource,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceOddsRatio,
            FieldEvidenceOddsRatioConfidenceIntervalLower,
            FieldEvidenceOddsRatioConfidenceIntervalUpper,
            FieldEvidencePValueExponent,
            FieldEvidencePValueMantissa,
            FieldEvidenceProjectId,
            FieldEvidencePublicationFirstAuthor,
            FieldEvidencePublicationYear,
            FieldEvidenceResourceScore,
            FieldEvidenceScore,
            FieldEvidenceStudyId,
            FieldEvidenceStudySampleSize,
            FieldEvidenceTargetFromSourceId,
            FieldEvidenceVariantEffect,
            FieldEvidenceVariantFunctionalConsequenceFromQtlId,
            FieldEvidenceVariantFunctionalConsequenceId,
            FieldEvidenceVariantId,
            FieldEvidenceVariantRsId,
        ],
    )
)
