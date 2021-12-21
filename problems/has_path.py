from collections import deque
from typing import Deque

from algorithms.helper import GRAPH


def has_path_dfs(
    graph: GRAPH,
    src: str,
    dst: str,
) -> bool:
    stack: Deque = deque(src)
    while len(stack) > 0:
        current: str = stack.pop()
        for neighbours in graph.get(current):
            for neighbour in neighbours:
                stack.append(neighbour)
                if neighbour == dst:
                    return True
    return False


def has_path_bfs(
    graph: GRAPH,
    src: str,
    dst: str,
) -> bool:
    queue: Deque = deque(src)
    while len(queue) > 0:
        current: str = queue.popleft()
        for neighbours in graph.get(current):
            for neighbour in neighbours:
                queue.append(neighbour)
                if neighbour == dst:
                    return True
    return False
