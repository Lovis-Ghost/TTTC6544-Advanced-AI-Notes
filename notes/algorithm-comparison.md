# Algorithm Comparison

## Why I need this table / 为什么需要比较

At first, many algorithms in this course looked similar to me because they all try to improve a solution. 但是慢慢看下来，它们其实差别在 acceptance rule、memory，还有 search space 的探索方式。

This table is mainly for revision. It helps me compare the algorithms quickly before going back to detailed notes.

## Comparison table

| Algorithm | Main idea | Accept worse solution? | Memory? | Single-solution or population-based? | My simple understanding |
|---|---|---|---|---|---|
| Hill Climbing | Move to a better neighbour | No, normally only better moves | No special memory | Single-solution | 最简单，看到更好的就走，但容易卡住 |
| Simulated Annealing | Use temperature and probability to explore | Yes, sometimes | No special memory | Single-solution | 像 hill climbing 加了温度，前期比较敢试 |
| Great Deluge | Accept solution if cost is below level | Yes, if under the level | No special memory | Single-solution | 用水位线判断能不能接受，不是用概率 |
| Tabu Search | Use tabu list to avoid recent reverse moves | Can accept non-best moves if allowed | Yes, tabu list | Single-solution | 有记忆，避免一直来回走 |
| Genetic Algorithm | Improve a population using selection, crossover, mutation | Not in the same neighbour sense | Population keeps many candidates | Population-based | 一群解一起进化，不是只改一个 current solution |
| Hyper-Heuristics | Choose or generate heuristics | Depends on selected heuristic and acceptance rule | May use performance history | Usually works above low-level heuristics | 不是直接改 solution，而是选择用哪个 heuristic |

## My current understanding

Hill Climbing is easiest but easy to get stuck. It is good for learning the basic idea of local search, but it is quite strict because it only accepts better neighbours.

SA and GD both can accept worse solutions, but SA uses probability and temperature, while GD uses level. 这两个我容易混在一起，所以我用 "temperature vs level" 来区分。

Tabu Search uses memory to avoid cycling. It reminds me that search is not only about choosing a good next move, but also about remembering what should not be repeated too soon.

GA searches with a population. I should remember that fitness function is used to compare chromosomes, and crossover/mutation create new candidates.

Hyper-Heuristic is higher-level because it chooses heuristics rather than directly changing solutions. This one still feels more abstract to me, so I need more examples.

## Common confusions

- Objective function vs fitness function: both evaluate quality, but fitness function is commonly used in GA.
- Neighbour vs low-level heuristic: neighbour is a nearby solution; low-level heuristic is a rule that can create or modify solutions.
- Metaheuristic vs hyper-heuristic: metaheuristic searches for solutions; hyper-heuristic chooses or generates heuristics.
- Local optimum vs global optimum: local optimum is best nearby; global optimum is best overall.

## Self-check questions

1. Why does Hill Climbing easily get stuck in local optimum?
2. What is the main difference between Simulated Annealing and Great Deluge?
3. How does Tabu Search use memory?
4. Why is Genetic Algorithm called population-based?
5. Why is Hyper-Heuristic considered higher-level than normal heuristics?
