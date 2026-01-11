"""Summary: namespaced MedDRA code for ADVERSE_REACTION node IDs.

Primary ID expression for ADVERSE_REACTION nodes: namespaces the MedDRA code
to create a stable identifier used by adverse reaction nodes/edges.
"""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.data.schema import FieldOpenfdaSignificantAdverseDrugReactionsMeddraCode
from open_targets.definition.helper import get_namespaced_expression

adverse_reaction_primary_id_expression: Final[Expression[str]] = get_namespaced_expression(
    "adverse_reaction",
    FieldOpenfdaSignificantAdverseDrugReactionsMeddraCode,
)
