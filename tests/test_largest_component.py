from problems.largest_component import get_largest_component
from algorithms.helper import graph_ccc, graph_ccc2, graph_empty
import pytest


@pytest.mark.parametrize(
    "graph,expected",
    [
        (
            graph_ccc,
            4,
        ),
        (
            graph_ccc2,
            6,
        ),
        (
            graph_empty,
            0,
        ),
    ],
)
def test_get_largest_component(graph, expected):
    results = get_largest_component(graph=graph)
    assert results == expected
