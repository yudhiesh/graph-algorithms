from algorithms.helper import Graph, Visited


def get_connected_components_count(graph: Graph) -> int:
    if not graph:
        return 0
    visited: Visited = set()
    count: int = 0
    for node in graph.keys():
        if explore(
            graph=graph,
            current=node,
            visited=visited,
        ):
            count += 1
    return count


def explore(
    graph: Graph,
    current: int,
    visited: Visited,
) -> bool:
    if current in visited:
        return False

    visited.add(current)
    for neighbour in graph.get(current):
        explore(
            graph=graph,
            current=neighbour,
            visited=visited,
        )
    return True
