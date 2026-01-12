"""Summary: CREDIBLE_SET nodes from CredibleSet dataset.

Definition for CREDIBLE_SET nodes: represents a set of variants (credible set)
fine-mapped from a StudyLocus, capturing method and confidence metadata.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionNodeAcquisitionDefinition,
)
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetCredibleSet,
    FieldCredibleSetConfidence,
    FieldCredibleSetCredibleSetIndex,
    FieldCredibleSetCredibleSetlog10Bf,
    FieldCredibleSetFinemappingMethod,
    FieldCredibleSetPurityMeanR2,
    FieldCredibleSetPurityMinR2,
    FieldCredibleSetSampleSize,
)
from open_targets.definition.reference_kg.expression import credible_set_primary_id_expression

node_credible_set: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetCredibleSet),
    primary_id=credible_set_primary_id_expression,
    label="CREDIBLE_SET",
    properties=[
        FieldCredibleSetFinemappingMethod,
        FieldCredibleSetConfidence,
        FieldCredibleSetCredibleSetlog10Bf,
        FieldCredibleSetCredibleSetIndex,
        FieldCredibleSetSampleSize,
        FieldCredibleSetPurityMeanR2,
        FieldCredibleSetPurityMinR2,
    ],
)
