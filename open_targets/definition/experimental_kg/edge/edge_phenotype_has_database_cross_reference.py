"""Acquisition definition that acquires 'has cross-reference' edges for HPO phenotypes."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetHpo,
    FieldHpoDbXRefs,
    FieldHpoDbXRefsElement,
    FieldHpoId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel, Namespace
from open_targets.definition.helper import get_namespaced_hash_expression

edge_phenotype_has_database_cross_reference: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetHpo,
            exploded_field=FieldHpoDbXRefs,
        ),
        primary_id=NewUuidExpression(),
        source=FieldHpoId,
        target=get_namespaced_hash_expression(
            Namespace.DATABASE_CROSS_REFERENCE,
            FieldHpoDbXRefsElement,
        ),
        label=EdgeLabel.HAS_DATABASE_CROSS_REFERENCE,
        properties=[],
    )
)
