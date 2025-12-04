"""Summary: TARGET -> PATHWAY membership edges (Reactome annotations).

Definition for INVOLVES_IN edges: explodes Reactome pathway annotations in the
Targets parquet to connect each TARGET to the PATHWAYs it participates in,
capturing pathway membership for functional context in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTargets,
    FieldTargetsId,
    FieldTargetsPathways,
    FieldTargetsPathwaysElementPathwayId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_involves_in_pathway: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetTargets,
        exploded_field=FieldTargetsPathways,
    ),
    primary_id=NewUuidExpression(),
    source=FieldTargetsId,
    target=FieldTargetsPathwaysElementPathwayId,
    label=EdgeLabel.INVOLVES_IN,
    properties=[],
)
