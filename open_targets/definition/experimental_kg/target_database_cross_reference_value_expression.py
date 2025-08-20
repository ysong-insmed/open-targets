"""Expression that builds a cross reference values for target database.

This expression builds a cross reference value for target database cross
references that align with other datasets. This is a workaround for the
inconsistency representation present in the target dataset.
"""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
    FieldExpression,
    LiteralExpression,
    StringConcatenationExpression,
    ToStringExpression,
)
from open_targets.data.schema import (
    FieldTargetsDbXrefsElementId,
    FieldTargetsDbXrefsElementSource,
)

target_database_cross_reference_value_expression: Final[Expression[str]] = StringConcatenationExpression(
    [
        ToStringExpression(FieldExpression(FieldTargetsDbXrefsElementSource)),
        LiteralExpression(":"),
        ToStringExpression(FieldExpression(FieldTargetsDbXrefsElementId)),
    ],
)
