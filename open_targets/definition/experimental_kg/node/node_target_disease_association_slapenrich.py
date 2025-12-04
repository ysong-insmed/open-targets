"""Summary: SLAPenrich pathway-enrichment inference linking genes to disease.

Definition for TARGET_DISEASE_ASSOCIATION_SLAPENRICH nodes: filters Evidence
parquet to slapenrich pathway-enrichment inference. SLAPenrich tests whether
mutations observed in a disease context are enriched in specific pathways. When
a pathway is significantly enriched, the genes in that pathway (targets) are
linked to the disease as inferred contributors. Records keep disease IDs, target
IDs, and enrichment/resource scores. Inference: collect somatic mutations →
test pathway enrichment → if enriched, link pathway genes to disease → store as
pathway-level evidence in the KG.
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

node_target_disease_association_slapenrich: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "slapenrich"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_SLAPENRICH",
        properties=[
            FieldEvidenceDiseaseFromSource,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceResourceScore,
            FieldEvidenceScore,
            FieldEvidenceTargetFromSourceId,
        ],
    )
)
