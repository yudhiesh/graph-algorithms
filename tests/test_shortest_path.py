from algorithms.helper import edges4, edges5
import pytest

from problems.shortest_path import get_shortest_path


@pytest.mark.parametrize(
    "edges,src,dst,expected",
    [
        (
            edges4,
            "e",
            "c",
            2,
        ),
        (
            edges5,
            "b",
            "g",
            -1,
        ),
    ],
)
def test_get_shortest_path(
    edges,
    src,
    dst,
    expected,
):
    results = get_shortest_path(
        edges=edges,
        src=src,
        dst=dst,
    )
    assert results == expected
