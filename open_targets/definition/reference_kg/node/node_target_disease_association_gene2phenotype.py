"""Summary: Gene2Phenotype curated gene-disease assertions.

Definition for TARGET_DISEASE_ASSOCIATION_GENE2PHENOTYPE nodes: filters
Evidence parquet to gene2phenotype curated gene-disease assertions. Gene2Phenotype
curators review human genetic evidence and specify allelic requirements, variant
functional consequence, and direction on trait. Each record carries disease IDs,
study ID, confidence, score, and target IDs. Inference: human variant observations
→ curator assessment of causal gene-disease link → recorded as a curated assertion
in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidenceGene2Phenotype,
    FieldEvidenceGene2PhenotypeAllelicRequirements,
    FieldEvidenceGene2PhenotypeConfidence,
    FieldEvidenceGene2PhenotypeDiseaseFromSource,
    FieldEvidenceGene2PhenotypeDiseaseFromSourceMappedId,
    FieldEvidenceGene2PhenotypeId,
    FieldEvidenceGene2PhenotypeLiterature,
    FieldEvidenceGene2PhenotypeScore,
    FieldEvidenceGene2PhenotypeStudyId,
    FieldEvidenceGene2PhenotypeTargetFromSourceId,
    FieldEvidenceGene2PhenotypeVariantFunctionalConsequenceId,
)

node_target_disease_association_gene2phenotype: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetEvidenceGene2Phenotype),
        primary_id=FieldEvidenceGene2PhenotypeId,
        label="TARGET_DISEASE_ASSOCIATION_GENE2PHENOTYPE",
        properties=[
            FieldEvidenceGene2PhenotypeAllelicRequirements,
            FieldEvidenceGene2PhenotypeConfidence,
            FieldEvidenceGene2PhenotypeDiseaseFromSource,
            FieldEvidenceGene2PhenotypeDiseaseFromSourceMappedId,
            FieldEvidenceGene2PhenotypeLiterature,
            FieldEvidenceGene2PhenotypeScore,
            FieldEvidenceGene2PhenotypeStudyId,
            FieldEvidenceGene2PhenotypeTargetFromSourceId,
            FieldEvidenceGene2PhenotypeVariantFunctionalConsequenceId,
        ],
    )
)
