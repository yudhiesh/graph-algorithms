import pytest
from algorithms.helper import grid, grid2, grid3, grid5
from algorithms.minimum_island import get_minimum_island


@pytest.mark.parametrize(
    "grid,expected",
    [
        (
            grid,
            2,
        ),
        (
            grid2,
            1,
        ),
        (
            grid3,
            9,
        ),
        (
            grid5,
            1,
        ),
    ],
)
def test_get_island_count(grid, expected):
    results = get_minimum_island(grid=grid)
    assert results == expected
