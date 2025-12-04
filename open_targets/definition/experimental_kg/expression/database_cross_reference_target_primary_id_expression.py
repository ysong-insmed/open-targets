"""Summary: hashed target xref IDs under `database_cross_reference`.

Primary ID expression for target DATABASE_CROSS_REFERENCE nodes: hashes the
normalized target xref value (`source:id`) under the `database_cross_reference`
namespace to create a stable identifier (raw value retained separately)."""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.definition.experimental_kg.expression.database_cross_reference_target_value_expression import (
    database_cross_reference_target_value_expression,
)
from open_targets.definition.helper import get_namespaced_hash_expression

database_cross_reference_target_primary_id_expression: Final[Expression[str]] = get_namespaced_hash_expression(
    "database_cross_reference",
    database_cross_reference_target_value_expression,
)
