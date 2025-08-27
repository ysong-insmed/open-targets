"""Acquisition definition that acquires edges between mouse targets and human targets."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetMousePhenotypes,
    FieldMousePhenotypesTargetFromSourceId,
    FieldMousePhenotypesTargetInModelEnsemblId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_modelled_by_mouse_gene: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetMousePhenotypes),
    primary_id=NewUuidExpression(),
    source=FieldMousePhenotypesTargetFromSourceId,
    target=FieldMousePhenotypesTargetInModelEnsemblId,
    label=EdgeLabel.MODELLED_BY,
    properties=[],
)
