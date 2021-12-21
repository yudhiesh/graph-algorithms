from typing import Deque
from helper import GRAPH, graph
from collections import deque


def breadth_first_search(
    graph: GRAPH,
    source: str,
) -> None:
    queue: Deque = deque(source)
    path: str = ""
    while len(queue) > 0:
        current: str = queue.popleft()
        path += current
        print(f"Current : {current}")
        for node, neighbours in graph.items():
            if node == current:
                for neighbour in neighbours:
                    queue.append(neighbour)

    print(f"Path : {path}")


if __name__ == "__main__":
    breadth_first_search(graph=graph, source="a")
