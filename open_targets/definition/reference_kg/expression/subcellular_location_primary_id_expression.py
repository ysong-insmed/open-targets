"""Summary: namespaced UniProt subcellular location term ID.

Primary ID expression for SUBCELLULAR_LOCATION nodes: namespaces the UniProt
subcellular location term ID to create a stable identifier.
"""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.data.schema import (
    FieldTargetSubcellularLocationsElementLocation,
)
from open_targets.definition.helper import get_namespaced_expression

subcellular_location_primary_id_expression: Final[Expression[str]] = get_namespaced_expression(
    "subcellular_location",
    FieldTargetSubcellularLocationsElementLocation,
)
