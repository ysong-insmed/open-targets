"""Acquisition definition that acquires 'has mechanism' edges for molecules."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetMechanismOfAction,
    FieldMechanismOfActionChemblIds,
    FieldMechanismOfActionChemblIdsElement,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import mechanism_of_action_primary_id_expression

edge_molecule_has_mechanism_of_action: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetMechanismOfAction,
        exploded_field=FieldMechanismOfActionChemblIds,
    ),
    primary_id=NewUuidExpression(),
    source=FieldMechanismOfActionChemblIdsElement,
    target=mechanism_of_action_primary_id_expression,
    label=EdgeLabel.HAS_MECHANISM_OF_ACTION,
    properties=[],
)
