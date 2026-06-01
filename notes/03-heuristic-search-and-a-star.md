# Heuristic Search and A*

## 1. What this topic is about / 这个主题在讲什么

Heuristic search uses extra information to guide the search. Instead of searching blindly, the algorithm uses an estimate of how close a state is to the goal.

A* Search combines the cost already spent and the estimated cost to the goal. This is why it is often written as:

```text
f(n) = g(n) + h(n)
```

## 2. Key terms / 关键词

| English term | Chinese explanation |
|---|---|
| Heuristic | 估计值，用来判断哪个方向比较有希望 |
| Greedy best-first search | 主要看 h(n)，选择看起来离目标最近的节点 |
| A* Search | 同时考虑已花费成本 g(n) 和估计剩余成本 h(n) |
| g(n) | 从起点到当前节点的实际成本 |
| h(n) | 从当前节点到目标的估计成本 |
| f(n) | A* 用来排序节点的总估计成本 |
| Admissible heuristic | 不高估真实成本的启发式函数 |

## 3. My understanding / 我的理解

我觉得 heuristic 就像经验判断。它不一定完全正确，但它可以帮助 search 不要乱找。中文可以把它想成 "有方向感的估计"，不是保证答案。

Greedy search only looks at which node seems closest to the goal. This can be fast, but sometimes it chooses a path that looks good now but is expensive overall. A* is more balanced because it also remembers the cost already paid.

At first, I kept mixing up `g(n)` and `h(n)`. Now I remember it like this: `g` is already gone, `h` is hope or guess for the remaining distance.

我现在看 A* 的时候，会先问两个问题：到这里已经花了多少 cost？从这里到 goal 还大概需要多少 cost？把这两个放在一起，就是 `f(n)` 的意思。

## 4. Step-by-step idea / 基本流程

1. Put the start node into an open list.
2. Calculate `f(n) = g(n) + h(n)`.
3. Choose the node with the smallest `f(n)`.
4. If it is the goal, stop.
5. Expand its neighbours.
6. Update costs if a cheaper path is found.
7. Repeat until the goal is found.

## 5. Small example / 小例子

Suppose we search from `A` to `G`.

```text
A -> B cost 1
A -> C cost 4
B -> G cost 6
C -> G cost 1
```

If the heuristic says `B` looks close, greedy search may choose `B` first. But the total path `A-B-G` costs 7. The path `A-C-G` costs 5.

A* checks both actual cost and estimated remaining cost, so it has a better chance to avoid this kind of trap if the heuristic is good.

Tiny calculation:

```text
For node B:
g(B) = 1
h(B) = maybe 6
f(B) = 7

For node C:
g(C) = 4
h(C) = maybe 1
f(C) = 5
```

Even though C costs more at the beginning, A* may still choose C because the total estimated cost is lower.

## 6. Common mistakes I made / 我容易混淆的地方

- I thought a heuristic is always correct. Actually it is an estimate.
- I forgot that `g(n)` is accumulated from the start.
- I assumed A* is always fast. If the search space is large or heuristic is weak, it can still be expensive.
- I mixed up "shortest path found" and "first goal found" for different search strategies.
- I sometimes only looked at `h(n)` and accidentally reasoned like greedy search instead of A*.

## 7. Self-check questions / 自测问题

1. What does `h(n)` estimate?
2. Why can greedy search make a poor choice?
3. Why does A* use both `g(n)` and `h(n)`?
4. What does admissible heuristic mean?
5. If two nodes have the same `f(n)`, what tie-breaking rule would I use?

## 8. Short summary / 小结

Heuristic search uses estimated knowledge to guide searching. A* is important because it combines past cost and future estimated cost in one score.
