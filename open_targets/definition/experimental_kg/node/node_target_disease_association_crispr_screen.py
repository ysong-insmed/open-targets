"""Summary: detailed CRISPR screen associations (cell type, contrast, log2FC).

Definition for TARGET_DISEASE_ASSOCIATION_CRISPR_SCREEN nodes: filters
Evidence parquet to crispr_screen source to emit detailed CRISPR screen results.
Screens perturb genes across cell types/libraries; significant contrasts (log2FC)
link a gene to a disease model. Records keep cell type, library, contrast,
genetic background, log2FC, project/study metadata, and scores. Inference: perturb
gene in disease-model cells → observe strong viability/phenotype shift → link
gene to disease in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceCellType,
    FieldEvidenceContrast,
    FieldEvidenceCrisprScreenLibrary,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceGeneticBackground,
    FieldEvidenceId,
    FieldEvidenceLog2FoldChangeValue,
    FieldEvidenceProjectId,
    FieldEvidenceResourceScore,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceStatisticalTestTail,
    FieldEvidenceStudyId,
    FieldEvidenceStudyOverview,
    FieldEvidenceTargetFromSourceId,
)

node_target_disease_association_crispr_screen: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "crispr_screen"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_CRISPR_SCREEN",
        properties=[
            FieldEvidenceCellType,
            FieldEvidenceContrast,
            FieldEvidenceCrisprScreenLibrary,
            FieldEvidenceDiseaseFromSource,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceGeneticBackground,
            FieldEvidenceLog2FoldChangeValue,
            FieldEvidenceProjectId,
            FieldEvidenceResourceScore,
            FieldEvidenceScore,
            FieldEvidenceStatisticalTestTail,
            FieldEvidenceStudyId,
            FieldEvidenceStudyOverview,
            FieldEvidenceTargetFromSourceId,
        ],
    )
)
