# TTTC6544-Advanced-AI-Notes

## About this repository

This repo is my personal learning portfolio for TC6544 Advanced Artificial Intelligence. I use it to record what I learned from lectures and to connect the theory with small Python examples. The notes are bilingual because I am still building my English academic vocabulary.

## Why I created this repo

I wanted one place to keep my revision notes, examples, and small reflections. Some topics are still a bit messy in my head, so I write them in my own words first instead of trying to sound like a textbook.

## Course map

| No. | Topic | Status |
|---|---|---|
| 1 | Fundamental Concept of AI and Optimization | Covered |
| 2 | State Space Search | Covered |
| 3 | Basic / Heuristic Search Techniques | Covered |
| 4 | Hill Climbing | Covered |
| 5 | Simulated Annealing | Covered |
| 6 | Great Deluge | Covered |
| 7 | Tabu Search | Covered |
| 8 | Genetic Algorithm | Covered |
| 9 | Nature Inspired Algorithm I | Not covered yet |
| 10 | Nature Inspired Algorithm II | Not covered yet |
| 11 | Hyper-Heuristics | Covered |
| 12 | Neural Network | Not covered yet |
| 13 | Fuzzy Logic | Not covered yet |

## Topics covered

The current notes focus on AI as search and optimization. I have written more detail for the first few topics because those ideas keep appearing again in later algorithms.

- AI and optimization basics
- State space search
- Heuristic search and A*
- Local search and hill climbing
- Simulated annealing
- Great deluge
- Tabu search
- Genetic algorithm
- Hyper-heuristics

## Learning Roadmap

AI Optimization Basics
-> State Space Search
-> Heuristic Search and A*
-> Local Search
-> Metaheuristics: SA, GD, Tabu Search
-> Population-based Algorithm: Genetic Algorithm
-> Hyper-Heuristics
-> Topics not covered yet: Nature Inspired Algorithms, Neural Network, Fuzzy Logic

This roadmap helps me see the course as one connected learning path, instead of separate algorithms.

## Python demos

The `code/` folder contains small Python scripts. They are not production code. They are just learning demos so I can see the algorithm steps printed in the terminal.

## Current progress

I have covered the topics taught so far in class. For topics not taught yet, I only created placeholder files with questions I want to come back to later.

## How to run the code

Use Python 3. No extra library is needed. On my Mac, I run the scripts with `python3`.

```bash
python3 code/bfs_dfs_state_space.py
python3 code/a_star_search.py
python3 code/greedy_tsp_nearest_neighbor.py
python3 code/hill_climbing_tsp.py
python3 code/simulated_annealing_tsp.py
python3 code/great_deluge_tsp.py
python3 code/tabu_search_tsp.py
python3 code/genetic_algorithm_maxone.py
```

## Reflection

At first I thought many algorithms were totally different. After a few lectures, I started to see that many of them are trying to answer the same question: how do we move from the current solution to a better one without checking everything? I still need more practice with choosing objective functions and understanding when a heuristic is useful.
