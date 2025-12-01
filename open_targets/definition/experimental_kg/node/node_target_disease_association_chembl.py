"""Definition for TARGET_DISEASE_ASSOCIATION_CHEMBL nodes: filters the Evidence
parquet to ChEMBL clinical evidence (`sourceId == chembl`) and emits reified
target–disease association nodes with trial phase/status, cohort, direction on
trait, variant effect, disease IDs, study IDs/dates, and score, representing
known-drug evidence in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceClinicalPhase,
    FieldEvidenceClinicalStatus,
    FieldEvidenceCohortPhenotypes,
    FieldEvidenceDirectionOnTrait,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceStudyId,
    FieldEvidenceStudyStartDate,
    FieldEvidenceStudyStopReason,
    FieldEvidenceStudyStopReasonCategories,
    FieldEvidenceVariantEffect,
)

node_target_disease_association_chembl: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetEvidence,
        predicate=EqualityExpression(FieldEvidenceSourceId, "chembl"),
    ),
    primary_id=FieldEvidenceId,
    label="TARGET_DISEASE_ASSOCIATION_CHEMBL",
    properties=[
        FieldEvidenceClinicalPhase,
        FieldEvidenceClinicalStatus,
        FieldEvidenceCohortPhenotypes,
        FieldEvidenceDirectionOnTrait,
        FieldEvidenceDiseaseFromSource,
        FieldEvidenceDiseaseFromSourceMappedId,
        FieldEvidenceScore,
        FieldEvidenceStudyId,
        FieldEvidenceStudyStartDate,
        FieldEvidenceStudyStopReason,
        FieldEvidenceStudyStopReasonCategories,
        FieldEvidenceVariantEffect,
    ],
)
