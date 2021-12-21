from collections import deque
from typing import Deque

from algorithms.helper import Graph


def depth_first_search(
    graph: Graph,
    source: str,
) -> str:
    stack: Deque[str] = deque(source)
    path: str = ""
    while len(stack) > 0:
        current: str = stack.pop()
        path += current
        for neighbours in graph.get(current):
            for neighbour in neighbours:
                stack.append(neighbour)
    return path


def depth_first_search_recursive(
    graph: Graph,
    source: str,
    path: str,
) -> str:
    path += source
    for node, neighbours in graph.items():
        if node == source:
            for neighbour in neighbours:
                depth_first_search_recursive(graph=graph, source=neighbour, path=path)
