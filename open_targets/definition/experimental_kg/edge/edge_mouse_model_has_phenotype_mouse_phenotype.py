"""Acquisition definition that acquires edges between mouse targets and human targets."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetMousePhenotypes,
    FieldMousePhenotypesBiologicalModels,
    FieldMousePhenotypesBiologicalModelsElementId,
    FieldMousePhenotypesModelPhenotypeId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_mouse_model_has_phenotype_mouse_phenotype: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetMousePhenotypes,
            exploded_field=FieldMousePhenotypesBiologicalModels,
        ),
        primary_id=NewUuidExpression(),
        source=FieldMousePhenotypesBiologicalModelsElementId,
        target=FieldMousePhenotypesModelPhenotypeId,
        label=EdgeLabel.HAS_PHENOTYPE,
        properties=[],
    )
)
