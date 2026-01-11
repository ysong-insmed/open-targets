"""Summary: differential expression links from Expression Atlas (case vs control).

Definition for TARGET_DISEASE_ASSOCIATION_EXPRESSION_ATLAS nodes: filters
Evidence parquet to expression_atlas differential expression evidence. Genes
measured in case vs control biosamples yield contrasts (log2FC/value/percentile);
significant differential expression in disease-relevant tissues links the gene to
the disease. Records store biosamples, contrasts, log2FC/percentile, literature,
study overview/ID, confidence/resource scores, and disease/target IDs. Inference:
measure expression in disease vs baseline → observe differential expression →
link gene to disease in the KG (note: expression evidence is not ontology-propagated).
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidenceExpressionAtlas,
    FieldEvidenceExpressionAtlasBiosamplesFromSource,
    FieldEvidenceExpressionAtlasConfidence,
    FieldEvidenceExpressionAtlasContrast,
    FieldEvidenceExpressionAtlasDiseaseFromSourceMappedId,
    FieldEvidenceExpressionAtlasId,
    FieldEvidenceExpressionAtlasLiterature,
    FieldEvidenceExpressionAtlasLog2FoldChangePercentileRank,
    FieldEvidenceExpressionAtlasLog2FoldChangeValue,
    FieldEvidenceExpressionAtlasResourceScore,
    FieldEvidenceExpressionAtlasScore,
    FieldEvidenceExpressionAtlasStudyId,
    FieldEvidenceExpressionAtlasStudyOverview,
    FieldEvidenceExpressionAtlasTargetFromSourceId,
)

node_target_disease_association_expression_atlas: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetEvidenceExpressionAtlas),
        primary_id=FieldEvidenceExpressionAtlasId,
        label="TARGET_DISEASE_ASSOCIATION_EXPRESSION_ATLAS",
        properties=[
            FieldEvidenceExpressionAtlasBiosamplesFromSource,
            FieldEvidenceExpressionAtlasConfidence,
            FieldEvidenceExpressionAtlasContrast,
            FieldEvidenceExpressionAtlasLiterature,
            FieldEvidenceExpressionAtlasDiseaseFromSourceMappedId,
            FieldEvidenceExpressionAtlasLog2FoldChangePercentileRank,
            FieldEvidenceExpressionAtlasLog2FoldChangeValue,
            FieldEvidenceExpressionAtlasResourceScore,
            FieldEvidenceExpressionAtlasScore,
            FieldEvidenceExpressionAtlasStudyId,
            FieldEvidenceExpressionAtlasStudyOverview,
            FieldEvidenceExpressionAtlasTargetFromSourceId,
        ],
    )
)
