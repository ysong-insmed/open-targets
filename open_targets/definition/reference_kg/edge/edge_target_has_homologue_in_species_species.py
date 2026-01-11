"""Summary: TARGET -> SPECIES homology edges with identity/confidence metrics.

Definition for HAS_HOMOLOGUE_IN_SPECIES edges: explodes homologue entries in the
Targets parquet to link each human TARGET to a SPECIES node, carrying homology
type, confidence, gene IDs/symbols, and percentage identity metrics to represent
cross-species homology in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTarget,
    FieldTargetHomologues,
    FieldTargetHomologuesElementHomologyType,
    FieldTargetHomologuesElementIsHighConfidence,
    FieldTargetHomologuesElementPriority,
    FieldTargetHomologuesElementQueryPercentageIdentity,
    FieldTargetHomologuesElementTargetGeneId,
    FieldTargetHomologuesElementTargetGeneSymbol,
    FieldTargetHomologuesElementTargetPercentageIdentity,
    FieldTargetId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import species_primary_id_expression

edge_target_has_homologue_in_species_species: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetTarget,
            exploded_field=FieldTargetHomologues,
        ),
        primary_id=NewUuidExpression(),
        source=FieldTargetId,
        target=species_primary_id_expression,
        label=EdgeLabel.HAS_HOMOLOGUE_IN_SPECIES,
        properties=[
            FieldTargetHomologuesElementHomologyType,
            FieldTargetHomologuesElementTargetGeneId,
            FieldTargetHomologuesElementTargetGeneSymbol,
            FieldTargetHomologuesElementIsHighConfidence,
            FieldTargetHomologuesElementQueryPercentageIdentity,
            FieldTargetHomologuesElementTargetPercentageIdentity,
            FieldTargetHomologuesElementPriority,
        ],
    )
)
