# Tabu Search

## 1. What this topic is about / 这个主题在讲什么

Tabu Search is a local search method that uses memory. It keeps a tabu list so the algorithm does not immediately undo recent moves.

## 2. Key terms / 关键词

| English term | Chinese explanation |
|---|---|
| Tabu list | 暂时禁止的移动或状态列表 |
| Tabu tenure | 一个移动留在 tabu list 的时间 |
| Aspiration criterion | 特殊情况下允许 tabu move 的规则 |
| Neighbourhood | 当前解附近可选择的新解集合 |

## 3. My understanding / 我的理解

The main idea I got is: do not keep walking back and forth. If I just swapped two cities, the tabu list can stop me from reversing that swap immediately.

## 4. Step-by-step idea / 基本流程

1. Start with an initial solution.
2. Generate neighbours.
3. Choose a good allowed move.
4. Add the move to tabu list.
5. Remove old tabu items when the list is too long.
6. Track the best solution found.

## 5. Small example / 小例子

For a route `A-B-C-D`, if I swap `B` and `C`, the move `(B, C)` can be tabu for a few iterations.

## 6. Common mistakes I made / 我容易混淆的地方

- I thought tabu search only rejects bad moves. Actually it rejects tabu moves.
- I forgot that the best solution should be stored separately.
- I need more practice with aspiration criterion.

## 7. Self-check questions / 自测问题

1. Why does tabu search use memory?
2. What is tabu tenure?
3. Why should we store the best solution separately?

## 8. Short summary / 小结

Tabu Search improves local search by using memory. The tabu list helps reduce cycling.
