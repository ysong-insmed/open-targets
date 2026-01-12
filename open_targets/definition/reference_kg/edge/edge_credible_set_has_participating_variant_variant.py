"""Summary: Edge connecting CredibleSet node to Variant node.

Definition for edge: CredibleSet -> Variant
"""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionEdgeAcquisitionDefinition,
)
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetCredibleSet,
    FieldCredibleSetLocus,
    FieldCredibleSetLocusElementBeta,
    FieldCredibleSetLocusElementLogBf,
    FieldCredibleSetLocusElementPosteriorProbability,
    FieldCredibleSetLocusElementPValueExponent,
    FieldCredibleSetLocusElementPValueMantissa,
    FieldCredibleSetLocusElementStandardError,
    FieldCredibleSetLocusElementVariantId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel
from open_targets.definition.reference_kg.expression import credible_set_primary_id_expression

edge_credible_set_has_participating_variant_variant: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetCredibleSet,
            exploded_field=FieldCredibleSetLocus,
        ),
        primary_id=NewUuidExpression(),
        source=credible_set_primary_id_expression,
        target=FieldCredibleSetLocusElementVariantId,
        label=EdgeLabel.HAS_PARTICIPATING_VARIANT,
        properties=[
            FieldCredibleSetLocusElementPosteriorProbability,
            FieldCredibleSetLocusElementLogBf,
            FieldCredibleSetLocusElementBeta,
            FieldCredibleSetLocusElementStandardError,
            FieldCredibleSetLocusElementPValueMantissa,
            FieldCredibleSetLocusElementPValueExponent,
        ],
    )
)
