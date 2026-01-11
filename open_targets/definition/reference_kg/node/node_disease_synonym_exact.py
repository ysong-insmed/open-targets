"""Summary: exact disease synonym nodes (hashed ID, raw synonym value).

Definition for DISEASE_SYNONYM nodes (exact): explodes exact synonyms from the
diseases parquet to emit synonym nodes keyed by namespaced hash, storing the
synonym string for DISEASE synonym edges in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDisease,
    FieldDiseaseSynonymsHasExactSynonym,
    FieldDiseaseSynonymsHasExactSynonymElement,
)
from open_targets.definition.reference_kg.constant import NodeLabel
from open_targets.definition.reference_kg.expression import disease_synonym_exact_primary_id_expression

node_disease_synonym_exact: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDisease,
        exploded_field=FieldDiseaseSynonymsHasExactSynonym,
    ),
    primary_id=disease_synonym_exact_primary_id_expression,
    label=NodeLabel.DISEASE_SYNONYM,
    properties=[
        ("value", FieldDiseaseSynonymsHasExactSynonymElement),
    ],
)
