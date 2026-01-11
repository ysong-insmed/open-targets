"""Summary: PanelApp expert-reviewed gene-disease associations.

Definition for TARGET_DISEASE_ASSOCIATION_GENOMICS_ENGLAND nodes: filters
Evidence parquet to genomics_england PanelApp associations. PanelApp curators
review clinical sequencing cases and decide whether a gene is implicated in a
disease, noting allelic requirements, confidence level, and supporting phenotypes.
Each record carries those curations, plus disease IDs, study overview/ID, score,
and target IDs. Inference: clinical cases -> expert panel evaluation -> gene-disease
assertion captured for use in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidenceGenomicsEngland,
    FieldEvidenceGenomicsEnglandAllelicRequirements,
    FieldEvidenceGenomicsEnglandCohortPhenotypes,
    FieldEvidenceGenomicsEnglandConfidence,
    FieldEvidenceGenomicsEnglandDiseaseFromSource,
    FieldEvidenceGenomicsEnglandDiseaseFromSourceId,
    FieldEvidenceGenomicsEnglandDiseaseFromSourceMappedId,
    FieldEvidenceGenomicsEnglandId,
    FieldEvidenceGenomicsEnglandLiterature,
    FieldEvidenceGenomicsEnglandScore,
    FieldEvidenceGenomicsEnglandStudyId,
    FieldEvidenceGenomicsEnglandStudyOverview,
    FieldEvidenceGenomicsEnglandTargetFromSourceId,
)

node_target_disease_association_genomics_england: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetEvidenceGenomicsEngland),
        primary_id=FieldEvidenceGenomicsEnglandId,
        label="TARGET_DISEASE_ASSOCIATION_GENOMICS_ENGLAND",
        properties=[
            FieldEvidenceGenomicsEnglandAllelicRequirements,
            FieldEvidenceGenomicsEnglandCohortPhenotypes,
            FieldEvidenceGenomicsEnglandConfidence,
            FieldEvidenceGenomicsEnglandDiseaseFromSource,
            FieldEvidenceGenomicsEnglandDiseaseFromSourceId,
            FieldEvidenceGenomicsEnglandDiseaseFromSourceMappedId,
            FieldEvidenceGenomicsEnglandLiterature,
            FieldEvidenceGenomicsEnglandScore,
            FieldEvidenceGenomicsEnglandStudyId,
            FieldEvidenceGenomicsEnglandStudyOverview,
            FieldEvidenceGenomicsEnglandTargetFromSourceId,
        ],
    )
)
