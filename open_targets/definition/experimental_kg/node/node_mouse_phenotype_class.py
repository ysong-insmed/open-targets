"""Acquisition definition that acquires nodes of mouse phenotypes."""

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
