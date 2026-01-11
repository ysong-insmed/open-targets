"""Summary: EVA somatic submissions (tumor variant interpretations).

Definition for TARGET_DISEASE_ASSOCIATION_EVA_SOMATIC nodes: filters Evidence
parquet to eva_somatic tumor submissions. Somatic submissions describe tumor-
acquired variants and their clinical interpretation. Each record carries variant
IDs (HGVS/RS), functional consequence, allele origins, allelic requirements,
direction on trait, clinical significance, cohort phenotypes, and disease/target
IDs with confidence/score. Inference: tumor sequencing → clinical interpretation
of variant relevance → map to gene and cancer → represent curated somatic evidence
in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidenceEvaSomatic,
    FieldEvidenceEvaSomaticAlleleOrigins,
    FieldEvidenceEvaSomaticAllelicRequirements,
    FieldEvidenceEvaSomaticClinicalSignificances,
    FieldEvidenceEvaSomaticConfidence,
    FieldEvidenceEvaSomaticDiseaseFromSource,
    FieldEvidenceEvaSomaticDiseaseFromSourceId,
    FieldEvidenceEvaSomaticDiseaseFromSourceMappedId,
    FieldEvidenceEvaSomaticId,
    FieldEvidenceEvaSomaticLiterature,
    FieldEvidenceEvaSomaticScore,
    FieldEvidenceEvaSomaticStudyId,
    FieldEvidenceEvaSomaticTargetFromSourceId,
    FieldEvidenceEvaSomaticVariantFunctionalConsequenceId,
    FieldEvidenceEvaSomaticVariantHgvsId,
    FieldEvidenceEvaSomaticVariantId,
    FieldEvidenceEvaSomaticVariantRsId,
)

node_target_disease_association_eva_somatic: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetEvidenceEvaSomatic),
        primary_id=FieldEvidenceEvaSomaticId,
        label="TARGET_DISEASE_ASSOCIATION_EVA_SOMATIC",
        properties=[
            FieldEvidenceEvaSomaticAlleleOrigins,
            FieldEvidenceEvaSomaticAllelicRequirements,
            FieldEvidenceEvaSomaticClinicalSignificances,
            FieldEvidenceEvaSomaticConfidence,
            FieldEvidenceEvaSomaticDiseaseFromSource,
            FieldEvidenceEvaSomaticDiseaseFromSourceId,
            FieldEvidenceEvaSomaticDiseaseFromSourceMappedId,
            FieldEvidenceEvaSomaticLiterature,
            FieldEvidenceEvaSomaticScore,
            FieldEvidenceEvaSomaticStudyId,
            FieldEvidenceEvaSomaticTargetFromSourceId,
            FieldEvidenceEvaSomaticVariantFunctionalConsequenceId,
            FieldEvidenceEvaSomaticVariantHgvsId,
            FieldEvidenceEvaSomaticVariantId,
            FieldEvidenceEvaSomaticVariantRsId,
        ],
    )
)
