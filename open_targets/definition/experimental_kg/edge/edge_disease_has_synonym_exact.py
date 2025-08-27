"""Acquisition definition that acquires 'has exact synonym' edges for diseases."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseases,
    FieldDiseasesId,
    FieldDiseasesSynonymsHasExactSynonym,
    FieldDiseasesSynonymsHasExactSynonymElement,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_disease_has_synonym_exact: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseases,
        exploded_field=FieldDiseasesSynonymsHasExactSynonym,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDiseasesId,
    target=FieldDiseasesSynonymsHasExactSynonymElement,
    label=EdgeLabel.HAS_SYNONYM,
    properties=[],
)
