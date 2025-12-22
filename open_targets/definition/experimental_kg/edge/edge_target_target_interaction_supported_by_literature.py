"""Summary: TARGET_TARGET_INTERACTION -> LITERATURE_ENTRY support edges.

Definition for SUPPORTED_BY edges (interaction -> literature): links each
TARGET_TARGET_INTERACTION node to its supporting LITERATURE_ENTRY (hashed id)
when a PubMed ID is present, capturing provenance for protein–protein interactions
in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression, NotExpression
from open_targets.data.schema import (
    DatasetInteractionEvidence,
    FieldInteractionEvidencePubmedId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import (
    target_target_interaction_literature_expression,
    target_target_interaction_primary_id_expression,
)

edge_target_target_interaction_supported_by_literature: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetInteractionEvidence,
            predicate=NotExpression(EqualityExpression(FieldInteractionEvidencePubmedId, None)),
        ),
        primary_id=NewUuidExpression(),
        source=target_target_interaction_primary_id_expression,
        target=target_target_interaction_literature_expression,
        label=EdgeLabel.SUPPORTED_BY,
        properties=[],
    )
)
