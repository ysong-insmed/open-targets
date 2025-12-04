"""Summary: PATHWAY hierarchy edges (child -> parent) from Reactome.

Definition for IS_PART_OF edges (pathway hierarchy): explodes parent lists in the
Reactome parquet to link each PATHWAY node to its parent PATHWAY, building the
Reactome hierarchy for traversal in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetReactome,
    FieldReactomeId,
    FieldReactomeParents,
    FieldReactomeParentsElement,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_pathway_is_part_of_pathway: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetReactome,
        exploded_field=FieldReactomeParents,
    ),
    primary_id=NewUuidExpression(),
    source=FieldReactomeId,
    target=FieldReactomeParentsElement,
    label=EdgeLabel.IS_PART_OF,
    properties=[],
)
