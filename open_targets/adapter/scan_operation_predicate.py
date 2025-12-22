from collections.abc import Iterable
from dataclasses import dataclass

from open_targets.adapter.data_view import DataViewPrimitiveValue
from open_targets.data.schema_base import Field


@dataclass(frozen=True)
class ScanOperationPredicateExpression:
    """Base class for all scan operation predicate expressions.

    The predicate will be used to run on the data side and filter the dataset.
    """


@dataclass(frozen=True)
class EqualityExpression(ScanOperationPredicateExpression):
    """Expression that filters the dataset based on equality.

    The comparand field must be a primitive type and not nested.
    """

    field: type[Field]
    value: DataViewPrimitiveValue | None


@dataclass(frozen=True)
class NotExpression(ScanOperationPredicateExpression):
    """Logical NOT of a predicate expression."""

    expression: ScanOperationPredicateExpression


@dataclass(frozen=True)
class AndExpression(ScanOperationPredicateExpression):
    """Logical AND over multiple predicate expressions."""

    expressions: Iterable[ScanOperationPredicateExpression]


@dataclass(frozen=True)
class OrExpression(ScanOperationPredicateExpression):
    """Logical OR over multiple predicate expressions."""

    expressions: Iterable[ScanOperationPredicateExpression]
