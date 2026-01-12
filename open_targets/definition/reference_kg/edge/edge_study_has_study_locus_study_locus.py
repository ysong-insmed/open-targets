"""Summary: Study HAS StudyLocus edge.

Definition for HAS_STUDY_LOCUS edge: Connects a Study to its child StudyLocus.
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
    DatasetCredibleSet,
    FieldCredibleSetStudyId,
    FieldCredibleSetStudyLocusId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_study_has_study_locus_study_locus: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetCredibleSet),
    primary_id=NewUuidExpression(),
    source=FieldCredibleSetStudyId,
    target=FieldCredibleSetStudyLocusId,
    label=EdgeLabel.HAS_STUDY_LOCUS,
    properties=[],
)
