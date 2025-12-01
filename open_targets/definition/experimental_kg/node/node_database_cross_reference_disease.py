"""Definition for DATABASE_CROSS_REFERENCE nodes (disease xrefs): explodes the
scalar `dbXRefs` array from the diseases parquet, hashes each string under the
`database_cross_reference` namespace for the primary ID, and stores the string
as property `value` so DISEASE nodes can point to external ontology/DB IDs."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseases,
    FieldDiseasesDbXRefs,
    FieldDiseasesDbXRefsElement,
)
from open_targets.definition.experimental_kg.constant import NodeLabel
from open_targets.definition.experimental_kg.expression import database_cross_reference_disease_primary_id_expression

node_database_cross_reference_disease: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseases,
        exploded_field=FieldDiseasesDbXRefs,
    ),
    primary_id=database_cross_reference_disease_primary_id_expression,
    label=NodeLabel.DATABASE_CROSS_REFERENCE,
    properties=[
        ("value", FieldDiseasesDbXRefsElement),
    ],
)
