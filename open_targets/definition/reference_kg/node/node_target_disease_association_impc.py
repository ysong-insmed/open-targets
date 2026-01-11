"""Summary: mouse knockout phenotypes mapped to human disease (IMPC).

Definition for TARGET_DISEASE_ASSOCIATION_IMPC nodes: filters Evidence
parquet to impc mouse model evidence. IMPC perturbs mouse genes, observes
phenotypes, maps those phenotypes to human diseases, and then maps the mouse
gene to the human ortholog. Records keep model IDs (Ensembl/MGI), variant effect,
direction on trait, disease IDs, and scores. Inference: mouse knockout → observed
mouse phenotype → mapped to human disease → mapped to human ortholog gene → stored
as in vivo evidence in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidenceImpc,
    FieldEvidenceImpcBiologicalModelAllelicComposition,
    FieldEvidenceImpcBiologicalModelGeneticBackground,
    FieldEvidenceImpcBiologicalModelId,
    FieldEvidenceImpcDatasourceId,
    FieldEvidenceImpcDirectionOnTrait,
    FieldEvidenceImpcDiseaseFromSource,
    FieldEvidenceImpcDiseaseFromSourceId,
    FieldEvidenceImpcDiseaseFromSourceMappedId,
    FieldEvidenceImpcId,
    FieldEvidenceImpcResourceScore,
    FieldEvidenceImpcScore,
    FieldEvidenceImpcTargetFromSourceId,
    FieldEvidenceImpcTargetId,
    FieldEvidenceImpcTargetInModel,
    FieldEvidenceImpcTargetInModelEnsemblId,
    FieldEvidenceImpcTargetInModelMgiId,
)

node_target_disease_association_impc: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceImpc),
    primary_id=FieldEvidenceImpcId,
    label="TARGET_DISEASE_ASSOCIATION_IMPC",
    properties=[
        FieldEvidenceImpcBiologicalModelAllelicComposition,
        FieldEvidenceImpcBiologicalModelGeneticBackground,
        FieldEvidenceImpcBiologicalModelId,
        FieldEvidenceImpcDatasourceId,
        FieldEvidenceImpcDirectionOnTrait,
        FieldEvidenceImpcDiseaseFromSource,
        FieldEvidenceImpcDiseaseFromSourceId,
        FieldEvidenceImpcDiseaseFromSourceMappedId,
        FieldEvidenceImpcResourceScore,
        FieldEvidenceImpcScore,
        FieldEvidenceImpcTargetFromSourceId,
        FieldEvidenceImpcTargetId,
        FieldEvidenceImpcTargetInModel,
        FieldEvidenceImpcTargetInModelEnsemblId,
        FieldEvidenceImpcTargetInModelMgiId,
    ],
)
