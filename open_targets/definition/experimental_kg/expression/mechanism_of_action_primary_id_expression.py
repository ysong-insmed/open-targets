"""Expression that builds a primary id for mechanisms of action."""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
    FieldExpression,
    StringHashExpression,
    ToStringExpression,
)
from open_targets.data.schema import FieldMechanismOfActionMechanismOfAction

mechanism_of_action_primary_id_expression: Final[Expression[str]] = StringHashExpression(
    ToStringExpression(FieldExpression(FieldMechanismOfActionMechanismOfAction)),
)
