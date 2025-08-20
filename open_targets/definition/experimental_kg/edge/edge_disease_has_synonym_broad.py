"""Acquisition definition that acquires 'has broad synonym' edges for diseases."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseases,
    FieldDiseasesId,
    FieldDiseasesSynonymsHasBroadSynonym,
    FieldDiseasesSynonymsHasBroadSynonymElement,
)

edge_disease_has_synonym_broad: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseases,
        exploded_field=FieldDiseasesSynonymsHasBroadSynonym,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDiseasesId,
    target=FieldDiseasesSynonymsHasBroadSynonymElement,
    label="HAS_SYNONYM",
    properties=[],
)
