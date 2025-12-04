"""Summary: normalize target xrefs to `source:id` strings.

Expression that normalizes target database cross-references into `source:id`
strings to align with other datasets (ChEMBL, Ensembl, etc.), working around
inconsistent representation in the targets parquet."""

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

database_cross_reference_target_value_expression: Final[Expression[str]] = StringConcatenationExpression(
    [
        ToStringExpression(FieldExpression(FieldTargetsDbXrefsElementSource)),
        LiteralExpression(":"),
        ToStringExpression(FieldExpression(FieldTargetsDbXrefsElementId)),
    ],
)
