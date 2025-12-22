# BioCypher Open Targets Data (24.09) Adapter

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

This repository contains a [BioCypher](https://biocypher.org) adapter for Open
Targets data version 24.09. The project is currently under active development.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Data Preparation](#data-preparation)
- [Usage](#usage)
- [Node and Edge Definitions](#node-and-edge-definitions)
- [Open Targets Data Schema](#open-targets-data-schema)
- [Code Generation](#code-generation)
- [Contributing](#contributing)
- [License](#license)

## Overview

BioCypher's modular design enables the use of different adapters to consume
various data sources and produce knowledge graphs. This adapter serves as a
["secondary
adapter"](https://biocypher.org/latest/learn/tutorials/tutorial003_adapters/)
for [Open Targets data](https://platform.opentargets.org/downloads), meaning it
adapts a pre-harmonised composite of atomic resources via the Open Targets
pipeline.

The adapter includes predefined sets of node types (entities) and edge types
(relationships), or in the language of this adapter, presets of node and edge
`definitions`. A script is provided to run BioCypher with the adapter, creating
a knowledge graph with all predefined nodes and edges. On a consumer laptop,
building the full graph typically takes 1-2 hours.

**Key Features:**
- Declarative syntax for graph schema construction
- Powered by [duckdb](https://duckdb.org/) for fast and memory-efficient processing
- True streaming from datasets to BioCypher with minimal intermediate memory usage
- Type-safe schema representation with Python classes

## Prerequisites

- [uv](https://github.com/astral-sh/uv) for dependency management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/biocypher/open-targets.git
   cd open-targets
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Activate the virtual environment (optional):
   ```bash
   source .venv/bin/activate  # On Unix/macOS
   .venv\Scripts\activate    # On Windows
   ```
   
   Or run commands directly with `uv run`:
   ```bash
   uv run python <script>
   ```

## Data Preparation

Download the required Open Targets datasets (version 24.09) from the [Open Targets FTP server](https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/24.09/output/etl/parquet/).

Place all downloaded datasets in the `data/ot_files` directory, maintaining the original directory structure from the FTP server:

```
data/ot_files/
├── targets/
│   └── **/
│       └── *.parquet
├── diseases/
│   └── **/
│       └── *.parquet
├── molecule/
│   └── **/
│       └── *.parquet
├── evidence/
│   └── **/
│       └── *.parquet
...
```

The adapter requires multiple datasets including `targets/`, `diseases/`, `molecule/`, `evidence/`, `go/`, `mousePhenotypes/`, `interaction/`, and others as needed by specific node/edge definitions.

## Usage

### Quick Start

1. Follow the [Installation](#installation) and [Data Preparation](#data-preparation) steps
2. Run the script:
   ```bash
   uv run python scripts/open_targets_biocypher_run.py
   ```

This generates a knowledge graph using all predefined node/edge definitions.

### Custom Subset

To use a custom subset of definitions:

```python
from biocypher import BioCypher
from open_targets.adapter.context import AcquisitionContext
from open_targets.definition.reference_kg.node import node_target, node_disease
from open_targets.definition.reference_kg.edge import edge_target_disease_association_has_object_disease

bc = BioCypher(biocypher_config_path="config/biocypher_config.yaml")
context = AcquisitionContext(
    node_definitions=[node_target, node_disease],
    edge_definitions=[edge_target_disease_association_has_object_disease],
    datasets_location="data/ot_files",
)

for node_def in context.node_definitions:
    bc.write_nodes(context.get_acquisition_generator(node_def))
for edge_def in context.edge_definitions:
    bc.write_edges(context.get_acquisition_generator(edge_def))

bc.write_import_call()
bc.summary()
```

## Node and Edge Definitions

The adapter includes 40+ node types and 50+ edge types. **Each definition file contains detailed docstrings explaining what it does, what data it uses, and how it works.**

### Finding Definition Files

- **Node definitions**: `open_targets/definition/reference_kg/node/`
- **Edge definitions**: `open_targets/definition/reference_kg/edge/`
- **Complete list**: `open_targets/definition/reference_kg/kg.py`

### Reading Docstrings

Each definition file (e.g., `node_target.py`, `edge_molecule_has_adverse_reaction_adverse_reaction.py`) starts with a module-level docstring that describes:
- What entities/relationships the definition creates
- Which Open Targets datasets it uses
- How the data is transformed
- What properties are included

**Example:**
```python
# In open_targets/definition/reference_kg/node/node_target.py
"""Summary: Ensembl target gene nodes (symbol/name/biotype/functions).

Definition for TARGET nodes: scans the Targets parquet to emit Ensembl gene
targets with symbol, name, biotype, and function descriptions as the core
target entities used across drug, association, and annotation edges in the KG.
"""
```

To explore available definitions:
1. Browse the files in `open_targets/definition/reference_kg/node/` and `edge/`
2. Read the docstring at the top of each file
3. Check `kg.py` to see how definitions are organized

For details on creating custom definitions, see the adapter layer documentation in `open_targets/adapter/` and examine existing definitions as examples.

## Open Targets Data Schema

The full schema of Open Targets data is represented as Python classes in `open_targets/data/schema.py`. This provides type checking for dataset and field references.

**Naming Conventions:**
- Dataset classes: `Dataset` prefix (e.g., `DatasetTargets`, `DatasetDiseases`)
- Field classes: `Field` prefix (e.g., `FieldTargetsId`, `FieldTargetsApprovedSymbol`)
- Field names follow their structural location in datasets

The schema is generated from Open Targets metadata using code generation (see below). Schema classes are used throughout node/edge definitions for type-safe data access.

## Code Generation

The Open Targets data schema is generated using [Jinja](https://jinja.palletsprojects.com/en/stable/) templates.

- **Templates**: `open_targets/*.jinja`
- **Generated code**: `open_targets/data/schema.py`
- **Generation script**: `code_generation/generate.py`

**Important:** Never edit generated files directly. Always modify templates and regenerate:
```bash
python code_generation/generate.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or create
an Issue if you discover any problems.

## License

This project is licensed under the MIT License - see the LICENSE file for
details.
