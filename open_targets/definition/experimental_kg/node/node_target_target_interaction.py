"""Acquisition definition that acquires nodes of interaction evidence."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetInteractionEvidence,
    FieldInteractionEvidenceEvidenceScore,
    FieldInteractionEvidenceExpansionMethodMiIdentifier,
    FieldInteractionEvidenceExpansionMethodShortName,
    FieldInteractionEvidenceHostOrganismScientificName,
    FieldInteractionEvidenceHostOrganismTaxId,
    FieldInteractionEvidenceHostOrganismTissueFullName,
    FieldInteractionEvidenceHostOrganismTissueShortName,
    FieldInteractionEvidenceIntA,
    FieldInteractionEvidenceIntABiologicalRole,
    FieldInteractionEvidenceIntASource,
    FieldInteractionEvidenceIntB,
    FieldInteractionEvidenceIntBBiologicalRole,
    FieldInteractionEvidenceIntBSource,
    FieldInteractionEvidenceInteractionDetectionMethodMiIdentifier,
    FieldInteractionEvidenceInteractionDetectionMethodShortName,
    FieldInteractionEvidenceInteractionScore,
    FieldInteractionEvidenceInteractionTypeMiIdentifier,
    FieldInteractionEvidenceInteractionTypeShortName,
)
from open_targets.definition.experimental_kg.expression import target_target_interaction_primary_id_expression

node_target_target_interaction: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetInteractionEvidence),
    primary_id=target_target_interaction_primary_id_expression,
    label="TARGET_TARGET_INTERACTION",
    properties=[
        FieldInteractionEvidenceEvidenceScore,
        FieldInteractionEvidenceExpansionMethodMiIdentifier,
        FieldInteractionEvidenceExpansionMethodShortName,
        FieldInteractionEvidenceHostOrganismScientificName,
        FieldInteractionEvidenceHostOrganismTaxId,
        FieldInteractionEvidenceHostOrganismTissueShortName,
        FieldInteractionEvidenceHostOrganismTissueFullName,
        FieldInteractionEvidenceIntA,
        FieldInteractionEvidenceIntABiologicalRole,
        FieldInteractionEvidenceIntASource,
        FieldInteractionEvidenceIntB,
        FieldInteractionEvidenceIntBBiologicalRole,
        FieldInteractionEvidenceIntBSource,
        FieldInteractionEvidenceInteractionDetectionMethodMiIdentifier,
        FieldInteractionEvidenceInteractionDetectionMethodShortName,
        FieldInteractionEvidenceInteractionScore,
        FieldInteractionEvidenceInteractionTypeMiIdentifier,
        FieldInteractionEvidenceInteractionTypeShortName,
    ],
)
