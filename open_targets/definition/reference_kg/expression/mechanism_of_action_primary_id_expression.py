"""Summary: hashed MoA text for MECHANISM_OF_ACTION IDs.

Primary ID expression for MECHANISM_OF_ACTION nodes: hashes the mechanism of
action text to form a stable identifier for reified MoA records.
"""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
    FieldExpression,
    StringHashExpression,
    ToStringExpression,
)
from open_targets.data.schema import FieldDrugMechanismOfActionMechanismOfAction

mechanism_of_action_primary_id_expression: Final[Expression[str]] = StringHashExpression(
    ToStringExpression(FieldExpression(FieldDrugMechanismOfActionMechanismOfAction)),
)
