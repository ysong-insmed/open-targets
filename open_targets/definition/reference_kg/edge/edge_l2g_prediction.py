"""Summary: L2G Prediction edge.

Definition for L2G_PREDICTION edge: Connects a StudyLocus (source) to a Target gene (target)
with an L2G score.
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
    DatasetL2GPrediction,
    FieldL2GPredictionGeneId,
    FieldL2GPredictionScore,
    FieldL2GPredictionStudyLocusId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_l2g_prediction: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetL2GPrediction),
    primary_id=NewUuidExpression(),
    source=FieldL2GPredictionStudyLocusId,
    target=FieldL2GPredictionGeneId,
    label=EdgeLabel.LOCUS_TO_GENE,  # Need to check if this label exists or add unique one
    properties=[
        FieldL2GPredictionScore,
    ],
)
