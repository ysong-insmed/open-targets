"""Summary: GWAS credible sets evidence.

Definition for TARGET_DISEASE_ASSOCIATION_GWAS_CREDIBLE_SETS nodes.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidenceGwasCredibleSets,
    FieldEvidenceGwasCredibleSetsCurationDate,
    FieldEvidenceGwasCredibleSetsDatasourceId,
    FieldEvidenceGwasCredibleSetsDatatypeId,
    FieldEvidenceGwasCredibleSetsDiseaseFromSourceMappedId,
    FieldEvidenceGwasCredibleSetsId,
    FieldEvidenceGwasCredibleSetsLiterature,
    FieldEvidenceGwasCredibleSetsScore,
    FieldEvidenceGwasCredibleSetsStudyLocusId,
    FieldEvidenceGwasCredibleSetsTargetFromSourceId,
    FieldEvidenceGwasCredibleSetsTargetId,
)

node_target_disease_association_gwas_credible_sets: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetEvidenceGwasCredibleSets),
        primary_id=FieldEvidenceGwasCredibleSetsId,
        label="TARGET_DISEASE_ASSOCIATION_GWAS_CREDIBLE_SETS",
        properties=[
            FieldEvidenceGwasCredibleSetsCurationDate,
            FieldEvidenceGwasCredibleSetsDatasourceId,
            FieldEvidenceGwasCredibleSetsDatatypeId,
            FieldEvidenceGwasCredibleSetsDiseaseFromSourceMappedId,
            FieldEvidenceGwasCredibleSetsLiterature,
            FieldEvidenceGwasCredibleSetsScore,
            FieldEvidenceGwasCredibleSetsStudyLocusId,
            FieldEvidenceGwasCredibleSetsTargetFromSourceId,
            FieldEvidenceGwasCredibleSetsTargetId,
        ],
    )
)
