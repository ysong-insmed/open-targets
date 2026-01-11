"""Summary: ChEMBL drug warning entities for safety annotations.

Definition for DRUG_WARNING nodes: scans ChEMBL drug warning records to emit
warning entities (toxicity class, country, description, warning type, year),
serving as safety annotations attached to molecules in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetDrugWarning,
    FieldDrugWarningCountry,
    FieldDrugWarningDescription,
    FieldDrugWarningToxicityClass,
    FieldDrugWarningWarningType,
    FieldDrugWarningYear,
)
from open_targets.definition.reference_kg.expression import drug_warning_primary_id_expression

node_drug_warning: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetDrugWarning),
    primary_id=drug_warning_primary_id_expression,
    label="DRUG_WARNING",
    properties=[
        FieldDrugWarningToxicityClass,
        FieldDrugWarningCountry,
        FieldDrugWarningDescription,
        FieldDrugWarningWarningType,
        FieldDrugWarningYear,
    ],
)
