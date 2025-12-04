"""Summary: MOUSE_GENE -> MOUSE_MODEL allele relationships.

Definition for ALLELE_IN edges: explodes biologicalModels in Mouse Phenotypes
parquet to link each MOUSE_GENE (Ensembl mouse gene) to the MOUSE_MODEL it
appears in, capturing allele/model relationships in the KG."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetMousePhenotypes,
    FieldMousePhenotypesBiologicalModels,
    FieldMousePhenotypesBiologicalModelsElementId,
    FieldMousePhenotypesTargetInModelEnsemblId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_mouse_gene_allele_in_mouse_model: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetMousePhenotypes,
        exploded_field=FieldMousePhenotypesBiologicalModels,
    ),
    primary_id=NewUuidExpression(),
    source=FieldMousePhenotypesTargetInModelEnsemblId,
    target=FieldMousePhenotypesBiologicalModelsElementId,
    label=EdgeLabel.ALLELE_IN,
    properties=[],
)
