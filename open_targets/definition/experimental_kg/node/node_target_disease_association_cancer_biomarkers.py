"""Definition for TARGET_DISEASE_ASSOCIATION_CANCER_BIOMARKERS nodes: filters
Evidence parquet to cancer_biomarkers source to emit reified associations with
biomarker name, confidence, disease/drug/target IDs, and score, capturing
biomarker-driven drug response evidence in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceBiomarkerName,
    FieldEvidenceConfidence,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceDrugFromSource,
    FieldEvidenceId,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceTargetFromSourceId,
)

node_target_disease_association_cancer_biomarkers: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "cancer_biomarkers"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_CANCER_BIOMARKERS",
        properties=[
            FieldEvidenceBiomarkerName,
            FieldEvidenceConfidence,
            FieldEvidenceDiseaseFromSource,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceDrugFromSource,
            FieldEvidenceScore,
            FieldEvidenceTargetFromSourceId,
        ],
    )
)
