"""Summary: Linking edges for Evidence datasets."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidenceCancerBiomarkers,
    DatasetEvidenceCancerGeneCensus,
    DatasetEvidenceChembl,
    DatasetEvidenceClingen,
    DatasetEvidenceCrispr,
    DatasetEvidenceCrisprScreen,
    DatasetEvidenceEuropepmc,
    DatasetEvidenceEva,
    DatasetEvidenceEvaSomatic,
    DatasetEvidenceExpressionAtlas,
    DatasetEvidenceGene2Phenotype,
    DatasetEvidenceGeneBurden,
    DatasetEvidenceGenomicsEngland,
    DatasetEvidenceGwasCredibleSets,
    DatasetEvidenceImpc,
    DatasetEvidenceIntogen,
    DatasetEvidenceOrphanet,
    DatasetEvidenceReactome,
    DatasetEvidenceUniprotLiterature,
    DatasetEvidenceUniprotVariants,
    FieldEvidenceCancerBiomarkersDiseaseId,
    FieldEvidenceCancerBiomarkersId,
    FieldEvidenceCancerBiomarkersTargetId,
    FieldEvidenceCancerGeneCensusDiseaseId,
    FieldEvidenceCancerGeneCensusId,
    FieldEvidenceCancerGeneCensusTargetId,
    FieldEvidenceChemblDiseaseId,
    FieldEvidenceChemblId,
    FieldEvidenceChemblTargetId,
    FieldEvidenceClingenDiseaseId,
    FieldEvidenceClingenId,
    FieldEvidenceClingenTargetId,
    FieldEvidenceCrisprDiseaseId,
    FieldEvidenceCrisprId,
    FieldEvidenceCrisprScreenDiseaseId,
    FieldEvidenceCrisprScreenId,
    FieldEvidenceCrisprScreenTargetId,
    FieldEvidenceCrisprTargetId,
    FieldEvidenceEuropepmcDiseaseId,
    FieldEvidenceEuropepmcId,
    FieldEvidenceEuropepmcTargetId,
    FieldEvidenceEvaDiseaseId,
    FieldEvidenceEvaId,
    FieldEvidenceEvaSomaticDiseaseId,
    FieldEvidenceEvaSomaticId,
    FieldEvidenceEvaSomaticTargetId,
    FieldEvidenceEvaTargetId,
    FieldEvidenceExpressionAtlasDiseaseId,
    FieldEvidenceExpressionAtlasId,
    FieldEvidenceExpressionAtlasTargetId,
    FieldEvidenceGene2PhenotypeDiseaseId,
    FieldEvidenceGene2PhenotypeId,
    FieldEvidenceGene2PhenotypeTargetId,
    FieldEvidenceGeneBurdenDiseaseId,
    FieldEvidenceGeneBurdenId,
    FieldEvidenceGeneBurdenTargetId,
    FieldEvidenceGenomicsEnglandDiseaseId,
    FieldEvidenceGenomicsEnglandId,
    FieldEvidenceGenomicsEnglandTargetId,
    FieldEvidenceGwasCredibleSetsDiseaseId,
    FieldEvidenceGwasCredibleSetsId,
    FieldEvidenceGwasCredibleSetsTargetId,
    FieldEvidenceImpcDiseaseId,
    FieldEvidenceImpcId,
    FieldEvidenceImpcTargetId,
    FieldEvidenceIntogenDiseaseId,
    FieldEvidenceIntogenId,
    FieldEvidenceIntogenTargetId,
    FieldEvidenceOrphanetDiseaseId,
    FieldEvidenceOrphanetId,
    FieldEvidenceOrphanetTargetId,
    FieldEvidenceReactomeDiseaseId,
    FieldEvidenceReactomeId,
    FieldEvidenceReactomeTargetId,
    FieldEvidenceUniprotLiteratureDiseaseId,
    FieldEvidenceUniprotLiteratureId,
    FieldEvidenceUniprotLiteratureTargetId,
    FieldEvidenceUniprotVariantsDiseaseId,
    FieldEvidenceUniprotVariantsId,
    FieldEvidenceUniprotVariantsTargetId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

edge_target_subject_of_evidence_cancer_biomarkers: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceCancerBiomarkers),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceCancerBiomarkersTargetId,
    target=FieldEvidenceCancerBiomarkersId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_cancer_biomarkers_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceCancerBiomarkers),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceCancerBiomarkersId,
    target=FieldEvidenceCancerBiomarkersDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_cancer_gene_census: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceCancerGeneCensus),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceCancerGeneCensusTargetId,
    target=FieldEvidenceCancerGeneCensusId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_cancer_gene_census_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceCancerGeneCensus),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceCancerGeneCensusId,
    target=FieldEvidenceCancerGeneCensusDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_chembl: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceChembl),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceChemblTargetId,
    target=FieldEvidenceChemblId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_chembl_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceChembl),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceChemblId,
    target=FieldEvidenceChemblDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_clingen: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceClingen),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceClingenTargetId,
    target=FieldEvidenceClingenId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_clingen_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceClingen),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceClingenId,
    target=FieldEvidenceClingenDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_crispr: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceCrispr),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceCrisprTargetId,
    target=FieldEvidenceCrisprId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_crispr_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceCrispr),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceCrisprId,
    target=FieldEvidenceCrisprDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_crispr_screen: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceCrisprScreen),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceCrisprScreenTargetId,
    target=FieldEvidenceCrisprScreenId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_crispr_screen_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceCrisprScreen),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceCrisprScreenId,
    target=FieldEvidenceCrisprScreenDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_europepmc: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceEuropepmc),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceEuropepmcTargetId,
    target=FieldEvidenceEuropepmcId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_europepmc_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceEuropepmc),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceEuropepmcId,
    target=FieldEvidenceEuropepmcDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_eva: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceEva),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceEvaTargetId,
    target=FieldEvidenceEvaId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_eva_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceEva),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceEvaId,
    target=FieldEvidenceEvaDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_eva_somatic: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceEvaSomatic),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceEvaSomaticTargetId,
    target=FieldEvidenceEvaSomaticId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_eva_somatic_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceEvaSomatic),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceEvaSomaticId,
    target=FieldEvidenceEvaSomaticDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_expression_atlas: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceExpressionAtlas),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceExpressionAtlasTargetId,
    target=FieldEvidenceExpressionAtlasId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_expression_atlas_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceExpressionAtlas),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceExpressionAtlasId,
    target=FieldEvidenceExpressionAtlasDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_gene2_phenotype: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceGene2Phenotype),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceGene2PhenotypeTargetId,
    target=FieldEvidenceGene2PhenotypeId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_gene2_phenotype_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceGene2Phenotype),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceGene2PhenotypeId,
    target=FieldEvidenceGene2PhenotypeDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_gene_burden: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceGeneBurden),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceGeneBurdenTargetId,
    target=FieldEvidenceGeneBurdenId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_gene_burden_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceGeneBurden),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceGeneBurdenId,
    target=FieldEvidenceGeneBurdenDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_genomics_england: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceGenomicsEngland),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceGenomicsEnglandTargetId,
    target=FieldEvidenceGenomicsEnglandId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_genomics_england_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceGenomicsEngland),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceGenomicsEnglandId,
    target=FieldEvidenceGenomicsEnglandDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_gwas_credible_sets: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceGwasCredibleSets),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceGwasCredibleSetsTargetId,
    target=FieldEvidenceGwasCredibleSetsId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_gwas_credible_sets_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceGwasCredibleSets),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceGwasCredibleSetsId,
    target=FieldEvidenceGwasCredibleSetsDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_impc: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceImpc),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceImpcTargetId,
    target=FieldEvidenceImpcId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_impc_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceImpc),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceImpcId,
    target=FieldEvidenceImpcDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_intogen: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceIntogen),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceIntogenTargetId,
    target=FieldEvidenceIntogenId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_intogen_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceIntogen),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceIntogenId,
    target=FieldEvidenceIntogenDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_orphanet: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceOrphanet),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceOrphanetTargetId,
    target=FieldEvidenceOrphanetId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_orphanet_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceOrphanet),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceOrphanetId,
    target=FieldEvidenceOrphanetDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_reactome: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceReactome),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceReactomeTargetId,
    target=FieldEvidenceReactomeId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_reactome_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceReactome),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceReactomeId,
    target=FieldEvidenceReactomeDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_uniprot_literature: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceUniprotLiterature),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceUniprotLiteratureTargetId,
    target=FieldEvidenceUniprotLiteratureId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_uniprot_literature_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceUniprotLiterature),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceUniprotLiteratureId,
    target=FieldEvidenceUniprotLiteratureDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

edge_target_subject_of_evidence_uniprot_variants: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceUniprotVariants),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceUniprotVariantsTargetId,
    target=FieldEvidenceUniprotVariantsId,
    label=EdgeLabel.SUBJECT_OF,
    properties=[],
)

edge_evidence_uniprot_variants_has_object_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidenceUniprotVariants),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceUniprotVariantsId,
    target=FieldEvidenceUniprotVariantsDiseaseId,
    label=EdgeLabel.HAS_OBJECT,
    properties=[],
)

