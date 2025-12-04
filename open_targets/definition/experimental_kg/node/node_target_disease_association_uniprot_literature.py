"""Summary: UniProt curator-reviewed literature assertions of target-disease.

Definition for TARGET_DISEASE_ASSOCIATION_UNIPROT_LITERATURE nodes: filters
Evidence parquet to uniprot_literature curated assertions. UniProt curators read
the literature and annotate when a protein is implicated in a disease, noting
target modulation and confidence. Records keep disease/target IDs and scores.
Inference: manual literature curation → curator asserts protein–disease link →
captured as curated literature evidence in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceConfidence,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceId,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceTargetFromSourceId,
    FieldEvidenceTargetModulation,
)

node_target_disease_association_uniprot_literature: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "uniprot_literature"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_UNIPROT_LITERATURE",
        properties=[
            FieldEvidenceConfidence,
            FieldEvidenceDiseaseFromSource,
            FieldEvidenceDiseaseFromSourceId,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceScore,
            FieldEvidenceTargetFromSourceId,
            FieldEvidenceTargetModulation,
        ],
    )
)
