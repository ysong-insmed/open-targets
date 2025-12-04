"""Summary: DISEASE hierarchy IS_A edges (child -> parent).

Definition for IS_A edges (disease hierarchy): explodes parent relationships in
the diseases parquet to link each DISEASE node to its parent DISEASE, forming
the ontology hierarchy in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseases,
    FieldDiseasesId,
    FieldDiseasesParents,
    FieldDiseasesParentsElement,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_disease_is_a_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseases,
        exploded_field=FieldDiseasesParents,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDiseasesId,
    target=FieldDiseasesParentsElement,
    label=EdgeLabel.IS_A,
    properties=[],
)
