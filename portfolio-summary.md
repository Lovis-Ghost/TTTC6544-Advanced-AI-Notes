# Portfolio Summary

This repository is my personal learning portfolio for **TC6544 Advanced Artificial Intelligence**.

I use it to keep bilingual notes, small reflections, comparison tables, and simple Python demos. My main focus is to understand how different AI search and optimization methods work, not just memorize algorithm names.

这个仓库是我整理 **TC6544 Advanced Artificial Intelligence** 的个人学习记录。

我把中文理解和英文 academic terms 放在一起，是因为这样比较适合我复习。中文帮助我把算法想法讲清楚，英文术语帮助我准备课堂、作业和考试中会出现的表达。

## What This Portfolio Shows

- I can organize TC6544 topics into clear learning notes.
- I can explain search and optimization algorithms in my own words.
- I can compare heuristic search, local search, metaheuristics, population-based algorithms, and hyper-heuristics.
- I can connect lecture ideas with small Python demos.
- I know which topics are still placeholders and should be updated after learning them properly.

## Topics Covered

- [x] AI Optimization Basics
- [x] State Space Search
- [x] Heuristic Search and A*
- [x] Local Search and Hill Climbing
- [x] Simulated Annealing
- [x] Great Deluge
- [x] Tabu Search
- [x] Genetic Algorithm
- [x] Hyper-Heuristics
- [ ] Nature Inspired Algorithm I
- [ ] Nature Inspired Algorithm II
- [ ] Neural Network
- [ ] Fuzzy Logic

## Python Demo Work

The Python demos include BFS/DFS, A* search, greedy TSP nearest neighbour, hill climbing for TSP, simulated annealing, great deluge, tabu search, and a Genetic Algorithm for the MAXONE problem.

These scripts are small on purpose. I use them to observe steps such as queue/stack order, `g(n)`, `h(n)`, `f(n)`, neighbour changes, acceptance rules, tabu memory, and population fitness.

## My Current Understanding

From building this repo, I learned that many Advanced AI algorithms are connected by the same basic question: how do we search through possible solutions and decide what to try next?

At first, I saw every algorithm as a separate topic. Now I can see some patterns:

- State space search builds paths from states and actions.
- Heuristic search uses extra information to guide the search.
- Local search improves a current solution through neighbours.
- Metaheuristics add rules to escape local optimum.
- Genetic Algorithm searches with a population.
- Hyper-Heuristics work at a higher level by choosing or generating heuristics.

## Next Updates

I want to improve my hand-calculation practice and add better notes after the remaining lectures, especially nature-inspired algorithms, neural networks, and fuzzy logic.

这些内容之后还会继续更新。现在的目标是先把已经学过的部分整理清楚，再慢慢补充还没有覆盖的主题。
