"""Definition for MOUSE_PHENOTYPE_CLASS nodes: explodes phenotype class entries
from the Mouse Phenotypes parquet to emit MP class terms (id/label) used to
classify mouse phenotypes in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionNodeAcquisitionDefinition,
)
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetMousePhenotypes,
    FieldMousePhenotypesModelPhenotypeClasses,
    FieldMousePhenotypesModelPhenotypeClassesElementId,
    FieldMousePhenotypesModelPhenotypeClassesElementLabel,
)

node_mouse_phenotype_class: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetMousePhenotypes,
        exploded_field=FieldMousePhenotypesModelPhenotypeClasses,
    ),
    primary_id=FieldMousePhenotypesModelPhenotypeClassesElementId,
    label="MOUSE_PHENOTYPE_CLASS",
    properties=[
        FieldMousePhenotypesModelPhenotypeClassesElementLabel,
    ],
)
