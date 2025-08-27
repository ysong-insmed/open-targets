"""Acquisition definition that acquires nodes of PMC literature entries."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetLiteratureIndex,
    FieldLiteratureIndexDate,
    FieldLiteratureIndexDay,
    FieldLiteratureIndexMonth,
    FieldLiteratureIndexPmcid,
    FieldLiteratureIndexPmid,
    FieldLiteratureIndexYear,
)
from open_targets.definition.experimental_kg.expression import literature_index_primary_id_expression

node_literature_entry: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetLiteratureIndex),
    primary_id=literature_index_primary_id_expression,
    label="LITERATURE_ENTRY",
    properties=[
        FieldLiteratureIndexPmid,
        FieldLiteratureIndexPmcid,
        FieldLiteratureIndexDate,
        FieldLiteratureIndexYear,
        FieldLiteratureIndexMonth,
        FieldLiteratureIndexDay,
    ],
)
