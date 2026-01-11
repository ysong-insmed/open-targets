"""Summary: mouse phenotype class (MP) terms for classifying phenotypes.

Definition for MOUSE_PHENOTYPE_CLASS nodes: explodes phenotype class entries from
the Mouse Phenotypes parquet to emit MP class terms (id/label) used to classify
mouse phenotypes.
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
    FieldMousePhenotypeModelPhenotypeClasses,
    FieldMousePhenotypeModelPhenotypeClassesElementId,
    FieldMousePhenotypeModelPhenotypeClassesElementLabel,
)

node_mouse_phenotype_class: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetMousePhenotype,
        exploded_field=FieldMousePhenotypeModelPhenotypeClasses,
    ),
    primary_id=FieldMousePhenotypeModelPhenotypeClassesElementId,
    label="MOUSE_PHENOTYPE_CLASS",
    properties=[
        FieldMousePhenotypeModelPhenotypeClassesElementLabel,
    ],
)
