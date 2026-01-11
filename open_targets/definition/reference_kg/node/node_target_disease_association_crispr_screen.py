"""Summary: detailed CRISPR screen associations (cell type, contrast, log2FC).

Definition for TARGET_DISEASE_ASSOCIATION_CRISPR_SCREEN nodes: filters
Evidence parquet to crispr_screen source to emit detailed CRISPR screen results.
Screens perturb genes across cell types/libraries; significant contrasts (log2FC)
link a gene to a disease model. Records keep cell type, library, contrast,
genetic background, log2FC, project/study metadata, and scores. Inference: perturb
gene in disease-model cells → observe strong viability/phenotype shift → link
gene to disease in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidenceCrisprScreen,
    FieldEvidenceCrisprScreenCellType,
    FieldEvidenceCrisprScreenContrast,
    FieldEvidenceCrisprScreenCrisprScreenLibrary,
    FieldEvidenceCrisprScreenDiseaseFromSource,
    FieldEvidenceCrisprScreenDiseaseFromSourceMappedId,
    FieldEvidenceCrisprScreenGeneticBackground,
    FieldEvidenceCrisprScreenId,
    FieldEvidenceCrisprScreenLog2FoldChangeValue,
    FieldEvidenceCrisprScreenProjectId,
    FieldEvidenceCrisprScreenResourceScore,
    FieldEvidenceCrisprScreenScore,
    FieldEvidenceCrisprScreenStatisticalTestTail,
    FieldEvidenceCrisprScreenStudyId,
    FieldEvidenceCrisprScreenStudyOverview,
    FieldEvidenceCrisprScreenTargetFromSourceId,
)

node_target_disease_association_crispr_screen: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetEvidenceCrisprScreen),
        primary_id=FieldEvidenceCrisprScreenId,
        label="TARGET_DISEASE_ASSOCIATION_CRISPR_SCREEN",
        properties=[
            FieldEvidenceCrisprScreenCellType,
            FieldEvidenceCrisprScreenContrast,
            FieldEvidenceCrisprScreenCrisprScreenLibrary,
            FieldEvidenceCrisprScreenDiseaseFromSource,
            FieldEvidenceCrisprScreenDiseaseFromSourceMappedId,
            FieldEvidenceCrisprScreenGeneticBackground,
            FieldEvidenceCrisprScreenLog2FoldChangeValue,
            FieldEvidenceCrisprScreenProjectId,
            FieldEvidenceCrisprScreenResourceScore,
            FieldEvidenceCrisprScreenScore,
            FieldEvidenceCrisprScreenStatisticalTestTail,
            FieldEvidenceCrisprScreenStudyId,
            FieldEvidenceCrisprScreenStudyOverview,
            FieldEvidenceCrisprScreenTargetFromSourceId,
        ],
    )
)
