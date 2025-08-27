"""Expression that builds a primary id for mechanisms of action."""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.data.schema import FieldTargetsTargetClassElementLabel
from open_targets.definition.helper import get_namespaced_hash_expression

target_classification_primary_id_expression: Final[Expression[str]] = get_namespaced_hash_expression(
    "target_classification",
    FieldTargetsTargetClassElementLabel,
)
