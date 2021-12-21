from collections import deque
from typing import Deque

from algorithms.helper import GRAPH


def breadth_first_search(
    graph: GRAPH,
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
