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
    stack: Deque = deque(src)
    graph: Graph = edges_to_graph(edges=edges)
    while len(stack) > 0:
        current: str = stack.pop()
        if current in visited:
            return False
        visited.add(current)
        for neighbours in graph.get(current):
            for neighbour in neighbours:
                stack.append(neighbour)
                if neighbour == dst:
                    return True
    return False
