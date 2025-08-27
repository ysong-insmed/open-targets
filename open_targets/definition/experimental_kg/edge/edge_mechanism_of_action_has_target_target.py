"""Acquisition definition that acquires 'targets' edges from mechanisms of action to targets."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetMechanismOfAction,
    FieldMechanismOfActionTargets,
    FieldMechanismOfActionTargetsElement,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression.mechanism_of_action_primary_id_expression import (
    mechanism_of_action_primary_id_expression,
)

edge_mechanism_of_action_has_target_target: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetMechanismOfAction,
            exploded_field=FieldMechanismOfActionTargets,
        ),
        primary_id=NewUuidExpression(),
        source=mechanism_of_action_primary_id_expression,
        target=FieldMechanismOfActionTargetsElement,
        label=EdgeLabel.HAS_TARGET,
        properties=[],
    )
)
