from collections import deque
from typing import Deque, List, Optional

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
        for neighbour in graph.get(current):
            stack.append(neighbour)
    return path


def depth_first_search_recursive(
    graph: Graph,
    source: str,
    path: Optional[List[str]] = None,
):
    if path is None:
        path = []
    if source in path:
        return False
    path.append(source)
    for neighbour in graph.get(source):
        depth_first_search_recursive(
            graph=graph,
            source=neighbour,
            path=path,
        )
    return "".join(path)
