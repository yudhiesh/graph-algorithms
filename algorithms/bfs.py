from collections import deque
from typing import Deque

from algorithms.helper import Graph


def breadth_first_search(
    graph: Graph,
    source: str,
) -> str:
    queue: Deque = deque(source)
    path: str = ""
    while len(queue) > 0:
        current: str = queue.popleft()
        path += current
        for neighbours in graph.get(current):
            for neighbour in neighbours:
                queue.append(neighbour)
    return path
