"""Summary: MOUSE_MODEL -> PHENOTYPE (HPO) edges (cross-species phenotypes).

Definition for HAS_PHENOTYPE edges (mouse model -> human phenotype): explodes
IMPC evidence human phenotype annotations to link each MOUSE_MODEL to HPO
PHENOTYPE terms, capturing cross-species phenotype observations in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceBiologicalModelId,
    FieldEvidenceDiseaseModelAssociatedHumanPhenotypes,
    FieldEvidenceDiseaseModelAssociatedHumanPhenotypesElementId,
    FieldEvidenceSourceId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_mouse_model_has_phenotype_phenotype: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetEvidence,
        exploded_field=FieldEvidenceDiseaseModelAssociatedHumanPhenotypes,
        predicate=EqualityExpression(FieldEvidenceSourceId, "impc"),
    ),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceBiologicalModelId,
    target=FieldEvidenceDiseaseModelAssociatedHumanPhenotypesElementId,
    label=EdgeLabel.HAS_PHENOTYPE,
    properties=[],
)
