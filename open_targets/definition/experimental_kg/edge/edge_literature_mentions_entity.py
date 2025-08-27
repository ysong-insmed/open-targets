"""Acquisition definition that acquires edges from literature entries to keywords."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetLiteratureIndex,
    FieldLiteratureIndexKeywordId,
    FieldLiteratureIndexKeywordType,
    FieldLiteratureIndexPmid,
    FieldLiteratureIndexRelevance,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_literature_mentions_entity: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetLiteratureIndex),
    primary_id=NewUuidExpression(),
    source=FieldLiteratureIndexPmid,
    target=FieldLiteratureIndexKeywordId,
    label=EdgeLabel.MENTIONS,
    properties=[
        FieldLiteratureIndexKeywordId,
        FieldLiteratureIndexKeywordType,
        FieldLiteratureIndexRelevance,
    ],
)
