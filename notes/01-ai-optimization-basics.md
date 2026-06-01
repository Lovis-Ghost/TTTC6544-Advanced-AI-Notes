# AI and Optimization Basics

## 1. What this topic is about / 这个主题在讲什么

This topic introduces what Artificial Intelligence is trying to do and why optimization appears so often in AI. In my understanding, AI is not only about making a computer "smart". It is also about letting the computer choose actions, search for answers, or improve a solution step by step.

Optimization means we have many possible choices, but we want the best one or at least a good enough one. In class, this became the starting point for many later algorithms.

## 2. Key terms / 关键词

| English term | Chinese explanation |
|---|---|
| Artificial Intelligence | 让机器表现出类似人类智能的能力，比如搜索、学习、推理和决策 |
| Optimization | 在很多候选方案中寻找最好或比较好的方案 |
| Objective function | 用来评价一个方案好不好，通常要最大化或最小化 |
| Fitness function | 在 Genetic Algorithm 里面常用的评价函数，意思和 objective function 很接近 |
| Constraint | 限制条件，不是所有方案都合法 |
| Search space | 所有可能解组成的空间 |
| Global optimum | 整个搜索空间里最好的解 |
| Local optimum | 附近看起来最好，但不一定是全局最好的解 |

## 3. My understanding / 我的理解

我觉得 AI 的很多问题最后都会变成一个选择问题。比如找路线、排时间表、玩游戏、分类资料，表面上很不同，但都需要在很多可能性里面做决定。老师讲 optimization 的时候，我开始明白不是每个 AI 问题都一定要像人一样思考，有时候重点是把问题写成可以 search 的形式。

At first I confused objective function and fitness function. Later I realized they are similar ideas used in different contexts. Objective function sounds more general. Fitness function is often used when we talk about population-based methods like Genetic Algorithm.

Another thing I learned is that "best" is not always simple. Sometimes the best route is shortest distance. Sometimes it must also consider time, cost, traffic, or other constraints. So before solving a problem, we must define what "good" means.

我也觉得 objective function 有点像给电脑的评分标准。如果评分标准写错了，algorithm 可能很努力地优化，但优化出来的答案还是不符合真实需求。

## 4. Step-by-step idea / 基本流程

1. Understand the problem.
2. Decide what a solution looks like.
3. Define the objective function.
4. Check constraints.
5. Choose a search or optimization method.
6. Compare the solution quality.
7. Reflect whether the result makes sense.

## 5. Small example / 小例子

Suppose I want to choose a path from my house to university.

- Solution: one possible route.
- Objective function: total travel time.
- Constraint: must use roads that are open.
- Best solution: route with minimum travel time.

If the map is small, I may check all routes. If the map is very large, I need a smarter search method.

Another simple example is exam revision planning:

- Solution: one possible timetable for revision.
- Objective function: maximize prepared topics, or minimize weak topics left.
- Constraint: only a few days before exam, and cannot study 24 hours.

这个例子让我觉得 optimization 不只是数学题，也可以是生活里面的安排问题。

## 6. Common mistakes I made / 我容易混淆的地方

- I sometimes forgot that the objective function must match the actual problem.
- I thought local optimum always means a bad solution, but actually it can still be useful.
- I mixed up constraints and objective function. Constraint decides if a solution is allowed. Objective function evaluates how good it is.
- I sometimes used "best" too casually. I should ask: best according to what measurement?

## 7. Self-check questions / 自测问题

1. What is the difference between a solution and a search space?
2. Why do we need an objective function?
3. Can a local optimum be useful?
4. What happens if the objective function is poorly designed?
5. In my own project, what could be a solution, objective function, and constraint?

## 8. Short summary / 小结

AI problems often involve searching or optimizing. Before applying an algorithm, I should first define the solution, objective function, constraints, and search space clearly.
