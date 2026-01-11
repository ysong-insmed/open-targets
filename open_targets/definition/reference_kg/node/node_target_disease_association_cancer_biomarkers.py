"""Summary: curated biomarker -> drug response associations in cancers.

Definition for TARGET_DISEASE_ASSOCIATION_CANCER_BIOMARKERS nodes: filters
Evidence parquet to cancer_biomarkers to emit biomarker-driven associations.
Cancer Biomarkers is a manually curated set of alterations (mutations, CNVs,
expression changes) observed to predict drug response or resistance in specific
cancers/tumor types. Curators review clinical/preclinical studies and score the
evidence. Inference: biomarker alteration in tumor -> reported sensitivity/
resistance to a drug -> expert curation/score -> target tied to the cancer with
confidence, score, and implicated drug. The KG captures this curated biomarker ->
response chain, not generic co-occurrence.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidenceCancerBiomarkers,
    FieldEvidenceCancerBiomarkersBiomarkerName,
    FieldEvidenceCancerBiomarkersConfidence,
    FieldEvidenceCancerBiomarkersDiseaseFromSource,
    FieldEvidenceCancerBiomarkersDiseaseFromSourceMappedId,
    FieldEvidenceCancerBiomarkersDrugFromSource,
    FieldEvidenceCancerBiomarkersId,
    FieldEvidenceCancerBiomarkersScore,
    FieldEvidenceCancerBiomarkersTargetFromSourceId,
)

node_target_disease_association_cancer_biomarkers: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetEvidenceCancerBiomarkers),
        primary_id=FieldEvidenceCancerBiomarkersId,
        label="TARGET_DISEASE_ASSOCIATION_CANCER_BIOMARKERS",
        properties=[
            FieldEvidenceCancerBiomarkersBiomarkerName,
            FieldEvidenceCancerBiomarkersConfidence,
            FieldEvidenceCancerBiomarkersDiseaseFromSource,
            FieldEvidenceCancerBiomarkersDiseaseFromSourceMappedId,
            FieldEvidenceCancerBiomarkersDrugFromSource,
            FieldEvidenceCancerBiomarkersScore,
            FieldEvidenceCancerBiomarkersTargetFromSourceId,
        ],
    )
)
