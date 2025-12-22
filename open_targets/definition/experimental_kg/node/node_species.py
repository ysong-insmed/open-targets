"""Summary: species nodes (id/name) used for target homology edges.

Definition for SPECIES nodes: explodes homologue entries from the Targets parquet
to emit species (id/name) nodes used in homology edges from human targets to
other species in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTargets,
    FieldTargetsHomologues,
    FieldTargetsHomologuesElementSpeciesId,
    FieldTargetsHomologuesElementSpeciesName,
)
from open_targets.definition.experimental_kg.expression import species_primary_id_expression

node_species: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetTargets,
        exploded_field=FieldTargetsHomologues,
    ),
    primary_id=species_primary_id_expression,
    label="SPECIES",
    properties=[
        FieldTargetsHomologuesElementSpeciesId,
        FieldTargetsHomologuesElementSpeciesName,
    ],
)
