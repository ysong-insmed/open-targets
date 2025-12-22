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
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidencePathways,
    FieldEvidencePathwaysElementId,
    FieldEvidenceReactionId,
    FieldEvidenceSourceId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_reaction_is_part_of_pathway: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetEvidence,
        exploded_field=FieldEvidencePathways,
        predicate=EqualityExpression(FieldEvidenceSourceId, "reactome"),
    ),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceReactionId,
    target=FieldEvidencePathwaysElementId,
    label=EdgeLabel.IS_PART_OF,
    properties=[],
)
