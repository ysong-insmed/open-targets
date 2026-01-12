"""Summary: COLOCALISATION nodes from Colocalisation dataset.

Definition for COLOCALISATION nodes: represents a colocalisation event between two StudyLocus nodes.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionNodeAcquisitionDefinition,
)
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetColocalisation,
    FieldColocalisationBetaRatioSignAverage,
    FieldColocalisationChromosome,
    FieldColocalisationClpp,
    FieldColocalisationColocalisationMethod,
    FieldColocalisationH3,
    FieldColocalisationH4,
    FieldColocalisationNumberColocalisingVariants,
    FieldColocalisationRightStudyType,
)
from open_targets.definition.reference_kg.expression import colocalisation_primary_id_expression

node_colocalisation: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetColocalisation),
    primary_id=colocalisation_primary_id_expression,
    label="COLOCALISATION",
    properties=[
        FieldColocalisationColocalisationMethod,
        FieldColocalisationClpp,
        FieldColocalisationH3,
        FieldColocalisationH4,
        FieldColocalisationBetaRatioSignAverage,
        FieldColocalisationNumberColocalisingVariants,
        FieldColocalisationChromosome,
        FieldColocalisationRightStudyType,
    ],
)
