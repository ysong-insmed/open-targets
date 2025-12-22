"""Summary: UniProt curator-reviewed variant assertions for target-disease.

Definition for TARGET_DISEASE_ASSOCIATION_UNIPROT_VARIANTS nodes: filters
Evidence parquet to uniprot_variants curated variant assertions. UniProt curators
review literature and databases for protein variants linked to disease, capturing
variant IDs (RS/id), functional consequence, target modulation, confidence, and
scores. Inference: manual variant curation → variant tied to protein and disease
→ stored as curated variant evidence in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceConfidence,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceId,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceTargetFromSourceId,
    FieldEvidenceTargetModulation,
    FieldEvidenceVariantFunctionalConsequenceId,
    FieldEvidenceVariantId,
    FieldEvidenceVariantRsId,
)

node_target_disease_association_uniprot_variants: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "uniprot_variants"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_UNIPROT_VARIANTS",
        properties=[
            FieldEvidenceConfidence,
            FieldEvidenceDiseaseFromSource,
            FieldEvidenceDiseaseFromSourceId,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceScore,
            FieldEvidenceTargetFromSourceId,
            FieldEvidenceTargetModulation,
            FieldEvidenceVariantFunctionalConsequenceId,
            FieldEvidenceVariantId,
            FieldEvidenceVariantRsId,
        ],
    )
)
