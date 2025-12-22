"""Summary: HPO phenotype terms (id/name/description) anchoring symptoms.

Definition for PHENOTYPE nodes: scans the HPO parquet to emit phenotype terms
with IDs, names, and descriptions, anchoring clinical signs/symptoms for disease
associations and mouse mapping in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetHpo,
    FieldHpoDescription,
    FieldHpoId,
    FieldHpoName,
)

node_phenotype: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetHpo),
    primary_id=FieldHpoId,
    label="PHENOTYPE",
    properties=[
        FieldHpoName,
        FieldHpoDescription,
    ],
)
