"""Summary: PATHWAY -> DISEASE Reactome annotation edges.

Definition for ANNOTATED_WITH edges (pathway -> disease): explodes Reactome
pathway annotations in Evidence (sourceId==reactome) to link PATHWAY nodes to
DISEASE nodes, indicating disease-relevant pathways in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetEvidenceReactome,
    FieldEvidenceReactomeDiseaseFromSourceMappedId,
    FieldEvidenceReactomePathways,
    FieldEvidenceReactomePathwaysElementId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_pathway_annotated_with_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetEvidenceReactome,
        exploded_field=FieldEvidenceReactomePathways,
    ),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceReactomePathwaysElementId,
    target=FieldEvidenceReactomeDiseaseFromSourceMappedId,
    label=EdgeLabel.ANNOTATED_WITH,
    properties=[],
)
