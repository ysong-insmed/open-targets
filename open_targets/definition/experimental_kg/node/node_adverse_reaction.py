"""Summary: MedDRA adverse reaction terms for pharmacovigilance.

Definition for ADVERSE_REACTION nodes: scans the adverse drug reaction parquet to
emit MedDRA reaction terms (PT codes/names) representing clinical adverse events
used by pharmacovigilance edges in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetAdverseDrugReactions,
    FieldAdverseDrugReactionsMeddraCode,
    FieldAdverseDrugReactionsReactionReactionmeddrapt,
)
from open_targets.definition.experimental_kg.expression import adverse_reaction_primary_id_expression

node_adverse_reaction: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetAdverseDrugReactions),
    primary_id=adverse_reaction_primary_id_expression,
    label="ADVERSE_REACTION",
    properties=[
        FieldAdverseDrugReactionsMeddraCode,
        FieldAdverseDrugReactionsReactionReactionmeddrapt,
    ],
)
