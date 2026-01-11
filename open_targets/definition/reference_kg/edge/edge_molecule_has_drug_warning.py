"""Summary: MOLECULE -> DRUG_WARNING safety edges (ChEMBL warnings).

Definition for HAS_DRUG_WARNING edges: explodes chemblIds in the drug warnings
parquet to link each MOLECULE node to a DRUG_WARNING node, attaching regulatory
safety warnings to drugs in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDrugWarning,
    FieldDrugWarningChemblIds,
    FieldDrugWarningChemblIdsElement,
)
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import drug_warning_primary_id_expression

edge_molecule_has_drug_warning: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDrugWarning,
        exploded_field=FieldDrugWarningChemblIds,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDrugWarningChemblIdsElement,
    target=drug_warning_primary_id_expression,
    label=EdgeLabel.HAS_DRUG_WARNING,
    properties=[],
)
