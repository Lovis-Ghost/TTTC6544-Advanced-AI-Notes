# Simulated Annealing

## 1. What this topic is about / 这个主题在讲什么

Simulated Annealing is a local search method that sometimes accepts worse moves. The idea comes from cooling metal slowly. At high temperature, the search is more willing to explore. At low temperature, it becomes more careful.

## 2. Key terms / 关键词

| English term | Chinese explanation |
|---|---|
| Temperature | 控制接受较差解的可能性 |
| Cooling schedule | 温度下降的规则 |
| Worse move | 成本更高或分数更差的移动 |
| Acceptance probability | 接受较差解的概率 |

## 3. My understanding / 我的理解

This algorithm feels like a smarter version of hill climbing. It does not panic when it sees a worse neighbour, because sometimes going worse first can help escape local optimum.

## 4. Step-by-step idea / 基本流程

1. Start with a solution and a high temperature.
2. Generate a neighbour.
3. Accept it if it is better.
4. If it is worse, maybe accept it based on probability.
5. Reduce the temperature.
6. Stop when temperature is low or iteration limit is reached.

## 5. Small example / 小例子

For TSP, if a swapped route is 3 units longer, hill climbing rejects it. Simulated annealing may accept it when temperature is high.

## 6. Common mistakes I made / 我容易混淆的地方

- I forgot that temperature should decrease.
- I thought worse moves are always accepted. Actually they are accepted with probability.
- I need more practice choosing cooling rate.

## 7. Self-check questions / 自测问题

1. Why accept a worse solution?
2. What happens when temperature is very low?
3. How is simulated annealing different from hill climbing?

## 8. Short summary / 小结

Simulated annealing adds controlled randomness to local search. This helps it escape some local optima.
