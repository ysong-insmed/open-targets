"""Summary: Edge connecting COLOCALISATION node to Left StudyLocus node.

Definition for edge: COLOCALISATION -> Left StudyLocus
"""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionEdgeAcquisitionDefinition,
)
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import DatasetColocalisation, FieldColocalisationLeftStudyLocusId
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import colocalisation_primary_id_expression

edge_study_locus_has_colocalisation_colocalisation_left: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetColocalisation),
        primary_id=NewUuidExpression(),
        source=colocalisation_primary_id_expression,
        target=FieldColocalisationLeftStudyLocusId,
        label=EdgeLabel.HAS_COLOCALISATION,
        properties=[],
    )
)
