"""Primary ID expression for LITERATURE_ENTRY nodes: namespaces the PMID to
produce a stable identifier for literature records."""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.data.schema import FieldLiteratureIndexPmid
from open_targets.definition.helper import get_namespaced_expression

literature_entry_primary_id_expression: Final[Expression[str]] = get_namespaced_expression(
    "literature_entry",
    FieldLiteratureIndexPmid,
)
