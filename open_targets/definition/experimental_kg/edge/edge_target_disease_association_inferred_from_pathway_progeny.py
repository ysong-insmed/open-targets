"""Definition for INFERRED_FROM edges (association → pathway, PROGENY): explodes
PROGENy pathway annotations in Evidence to link each TARGET_DISEASE_ASSOCIATION
node (evidence id) to the PATHWAY it was inferred from, capturing pathway-based
inference in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceId,
    FieldEvidencePathways,
    FieldEvidencePathwaysElementId,
    FieldEvidenceSourceId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_disease_association_inferred_from_pathway_progeny: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetEvidence,
            exploded_field=FieldEvidencePathways,
            predicate=EqualityExpression(FieldEvidenceSourceId, "progeny"),
        ),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceId,
        target=FieldEvidencePathwaysElementId,
        label=EdgeLabel.INFERRED_FROM,
        properties=[],
    )
)
