"""Summary: ClinVar/EVA germline variant assertions (pathogenicity to disease).

Definition for TARGET_DISEASE_ASSOCIATION_EVA nodes: filters Evidence parquet
to eva germline submissions (ClinVar/EVA). ClinVar submitters assert whether a
germline variant is pathogenic/benign for a disease. Each record keeps variant
IDs (HGVS/RS), functional consequence, allele origin, allelic requirements,
direction on trait, clinical significance, cohort phenotypes, and confidence/
score with disease/target IDs. Inference: clinical genetics lab submission →
asserted variant pathogenicity → map to gene and disease → represent curated
germline evidence in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidenceEva,
    FieldEvidenceEvaAlleleOrigins,
    FieldEvidenceEvaAllelicRequirements,
    FieldEvidenceEvaClinicalSignificances,
    FieldEvidenceEvaConfidence,
    FieldEvidenceEvaDiseaseFromSource,
    FieldEvidenceEvaDiseaseFromSourceId,
    FieldEvidenceEvaDiseaseFromSourceMappedId,
    FieldEvidenceEvaId,
    FieldEvidenceEvaLiterature,
    FieldEvidenceEvaScore,
    FieldEvidenceEvaStudyId,
    FieldEvidenceEvaTargetFromSourceId,
    FieldEvidenceEvaVariantFunctionalConsequenceId,
    FieldEvidenceEvaVariantHgvsId,
    FieldEvidenceEvaVariantId,
    FieldEvidenceEvaVariantRsId,
)

node_target_disease_association_eva: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceEva),
    primary_id=FieldEvidenceEvaId,
    label="TARGET_DISEASE_ASSOCIATION_EVA",
    properties=[
        FieldEvidenceEvaAlleleOrigins,
        FieldEvidenceEvaAllelicRequirements,
        FieldEvidenceEvaClinicalSignificances,
        FieldEvidenceEvaConfidence,
        FieldEvidenceEvaDiseaseFromSource,
        FieldEvidenceEvaDiseaseFromSourceId,
        FieldEvidenceEvaDiseaseFromSourceMappedId,
        FieldEvidenceEvaLiterature,
        FieldEvidenceEvaScore,
        FieldEvidenceEvaStudyId,
        FieldEvidenceEvaTargetFromSourceId,
        FieldEvidenceEvaVariantFunctionalConsequenceId,
        FieldEvidenceEvaVariantHgvsId,
        FieldEvidenceEvaVariantId,
        FieldEvidenceEvaVariantRsId,
    ],
)
