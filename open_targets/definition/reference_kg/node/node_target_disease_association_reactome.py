"""Summary: Reactome pathway annotations propagated to targets.

Definition for TARGET_DISEASE_ASSOCIATION_REACTOME nodes: filters Evidence
parquet to reactome pathway-based inference. Reactome links proteins to pathway
steps and curates disease annotations for those pathways. If a target is involved
in a disease-annotated pathway, it is linked to the disease with modulation and
score. Records include target modulation, variant amino acid descriptions, and
disease/target IDs. Inference: target participates in pathway → pathway annotated
to disease → target inherits disease link (pathway-level inference, not direct
genetic/clinical evidence).
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidenceReactome,
    FieldEvidenceReactomeDatasourceId,
    FieldEvidenceReactomeDiseaseFromSource,
    FieldEvidenceReactomeDiseaseFromSourceId,
    FieldEvidenceReactomeDiseaseFromSourceMappedId,
    FieldEvidenceReactomeId,
    FieldEvidenceReactomeScore,
    FieldEvidenceReactomeTargetFromSourceId,
    FieldEvidenceReactomeTargetModulation,
    FieldEvidenceReactomeVariantAminoacidDescriptions,
)

node_target_disease_association_reactome: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceReactome),
    primary_id=FieldEvidenceReactomeId,
    label="TARGET_DISEASE_ASSOCIATION_REACTOME",
    properties=[
        FieldEvidenceReactomeDatasourceId,
        FieldEvidenceReactomeDiseaseFromSource,
        FieldEvidenceReactomeDiseaseFromSourceId,
        FieldEvidenceReactomeDiseaseFromSourceMappedId,
        FieldEvidenceReactomeScore,
        FieldEvidenceReactomeTargetFromSourceId,
        FieldEvidenceReactomeTargetModulation,
        FieldEvidenceReactomeVariantAminoacidDescriptions,
    ],
)
