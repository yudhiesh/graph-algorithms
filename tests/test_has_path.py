from algorithms.helper import Graph
from problems.has_path import has_path_bfs, has_path_dfs
import pytest

graph: Graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": [],
}

graph2: Graph = {
    "v": ["x", "w"],
    "w": [],
    "x": [],
    "y": ["z"],
    "z": [],
}


@pytest.mark.parametrize(
    "graph,src,dst,expected",
    [
        (
            graph,
            "f",
            "k",
            True,
        ),
        (
            graph2,
            "v",
            "z",
            False,
        ),
    ],
)
def test_has_path_dfs(
    graph,
    src,
    dst,
    expected,
):
    results = has_path_dfs(
        graph=graph,
        src=src,
        dst=dst,
    )
    assert results == expected


@pytest.mark.parametrize(
    "graph,src,dst,expected",
    [
        (
            graph,
            "f",
            "k",
            True,
        ),
        (
            graph2,
            "v",
            "z",
            False,
        ),
    ],
)
def test_has_path_bfs(
    graph,
    src,
    dst,
    expected,
):
    results = has_path_bfs(
        graph=graph,
        src=src,
        dst=dst,
    )
    assert results == expected
