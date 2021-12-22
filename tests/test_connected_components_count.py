from problems.connected_components_count import get_connected_components_count
from algorithms.helper import graph_ccc, graph_ccc2, graph_cc3
import pytest


@pytest.mark.parametrize(
    "graph,expected",
    [
        (
            graph_ccc,
            2,
        ),
        (
            graph_ccc2,
            1,
        ),
        (
            graph_cc3,
            0,
        ),
    ],
)
def test_get_connected_components_count(graph, expected):
    results = get_connected_components_count(graph=graph)
    assert results == expected
