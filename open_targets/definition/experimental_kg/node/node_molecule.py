"""Acquisition definition that acquires nodes of molecules."""

from typing import Final

from open_targets.adapter.acquisition_definition import (
    AcquisitionDefinition,
    ExpressionNodeAcquisitionDefinition,
)
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetMolecule,
    FieldMoleculeBlackBoxWarning,
    FieldMoleculeDescription,
    FieldMoleculeDrugType,
    FieldMoleculeHasBeenWithdrawn,
    FieldMoleculeId,
    FieldMoleculeInchiKey,
    FieldMoleculeIsApproved,
    FieldMoleculeMaximumClinicalTrialPhase,
    FieldMoleculeName,
    FieldMoleculeSynonyms,
    FieldMoleculeTradeNames,
    FieldMoleculeYearOfFirstApproval,
)

node_molecule: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetMolecule),
    primary_id=FieldMoleculeId,
    label="MOLECULE",
    properties=[
        FieldMoleculeInchiKey,
        FieldMoleculeDrugType,
        FieldMoleculeBlackBoxWarning,
        FieldMoleculeName,
        FieldMoleculeYearOfFirstApproval,
        FieldMoleculeMaximumClinicalTrialPhase,
        FieldMoleculeHasBeenWithdrawn,
        FieldMoleculeIsApproved,
        FieldMoleculeTradeNames,
        FieldMoleculeSynonyms,
        FieldMoleculeDescription,
    ],
)
