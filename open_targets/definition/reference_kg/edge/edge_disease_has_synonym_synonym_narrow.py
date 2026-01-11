"""Summary: DISEASE -> narrow synonym edges.

Definition for HAS_SYNONYM edges (narrow): explodes narrow synonyms from the
diseases parquet to link each DISEASE node to its DISEASE_SYNONYM (narrow) node,
capturing synonym relationships in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDisease,
    FieldDiseaseId,
    FieldDiseaseSynonymsHasNarrowSynonym,
)
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import disease_synonym_narrow_primary_id_expression

edge_disease_has_synonym_synonym_narrow: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDisease,
        exploded_field=FieldDiseaseSynonymsHasNarrowSynonym,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDiseaseId,
    target=disease_synonym_narrow_primary_id_expression,
    label=EdgeLabel.HAS_SYNONYM,
    properties=[],
)
