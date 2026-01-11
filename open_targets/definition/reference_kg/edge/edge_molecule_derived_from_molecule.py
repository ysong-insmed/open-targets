"""Summary: child MOLECULE -> parent MOLECULE relationships (ChEMBL salts).

Definition for DERIVED_FROM edges: links child MOLECULE nodes to their parent
ChEMBL molecule (non-null parentId) to represent salt/child-parent relationships
in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression, NotExpression
from open_targets.data.schema import (
    DatasetDrugMolecule,
    FieldDrugMoleculeId,
    FieldDrugMoleculeParentId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_molecule_derived_from_molecule: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetDrugMolecule,
        predicate=NotExpression(EqualityExpression(FieldDrugMoleculeParentId, None)),
    ),
    primary_id=NewUuidExpression(),
    source=FieldDrugMoleculeId,
    target=FieldDrugMoleculeParentId,
    label=EdgeLabel.DERIVED_FROM,
    properties=[],
)
