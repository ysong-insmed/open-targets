"""Acquisition definition that acquires edges between diseases and phenotypes."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseaseToPhenotype,
    FieldDiseaseToPhenotypeDisease,
    FieldDiseaseToPhenotypeEvidence,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import disease_phenotype_association_primary_id_expression

edge_disease_subject_of_disease_phenotype_association: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetDiseaseToPhenotype,
            exploded_field=FieldDiseaseToPhenotypeEvidence,
        ),
        primary_id=NewUuidExpression(),
        source=FieldDiseaseToPhenotypeDisease,
        target=disease_phenotype_association_primary_id_expression,
        label=EdgeLabel.SUBJECT_OF,
        properties=[],
    )
)
