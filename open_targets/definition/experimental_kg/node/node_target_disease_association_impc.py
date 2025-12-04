"""Summary: mouse knockout phenotypes mapped to human disease (IMPC).

Definition for TARGET_DISEASE_ASSOCIATION_IMPC nodes: filters Evidence
parquet to impc mouse model evidence. IMPC perturbs mouse genes, observes
phenotypes, maps those phenotypes to human diseases, and then maps the mouse
gene to the human ortholog. Records keep model IDs (Ensembl/MGI), variant effect,
direction on trait, disease IDs, and scores. Inference: mouse knockout → observed
mouse phenotype → mapped to human disease → mapped to human ortholog gene → stored
as in vivo evidence in the KG."""

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
