"""Acquisition definition that acquires edges between diseases and phenotypes."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetInteractionEvidence,
    FieldInteractionEvidencePubmedId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import (
    target_target_interaction_primary_id_expression,
)

edge_target_target_interaction_supported_by: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetInteractionEvidence),
        primary_id=NewUuidExpression(),
        source=target_target_interaction_primary_id_expression,
        target=FieldInteractionEvidencePubmedId,
        label=EdgeLabel.SUPPORTED_BY,
        properties=[],
    )
)
