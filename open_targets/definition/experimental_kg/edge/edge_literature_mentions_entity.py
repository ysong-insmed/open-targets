"""Summary: LITERATURE_ENTRY mentions entity edges (keyword + relevance).

Definition for MENTIONS edges: links each LITERATURE_ENTRY to a keyword entity
(target/disease/molecule/phenotype) using the literature index parquet, carrying
keyword type and relevance so text-mined evidence can be traversed in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetLiteratureIndex,
    FieldLiteratureIndexKeywordId,
    FieldLiteratureIndexKeywordType,
    FieldLiteratureIndexRelevance,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import literature_entry_primary_id_expression

edge_literature_mentions_entity: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetLiteratureIndex),
    primary_id=NewUuidExpression(),
    source=literature_entry_primary_id_expression,
    target=FieldLiteratureIndexKeywordId,
    label=EdgeLabel.MENTIONS,
    properties=[
        FieldLiteratureIndexKeywordId,
        FieldLiteratureIndexKeywordType,
        FieldLiteratureIndexRelevance,
    ],
)
