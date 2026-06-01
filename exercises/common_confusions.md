# Common Confusions

## Objective function vs fitness function

I used to treat them as totally different. Now I think of them as very similar evaluation ideas, but fitness function is often used in evolutionary algorithms.

## Graph vs search tree

The graph is the problem structure. The search tree is what the algorithm creates while exploring.

## Greedy search vs A*

Greedy search mainly follows the heuristic. A* uses both actual cost and estimated remaining cost.

## Local optimum vs global optimum

Local optimum is best nearby. Global optimum is best overall. A local search method may stop at a local optimum.

## Hill climbing vs simulated annealing

Hill climbing accepts better moves only. Simulated annealing may accept worse moves based on temperature and probability.

## Tabu list vs visited list

A visited list in graph search prevents repeated states. A tabu list in local search prevents recent moves from being reversed too quickly.
