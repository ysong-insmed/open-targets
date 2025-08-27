"""Expression that builds a primary id for disease-phenotype associations.

To be honest this is a guess, but it's the only way I can think of to
ensure that the primary id is unique.
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
