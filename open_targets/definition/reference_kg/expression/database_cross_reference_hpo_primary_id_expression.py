"""Summary: hashed HPO xref IDs under `database_cross_reference`.

Primary ID expression for HPO DATABASE_CROSS_REFERENCE nodes: hashes each
`dbXRefs` string under the `database_cross_reference` namespace to create a stable
identifier (raw xref is stored on the node as value).
"""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.data.schema import FieldDiseaseHpoDbXRefsElement
from open_targets.definition.helper import get_namespaced_hash_expression

database_cross_reference_hpo_primary_id_expression: Final[Expression[str]] = get_namespaced_hash_expression(
    "database_cross_reference",
    FieldDiseaseHpoDbXRefsElement,
)
