"""Expression that builds a primary id for literature index."""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.data.schema import FieldLiteratureIndexPmid
from open_targets.definition.helper import get_namespaced_expression

literature_index_primary_id_expression: Final[Expression[str]] = get_namespaced_expression(
    "literature_index",
    FieldLiteratureIndexPmid,
)
