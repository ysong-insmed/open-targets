"""Expression that builds a primary id for mechanisms of action."""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.data.schema import FieldAdverseDrugReactionsMeddraCode
from open_targets.definition.helper import get_namespaced_expression

adverse_reaction_primary_id_expression: Final[Expression[str]] = get_namespaced_expression(
    "adverse_reaction",
    FieldAdverseDrugReactionsMeddraCode,
)
