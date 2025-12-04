"""Summary: IntOGen somatic driver calls (positive selection in tumors).

Definition for TARGET_DISEASE_ASSOCIATION_INTOGEN nodes: filters Evidence
parquet to intogen driver discovery results. IntOGen aggregates tumor sequencing
studies and runs driver-calling methods to identify genes under positive selection
in specific cancers. Records retain cohort IDs/descriptions, significant driver
methods, direction on trait, variant effect, resource/score, and target/disease
IDs. Inference: aggregate somatic mutations → apply driver detection → call gene
as driver in a cancer → record as driver-based association in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceCohortDescription,
    FieldEvidenceCohortId,
    FieldEvidenceCohortShortName,
    FieldEvidenceDirectionOnTrait,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceResourceScore,
    FieldEvidenceScore,
    FieldEvidenceSignificantDriverMethods,
    FieldEvidenceSourceId,
    FieldEvidenceTargetFromSourceId,
    FieldEvidenceVariantEffect,
)

node_target_disease_association_intogen: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetEvidence,
        predicate=EqualityExpression(FieldEvidenceSourceId, "intogen"),
    ),
    primary_id=FieldEvidenceId,
    label="TARGET_DISEASE_ASSOCIATION_INTOGEN",
    properties=[
        FieldEvidenceCohortDescription,
        FieldEvidenceCohortId,
        FieldEvidenceCohortShortName,
        FieldEvidenceDirectionOnTrait,
        FieldEvidenceDiseaseFromSource,
        FieldEvidenceDiseaseFromSourceMappedId,
        FieldEvidenceResourceScore,
        FieldEvidenceScore,
        FieldEvidenceSignificantDriverMethods,
        FieldEvidenceTargetFromSourceId,
        FieldEvidenceVariantEffect,
    ],
)
