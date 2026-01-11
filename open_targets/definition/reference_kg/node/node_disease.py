"""Summary: EFO/MONDO disease/phenotype terms anchoring KG associations.

Definition for DISEASE nodes: scans the diseases parquet (EFO/MONDO-derived) to
yield clinical/phenotype concepts with names, codes, descriptions, and
therapeutic-area flags that anchor associations, indications, and ontology
hierarchies in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetDisease,
    FieldDiseaseCode,
    FieldDiseaseDescription,
    FieldDiseaseId,
    FieldDiseaseName,
    FieldDiseaseOntologyIsTherapeuticArea,
)

node_disease: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetDisease),
    primary_id=FieldDiseaseId,
    label="DISEASE",
    properties=[
        FieldDiseaseCode,
        FieldDiseaseDescription,
        FieldDiseaseName,
        FieldDiseaseOntologyIsTherapeuticArea,
    ],
)
