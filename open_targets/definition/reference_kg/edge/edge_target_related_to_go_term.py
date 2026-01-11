"""Summary: TARGET -> GO_TERM annotation edges with mapped evidence/aspects.

Definition for RELATED_TO edges (target -> GO): explodes GO annotations in the
Targets parquet to link each TARGET (Ensembl gene) to GO_TERM nodes, mapping
evidence codes and aspects into readable labels and carrying ECO/evidence/source
fields so functional annotations and their provenance are explicit in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import FieldExpression, NewUuidExpression, TransformExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTarget,
    FieldTargetGo,
    FieldTargetGoElementEcoId,
    FieldTargetGoElementEvidence,
    FieldTargetGoElementGeneProduct,
    FieldTargetGoElementId,
    FieldTargetGoElementSource,
    FieldTargetId,
)
from open_targets.definition.reference_kg.constant import EdgeLabel

_aspect_map = {
    "F": "Molecular Function",
    "P": "Biological Process",
    "C": "Cellular Component",
}

_evidence_label_map = {
    "EXP": "Inferred from Experiment",
    "IDA": "Inferred from Direct Assay",
    "IPI": "Inferred from Physical Interaction",
    "IMP": "Inferred from Mutant Phenotype",
    "IGI": "Inferred from Genetic Interaction",
    "IEP": "Inferred from Expression Pattern",
    "HTP": "Inferred from High Throughput Experiment",
    "HDA": "Inferred from High Throughput Direct Assay",
    "HMP": "Inferred from High Throughput Mutant Phenotype",
    "HGI": "Inferred from High Throughput Genetic Interaction",
    "HEP": "Inferred from High Throughput Expression Pattern",
    "IBA": "Inferred from Biological aspect of Ancestor",
    "IBD": "Inferred from Biological aspect of Descendant",
    "IKR": "Inferred from Key Residues",
    "IRD": "Inferred from Rapid Divergence",
    "ISS": "Inferred from Sequence or structural Similarity",
    "ISO": "Inferred from Sequence Orthology",
    "ISA": "Inferred from Sequence Alignment",
    "ISM": "Inferred from Sequence Model",
    "IGC": "Inferred from Genomic Context",
    "RCA": "Inferred from Reviewed Computational Analysis",
    "TAS": "Traceable Author Statement",
    "NAS": "Non-traceable Author Statement",
    "IC": "Inferred by Curator",
    "ND": "No biological Data available",
    "IEA": "Inferred from Electronic Annotation",
}


def _map_aspect(aspect: str) -> str:
    return _aspect_map.get(aspect, "")


def _map_evidence_label(evidence_label: str) -> str:
    return _evidence_label_map.get(evidence_label, "")


edge_target_related_to_go_term: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetTarget,
        exploded_field=FieldTargetGo,
    ),
    primary_id=NewUuidExpression(),
    source=FieldTargetId,
    target=FieldTargetGoElementId,
    label=EdgeLabel.RELATED_TO,
    properties=[
        FieldTargetGoElementSource,
        (
            FieldTargetGoElementEvidence.name,
            TransformExpression(FieldExpression(FieldTargetGoElementEvidence), _map_evidence_label),
        ),
        FieldTargetGoElementEcoId,
        (
            FieldTargetGoElementEvidence.name,
            TransformExpression(FieldExpression(FieldTargetGoElementEvidence), _map_aspect),
        ),
        FieldTargetGoElementGeneProduct,
    ],
)
