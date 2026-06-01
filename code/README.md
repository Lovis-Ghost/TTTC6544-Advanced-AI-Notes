# Python Demo Notes

These Python files are small learning demos. I use them to see the algorithm process in the terminal, not to write perfect software.

| File | Algorithm | What I should observe |
| ---- | --------- | --------------------- |
| `bfs_dfs_state_space.py` | BFS and DFS | How queue and stack create different visiting orders. |
| `a_star_search.py` | A* Search | How `g`, `h`, and `f` are printed when choosing nodes. |
| `greedy_tsp_nearest_neighbor.py` | Greedy nearest neighbour for TSP | How the algorithm always picks the nearest unvisited city. |
| `hill_climbing_tsp.py` | Hill Climbing | How only better routes are accepted. |
| `simulated_annealing_tsp.py` | Simulated Annealing | How a worse route may be accepted when temperature allows it. |
| `great_deluge_tsp.py` | Great Deluge | How the level controls whether a route is accepted. |
| `tabu_search_tsp.py` | Tabu Search | How the tabu list blocks some recent moves. |
| `genetic_algorithm_maxone.py` | Genetic Algorithm | How population fitness improves across generations. |

## How to run

Use `python3`, for example:

```bash
python3 code/bfs_dfs_state_space.py
```

From the repository root, I can replace the filename with any other demo script.
