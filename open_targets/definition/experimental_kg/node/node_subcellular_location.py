"""Definition for SUBCELLULAR_LOCATION nodes: scans UniProt subcellular location
parquet to emit localization terms (labelSL/location/termSL) that targets can
link to for cellular compartment context in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTargets,
    FieldTargetsSubcellularLocations,
    FieldTargetsSubcellularLocationsElementLabelSl,
    FieldTargetsSubcellularLocationsElementLocation,
    FieldTargetsSubcellularLocationsElementTermSl,
)
from open_targets.definition.experimental_kg.expression import subcellular_location_primary_id_expression

node_subcellular_location: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetTargets,
        exploded_field=FieldTargetsSubcellularLocations,
    ),
    primary_id=subcellular_location_primary_id_expression,
    label="SUBCELLULAR_LOCATION",
    properties=[
        FieldTargetsSubcellularLocationsElementLocation,
        FieldTargetsSubcellularLocationsElementLabelSl,
        FieldTargetsSubcellularLocationsElementTermSl,
    ],
)
