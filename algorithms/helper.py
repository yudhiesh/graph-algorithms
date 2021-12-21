from typing import Dict, List, Optional

GRAPH = Dict[str, List[Optional[str]]]

graph: GRAPH = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}
