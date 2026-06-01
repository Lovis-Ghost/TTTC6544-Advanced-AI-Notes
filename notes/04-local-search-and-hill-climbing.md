# Local Search and Hill Climbing

## 1. What this topic is about / 这个主题在讲什么

Local Search focuses on improving a current solution instead of building a path from start to goal. This is useful for optimization problems where we mainly care about the final solution quality.

Hill Climbing is a simple local search method. It looks at neighbouring solutions and moves to a better one.

## 2. Key terms / 关键词

| English term | Chinese explanation |
|---|---|
| Local search | 从一个当前解开始，在附近找更好的解 |
| Current solution | 当前正在考虑的解 |
| Neighbour | 通过小改变得到的新解 |
| Objective value | 解的评价分数或成本 |
| Hill climbing | 只接受更好邻居的局部搜索方法 |
| Local optimum | 附近没有更好解，但不一定是全局最好 |
| Plateau | 很多邻居分数差不多，算法不知道往哪里走 |

## 3. My understanding / 我的理解

Hill climbing is easy to understand because it is like always walking uphill. If we are maximizing, we move to a higher value. If we are minimizing, we move to a lower cost.

But the weakness is also clear. If the algorithm reaches a place where all neighbours are worse, it stops. The problem is that this point may only be a local optimum.

For TSP, a solution can be one route. A neighbour can be made by swapping two cities. If the new route distance is shorter, hill climbing accepts it.

## 4. Step-by-step idea / 基本流程

1. Start with an initial solution.
2. Calculate its cost or score.
3. Generate neighbouring solutions.
4. Pick a neighbour.
5. If the neighbour is better, move to it.
6. If no better neighbour exists, stop.

## 5. Small example / 小例子

Route:

```text
A -> B -> C -> D -> A
```

Neighbour by swapping `B` and `C`:

```text
A -> C -> B -> D -> A
```

If the new route is shorter, hill climbing keeps the new route. If not, it stays with the old one.

## 6. Common mistakes I made / 我容易混淆的地方

- I forgot that hill climbing can be used for minimization too. "Up" just means better.
- I thought stopping means the global best is found. Actually it may only be local optimum.
- I sometimes generated neighbours in a random way and then wondered why the result changed each run.
- I confused hill climbing with simulated annealing. Hill climbing rejects worse moves, but simulated annealing may accept them sometimes.

## 7. Self-check questions / 自测问题

1. What is a neighbour solution?
2. Why can hill climbing get stuck?
3. How can TSP create neighbours?
4. What is the difference between local optimum and global optimum?

## 8. Short summary / 小结

Hill climbing is simple and useful for understanding local search. It improves a solution step by step, but it can get stuck because it does not normally accept worse moves.
