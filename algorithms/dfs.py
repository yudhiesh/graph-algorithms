from collections import deque
from typing import Deque, List

from algorithms.helper import Graph, graph


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
) -> None:
    path: List[str] = []
    dfs(
        graph=graph,
        source=source,
        path=path,
    )
    return "".join(path)


def dfs(
    graph: Graph,
    source: str,
    path: List[str],
):
    if source in path:
        return False
    path.append(source)
    for neighbour in graph.get(source):
        dfs(
            graph=graph,
            source=neighbour,
            path=path,
        )
