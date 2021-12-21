from typing import Deque
from helper import GRAPH, graph
from collections import deque


def depth_first_search(
    graph: GRAPH,
    source: str,
) -> None:
    stack: Deque[str] = deque(source)
    path: str = ""
    while len(stack) > 0:
        current: str = stack.pop()
        print(f"Current : {current}")
        path += current
        for node, neighbours in graph.items():
            if node == current:
                for neighbour in neighbours:
                    stack.append(neighbour)
    print(f"Final path : {path}")


def depth_first_search_recursive(
    graph: GRAPH,
    source: str,
) -> None:
    print(f"Source : {source}")
    for node, neighbours in graph.items():
        if node == source:
            for neighbour in neighbours:
                depth_first_search_recursive(graph=graph, source=neighbour)


if __name__ == "__main__":
    depth_first_search(graph=graph, source="a")
    depth_first_search_recursive(graph=graph, source="a")
