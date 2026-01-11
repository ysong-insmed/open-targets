"""Summary: reified disease–phenotype (HPO) evidence with curation metadata.

Definition for DISEASE_PHENOTYPE_ASSOCIATION nodes: explodes disease->HPO
evidence from the DiseaseToPhenotype parquet to reify each association with
mapped aspect, evidence type, frequency, sex, and curation metadata, providing
traceable disease–phenotype links in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.expression import FieldExpression, TransformExpression
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseasePhenotype,
    FieldDiseasePhenotypeEvidence,
    FieldDiseasePhenotypeEvidenceElementAspect,
    FieldDiseasePhenotypeEvidenceElementBioCuration,
    FieldDiseasePhenotypeEvidenceElementEvidenceType,
    FieldDiseasePhenotypeEvidenceElementFrequency,
    FieldDiseasePhenotypeEvidenceElementSex,
)
from open_targets.definition.reference_kg.expression import disease_phenotype_association_primary_id_expression

_evidence_type_map = {
    "IEA": "Inferred from Electronic Annotations",
    "PCS": "Published Clinical Study",
    "TAS": "Traceable Author Statement",
}

_aspect_map = {
    "P": "Phenotypic abnormality",
    "I": "Inheritance",
    "C": "Onset and clinical course",
    "M": "Clinical modifier",
    "H": "Past medical history",
}


def _map_aspect(aspect: str) -> str:
    return _aspect_map.get(aspect, "")


def _map_evidence_type(evidence_type: str) -> str:
    return _evidence_type_map.get(evidence_type, "")


node_disease_phenotype_association: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseasePhenotype,
        exploded_field=FieldDiseasePhenotypeEvidence,
    ),
    primary_id=disease_phenotype_association_primary_id_expression,
    label="DISEASE_PHENOTYPE_ASSOCIATION",
    properties=[
        (
            FieldDiseasePhenotypeEvidenceElementAspect.name,
            TransformExpression(FieldExpression(FieldDiseasePhenotypeEvidenceElementAspect), _map_aspect),
        ),
        FieldDiseasePhenotypeEvidenceElementBioCuration,
        (
            FieldDiseasePhenotypeEvidenceElementEvidenceType.name,
            TransformExpression(
                FieldExpression(FieldDiseasePhenotypeEvidenceElementEvidenceType),
                _map_evidence_type,
            ),
        ),
        FieldDiseasePhenotypeEvidenceElementFrequency,
        FieldDiseasePhenotypeEvidenceElementSex,
    ],
)
