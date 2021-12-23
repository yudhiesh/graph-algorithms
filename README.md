# Graph Algorithms Course for Technical Interviews

Code for the video, [Graph Algorithms Course for Technical Interviews](https://www.youtube.com/watch?v=2_Uuixtc5i0).

## Documentation

```
|-- algorithms
|   |-- __init__.py
|   |-- bfs.py                             <- breath first search basic example
|   |-- dfs.py                             <- depth first search basic example
|   `-- helper.py                          <- helper code which contains the data for tests, type definitions & classes
|-- problems                               <- all the problem statements and their implementation can be found here
|   |-- connected_components_count.py
|   |-- has_path.py
|   |-- island_count.py
|   |-- largest_component.py
|   |-- minimum_island.py
|   |-- shortest_path.py
|   `-- undirected_path.py
|-- requirements_test.txt
`-- tests                                  <- all the tests for the problem statements can be found here
    |-- test_algorithms.py
    |-- test_connected_components_count.py
    |-- test_has_path.py
    |-- test_island_count.py
    |-- test_largest_component.py
    |-- test_minimum_island.py
    |-- test_shortest_path.py
    `-- test_undirected_path.py
```

## Running Tests

To run tests, run the following command

```bash
  pytest -vv
  # if your python path has not been set locally then use
  python -m pytest tests -v
```

### Output:

```
===================================================================================== test session starts =====================================================================================
platform darwin -- Python 3.10.0, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /Users/yravindranath/opt/anaconda3/envs/graphs/bin/python
cachedir: .pytest_cache
rootdir: /Users/yravindranath/graph_algorithms
plugins: xdist-2.5.0, forked-1.4.0
collected 27 items

tests/test_algorithms.py::test_breadth_first_search[graph0-a-acbedf] PASSED                                                                                                             [  3%]
tests/test_algorithms.py::test_depth_first_search[graph0-a-abdfce] PASSED                                                                                                               [  7%]
tests/test_algorithms.py::test_depth_first_search_recursive[graph0-a-acebdf] PASSED                                                                                                     [ 11%]
tests/test_connected_components_count.py::test_get_connected_components_count[graph0-2] PASSED                                                                                          [ 14%]
tests/test_connected_components_count.py::test_get_connected_components_count[graph1-1] PASSED                                                                                          [ 18%]
tests/test_connected_components_count.py::test_get_connected_components_count[graph2-0] PASSED                                                                                          [ 22%]
tests/test_has_path.py::test_has_path_dfs[graph0-f-k-True] PASSED                                                                                                                       [ 25%]
tests/test_has_path.py::test_has_path_dfs[graph1-v-z-False] PASSED                                                                                                                      [ 29%]
tests/test_has_path.py::test_has_path_bfs[graph0-f-k-True] PASSED                                                                                                                       [ 33%]
tests/test_has_path.py::test_has_path_bfs[graph1-v-z-False] PASSED                                                                                                                      [ 37%]
tests/test_island_count.py::test_get_island_count[grid0-3] PASSED                                                                                                                       [ 40%]
tests/test_island_count.py::test_get_island_count[grid1-4] PASSED                                                                                                                       [ 44%]
tests/test_island_count.py::test_get_island_count[grid2-1] PASSED                                                                                                                       [ 48%]
tests/test_island_count.py::test_get_island_count[grid3-0] PASSED                                                                                                                       [ 51%]
tests/test_largest_component.py::test_get_largest_component[graph0-4] PASSED                                                                                                            [ 55%]
tests/test_largest_component.py::test_get_largest_component[graph1-6] PASSED                                                                                                            [ 59%]
tests/test_largest_component.py::test_get_largest_component[graph2-0] PASSED                                                                                                            [ 62%]
tests/test_minimum_island.py::test_get_mininum_island[grid0-2] PASSED                                                                                                                   [ 66%]
tests/test_minimum_island.py::test_get_mininum_island[grid1-1] PASSED                                                                                                                   [ 70%]
tests/test_minimum_island.py::test_get_mininum_island[grid2-9] PASSED                                                                                                                   [ 74%]
tests/test_minimum_island.py::test_get_mininum_island[grid3-1] PASSED                                                                                                                   [ 77%]
tests/test_shortest_path.py::test_get_shortest_path[edges0-e-c-2] PASSED                                                                                                                [ 81%]
tests/test_shortest_path.py::test_get_shortest_path[edges1-b-g--1] PASSED                                                                                                               [ 85%]
tests/test_undirected_path.py::test_edges_to_graph[edges0-expected0] PASSED                                                                                                             [ 88%]
tests/test_undirected_path.py::test_has_undirected_path_dfs[edges0-j-m-True] PASSED                                                                                                     [ 92%]
tests/test_undirected_path.py::test_has_undirected_path_dfs[edges1-a-b-True] PASSED                                                                                                     [ 96%]
tests/test_undirected_path.py::test_has_undirected_path_dfs[edges2-r-b-False] PASSED                                                                                                    [100%]

===================================================================================== 27 passed in 0.10s ======================================================================================
```
