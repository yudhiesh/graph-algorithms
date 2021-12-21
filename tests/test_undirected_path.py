from problems.undirected_path import edges_to_graph, has_undirected_path_dfs
from algorithms.helper import graph_from_edges, edges, edges2, edges3
import pytest


@pytest.mark.parametrize(
    "edges,expected",
    [
        (
            edges,
            graph_from_edges,
        )
    ],
)
def test_edges_to_graph(edges, expected):
    results = edges_to_graph(edges=edges)
    assert results == expected


@pytest.mark.parametrize(
    "edges,src,dst,expected",
    [
        (
            edges,
            "j",
            "m",
            True,
        ),
        (
            edges2,
            "a",
            "b",
            True,
        ),
        (
            edges3,
            "r",
            "b",
            False,
        ),
    ],
)
def test_has_undirected_path_dfs(
    edges,
    src,
    dst,
    expected,
):
    results = has_undirected_path_dfs(
        edges=edges,
        src=src,
        dst=dst,
    )
    assert results == expected
