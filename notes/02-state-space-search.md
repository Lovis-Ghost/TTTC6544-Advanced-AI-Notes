# State Space Search

## 1. What this topic is about / 这个主题在讲什么

State Space Search is about representing a problem as states and transitions. A state means one situation in the problem. An action changes one state into another state.

This topic is important because many AI problems can be converted into: start from an initial state, then search until reaching a goal state.

## 2. Key terms / 关键词

| English term | Chinese explanation |
|---|---|
| State | 问题中的一个情况或配置 |
| Initial state | 起点状态 |
| Goal state | 目标状态 |
| Action / Operator | 从一个状态转移到另一个状态的方法 |
| Transition | 状态之间的变化 |
| State space | 所有可能状态和连接关系 |
| Path | 从起点到某个状态经过的路线 |
| Search tree | 搜索过程中展开出来的树状结构 |

## 3. My understanding / 我的理解

我把 state space 想成一张地图。每一个 state 是地图上的一个点，action 是从一个点走到另一个点的路。Search algorithm 的工作就是决定先看哪里、后看哪里。这样想之后，BFS 和 DFS 就比较容易理解，不只是背定义。

The part I found useful is that the same problem can be represented in different ways. If the representation is good, the search may become easier. If the representation is poor, even a simple problem can look complicated.

For example, in a puzzle problem, a state can be the current arrangement of tiles. In route finding, a state can be the current city.

我觉得最容易被忽略的是 "how to represent a state"。如果 state 定义太少，可能不能完整描述问题；如果定义太多，search space 又会变得很大。

## 4. Step-by-step idea / 基本流程

1. Define all possible states.
2. Pick the initial state.
3. Define the goal test.
4. Define valid actions.
5. Choose a search strategy such as BFS or DFS.
6. Expand states until the goal is found or no states are left.

## 5. Small example / 小例子

Graph:

```text
A -> B, C
B -> D
C -> E
D -> Goal
E -> Goal
```

Initial state is `A`. Goal state is `Goal`.

BFS may visit level by level: `A, B, C, D, E, Goal`.
DFS may go deep first: `A, B, D, Goal`.

Both can find the goal, but their visiting order is different.

Another example:

```text
Room problem:
State = current room
Action = move through one door
Goal = reach the exit room
```

这个例子很简单，但它提醒我 state space search 不一定要一开始就想复杂图，只要先把 state 和 action 写清楚。

## 6. Common mistakes I made / 我容易混淆的地方

- I sometimes drew the search tree and graph as if they are the same. The graph is the original problem structure. The search tree is what the algorithm expands.
- I forgot to keep a visited list, so the search may repeat states.
- I thought DFS is always faster because it goes deep, but it can also go down a bad branch first.
- I sometimes forgot that BFS usually needs more memory because it keeps many frontier nodes.

## 7. Self-check questions / 自测问题

1. What is a state in a route finding problem?
2. Why do we need a goal test?
3. What is the difference between BFS and DFS visiting order?
4. Why is repeated-state checking important?
5. If I model a problem badly, how can it affect the search?

## 8. Short summary / 小结

State space search gives a structured way to model AI problems. The algorithm does not understand the real world directly. It searches through states that we define.
