# Genetic Algorithm

## 1. What this topic is about / 这个主题在讲什么

Genetic Algorithm is a population-based optimization method inspired by evolution. Instead of improving one solution only, it keeps a group of solutions.

## 2. Key terms / 关键词

| English term | Chinese explanation |
|---|---|
| Population | 一组候选解 |
| Chromosome | 一个编码后的解 |
| Gene | 解里面的一个小部分 |
| Fitness | 解的好坏分数 |
| Selection | 选择较好的个体 |
| Crossover | 交换两个个体的部分基因 |
| Mutation | 随机改变一点点基因 |

## 3. My understanding / 我的理解

GA feels different from hill climbing because it does not depend on one current solution. The population gives more diversity, but also makes the algorithm a bit harder to trace by hand.

## 4. Step-by-step idea / 基本流程

1. Create an initial population.
2. Evaluate fitness.
3. Select parents.
4. Apply crossover.
5. Apply mutation.
6. Create the next generation.
7. Repeat until stopping condition.

## 5. Small example / 小例子

MAXONE problem: the goal is to make a binary string with as many `1`s as possible.

```text
10101 fitness = 3
11101 fitness = 4
```

## 6. Common mistakes I made / 我容易混淆的地方

- I confused objective function and fitness function.
- I thought mutation should be large, but usually it is small.
- I forgot that selection should still keep some diversity.

## 7. Self-check questions / 自测问题

1. What is the role of crossover?
2. Why do we need mutation?
3. What does fitness mean in MAXONE?

## 8. Short summary / 小结

Genetic Algorithm searches using a population. It combines selection, crossover, and mutation to improve solutions over generations.
