"""Acquisition definition that acquires 'is a' edges between diseases."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseases,
    FieldDiseasesId,
    FieldDiseasesParents,
    FieldDiseasesParentsElement,
)

edge_disease_is_a: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseases,
        exploded_field=FieldDiseasesParents,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDiseasesId,
    target=FieldDiseasesParentsElement,
    label="IS_A",
    properties=[],
)
