from enum import Enum


class Namespace(str, Enum):
    """Namespaces for experimental KG."""

    DATABASE_CROSS_REFERENCE = "database_cross_reference"
    SYNONYM = "synonym"
