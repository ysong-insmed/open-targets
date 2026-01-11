"""Summary: reified mechanisms of action for drugs (action type, targets).

Definition for MECHANISM_OF_ACTION nodes: explodes Mechanism of Action records
by chemblId to emit reified pharmacology entries (action type, mechanism text,
target type/name) that link molecules to their biological targets and provenance
in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDrugMechanismOfAction,
    FieldDrugMechanismOfActionActionType,
    FieldDrugMechanismOfActionChemblIds,
    FieldDrugMechanismOfActionMechanismOfAction,
    FieldDrugMechanismOfActionTargetName,
    FieldDrugMechanismOfActionTargetType,
)
from open_targets.definition.reference_kg.expression.mechanism_of_action_primary_id_expression import (
    mechanism_of_action_primary_id_expression,
)

node_mechanism_of_action: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDrugMechanismOfAction,
        exploded_field=FieldDrugMechanismOfActionChemblIds,
    ),
    primary_id=mechanism_of_action_primary_id_expression,
    label="MECHANISM_OF_ACTION",
    properties=[
        FieldDrugMechanismOfActionActionType,
        FieldDrugMechanismOfActionMechanismOfAction,
        FieldDrugMechanismOfActionTargetName,
        FieldDrugMechanismOfActionTargetType,
    ],
)
