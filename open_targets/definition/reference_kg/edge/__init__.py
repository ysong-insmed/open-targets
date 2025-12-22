"""Summary: edge definitions for the reference knowledge graph."""

from open_targets.definition.reference_kg.edge.edge_cell_line_sampled_from_tissue import (
    edge_cell_line_sampled_from_tissue,
)
from open_targets.definition.reference_kg.edge.edge_disease_has_database_cross_reference_database_cross_reference import (
    edge_disease_has_database_cross_reference_database_cross_reference,
)
from open_targets.definition.reference_kg.edge.edge_disease_has_synonym_synonym_broad import (
    edge_disease_has_synonym_synonym_broad,
)
from open_targets.definition.reference_kg.edge.edge_disease_has_synonym_synonym_exact import (
    edge_disease_has_synonym_synonym_exact,
)
from open_targets.definition.reference_kg.edge.edge_disease_has_synonym_synonym_narrow import (
    edge_disease_has_synonym_synonym_narrow,
)
from open_targets.definition.reference_kg.edge.edge_disease_has_synonym_synonym_related import (
    edge_disease_has_synonym_synonym_related,
)
from open_targets.definition.reference_kg.edge.edge_disease_is_a_disease import edge_disease_is_a_disease
from open_targets.definition.reference_kg.edge.edge_disease_phenotype_association_has_object_phenotype import (
    edge_disease_phenotype_association_has_object_phenotype,
)
from open_targets.definition.reference_kg.edge.edge_disease_subject_of_disease_phenotype_association import (
    edge_disease_subject_of_disease_phenotype_association,
)
from open_targets.definition.reference_kg.edge.edge_literature_mentions_entity import edge_literature_mentions_entity
from open_targets.definition.reference_kg.edge.edge_mechanism_of_action_has_target_target import (
    edge_mechanism_of_action_has_target_target,
)
from open_targets.definition.reference_kg.edge.edge_molecule_derived_from_molecule import (
    edge_molecule_derived_from_molecule,
)
from open_targets.definition.reference_kg.edge.edge_molecule_has_adverse_reaction_adverse_reaction import (
    edge_molecule_has_adverse_reaction_adverse_reaction,
)
from open_targets.definition.reference_kg.edge.edge_molecule_has_drug_warning import edge_molecule_has_drug_warning
from open_targets.definition.reference_kg.edge.edge_molecule_has_mechanism_of_action import (
    edge_molecule_has_mechanism_of_action,
)
from open_targets.definition.reference_kg.edge.edge_molecule_indicates_disease import edge_molecule_indicates_disease
from open_targets.definition.reference_kg.edge.edge_mouse_gene_allele_in_mouse_model import (
    edge_mouse_gene_allele_in_mouse_model,
)
from open_targets.definition.reference_kg.edge.edge_mouse_model_has_phenotype_mouse_phenotype import (
    edge_mouse_model_has_phenotype_mouse_phenotype,
)
from open_targets.definition.reference_kg.edge.edge_mouse_model_has_phenotype_phenotype import (
    edge_mouse_model_has_phenotype_phenotype,
)
from open_targets.definition.reference_kg.edge.edge_mouse_phenotype_classified_as_mouse_phenotype_class import (
    edge_mouse_phenotype_classified_as_mouse_phenotype_class,
)
from open_targets.definition.reference_kg.edge.edge_pathway_annotated_with_disease import (
    edge_pathway_annotated_with_disease,
)
from open_targets.definition.reference_kg.edge.edge_pathway_is_part_of_pathway import edge_pathway_is_part_of_pathway
from open_targets.definition.reference_kg.edge.edge_phenotype_has_database_cross_reference_database_cross_reference import (
    edge_phenotype_has_database_cross_reference_database_cross_reference,
)
from open_targets.definition.reference_kg.edge.edge_phenotype_is_a_phenotype import edge_phenotype_is_a_phenotype
from open_targets.definition.reference_kg.edge.edge_reaction_is_part_of_pathway import (
    edge_reaction_is_part_of_pathway,
)
from open_targets.definition.reference_kg.edge.edge_target_associated_with_adverse_reaction import (
    edge_target_associated_with_adverse_reaction,
)
from open_targets.definition.reference_kg.edge.edge_target_belongs_to_target_classification import (
    edge_target_belongs_to_target_classification,
)
from open_targets.definition.reference_kg.edge.edge_target_disease_association_cancer_biomarkers_has_drug_response_entity import (
    edge_target_disease_association_cancer_biomarkers_has_drug_response_entity,
)
from open_targets.definition.reference_kg.edge.edge_target_disease_association_cancer_biomarkers_has_molecule_molecule import (
    edge_target_disease_association_cancer_biomarkers_has_molecule_molecule,
)
from open_targets.definition.reference_kg.edge.edge_target_disease_association_chembl_has_molecule_molecule import (
    edge_target_disease_association_chembl_has_molecule_molecule,
)
from open_targets.definition.reference_kg.edge.edge_target_disease_association_crispr_tested_in_cell_line import (
    edge_target_disease_association_crispr_tested_in_cell_line,
)
from open_targets.definition.reference_kg.edge.edge_target_disease_association_has_object_disease import (
    edge_target_disease_association_has_object_disease,
)
from open_targets.definition.reference_kg.edge.edge_target_disease_association_inferred_from_mouse_model import (
    edge_target_disease_association_inferred_from_mouse_model,
)
from open_targets.definition.reference_kg.edge.edge_target_disease_association_inferred_from_pathway_progeny import (
    edge_target_disease_association_inferred_from_pathway_progeny,
)
from open_targets.definition.reference_kg.edge.edge_target_disease_association_inferred_from_pathway_slapenrich import (
    edge_target_disease_association_inferred_from_pathway_slapenrich,
)
from open_targets.definition.reference_kg.edge.edge_target_disease_association_inferred_from_reaction import (
    edge_target_disease_association_inferred_from_reaction,
)
from open_targets.definition.reference_kg.edge.edge_target_disease_association_supported_by_literature import (
    edge_target_disease_association_supported_by_literature,
)
from open_targets.definition.reference_kg.edge.edge_target_has_database_cross_reference_database_cross_reference import (
    edge_target_has_database_cross_reference_database_cross_reference,
)
from open_targets.definition.reference_kg.edge.edge_target_has_homologue_in_species_species import (
    edge_target_has_homologue_in_species_species,
)
from open_targets.definition.reference_kg.edge.edge_target_has_summary_association_by_datasource_direct_disease import (
    edge_target_has_summary_association_by_datasource_direct_disease,
)
from open_targets.definition.reference_kg.edge.edge_target_has_summary_association_by_datasource_indirect_disease import (
    edge_target_has_summary_association_by_datasource_indirect_disease,
)
from open_targets.definition.reference_kg.edge.edge_target_has_summary_association_by_datatype_direct_disease import (
    edge_target_has_summary_association_by_datatype_direct_disease,
)
from open_targets.definition.reference_kg.edge.edge_target_has_summary_association_by_datatype_indirect_disease import (
    edge_target_has_summary_association_by_datatype_indirect_disease,
)
from open_targets.definition.reference_kg.edge.edge_target_has_summary_association_by_overall_direct_disease import (
    edge_target_has_summary_association_by_overall_direct_disease,
)
from open_targets.definition.reference_kg.edge.edge_target_has_summary_association_by_overall_indirect_disease import (
    edge_target_has_summary_association_by_overall_indirect_disease,
)
from open_targets.definition.reference_kg.edge.edge_target_has_target_target_interaction_target_a import (
    edge_target_has_target_target_interaction_target_a,
)
from open_targets.definition.reference_kg.edge.edge_target_has_target_target_interaction_target_b import (
    edge_target_has_target_target_interaction_target_b,
)
from open_targets.definition.reference_kg.edge.edge_target_involves_in_pathway import edge_target_involves_in_pathway
from open_targets.definition.reference_kg.edge.edge_target_located_in_subcellular_location import (
    edge_target_located_in_subcellular_location,
)
from open_targets.definition.reference_kg.edge.edge_target_modelled_by_mouse_gene import (
    edge_target_modelled_by_mouse_gene,
)
from open_targets.definition.reference_kg.edge.edge_target_related_to_go_term import edge_target_related_to_go_term
from open_targets.definition.reference_kg.edge.edge_target_subject_of_target_disease_association import (
    edge_target_subject_of_target_disease_association,
)
from open_targets.definition.reference_kg.edge.edge_target_target_interaction_supported_by_literature import (
    edge_target_target_interaction_supported_by_literature,
)

__all__ = [
    "edge_cell_line_sampled_from_tissue",
    "edge_disease_has_database_cross_reference_database_cross_reference",
    "edge_disease_has_synonym_synonym_broad",
    "edge_disease_has_synonym_synonym_exact",
    "edge_disease_has_synonym_synonym_narrow",
    "edge_disease_has_synonym_synonym_related",
    "edge_disease_is_a_disease",
    "edge_disease_phenotype_association_has_object_phenotype",
    "edge_disease_subject_of_disease_phenotype_association",
    "edge_literature_mentions_entity",
    "edge_mechanism_of_action_has_target_target",
    "edge_molecule_derived_from_molecule",
    "edge_molecule_has_adverse_reaction_adverse_reaction",
    "edge_molecule_has_drug_warning",
    "edge_molecule_has_mechanism_of_action",
    "edge_molecule_indicates_disease",
    "edge_mouse_gene_allele_in_mouse_model",
    "edge_mouse_model_has_phenotype_mouse_phenotype",
    "edge_mouse_model_has_phenotype_phenotype",
    "edge_mouse_phenotype_classified_as_mouse_phenotype_class",
    "edge_pathway_annotated_with_disease",
    "edge_pathway_is_part_of_pathway",
    "edge_phenotype_has_database_cross_reference_database_cross_reference",
    "edge_phenotype_is_a_phenotype",
    "edge_reaction_is_part_of_pathway",
    "edge_target_associated_with_adverse_reaction",
    "edge_target_belongs_to_target_classification",
    "edge_target_disease_association_cancer_biomarkers_has_drug_response_entity",
    "edge_target_disease_association_cancer_biomarkers_has_molecule_molecule",
    "edge_target_disease_association_chembl_has_molecule_molecule",
    "edge_target_disease_association_crispr_tested_in_cell_line",
    "edge_target_disease_association_has_object_disease",
    "edge_target_disease_association_inferred_from_mouse_model",
    "edge_target_disease_association_inferred_from_pathway_progeny",
    "edge_target_disease_association_inferred_from_pathway_slapenrich",
    "edge_target_disease_association_inferred_from_reaction",
    "edge_target_disease_association_supported_by_literature",
    "edge_target_has_database_cross_reference_database_cross_reference",
    "edge_target_has_homologue_in_species_species",
    "edge_target_has_summary_association_by_datasource_direct_disease",
    "edge_target_has_summary_association_by_datasource_indirect_disease",
    "edge_target_has_summary_association_by_datatype_direct_disease",
    "edge_target_has_summary_association_by_datatype_indirect_disease",
    "edge_target_has_summary_association_by_overall_direct_disease",
    "edge_target_has_summary_association_by_overall_indirect_disease",
    "edge_target_has_target_target_interaction_target_a",
    "edge_target_has_target_target_interaction_target_b",
    "edge_target_involves_in_pathway",
    "edge_target_located_in_subcellular_location",
    "edge_target_modelled_by_mouse_gene",
    "edge_target_related_to_go_term",
    "edge_target_subject_of_target_disease_association",
    "edge_target_target_interaction_supported_by_literature",
]
