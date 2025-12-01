"""Definition for DISEASE_SYNONYM nodes (exact): explodes exact synonyms from
the diseases parquet to emit synonym nodes keyed by namespaced hash, storing the
synonym string for DISEASE synonym edges in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseases,
    FieldDiseasesSynonymsHasExactSynonym,
    FieldDiseasesSynonymsHasExactSynonymElement,
)
from open_targets.definition.experimental_kg.constant import NodeLabel
from open_targets.definition.experimental_kg.expression import disease_synonym_exact_primary_id_expression

node_disease_synonym_exact: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseases,
        exploded_field=FieldDiseasesSynonymsHasExactSynonym,
    ),
    primary_id=disease_synonym_exact_primary_id_expression,
    label=NodeLabel.DISEASE_SYNONYM,
    properties=[
        ("value", FieldDiseasesSynonymsHasExactSynonymElement),
    ],
)
