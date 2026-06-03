# Topic 1: AI Optimization Basics

## 1. What is Optimization?

Optimization means finding the best or near-best solution from many possible choices. In AI, many problems can be treated as optimization problems because we usually cannot directly tell the computer the perfect answer. Instead, we define an objective function, constraints, and a search space. Then the computer searches among possible solutions and tries to find a good result.

中文理解：Optimization 就是在很多可能答案里面找最优解或者比较好的解。AI 里面很多问题不是直接给电脑一个答案，而是给它目标、限制条件和搜索范围，让它自己寻找比较好的方案。

My understanding: optimization is like telling the computer what "good" means, then asking it to search for a better answer step by step.

## 2. Objective Function

An objective function is a formula or measurement used to evaluate the quality of a solution. The goal is usually to maximize or minimize this value.

For example, in TSP, the objective function can be the total distance of the tour:

```text
F = distance(city1, city2) + distance(city2, city3) + distance(city3, city1)
```

In this case, we want to minimize F. The objective function can also be total time, fuel cost, delivery cost, or other values depending on the problem.

中文理解：Objective function 就是给一个方案打分的标准。不同方案会得到不同分数，optimization 的目标就是让这个分数尽量高或尽量低。

I think objective function is very important because if the scoring rule is wrong, the algorithm may still optimize, but the answer may not match the real need.

## 3. Constraints

A constraint is a rule or limitation that a solution should follow.

A hard constraint must be satisfied. If it is violated, the solution becomes infeasible. For example, in exam scheduling, two exams taken by the same student cannot be arranged at the same time.

A soft constraint is preferred but not compulsory. If it is violated, the solution can still be used, but its quality becomes worse or receives a penalty. For example, it is better not to arrange two exams for the same student back-to-back on the same day.

中文理解：Hard constraint 是必须满足的规则，违反了方案就不可行。Soft constraint 是最好满足的偏好，违反了不一定无效，但会降低方案质量。

Simple example: if I make a revision timetable, "exam date cannot be changed" is more like a hard constraint. "I prefer not to study too late at night" is more like a soft constraint.

## 4. Search Space and Types of Solutions

The search space is the set of all possible solutions that can be explored during optimization. It may include both feasible and infeasible solutions.

A feasible solution satisfies all hard constraints.

An optimal solution is the best feasible solution according to the objective function.

A near-optimal solution is feasible and has good quality, but it is not guaranteed to be the absolute best solution.

中文理解：Search space 是所有可能解的范围。Feasible solution 是可行解，optimal solution 是最优解，near-optimal solution 是接近最优但不保证绝对最优的解。

My understanding: search space can be very big, and the algorithm is trying to move inside this space to find a good feasible answer.

## 5. Why Near-Optimal Solutions Are Useful

In many real-world AI optimization problems, finding the absolute optimal solution is not always necessary. Sometimes, response time is more important than perfect accuracy. For example, in autonomous driving, getting a near-optimal decision within a few milliseconds is more useful than getting the theoretically optimal decision after two seconds.

Also, searching for the optimal solution may require too much computation, while the improvement over a near-optimal solution may be very small. Therefore, accepting a near-optimal solution is often more practical.

中文理解：现实问题里不一定非要找 absolute optimal solution。因为最优解可能太慢、太贵，而 near-optimal solution 已经足够好，更适合实际应用。

This part makes me feel that AI optimization is not only about being perfect. It is also about being useful in real time.

## 6. Continuous vs Combinatorial Optimization

Continuous optimization means that the decision variables can take continuous values, usually real numbers. For example, speed, time, angle, or percentage can be continuous variables.

Combinatorial optimization means that the decision variables are discrete or arranged in combinations. For example, in TSP, the solution is the visiting order of cities. In exam scheduling, the solution is the assignment of exams to time slots.

中文理解：Continuous optimization 的变量是连续数值，比如速度、时间、比例。Combinatorial optimization 的变量是离散选择，比如城市访问顺序、考试时间段安排。

My simple way to remember: continuous is like choosing a value on a line, while combinatorial is like choosing an order, group, or arrangement.

## 7. Why TSP is a Combinatorial Optimization Problem

TSP is usually treated as a combinatorial optimization problem because its solution is a permutation of cities rather than a continuous value. A solution is not like choosing a speed or percentage, but choosing the visiting order of all cities.

The search space of TSP grows very quickly. If there are more cities, the number of possible tours increases in a factorial way. Therefore, it becomes impractical to check every possible route when the number of cities is large.

中文理解：TSP 的解是城市访问顺序，是排列组合问题。城市数量增加后，路线数量会按阶乘级增长，所以不能简单穷举。

Example: for only 4 cities, I can still imagine checking many routes. But for 50 cities, checking every route is basically not realistic.

## 8. Simple Problems vs Hard Problems

A simple problem usually has only a few decision variables, simple constraints, and one clear objective. The objective function is easy to calculate, and the problem is usually deterministic.

A hard problem usually has many decision variables and a very large search space. It may have many hard and soft constraints, multiple conflicting objectives, and dynamic or stochastic factors.

中文理解：Simple problem 通常变量少、约束少、目标明确。Hard problem 通常变量多、search space 很大，约束复杂，还可能有随机变化。

My understanding: hard problems are hard not only because the formula is difficult, but also because there are too many possible answers to compare.

## 9. Heuristic vs Exact Algorithm

An exact algorithm tries to guarantee the true optimal solution, but it may take too much time or memory for large problems.

A heuristic is an experience-based rule or method used to guide the search process. It does not guarantee the optimal solution, but it helps find a good or near-optimal solution faster.

For example, if I lose my keys, an exact search would mean checking every possible place one by one. A heuristic search would mean checking the most likely places first, such as my desk, bag, or pocket.

中文理解：Exact algorithm 更追求保证最优解，但可能很慢。Heuristic 更像根据经验来减少盲目搜索，速度更快，但不保证一定最优。

I think heuristic is like using common sense to guide the search, not just searching blindly.

## 10. Blind Search vs Heuristic Search

Blind search does not use extra problem-specific information to judge which state is closer to the goal. BFS and DFS are examples of blind search.

Heuristic search uses additional information or a heuristic function to guide the search. For example, A* uses a heuristic estimate, and the nearest neighbour rule in TSP chooses the closest unvisited city as the next step.

中文理解：Blind search 是没有方向感的搜索，只按照固定规则展开。Heuristic search 是有一定方向感的搜索，会利用额外信息判断哪个选择更可能接近目标。

Small example: if I search for a classroom building without any clue, that is more like blind search. If I know the building is near the library, I will search that area first, which is more like heuristic search.

## 11. My Summary

For an AI optimization problem, we first define the problem, decision variables, objective function, constraints, and search space. Then the algorithm searches within the search space to find a feasible solution. In real-world problems, finding the absolute optimal solution may be too slow or expensive, so a near-optimal solution is often more practical.

中文总结：AI optimization problem 一般先定义问题，再找出 decision variables、objective function、constraints 和 search space。最后算法会在 search space 里面寻找 feasible solution，并尽量找到 optimal 或 near-optimal solution。

My understanding after this topic: optimization is a basic way to describe many AI problems. The important part is not only choosing an algorithm, but also defining the problem clearly first.
