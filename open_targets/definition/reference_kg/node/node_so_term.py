"""Summary: SO_TERM nodes from SO dataset.

Definition for SO_TERM nodes: represents Sequence Ontology (SO) terms used to
classify consequences of genetic variants (e.g., missense_variant), providing a
consistent ontology for variant annotation in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetSo,
    FieldSoId,
    FieldSoLabel,
)
from open_targets.definition.reference_kg.constant import NodeLabel

node_so_term: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetSo),
    primary_id=FieldSoId,
    label=NodeLabel.SO_TERM,
    properties=[
        FieldSoLabel,
    ],
)
