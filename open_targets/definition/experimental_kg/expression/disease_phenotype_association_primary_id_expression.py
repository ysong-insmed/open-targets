"""Summary: hashed ID combining disease, phenotype, and source disease fields.

Primary ID expression for DISEASE_PHENOTYPE_ASSOCIATION nodes: hashes the
disease ID, phenotype ID, and source disease string together to make a stable
identifier for each reified disease–phenotype evidence record.
"""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
    FieldExpression,
    StringConcatenationExpression,
    StringHashExpression,
    ToStringExpression,
)
from open_targets.data.schema import (
    FieldDiseaseToPhenotypeDisease,
    FieldDiseaseToPhenotypeEvidenceElementDiseaseFromSource,
    FieldDiseaseToPhenotypePhenotype,
)

disease_phenotype_association_primary_id_expression: Final[Expression[str]] = StringHashExpression(
    StringConcatenationExpression(
        [
            ToStringExpression(FieldExpression(FieldDiseaseToPhenotypeDisease)),
            ToStringExpression(FieldExpression(FieldDiseaseToPhenotypePhenotype)),
            ToStringExpression(FieldExpression(FieldDiseaseToPhenotypeEvidenceElementDiseaseFromSource)),
        ],
    ),
)
