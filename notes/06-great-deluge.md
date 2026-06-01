# Great Deluge

## 1. What this topic is about / 这个主题在讲什么

Great Deluge is a local search algorithm that uses a water level idea. A solution is accepted if its cost is below a changing level.

## 2. Key terms / 关键词

| English term | Chinese explanation |
|---|---|
| Level | 接受解的水位线 |
| Up / decay | 水位变化的参数 |
| Candidate solution | 候选解 |
| Acceptance rule | 判断是否接受新解的规则 |

## 3. My understanding / 我的理解

I remember it as "can the solution survive below the water level?" For minimization problems, if the cost is not higher than the level, it can be accepted.

## 4. Step-by-step idea / 基本流程

1. Start with a solution.
2. Set an initial level.
3. Generate a neighbour.
4. Accept the neighbour if its cost is under the level.
5. Update the level.
6. Repeat.

## 5. Small example / 小例子

If water level is 40, a TSP route with cost 38 can be accepted. A route with cost 45 is rejected.

## 6. Common mistakes I made / 我容易混淆的地方

- I mixed up Great Deluge with simulated annealing.
- I need to remember that the acceptance rule uses level, not temperature.
- The meaning of UP still needs more practice from examples.

## 7. Self-check questions / 自测问题

1. What does the level represent?
2. How is Great Deluge different from simulated annealing?
3. Why can it accept a solution that is not immediately better?

## 8. Short summary / 小结

Great Deluge accepts solutions based on a level threshold. It is another way to allow exploration in local search.
