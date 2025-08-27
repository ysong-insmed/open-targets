"""Acquisition definition that acquires 'is a' edges between HPO phenotypes."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetHpo,
    FieldHpoId,
    FieldHpoParents,
    FieldHpoParentsElement,
)

edge_phenotype_is_a: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetHpo,
        exploded_field=FieldHpoParents,
    ),
    primary_id=NewUuidExpression(),
    source=FieldHpoId,
    target=FieldHpoParentsElement,
    label="IS_A",
    properties=[],
)
