"""Summary: Enhancer to Gene edge.

Definition for ENHANCER_TO_GENE edge: Connects a Biosample (source) to a Target (gene)
indicating regulation via an enhancer region.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionEdgeAcquisitionDefinition,
)
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEnhancerToGene,
    FieldEnhancerToGeneBiosampleId,
    FieldEnhancerToGeneChromosome,
    FieldEnhancerToGeneDatasourceId,
    FieldEnhancerToGeneDistanceToTss,
    FieldEnhancerToGeneEnd,
    FieldEnhancerToGeneGeneId,
    FieldEnhancerToGeneScore,
    FieldEnhancerToGeneStart,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_enhancer_to_gene: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEnhancerToGene),
    primary_id=NewUuidExpression(),
    source=FieldEnhancerToGeneBiosampleId,
    target=FieldEnhancerToGeneGeneId,
    label=EdgeLabel.REGULATES,
    properties=[
        FieldEnhancerToGeneChromosome,
        FieldEnhancerToGeneDatasourceId,
        FieldEnhancerToGeneDistanceToTss,
        FieldEnhancerToGeneEnd,
        FieldEnhancerToGeneScore,
        FieldEnhancerToGeneStart,
    ],
)
