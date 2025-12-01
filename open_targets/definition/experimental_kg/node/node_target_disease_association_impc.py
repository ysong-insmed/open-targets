"""Definition for TARGET_DISEASE_ASSOCIATION_IMPC nodes: filters Evidence
parquet to impc source to emit mouse model associations with disease IDs,
mouse model IDs (Ensembl/MGI), variant effect, direction on trait, resource/score,
capturing in vivo mouse evidence mapped to human targets/diseases in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceDirectionOnTrait,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceId,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceResourceScore,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceTargetFromSourceId,
    FieldEvidenceTargetInModel,
    FieldEvidenceTargetInModelEnsemblId,
    FieldEvidenceTargetInModelMgiId,
    FieldEvidenceVariantEffect,
)

node_target_disease_association_impc: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetEvidence,
        predicate=EqualityExpression(FieldEvidenceSourceId, "impc"),
    ),
    primary_id=FieldEvidenceId,
    label="TARGET_DISEASE_ASSOCIATION_IMPC",
    properties=[
        FieldEvidenceDirectionOnTrait,
        FieldEvidenceDiseaseFromSource,
        FieldEvidenceDiseaseFromSourceId,
        FieldEvidenceDiseaseFromSourceMappedId,
        FieldEvidenceResourceScore,
        FieldEvidenceScore,
        FieldEvidenceTargetFromSourceId,
        FieldEvidenceTargetInModel,
        FieldEvidenceTargetInModelEnsemblId,
        FieldEvidenceTargetInModelMgiId,
        FieldEvidenceVariantEffect,
    ],
)
