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
    DatasetAdverseTargetReactions,
    FieldAdverseTargetReactionsA,
    FieldAdverseTargetReactionsActerm,
    FieldAdverseTargetReactionsAterm,
    FieldAdverseTargetReactionsB,
    FieldAdverseTargetReactionsC,
    FieldAdverseTargetReactionsCterm,
    FieldAdverseTargetReactionsD,
    FieldAdverseTargetReactionsLlr,
    FieldAdverseTargetReactionsTargetId,
    FieldAdverseTargetReactionsUniqReportIdsByReaction,
    FieldAdverseTargetReactionsUniqReportIdsByTarget,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import adverse_reaction_primary_id_expression

edge_target_associated_with_adverse_reaction: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetAdverseTargetReactions),
        primary_id=NewUuidExpression(),
        source=FieldAdverseTargetReactionsTargetId,
        target=adverse_reaction_primary_id_expression,
        label=EdgeLabel.ASSOCIATED_WITH,
        properties=[
            FieldAdverseTargetReactionsActerm,
            FieldAdverseTargetReactionsAterm,
            FieldAdverseTargetReactionsCterm,
            FieldAdverseTargetReactionsLlr,
            FieldAdverseTargetReactionsA,
            FieldAdverseTargetReactionsB,
            FieldAdverseTargetReactionsC,
            FieldAdverseTargetReactionsD,
            FieldAdverseTargetReactionsUniqReportIdsByReaction,
            FieldAdverseTargetReactionsUniqReportIdsByTarget,
        ],
    )
)
