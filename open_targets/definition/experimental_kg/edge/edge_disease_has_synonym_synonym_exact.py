"""Summary: DISEASE -> exact synonym edges.

Definition for HAS_SYNONYM edges (exact): explodes exact synonyms from the
diseases parquet to link each DISEASE node to its DISEASE_SYNONYM (exact) node,
capturing synonym relationships in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseases,
    FieldDiseasesId,
    FieldDiseasesSynonymsHasExactSynonym,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import disease_synonym_exact_primary_id_expression

edge_disease_has_synonym_synonym_exact: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseases,
        exploded_field=FieldDiseasesSynonymsHasExactSynonym,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDiseasesId,
    target=disease_synonym_exact_primary_id_expression,
    label=EdgeLabel.HAS_SYNONYM,
    properties=[],
)
