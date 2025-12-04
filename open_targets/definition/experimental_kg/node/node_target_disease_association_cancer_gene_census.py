"""Summary: expert-curated somatic driver calls from Cancer Gene Census.

Definition for TARGET_DISEASE_ASSOCIATION_CANCER_GENE_CENSUS nodes: filters
Evidence parquet to cancer_gene_census (CGC) somatic driver calls. CGC experts
review tumor sequencing and literature to declare genes as drivers in specific
cancers. Each record is that curated call: disease mapping, target ID, variant
effect, direction on trait, and resource/evidence scores. The inference chain is
tumor sequencing → expert curation of driver status → driver gene linked to cancer
in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceDirectionOnTrait,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceResourceScore,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceStudyId,
    FieldEvidenceTargetFromSourceId,
    FieldEvidenceVariantEffect,
)

node_target_disease_association_cancer_gene_census: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "cancer_gene_census"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_CANCER_GENE_CENSUS",
        properties=[
            FieldEvidenceDirectionOnTrait,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceResourceScore,
            FieldEvidenceScore,
            FieldEvidenceStudyId,
            FieldEvidenceTargetFromSourceId,
            FieldEvidenceVariantEffect,
        ],
    )
)
