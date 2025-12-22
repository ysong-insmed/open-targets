"""Summary: TARGET -> MOUSE_GENE modelling edges (mouse orthologs).

Definition for MODELLED_BY edges: scans Mouse Phenotypes parquet to link each
human TARGET to its mouse gene ortholog (MOUSE_GENE) used in models, capturing
cross-species modeling relationships in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetMousePhenotypes,
    FieldMousePhenotypesTargetFromSourceId,
    FieldMousePhenotypesTargetInModelEnsemblId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_modelled_by_mouse_gene: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetMousePhenotypes),
    primary_id=NewUuidExpression(),
    source=FieldMousePhenotypesTargetFromSourceId,
    target=FieldMousePhenotypesTargetInModelEnsemblId,
    label=EdgeLabel.MODELLED_BY,
    properties=[],
)
