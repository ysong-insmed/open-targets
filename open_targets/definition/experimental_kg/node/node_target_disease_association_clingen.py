"""Summary: ClinGen expert-curated gene-disease validity.

Definition for TARGET_DISEASE_ASSOCIATION_CLINGEN nodes: filters Evidence
parquet to clingen curated clinical genetics. ClinGen experts review human
genetic evidence and assign gene-disease validity with allelic requirements and
confidence. Records retain disease IDs (source/mapped), study ID, score, target
IDs, and allelic requirements. The logic is human variant observations →
expert validity assessment → gene-disease assertion captured in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceAllelicRequirements,
    FieldEvidenceConfidence,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceId,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceStudyId,
    FieldEvidenceTargetFromSourceId,
)

node_target_disease_association_clingen: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetEvidence,
        predicate=EqualityExpression(FieldEvidenceSourceId, "clingen"),
    ),
    primary_id=FieldEvidenceId,
    label="TARGET_DISEASE_ASSOCIATION_CLINGEN",
    properties=[
        FieldEvidenceAllelicRequirements,
        FieldEvidenceConfidence,
        FieldEvidenceDiseaseFromSource,
        FieldEvidenceDiseaseFromSourceId,
        FieldEvidenceDiseaseFromSourceMappedId,
        FieldEvidenceScore,
        FieldEvidenceStudyId,
        FieldEvidenceTargetFromSourceId,
    ],
)
