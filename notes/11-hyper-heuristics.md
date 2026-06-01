# Hyper-Heuristics

## 1. What this topic is about / 这个主题在讲什么

Hyper-Heuristics are about choosing or generating heuristics instead of directly solving the problem with one fixed heuristic. I understand it as "a method above heuristics".

## 2. Key terms / 关键词

| English term | Chinese explanation |
|---|---|
| Heuristic | 解题规则或经验方法 |
| Hyper-heuristic | 选择或生成 heuristic 的高层方法 |
| Low-level heuristic | 实际修改解或构造解的小规则 |
| Selection mechanism | 决定用哪个 heuristic 的方法 |

## 3. My understanding / 我的理解

This topic feels more abstract. Instead of asking "which solution should I choose?", we ask "which heuristic should I use now?" I think this is useful when one heuristic is not always good for every situation.

## 4. Step-by-step idea / 基本流程

1. Prepare several low-level heuristics.
2. Evaluate current problem state.
3. Select one heuristic.
4. Apply it to the solution.
5. Check improvement.
6. Update selection preference.

## 5. Small example / 小例子

For TSP, low-level heuristics may include swap two cities, reverse part of a route, or insert one city somewhere else. A hyper-heuristic decides which one to use.

## 6. Common mistakes I made / 我容易混淆的地方

- I first thought hyper-heuristic is just a stronger heuristic.
- I need to remember that it works at a higher level.
- The difference between selection and generation hyper-heuristics still needs more revision.

## 7. Self-check questions / 自测问题

1. What does a hyper-heuristic choose?
2. What is a low-level heuristic?
3. Why might one heuristic not be enough?

## 8. Short summary / 小结

Hyper-heuristics focus on managing heuristics. This can make search methods more general across problem types.
