"""Summary: MOUSE_PHENOTYPE -> MOUSE_PHENOTYPE_CLASS classification edges.

Definition for CLASSIFIED_AS edges: explodes phenotype class annotations in Mouse
Phenotypes parquet to link each MOUSE_PHENOTYPE to its MOUSE_PHENOTYPE_CLASS,
capturing MP class grouping in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetMousePhenotype,
    FieldMousePhenotypeModelPhenotypeClasses,
    FieldMousePhenotypeModelPhenotypeClassesElementId,
    FieldMousePhenotypeModelPhenotypeId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_mouse_phenotype_classified_as_mouse_phenotype_class: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetMousePhenotype,
            exploded_field=FieldMousePhenotypeModelPhenotypeClasses,
        ),
        primary_id=NewUuidExpression(),
        source=FieldMousePhenotypeModelPhenotypeId,
        target=FieldMousePhenotypeModelPhenotypeClassesElementId,
        label=EdgeLabel.CLASSIFIED_AS,
        properties=[],
    )
)
