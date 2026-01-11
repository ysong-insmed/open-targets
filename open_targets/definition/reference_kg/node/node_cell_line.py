"""Summary: cell line entities from CRISPR evidence (assay context).

Definition for CELL_LINE nodes: explodes CRISPR evidence cell line entries from
the Evidence parquet (sourceId==crispr) to emit experimental cell lines with IDs
and names used as assay contexts in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetEvidenceCrispr,
    FieldEvidenceCrisprDiseaseCellLines,
    FieldEvidenceCrisprDiseaseCellLinesElementId,
    FieldEvidenceCrisprDiseaseCellLinesElementName,
    FieldEvidenceCrisprDiseaseCellLinesElementTissue,
    FieldEvidenceCrisprDiseaseCellLinesElementTissueId,
)

node_cell_line: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetEvidenceCrispr,
        exploded_field=FieldEvidenceCrisprDiseaseCellLines,
    ),
    primary_id=FieldEvidenceCrisprDiseaseCellLinesElementId,
    label="CELL_LINE",
    properties=[
        FieldEvidenceCrisprDiseaseCellLinesElementName,
        FieldEvidenceCrisprDiseaseCellLinesElementTissueId,
        FieldEvidenceCrisprDiseaseCellLinesElementTissue,
    ],
)
