"""Summary: namespaced species identifier for homology nodes.

Primary ID expression for SPECIES nodes: namespaces the species identifier
from homology data to create a stable SPECIES node ID.
"""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.data.schema import FieldTargetsHomologuesElementSpeciesId
from open_targets.definition.helper import get_namespaced_expression

species_primary_id_expression: Final[Expression[str]] = get_namespaced_expression(
    "species",
    FieldTargetsHomologuesElementSpeciesId,
)
