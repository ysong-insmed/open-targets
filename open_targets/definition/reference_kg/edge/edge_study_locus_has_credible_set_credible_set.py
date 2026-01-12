"""Summary: Edge connecting StudyLocus node to CredibleSet node.

Definition for edge: StudyLocus -> CredibleSet
"""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionEdgeAcquisitionDefinition,
)
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import DatasetCredibleSet, FieldCredibleSetStudyLocusId
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import credible_set_primary_id_expression

edge_study_locus_has_credible_set_credible_set: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetCredibleSet),
        primary_id=NewUuidExpression(),
        source=FieldCredibleSetStudyLocusId,
        target=credible_set_primary_id_expression,
        label=EdgeLabel.HAS_CREDIBLE_SET,
        properties=[],
    )
)
