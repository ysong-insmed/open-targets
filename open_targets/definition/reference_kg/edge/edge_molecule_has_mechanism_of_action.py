"""Summary: MOLECULE -> MECHANISM_OF_ACTION edges (pharmacology linkage).

Definition for HAS_MECHANISM_OF_ACTION edges: explodes chemblIds in the Mechanism
of Action parquet to connect each MOLECULE node (ChEMBL drug) to its
MECHANISM_OF_ACTION node, capturing which pharmacological mechanisms are
attributed to each drug in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDrugMechanismOfAction,
    FieldDrugMechanismOfActionChemblIds,
    FieldDrugMechanismOfActionChemblIdsElement,
)
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import mechanism_of_action_primary_id_expression

edge_molecule_has_mechanism_of_action: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDrugMechanismOfAction,
        exploded_field=FieldDrugMechanismOfActionChemblIds,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDrugMechanismOfActionChemblIdsElement,
    target=mechanism_of_action_primary_id_expression,
    label=EdgeLabel.HAS_MECHANISM_OF_ACTION,
    properties=[],
)
