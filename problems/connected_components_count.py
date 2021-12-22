from collections import deque
from typing import Deque
from algorithms.helper import Graph, Visited


def get_connected_components_count(graph: Graph) -> int:
    visited: Visited = set()
    if not graph:
        return 0
    source: int = list(graph.keys())[0]
    stack: Deque[int] = deque([source])
    explored = [
        explore(graph=graph, stack=stack, visited=visited, current=node)
        for node in graph.keys()
    ]
    num_explored = sum(bool(value) for value in explored)
    return num_explored


def explore(
    graph: Graph,
    stack: Deque[int],
    visited: Visited,
    current: int,
) -> bool:
    while len(stack) > 0:
        current: int = stack.pop()
        if current in visited:
            return False
        visited.add(current)
        for neighbours in graph.get(current):
            stack.append(neighbours)
    return True
