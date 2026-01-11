"""Summary: literature publication nodes (PMID/PMCID/date).

Definition for LITERATURE_ENTRY nodes: scans the literature index parquet to emit
publication nodes (PMID/PMCID/date) keyed by a hashed primary ID, serving as
reified articles that can support associations or mention entities in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetLiterature,
    FieldLiteratureDay,
    FieldLiteratureMonth,
    FieldLiteraturePmcid,
    FieldLiteraturePmid,
    FieldLiteratureYear,
)
from open_targets.definition.reference_kg.expression import literature_entry_primary_id_expression

node_literature_entry: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetLiterature),
    primary_id=literature_entry_primary_id_expression,
    label="LITERATURE_ENTRY",
    properties=[
        FieldLiteraturePmid,
        FieldLiteraturePmcid,
        FieldLiteratureYear,
        FieldLiteratureMonth,
        FieldLiteratureDay,
    ],
)
