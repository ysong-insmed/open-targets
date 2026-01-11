"""Summary: MOLECULE -> DISEASE indication edges with max clinical phase.

Definition for INDICATES edges: explodes drug indication records in the Indication
parquet to link each MOLECULE (ChEMBL drug) to an EFO/MONDO DISEASE, carrying
`maxPhaseForIndication` to reflect development stage of the therapeutic indication
in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDrugIndication,
    FieldDrugIndicationId,
    FieldDrugIndicationIndications,
    FieldDrugIndicationIndicationsElementDisease,
    FieldDrugIndicationIndicationsElementMaxPhaseForIndication,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_molecule_indicates_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDrugIndication,
        exploded_field=FieldDrugIndicationIndications,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDrugIndicationId,
    target=FieldDrugIndicationIndicationsElementDisease,
    label=EdgeLabel.INDICATES,
    properties=[
        FieldDrugIndicationIndicationsElementMaxPhaseForIndication,
    ],
)
