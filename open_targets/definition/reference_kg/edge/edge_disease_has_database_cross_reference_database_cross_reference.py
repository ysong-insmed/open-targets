"""Summary: DISEASE -> DATABASE_CROSS_REFERENCE links for disease xrefs.

Definition for HAS_DATABASE_CROSS_REFERENCE edges: explodes the scalar `dbXRefs`
array in the diseases parquet and links each DISEASE node to its
DATABASE_CROSS_REFERENCE node (ID = namespaced hash `database_cross_reference`
of the xref string; the raw string is stored on the target node), making external
disease IDs traversable in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDisease,
    FieldDiseaseDbXRefs,
    FieldDiseaseId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import database_cross_reference_disease_primary_id_expression

edge_disease_has_database_cross_reference_database_cross_reference: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetDisease,
            exploded_field=FieldDiseaseDbXRefs,
        ),
        primary_id=NewUuidExpression(),
        source=FieldDiseaseId,
        target=database_cross_reference_disease_primary_id_expression,
        label=EdgeLabel.HAS_DATABASE_CROSS_REFERENCE,
        properties=[],
    )
)
