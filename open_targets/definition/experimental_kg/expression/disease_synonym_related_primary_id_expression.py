"""Primary ID expression for related DISEASE_SYNONYM nodes: hashes each synonym
string under the `disease_synonym` namespace to create a stable identifier."""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.data.schema import FieldDiseasesSynonymsHasRelatedSynonymElement
from open_targets.definition.helper import get_namespaced_hash_expression

disease_synonym_related_primary_id_expression: Final[Expression[str]] = get_namespaced_hash_expression(
    "disease_synonym",
    FieldDiseasesSynonymsHasRelatedSynonymElement,
)
