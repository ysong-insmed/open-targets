"""Summary: mouse models with allelic composition/genetic background.

Definition for MOUSE_MODEL nodes: explodes biologicalModels from the Mouse
Phenotypes parquet to emit individual mouse models with allelic composition and
genetic background, providing in vivo model entities for phenotype and inference
edges in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionNodeAcquisitionDefinition,
)
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetMousePhenotype,
    FieldMousePhenotypeBiologicalModels,
    FieldMousePhenotypeBiologicalModelsElementAllelicComposition,
    FieldMousePhenotypeBiologicalModelsElementGeneticBackground,
    FieldMousePhenotypeBiologicalModelsElementId,
)

node_mouse_model: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetMousePhenotype,
        exploded_field=FieldMousePhenotypeBiologicalModels,
    ),
    primary_id=FieldMousePhenotypeBiologicalModelsElementId,
    label="MOUSE_MODEL",
    properties=[
        FieldMousePhenotypeBiologicalModelsElementAllelicComposition,
        FieldMousePhenotypeBiologicalModelsElementGeneticBackground,
    ],
)
