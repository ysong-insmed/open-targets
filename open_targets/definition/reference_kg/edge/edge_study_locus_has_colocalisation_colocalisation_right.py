"""Summary: Edge connecting COLOCALISATION node to Right StudyLocus node.

Definition for edge: COLOCALISATION -> Right StudyLocus
"""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionEdgeAcquisitionDefinition,
)
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import DatasetColocalisation, FieldColocalisationRightStudyLocusId
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import colocalisation_primary_id_expression

edge_study_locus_has_colocalisation_colocalisation_right: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetColocalisation),
        primary_id=NewUuidExpression(),
        source=colocalisation_primary_id_expression,
        target=FieldColocalisationRightStudyLocusId,
        label=EdgeLabel.HAS_COLOCALISATION,
        properties=[],
    )
)
