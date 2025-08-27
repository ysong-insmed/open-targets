"""Acquisition definition that acquires nodes of drug warning references."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetDrugWarnings,
    FieldDrugWarningsCountry,
    FieldDrugWarningsDescription,
    FieldDrugWarningsToxicityClass,
    FieldDrugWarningsWarningType,
    FieldDrugWarningsYear,
)
from open_targets.definition.experimental_kg.expression import drug_warning_primary_id_expression

node_drug_warning: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetDrugWarnings),
    primary_id=drug_warning_primary_id_expression,
    label="DRUG_WARNING",
    properties=[
        FieldDrugWarningsToxicityClass,
        FieldDrugWarningsCountry,
        FieldDrugWarningsDescription,
        FieldDrugWarningsWarningType,
        FieldDrugWarningsYear,
    ],
)
