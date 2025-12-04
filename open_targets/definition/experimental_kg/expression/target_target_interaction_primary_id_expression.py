"""Summary: hashed pair of targets for TARGET_TARGET_INTERACTION IDs.

Primary ID expression for TARGET_TARGET_INTERACTION nodes: hashes the pair
of interacting targets (A,B) to create a stable identifier for the interaction
record."""

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
