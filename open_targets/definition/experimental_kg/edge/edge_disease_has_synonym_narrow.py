"""Acquisition definition that acquires 'has narrow synonym' edges for diseases."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseases,
    FieldDiseasesId,
    FieldDiseasesSynonymsHasNarrowSynonym,
    FieldDiseasesSynonymsHasNarrowSynonymElement,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_disease_has_synonym_narrow: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseases,
        exploded_field=FieldDiseasesSynonymsHasNarrowSynonym,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDiseasesId,
    target=FieldDiseasesSynonymsHasNarrowSynonymElement,
    label=EdgeLabel.HAS_SYNONYM,
    properties=[],
)
