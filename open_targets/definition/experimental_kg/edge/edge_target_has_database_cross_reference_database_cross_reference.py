"""Acquisition definition that acquires edges from targets to cross-references."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTargets,
    FieldTargetsDbXrefs,
    FieldTargetsId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import database_cross_reference_target_value_expression

edge_target_has_database_cross_reference_database_cross_reference: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetTargets,
            exploded_field=FieldTargetsDbXrefs,
        ),
        primary_id=NewUuidExpression(),
        source=FieldTargetsId,
        target=database_cross_reference_target_value_expression,
        label=EdgeLabel.HAS_DATABASE_CROSS_REFERENCE,
        properties=[],
    )
)
