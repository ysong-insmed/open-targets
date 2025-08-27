from typing import Any, get_args

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.expression import (
    Expression,
    FieldExpression,
    LiteralExpression,
    StringConcatenationExpression,
    StringHashExpression,
    ToStringExpression,
)
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import ScanOperation
from open_targets.data.schema_base import Field
from open_targets.definition.experimental_kg.constant import Namespace


def get_arrow_expression(
    source: Expression[Any] | type[Field],
    target: Expression[Any] | type[Field],
) -> Expression[str]:
    """Get an expression that returns `{source}->{target}`."""
    if isinstance(source, type):
        source = FieldExpression(source)
    if isinstance(target, type):
        target = FieldExpression(target)

    return StringConcatenationExpression(
        expressions=[
            ToStringExpression(source),
            LiteralExpression("->"),
            ToStringExpression(target),
        ],
    )


def get_namespaced_expression(
    namespace: str,
    value_expression: Expression[Any] | type[Field],
) -> Expression[str]:
    """Get an expression that prefixes a string with a namespace.

    This return an expression that produces a string like `namespace::value`.
    This helper automatically converts the value expression to a string if the
    expression is not already a string.
    """
    if isinstance(value_expression, type):
        value_expression = FieldExpression(value_expression)
    if get_args(type(value_expression))[0] is not str:
        value_expression = ToStringExpression(value_expression)
    return StringConcatenationExpression(
        expressions=[
            LiteralExpression(f"{namespace}::"),
            value_expression,
        ],
    )


def get_namespaced_hash_expression(
    namespace: str,
    value_expression: Expression[Any] | type[Field],
) -> Expression[str]:
    """Get an expression that hashes a string and prefix it with a namespace.

    This return an expression that produces a string like
    `namespace::hash(value)`. This helper automatically converts the value
    expression to a string if the expression is not already a string.
    """
    if isinstance(value_expression, type):
        value_expression = FieldExpression(value_expression)
    if get_args(type(value_expression))[0] is not str:
        value_expression = ToStringExpression(value_expression)
    return get_namespaced_expression(namespace, StringHashExpression(value_expression))


def get_simple_value_node_definition(
    *,
    scan_operation: ScanOperation,
    namespace: Namespace,
    value_expression: Expression[Any] | type[Field],
    label: str,
) -> AcquisitionDefinition[NodeInfo]:
    """Get a simple value node definition.

    This helper automatically converts the value expression to a string if the
    expression is not already a string.
    """
    if isinstance(value_expression, type):
        value_expression = FieldExpression(value_expression)

    if get_args(type(value_expression))[0] is not str:
        value_expression = ToStringExpression(value_expression)

    return ExpressionNodeAcquisitionDefinition(
        scan_operation=scan_operation,
        primary_id=get_namespaced_hash_expression(namespace, value_expression),
        label=label,
        properties=[
            ("value", value_expression),
        ],
    )
