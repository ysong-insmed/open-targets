"""Summary: MOUSE_MODEL -> MOUSE_PHENOTYPE edges (observed phenotypes).

Definition for HAS_PHENOTYPE edges (mouse model -> mouse phenotype): explodes
biologicalModels in the Mouse Phenotypes parquet to connect each MOUSE_MODEL to
its observed MOUSE_PHENOTYPE term, capturing in vivo phenotype outcomes in the
KG."""

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
