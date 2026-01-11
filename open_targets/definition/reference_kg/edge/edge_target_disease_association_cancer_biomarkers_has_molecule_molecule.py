"""Summary: cancer_biomarkers association -> MOLECULE edges.

Definition for HAS_MOLECULE edges (cancer_biomarkers): links each
TARGET_DISEASE_ASSOCIATION_CANCER_BIOMARKERS node (evidence id) to its drug
Molecule when present, capturing the biomarker-associated molecule in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression, NotExpression
from open_targets.data.schema import (
    DatasetEvidenceCancerBiomarkers,
    FieldEvidenceCancerBiomarkersDrugId,
    FieldEvidenceCancerBiomarkersId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_target_disease_association_cancer_biomarkers_has_molecule_molecule: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidenceCancerBiomarkers,
            predicate=NotExpression(EqualityExpression(FieldEvidenceCancerBiomarkersDrugId, None)),
        ),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceCancerBiomarkersId,
        target=FieldEvidenceCancerBiomarkersDrugId,
        label=EdgeLabel.HAS_MOLECULE,
        properties=[],
    )
)
