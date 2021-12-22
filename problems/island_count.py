from algorithms.helper import Grid, Position, VisitedGrid


def get_island_count(grid: Grid) -> int:
    count: int = 0
    visited: VisitedGrid = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if explore(
                position=Position(row=i, column=j),
                grid=grid,
                visited=visited,
            ):
                count += 1

    return count


def explore(
    position: Position,
    grid: Grid,
    visited: VisitedGrid,
) -> bool:
    row_in_bounds: bool = 0 <= position.row and position.row < len(
        grid,
    )
    column_in_bounds: bool = 0 <= position.column and position.column < len(
        grid[0],
    )
    # Base case 1: handle out of bounds errors
    if not row_in_bounds or not column_in_bounds:
        return False
    # Base case 2: handle position at water
    if grid[position.row][position.column] == "W":
        return False
    # Base case 3: handle already visited positions
    if position in visited:
        return False
    visited.add(position)
    # up
    explore(
        position=Position(
            row=position.row - 1,
            column=position.column,
        ),
        grid=grid,
        visited=visited,
    )
    # down
    explore(
        position=Position(
            row=position.row + 1,
            column=position.column,
        ),
        grid=grid,
        visited=visited,
    )
    # left
    explore(
        position=Position(
            row=position.row,
            column=position.column - 1,
        ),
        grid=grid,
        visited=visited,
    )
    # right
    explore(
        position=Position(
            row=position.row,
            column=position.column + 1,
        ),
        grid=grid,
        visited=visited,
    )
    return True
