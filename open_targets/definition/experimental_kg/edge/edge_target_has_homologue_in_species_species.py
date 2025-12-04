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
    DatasetTargets,
    FieldTargetsHomologues,
    FieldTargetsHomologuesElementHomologyType,
    FieldTargetsHomologuesElementIsHighConfidence,
    FieldTargetsHomologuesElementPriority,
    FieldTargetsHomologuesElementQueryPercentageIdentity,
    FieldTargetsHomologuesElementTargetGeneId,
    FieldTargetsHomologuesElementTargetGeneSymbol,
    FieldTargetsHomologuesElementTargetPercentageIdentity,
    FieldTargetsId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import species_primary_id_expression

edge_target_has_homologue_in_species_species: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetTargets,
            exploded_field=FieldTargetsHomologues,
        ),
        primary_id=NewUuidExpression(),
        source=FieldTargetsId,
        target=species_primary_id_expression,
        label=EdgeLabel.HAS_HOMOLOGUE_IN_SPECIES,
        properties=[
            FieldTargetsHomologuesElementHomologyType,
            FieldTargetsHomologuesElementTargetGeneId,
            FieldTargetsHomologuesElementTargetGeneSymbol,
            FieldTargetsHomologuesElementIsHighConfidence,
            FieldTargetsHomologuesElementQueryPercentageIdentity,
            FieldTargetsHomologuesElementTargetPercentageIdentity,
            FieldTargetsHomologuesElementPriority,
        ],
    )
)
