"""Summary: MOLECULE -> DISEASE indication edges with max clinical phase.

Definition for INDICATES edges: explodes drug indication records in the Indication
parquet to link each MOLECULE (ChEMBL drug) to an EFO/MONDO DISEASE, carrying
`maxPhaseForIndication` to reflect development stage of the therapeutic indication
in the KG."""

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
