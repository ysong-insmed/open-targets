"""Acquisition definition that acquires 'has child' edges for molecules."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetMolecule,
    FieldMoleculeId,
    FieldMoleculeParentId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_molecule_has_child: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetMolecule),
    primary_id=NewUuidExpression(),
    source=FieldMoleculeId,
    target=FieldMoleculeParentId,
    label=EdgeLabel.DERIVED_FROM,
    properties=[],
)
