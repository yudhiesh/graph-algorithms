from collections import defaultdict, deque
from typing import Deque
from algorithms.helper import Edges, Graph, Path, Visited


def get_shortest_path(
    edges: Edges,
    src: str,
    dst: str,
) -> int:
    source_path = Path(
        node=src,
        distance=0,
    )
    queue: Deque[Path] = deque([source_path])
    graph: Graph = graph_from_edges(edges=edges)
    visited: Visited = set()
    while queue:
        current: Path = queue.popleft()
        if current.node == dst:
            return current.distance
        for neighbour in graph.get(current.node):
            if neighbour not in visited:
                current_path = Path(
                    node=neighbour,
                    distance=current.distance + 1,
                )
                queue.append(current_path)
                visited.add(current_path.node)
    return -1


def graph_from_edges(edges: Edges) -> Graph:
    graph: Graph = defaultdict(list)
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    return graph
