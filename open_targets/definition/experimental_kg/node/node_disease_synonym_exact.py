"""Acquisition definition that acquires nodes of exact disease synonyms."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseases,
    FieldDiseasesSynonymsHasExactSynonym,
    FieldDiseasesSynonymsHasExactSynonymElement,
)
from open_targets.definition.experimental_kg.namespace import Namespace
from open_targets.definition.helper import get_simple_value_node_definition

node_disease_synonym_exact: Final[AcquisitionDefinition[NodeInfo]] = get_simple_value_node_definition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseases,
        exploded_field=FieldDiseasesSynonymsHasExactSynonym,
    ),
    namespace=Namespace.SYNONYM,
    value_expression=FieldDiseasesSynonymsHasExactSynonymElement,
    label="EXACT_SYNONYM",
)
