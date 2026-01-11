"""Summary: TARGET -> ADVERSE_REACTION safety edges (FAERS disproportionality).

Definition for ASSOCIATED_WITH edges (target - adverse reaction): scans adverse
target reaction parquet to link TARGET nodes to ADVERSE_REACTION nodes, carrying
FAERS disproportionality statistics (LLR, A/B/C/D) and report counts to represent
target-level safety signals in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetOpenfdaSignificantAdverseTargetReactions,
    FieldOpenfdaSignificantAdverseTargetReactionsCount,
    FieldOpenfdaSignificantAdverseTargetReactionsCritval,
    FieldOpenfdaSignificantAdverseTargetReactionsEvent,
    FieldOpenfdaSignificantAdverseTargetReactionsLlr,
    FieldOpenfdaSignificantAdverseTargetReactionsMeddraCode,
    FieldOpenfdaSignificantAdverseTargetReactionsTargetId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import adverse_reaction_primary_id_expression

edge_target_associated_with_adverse_reaction: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetOpenfdaSignificantAdverseTargetReactions),
        primary_id=NewUuidExpression(),
        source=FieldOpenfdaSignificantAdverseTargetReactionsTargetId,
        target=adverse_reaction_primary_id_expression,
        label=EdgeLabel.ASSOCIATED_WITH,
        properties=[
            FieldOpenfdaSignificantAdverseTargetReactionsEvent,
            FieldOpenfdaSignificantAdverseTargetReactionsMeddraCode,
            FieldOpenfdaSignificantAdverseTargetReactionsLlr,
            FieldOpenfdaSignificantAdverseTargetReactionsCount,
            FieldOpenfdaSignificantAdverseTargetReactionsCritval,
        ],
    )
)
