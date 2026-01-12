"""Summary: STUDY nodes from Study dataset.

Definition for STUDY nodes: represents scientific studies (e.g., GWAS, clinical trials)
from the Study dataset, acting as central hubs for linking traits, diseases, and
genetic associations in the KG.
"""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetStudy,
    FieldStudyBiosampleId,
    FieldStudyGeneId,
    FieldStudyHasSumstats,
    FieldStudyInitialSampleSize,
    FieldStudyNCases,
    FieldStudyNControls,
    FieldStudyNSamples,
    FieldStudyProjectId,
    FieldStudyPublicationDate,
    FieldStudyPublicationFirstAuthor,
    FieldStudyPublicationJournal,
    FieldStudyPublicationTitle,
    FieldStudyPubmedId,
    FieldStudyStudyId,
    FieldStudyStudyType,
    FieldStudyTraitFromSource,
)

node_study: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetStudy),
    primary_id=FieldStudyStudyId,
    label="STUDY",
    properties=[
        FieldStudyProjectId,
        FieldStudyStudyType,
        FieldStudyTraitFromSource,
        FieldStudyPublicationFirstAuthor,
        FieldStudyPublicationTitle,
        FieldStudyPublicationJournal,
        FieldStudyPublicationDate,
        FieldStudyPubmedId,
        FieldStudyNSamples,
        FieldStudyNCases,
        FieldStudyNControls,
        FieldStudyInitialSampleSize,
        FieldStudyHasSumstats,
        FieldStudyGeneId,
        FieldStudyBiosampleId,
    ],
)
