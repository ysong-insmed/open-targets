"""Definition for TARGET_DISEASE_ASSOCIATION_GENE2PHENOTYPE nodes: filters
Evidence parquet to gene2phenotype source to emit curated gene–disease links
with allelic requirements, direction on trait, variant functional consequence,
disease IDs, study ID, confidence, and score, capturing G2P assertions in the
KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceAllelicRequirements,
    FieldEvidenceConfidence,
    FieldEvidenceDirectionOnTrait,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceId,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceStudyId,
    FieldEvidenceTargetFromSourceId,
    FieldEvidenceVariantEffect,
    FieldEvidenceVariantFunctionalConsequenceId,
)

node_target_disease_association_gene2phenotype: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "gene2phenotype"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_GENE2PHENOTYPE",
        properties=[
            FieldEvidenceAllelicRequirements,
            FieldEvidenceConfidence,
            FieldEvidenceDirectionOnTrait,
            FieldEvidenceDiseaseFromSource,
            FieldEvidenceDiseaseFromSourceId,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceScore,
            FieldEvidenceStudyId,
            FieldEvidenceTargetFromSourceId,
            FieldEvidenceVariantEffect,
            FieldEvidenceVariantFunctionalConsequenceId,
        ],
    )
)
