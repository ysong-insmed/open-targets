"""Summary: Colocalisation edge.

Definition for COLOCALISES_WITH edge: Connects two StudyLocus nodes indicating
colocalisation of genetic signals.
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
    DatasetColocalisation,
    FieldColocalisationBetaRatioSignAverage,
    FieldColocalisationChromosome,
    FieldColocalisationClpp,
    FieldColocalisationColocalisationMethod,
    FieldColocalisationH3,
    FieldColocalisationH4,
    FieldColocalisationLeftStudyLocusId,
    FieldColocalisationRightStudyLocusId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_colocalisation: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetColocalisation),
    primary_id=NewUuidExpression(),
    source=FieldColocalisationLeftStudyLocusId,
    target=FieldColocalisationRightStudyLocusId,
    label=EdgeLabel.COLOCALISES_WITH,
    properties=[
        FieldColocalisationBetaRatioSignAverage,
        FieldColocalisationChromosome,
        FieldColocalisationClpp,
        FieldColocalisationColocalisationMethod,
        FieldColocalisationH3,
        FieldColocalisationH4,
    ],
)
