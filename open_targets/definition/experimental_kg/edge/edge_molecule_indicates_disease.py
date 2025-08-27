"""Acquisition definition that acquires 'has indication' edges for drugs."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetIndication,
    FieldIndicationId,
    FieldIndicationIndications,
    FieldIndicationIndicationsElementDisease,
    FieldIndicationIndicationsElementMaxPhaseForIndication,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_molecule_indicates_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetIndication,
        exploded_field=FieldIndicationIndications,
    ),
    primary_id=NewUuidExpression(),
    source=FieldIndicationId,
    target=FieldIndicationIndicationsElementDisease,
    label=EdgeLabel.INDICATES,
    properties=[
        FieldIndicationIndicationsElementMaxPhaseForIndication,
    ],
)
