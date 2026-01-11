"""Summary: MOLECULE -> ADVERSE_REACTION pharmacovigilance edges (FAERS stats).

Definition for HAS_ADVERSE_REACTION edges: scans adverse drug reaction parquet
(FAERS-derived) to link MOLECULE nodes to ADVERSE_REACTION nodes, carrying
disproportionality statistics (LLR, A/B/C/D) and unique report counts to model
pharmacovigilance signals in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetOpenfdaSignificantAdverseDrugReactions,
    FieldOpenfdaSignificantAdverseDrugReactionsChemblId,
    FieldOpenfdaSignificantAdverseDrugReactionsCount,
    FieldOpenfdaSignificantAdverseDrugReactionsCritval,
    FieldOpenfdaSignificantAdverseDrugReactionsEvent,
    FieldOpenfdaSignificantAdverseDrugReactionsLlr,
    FieldOpenfdaSignificantAdverseDrugReactionsMeddraCode,
)
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import adverse_reaction_primary_id_expression

edge_molecule_has_adverse_reaction_adverse_reaction: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetOpenfdaSignificantAdverseDrugReactions),
        primary_id=NewUuidExpression(),
        source=FieldOpenfdaSignificantAdverseDrugReactionsChemblId,
        target=adverse_reaction_primary_id_expression,
        label=EdgeLabel.HAS_ADVERSE_REACTION,
        properties=[
            FieldOpenfdaSignificantAdverseDrugReactionsEvent,
            FieldOpenfdaSignificantAdverseDrugReactionsMeddraCode,
            FieldOpenfdaSignificantAdverseDrugReactionsLlr,
            FieldOpenfdaSignificantAdverseDrugReactionsCount,
            FieldOpenfdaSignificantAdverseDrugReactionsCritval,
        ],
    )
)
