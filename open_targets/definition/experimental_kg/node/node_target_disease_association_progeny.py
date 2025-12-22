"""Summary: PROGENy pathway-activity inference linking genes to disease.

Definition for TARGET_DISEASE_ASSOCIATION_PROGENY nodes: filters Evidence
parquet to progeny pathway-activity inference. PROGENy computes pathway activity
scores from gene expression and tests if a pathway is perturbed in a disease.
If a pathway is up/downregulated, the genes driving that signature are linked to
the disease with resource/overall scores. Inference: expression data → inferred
pathway activity → associate pathway’s genes with disease → store as pathway-based
evidence in the KG (not direct genetic or clinical evidence).
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceResourceScore,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceTargetFromSourceId,
)

node_target_disease_association_progeny: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetEvidence,
        predicate=EqualityExpression(FieldEvidenceSourceId, "progeny"),
    ),
    primary_id=FieldEvidenceId,
    label="TARGET_DISEASE_ASSOCIATION_PROGENY",
    properties=[
        FieldEvidenceDiseaseFromSource,
        FieldEvidenceDiseaseFromSourceMappedId,
        FieldEvidenceResourceScore,
        FieldEvidenceScore,
        FieldEvidenceTargetFromSourceId,
    ],
)
