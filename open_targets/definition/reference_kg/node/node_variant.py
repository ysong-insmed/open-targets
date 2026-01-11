"""Summary: Genetic variant nodes (SNPs, indels, etc.).

Definition for VARIANT nodes: represents genetic variants (e.g., SNPs, indels)
identified by their unique ID, enabling the mapping of genotype-phenotype
associations in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetVariant,
    FieldVariantAlternateAllele,
    FieldVariantChromosome,
    FieldVariantPosition,
    FieldVariantReferenceAllele,
    FieldVariantVariantId,
)
from open_targets.definition.reference_kg.constant import NodeLabel

node_variant: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetVariant),
    primary_id=FieldVariantVariantId,
    label=NodeLabel.VARIANT,
    properties=[
        FieldVariantChromosome,
        FieldVariantPosition,
        FieldVariantReferenceAllele,
        FieldVariantAlternateAllele,
    ],
)
