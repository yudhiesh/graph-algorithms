import pytest
from algorithms.helper import grid, grid2, grid3, grid4
from problems.island_count import get_island_count


@pytest.mark.parametrize(
    "grid,expected",
    [
        (
            grid,
            3,
        ),
        (
            grid2,
            4,
        ),
        (
            grid3,
            1,
        ),
        (
            grid4,
            0,
        ),
    ],
)
def test_get_island_count(grid, expected):
    results = get_island_count(grid=grid)
    assert results == expected
