"""Summary: DISEASE -> related synonym edges.

Definition for HAS_SYNONYM edges (related): explodes related synonyms from the
diseases parquet to link each DISEASE node to its DISEASE_SYNONYM (related) node,
capturing synonym relationships in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseases,
    FieldDiseasesId,
    FieldDiseasesSynonymsHasRelatedSynonym,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import disease_synonym_related_primary_id_expression

edge_disease_has_synonym_synonym_related: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseases,
        exploded_field=FieldDiseasesSynonymsHasRelatedSynonym,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDiseasesId,
    target=disease_synonym_related_primary_id_expression,
    label=EdgeLabel.HAS_SYNONYM,
    properties=[],
)
