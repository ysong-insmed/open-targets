"""Summary: STUDY_LOCUS nodes from L2GPrediction dataset.

Definition for STUDY_LOCUS nodes: represents a unique Study-Locus combination
derived from L2GPrediction dataset (or CredibleSets), used as a hub for colocalisation
and fine-mapping data.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetL2GPrediction,
    FieldL2GPredictionStudyLocusId,
)
from open_targets.definition.reference_kg.constant import NodeLabel

node_study_locus: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetL2GPrediction),
    primary_id=FieldL2GPredictionStudyLocusId,
    label=NodeLabel.STUDY_LOCUS,
    properties=[],
)
