"""Expressions that are reused across multiple definitions.

This is a workaround for some of the relationships that are missing primary
ids or inconsistencies in the data.
"""

from open_targets.definition.experimental_kg.expression.adverse_reaction_primary_id_expression import (
    adverse_reaction_primary_id_expression,
)
from open_targets.definition.experimental_kg.expression.disease_phenotype_association_primary_id_expression import (
    disease_phenotype_association_primary_id_expression,
)
from open_targets.definition.experimental_kg.expression.drug_warning_primary_id_expression import (
    drug_warning_primary_id_expression,
)
from open_targets.definition.experimental_kg.expression.literature_index_primary_id_expression import (
    literature_index_primary_id_expression,
)
from open_targets.definition.experimental_kg.expression.mechanism_of_action_primary_id_expression import (
    mechanism_of_action_primary_id_expression,
)
from open_targets.definition.experimental_kg.expression.species_primary_id_expression import (
    species_primary_id_expression,
)
from open_targets.definition.experimental_kg.expression.subcellular_location_primary_id_expression import (
    subcellular_location_primary_id_expression,
)
from open_targets.definition.experimental_kg.expression.target_classification_primary_id_expression import (
    target_classification_primary_id_expression,
)
from open_targets.definition.experimental_kg.expression.target_database_cross_reference_value_expression import (
    target_database_cross_reference_value_expression,
)
from open_targets.definition.experimental_kg.expression.target_target_interaction_primary_id_expression import (
    target_target_interaction_primary_id_expression,
)

__all__ = [
    "adverse_reaction_primary_id_expression",
    "disease_phenotype_association_primary_id_expression",
    "drug_warning_primary_id_expression",
    "literature_index_primary_id_expression",
    "mechanism_of_action_primary_id_expression",
    "species_primary_id_expression",
    "subcellular_location_primary_id_expression",
    "target_classification_primary_id_expression",
    "target_database_cross_reference_value_expression",
    "target_target_interaction_primary_id_expression",
]
