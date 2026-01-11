"""Summary: REACTION -> PATHWAY edges building reaction-to-pathway hierarchy.

Definition for IS_PART_OF edges (reaction -> pathway): explodes parent pathway
links from Reactome reactions (Evidence sourceId==reactome) to connect REACTION
nodes to their PATHWAYs, building the reaction-to-pathway hierarchy in the KG.
"""

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
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_reaction_is_part_of_pathway: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
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
