"""Expression that builds a primary id for mechanisms of action."""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
    FieldExpression,
    StringConcatenationExpression,
    StringHashExpression,
    ToStringExpression,
)
from open_targets.data.schema import (
    FieldInteractionEvidenceTargetA,
    FieldInteractionEvidenceTargetB,
)

target_target_interaction_primary_id_expression: Final[Expression[str]] = StringHashExpression(
    StringConcatenationExpression(
        [
            ToStringExpression(FieldExpression(FieldInteractionEvidenceTargetA)),
            ToStringExpression(FieldExpression(FieldInteractionEvidenceTargetB)),
        ],
    ),
)
