from collections import defaultdict, deque
from typing import Deque
from algorithms.helper import Edges, Graph, Visited


def edges_to_graph(edges: Edges) -> Graph:
    graph: Graph = defaultdict(list)
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    return graph


def has_undirected_path_dfs(
    edges: Edges,
    src: str,
    dst: str,
) -> bool:
    visited: Visited = set()
    graph: Graph = edges_to_graph(edges=edges)
    return has_path(graph=graph, visited=visited, src=src, dst=dst)


def has_path(
    graph: Graph,
    visited: Visited,
    src: str,
    dst: str,
) -> bool:
    if src == dst:
        return True

    if src in visited:
        return False

    visited.add(src)

    for neighbour in graph.get(src):
        if has_path(
            graph=graph,
            visited=visited,
            src=neighbour,
            dst=dst,
        ):
            return True
    return False
