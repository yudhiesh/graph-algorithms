from collections import deque
from typing import Deque

from algorithms.helper import GRAPH

graph: GRAPH = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": [],
}

graph2: GRAPH = {
    "v": ["x", "w"],
    "w": [],
    "x": [],
    "y": ["z"],
    "z": [],
}


def has_path_dfs(
    graph: GRAPH,
    src: str,
    dst: str,
) -> bool:
    stack: Deque = deque(src)
    while len(stack) > 0:
        current: str = stack.pop()
        for node, neighbours in graph.items():
            if node == current:
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
        for node, neighbours in graph.items():
            if node == current:
                for neighbour in neighbours:
                    queue.append(neighbour)
                    if neighbour == dst:
                        return True
    return False


if __name__ == "__main__":
    assert has_path_dfs(graph=graph, src="f", dst="k")
    assert not has_path_dfs(graph=graph2, src="v", dst="z")
    assert has_path_bfs(graph=graph, src="f", dst="k")
    assert not has_path_bfs(graph=graph2, src="v", dst="z")
