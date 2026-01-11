"""Summary: TARGET -> SUBCELLULAR_LOCATION edges (localization source).

Definition for LOCATED_IN edges: explodes subcellular location annotations in
Targets parquet to connect each TARGET to a SUBCELLULAR_LOCATION node, carrying
the source of the localization, to provide compartment context in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTarget,
    FieldTargetId,
    FieldTargetSubcellularLocations,
    FieldTargetSubcellularLocationsElementSource,
)
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import subcellular_location_primary_id_expression

edge_target_located_in_subcellular_location: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetTarget,
            exploded_field=FieldTargetSubcellularLocations,
        ),
        primary_id=NewUuidExpression(),
        source=FieldTargetId,
        target=subcellular_location_primary_id_expression,
        label=EdgeLabel.LOCATED_IN,
        properties=[
            FieldTargetSubcellularLocationsElementSource,
        ],
    )
)
