from collections import defaultdict
from typing import Any, DefaultDict, List, Optional, Set, Tuple, Union, Dict, NamedTuple


class Path(NamedTuple):
    node: str
    distance: int


class Position(NamedTuple):
    row: int
    column: int


Graph = Union[DefaultDict[Any, List[Optional[Any]]], Dict]
Edges = List[Tuple[str, str]]
Visited = Set[str]
VisitedGrid = Set[Position]
Grid = List[List[str]]


graph: Graph = defaultdict(
    list,
    {
        "a": ["c", "b"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": [],
    },
)

edges: Edges = [
    ("i", "j"),
    ("k", "i"),
    ("m", "k"),
    ("k", "l"),
    ("o", "n"),
]

edges2: Edges = [
    ("b", "a"),
    ("c", "a"),
    ("b", "c"),
    ("q", "r"),
    ("q", "s"),
    ("q", "u"),
    ("q", "t"),
]

edges3: Edges = [
    ("b", "a"),
    ("c", "a"),
    ("b", "c"),
    ("q", "r"),
    ("q", "s"),
    ("q", "u"),
    ("q", "t"),
]

edges4: Edges = [
    ("a", "c"),
    ("a", "b"),
    ("c", "b"),
    ("c", "d"),
    ("b", "d"),
    ("e", "d"),
    ("g", "f"),
]

edges5: Edges = [
    ("a", "c"),
    ("a", "b"),
    ("c", "b"),
    ("c", "d"),
    ("b", "d"),
    ("e", "d"),
    ("g", "f"),
]

graph_from_edges: Graph = defaultdict(
    list,
    {
        "i": ["j", "k"],
        "j": ["i"],
        "k": ["i", "m", "l"],
        "m": ["k"],
        "l": ["k"],
        "o": ["n"],
        "n": ["o"],
    },
)

graph_ccc: Graph = defaultdict(
    list,
    {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
    },
)

graph_ccc2: Graph = defaultdict(
    list,
    {
        1: [2],
        2: [1, 8],
        6: [7],
        9: [8],
        7: [6, 8],
        8: [9, 7, 2],
    },
)

graph_empty: Graph = {}

grid: Grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]

grid2: Grid = [
    ["L", "W", "W", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["W", "L", "W", "L", "W"],
    ["W", "W", "W", "W", "W"],
    ["W", "W", "L", "L", "L"],
]

grid3: Grid = [
    ["L", "L", "L"],
    ["L", "L", "L"],
    ["L", "L", "L"],
]

grid4: Grid = [
    ["W", "W"],
    ["W", "W"],
    ["W", "W"],
]

grid5: Grid = [
    ["W", "W"],
    ["L", "L"],
    ["W", "W"],
    ["W", "L"],
]
