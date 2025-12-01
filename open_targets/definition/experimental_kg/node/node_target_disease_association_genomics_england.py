"""Definition for TARGET_DISEASE_ASSOCIATION_GENOMICS_ENGLAND nodes: filters
Evidence parquet to genomics_england source to emit PanelApp-style associations
with cohort phenotypes, allelic requirements, confidence, disease IDs, study
overview/ID, score, and target IDs, capturing curated clinical evidence in the
KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceAllelicRequirements,
    FieldEvidenceCohortPhenotypes,
    FieldEvidenceConfidence,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceId,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceStudyId,
    FieldEvidenceStudyOverview,
    FieldEvidenceTargetFromSourceId,
)

node_target_disease_association_genomics_england: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "genomics_england"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_GENOMICS_ENGLAND",
        properties=[
            FieldEvidenceAllelicRequirements,
            FieldEvidenceCohortPhenotypes,
            FieldEvidenceConfidence,
            FieldEvidenceDiseaseFromSource,
            FieldEvidenceDiseaseFromSourceId,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceScore,
            FieldEvidenceStudyId,
            FieldEvidenceStudyOverview,
            FieldEvidenceTargetFromSourceId,
        ],
    )
)
