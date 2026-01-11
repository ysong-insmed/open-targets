"""Summary: namespaced ID for DRUG_WARNING records.

Primary ID expression for DRUG_WARNING nodes: namespaces the warning ID to
provide a stable identifier for drug warning records.
"""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.data.schema import FieldDrugWarningId
from open_targets.definition.helper import get_namespaced_expression

drug_warning_primary_id_expression: Final[Expression[str]] = get_namespaced_expression(
    "drug_warning",
    FieldDrugWarningId,
)
