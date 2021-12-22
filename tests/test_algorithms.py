from algorithms.bfs import breadth_first_search
from algorithms.dfs import depth_first_search, depth_first_search_recursive
from algorithms.helper import graph
import pytest


@pytest.mark.parametrize(
    "graph,source,expected",
    [
        (
            graph,
            "a",
            "acbedf",
        )
    ],
)
def test_breadth_first_search(
    graph,
    source,
    expected,
):
    results = breadth_first_search(
        graph=graph,
        source=source,
    )
    assert results == expected


@pytest.mark.parametrize(
    "graph,source,expected",
    [
        (
            graph,
            "a",
            "abdfce",
        )
    ],
)
def test_depth_first_search(
    graph,
    source,
    expected,
):
    results = depth_first_search(
        graph=graph,
        source=source,
    )
    assert results == expected


@pytest.mark.parametrize(
    "graph,source,expected",
    [
        (
            graph,
            "a",
            "acebdf",
        )
    ],
)
def test_depth_first_search_recursive(
    graph,
    source,
    expected,
):
    results = depth_first_search_recursive(
        graph=graph,
        source=source,
    )
    assert results == expected
