"""Summary: UniProt subcellular location nodes for compartment context.

Definition for SUBCELLULAR_LOCATION nodes: scans UniProt subcellular location
parquet to emit localization terms (labelSL/location/termSL) that targets can
link to for cellular compartment context in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTarget,
    FieldTargetSubcellularLocations,
    FieldTargetSubcellularLocationsElementLabelSl,
    FieldTargetSubcellularLocationsElementLocation,
    FieldTargetSubcellularLocationsElementTermSl,
)
from open_targets.definition.reference_kg.expression import subcellular_location_primary_id_expression

node_subcellular_location: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetTarget,
        exploded_field=FieldTargetSubcellularLocations,
    ),
    primary_id=subcellular_location_primary_id_expression,
    label="SUBCELLULAR_LOCATION",
    properties=[
        FieldTargetSubcellularLocationsElementLocation,
        FieldTargetSubcellularLocationsElementLabelSl,
        FieldTargetSubcellularLocationsElementTermSl,
    ],
)
