from collections import defaultdict
from typing import DefaultDict, List, Optional, Set


Graph = DefaultDict[str, List[Optional[str]]]
Edges = List[List[str]]
Visited = Set[str]

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
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
]

edges2: Edges = [
    ["b", "a"],
    ["c", "a"],
    ["b", "c"],
    ["q", "r"],
    ["q", "s"],
    ["q", "u"],
    ["q", "t"],
]

edges3: Edges = [
    ["b", "a"],
    ["c", "a"],
    ["b", "c"],
    ["q", "r"],
    ["q", "s"],
    ["q", "u"],
    ["q", "t"],
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
