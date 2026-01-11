"""Summary: DISEASE -> broad synonym edges.

Definition for HAS_SYNONYM edges (broad): explodes broad synonyms from the
diseases parquet to link each DISEASE node to its DISEASE_SYNONYM (broad) node,
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
    FieldDiseaseSynonymsHasBroadSynonym,
)
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import disease_synonym_broad_primary_id_expression

edge_disease_has_synonym_synonym_broad: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDisease,
        exploded_field=FieldDiseaseSynonymsHasBroadSynonym,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDiseaseId,
    target=disease_synonym_broad_primary_id_expression,
    label=EdgeLabel.HAS_SYNONYM,
    properties=[],
)
