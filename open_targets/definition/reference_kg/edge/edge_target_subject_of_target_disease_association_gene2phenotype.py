"""Summary: TARGET -> TARGET_DISEASE_ASSOCIATION_GENE2PHENOTYPE edges.

Definition for SUBJECT_OF edges (target -> target_disease_association_gene2phenotype):
links each TARGET to the TARGET_DISEASE_ASSOCIATION_GENE2PHENOTYPE nodes it is the subject of.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidenceGene2Phenotype,
    FieldEvidenceGene2PhenotypeId,
    FieldEvidenceGene2PhenotypeTargetId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_target_subject_of_target_disease_association_gene2phenotype: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetEvidenceGene2Phenotype),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceGene2PhenotypeTargetId,
        target=FieldEvidenceGene2PhenotypeId,
        label=EdgeLabel.SUBJECT_OF,
        properties=[],
    )
)
