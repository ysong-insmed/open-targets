# type: ignore[reportUnknownMemberType]

"""A pipeline to build Open Targets platform data as a BioCypher KG."""

import logging

from biocypher import BioCypher

from open_targets.adapter.context import AcquisitionContext
from open_targets.definition.reference_kg.kg import reference_kg_definition


def main():
    """Run the import using BioCypher and the Open Targets adapter."""
    # Start BioCypher
    bc = BioCypher(
        biocypher_config_path="config/biocypher_config.yaml",
    )
    # Set logging level to ERROR only
    logging.getLogger("biocypher").setLevel(logging.ERROR)

    # Check the schema
    bc.show_ontology_structure()

    # Open Targets
    context = AcquisitionContext(
        node_definitions=reference_kg_definition.node_definitions,
        edge_definitions=reference_kg_definition.edge_definitions,
        datasets_location="datasets",
    )

    count = 1
    for node_definition in reference_kg_definition.node_definitions:
        print(f"{count}: {node_definition.label}")
        count += 1
        bc.write_nodes(context.get_acquisition_generator(node_definition))
    for edge_definition in reference_kg_definition.edge_definitions:
        print(f"{count}: {edge_definition.label}")
        count += 1
        bc.write_edges(context.get_acquisition_generator(edge_definition))

    # Post import functions
    bc.write_import_call()
    bc.summary()


if __name__ == "__main__":
    main()
