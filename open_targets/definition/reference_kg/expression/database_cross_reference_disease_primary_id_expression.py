"""Summary: hashed disease xref IDs under `database_cross_reference`.

Primary ID expression for disease DATABASE_CROSS_REFERENCE nodes: hashes each
`dbXRefs` string under the `database_cross_reference` namespace to ensure a stable
identifier (raw xref is stored on the node as value).
"""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.data.schema import FieldDiseaseDbXRefsElement
from open_targets.definition.helper import get_namespaced_hash_expression

database_cross_reference_disease_primary_id_expression: Final[Expression[str]] = get_namespaced_hash_expression(
    "database_cross_reference",
    FieldDiseaseDbXRefsElement,
)
