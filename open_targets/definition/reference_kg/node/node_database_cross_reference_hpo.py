"""Summary: HPO cross-reference nodes (hashed ID, raw value property).

Definition for DATABASE_CROSS_REFERENCE nodes (HPO xrefs): explodes `dbXRefs`
from the HPO parquet, hashes each string under the `database_cross_reference`
namespace for the primary ID, and stores the raw string as property `value` so
PHENOTYPE/HPO nodes can expose external identifiers.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseaseHpo,
    FieldDiseaseHpoDbXRefs,
    FieldDiseaseHpoDbXRefsElement,
)
from open_targets.definition.reference_kg.constant import NodeLabel
from open_targets.definition.reference_kg.expression import database_cross_reference_hpo_primary_id_expression

node_database_cross_reference_hpo: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseaseHpo,
        exploded_field=FieldDiseaseHpoDbXRefs,
    ),
    primary_id=database_cross_reference_hpo_primary_id_expression,
    label=NodeLabel.DATABASE_CROSS_REFERENCE,
    properties=[
        ("value", FieldDiseaseHpoDbXRefsElement),
    ],
)
