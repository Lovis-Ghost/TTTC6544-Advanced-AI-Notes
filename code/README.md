# Python Demo Notes / Python 代码示例

These Python files are small learning demos. I use them to see the algorithm process in the terminal, not to write perfect software.

这些代码主要是为了复习 TC6544 Advanced AI 里面的 search 和 optimization algorithms。它们不是正式项目代码，而是帮助我看清楚每个算法大概怎么运行。

## Structure / 文件内容

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

## How to run / 运行方式

Use `python3`, for example:

```bash
python3 code/bfs_dfs_state_space.py
```

From the repository root, I can replace the filename with any other demo script.

## Notes / 说明

No extra Python library is needed for these demos. I keep the output readable because the main purpose is revision: I want to see the search order, cost changes, acceptance decisions, and fitness changes step by step.
