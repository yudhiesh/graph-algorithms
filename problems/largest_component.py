from algorithms.helper import Graph, Visited


def get_largest_component(graph: Graph) -> int:
    if not graph:
        return 0
    largest: int = 0
    visited: Visited = set()
    for node in graph.keys():
        size = explore(
            graph=graph,
            visited=visited,
            current=node,
        )
        largest = max(size, largest)
    return largest


def explore(
    graph: Graph,
    visited: Visited,
    current: int,
) -> int:
    size: int = 0
    if current in visited:
        return 0
    visited.add(current)
    size = 1
    for neighbour in graph.get(current):
        size += explore(
            graph=graph,
            visited=visited,
            current=neighbour,
        )
    return size
