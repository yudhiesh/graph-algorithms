from algorithms.helper import Grid, Position, VisitedGrid


def get_minimum_island(grid: Grid) -> float:
    size: float = float("inf")
    visited: VisitedGrid = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            current_position = Position(
                row=i,
                column=j,
            )
            current_size = explore(
                grid=grid,
                position=current_position,
                visited=visited,
            )
            # base case returns 0(islands must be greater than 0)
            if current_size > 0:
                size = min(current_size, size)
    return size


def explore(
    grid: Grid,
    position: Position,
    visited: VisitedGrid,
) -> int:
    size: int = 0
    row_in_bounds = 0 <= position.row and position.row < len(grid)
    column_in_bounds = 0 <= position.column and position.column < len(grid[0])
    # Base case 1: Check row & columns inbound
    if not row_in_bounds or not column_in_bounds:
        return 0
    # Base case 2: Check position not at water
    if grid[position.row][position.column] == "W":
        return 0
    # Base case 3: Check that position has not been visited
    if position in visited:
        return 0
    visited.add(position)
    size = 1
    # Up
    size += explore(
        grid=grid,
        position=Position(
            row=position.row - 1,
            column=position.column,
        ),
        visited=visited,
    )
    # Down
    size += explore(
        grid=grid,
        position=Position(
            row=position.row + 1,
            column=position.column,
        ),
        visited=visited,
    )
    # Left
    size += explore(
        grid=grid,
        position=Position(
            row=position.row,
            column=position.column - 1,
        ),
        visited=visited,
    )
    # Right
    size += explore(
        grid=grid,
        position=Position(
            row=position.row,
            column=position.column + 1,
        ),
        visited=visited,
    )
    return size
