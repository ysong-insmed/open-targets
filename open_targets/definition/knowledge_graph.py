"""Dataclass for defining a knowledge graph."""

from collections.abc import Sequence
from dataclasses import dataclass

from open_targets.adapter.acquisition_definition import AcquisitionDefinition
from open_targets.adapter.output import EdgeInfo, NodeInfo


@dataclass(frozen=True, kw_only=True)
class KnowledgeGraphDefinition:
    """Definition of a knowledge graph.

    A knowledge graph is a collection of nodes and edges that represent the
    relationships between entities in the data.
    """

    node_definitions: Sequence[AcquisitionDefinition[NodeInfo]]
    edge_definitions: Sequence[AcquisitionDefinition[EdgeInfo]]
