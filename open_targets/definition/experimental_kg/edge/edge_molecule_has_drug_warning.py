"""Acquisition definition that acquires edges between molecules and drug warnings."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDrugWarnings,
    FieldDrugWarningsChemblIds,
    FieldDrugWarningsChemblIdsElement,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import drug_warning_primary_id_expression

edge_molecule_has_drug_warning: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDrugWarnings,
        exploded_field=FieldDrugWarningsChemblIds,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDrugWarningsChemblIdsElement,
    target=drug_warning_primary_id_expression,
    label=EdgeLabel.HAS_DRUG_WARNING,
    properties=[],
)
