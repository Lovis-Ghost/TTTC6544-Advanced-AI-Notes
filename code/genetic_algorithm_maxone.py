import random


random.seed(11)

POPULATION_SIZE = 6
CHROMOSOME_LENGTH = 8
MUTATION_RATE = 0.1
GENERATIONS = 8


def create_chromosome():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]


def fitness(chromosome):
    return sum(chromosome)


def select_parent(population):
    # Simple tournament selection: pick two, keep the better one.
    a, b = random.sample(population, 2)
    return a if fitness(a) >= fitness(b) else b


def crossover(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child = parent1[:point] + parent2[point:]
    return child


def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]
    return chromosome


def run_ga():
    population = [create_chromosome() for _ in range(POPULATION_SIZE)]

    for generation in range(GENERATIONS):
        population.sort(key=fitness, reverse=True)
        best = population[0]
        print(f"Generation {generation + 1}: best={best}, fitness={fitness(best)}")

        new_population = [best[:]]
        while len(new_population) < POPULATION_SIZE:
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    population.sort(key=fitness, reverse=True)
    return population[0], fitness(population[0])


if __name__ == "__main__":
    best, score = run_ga()
    print("\nBest chromosome:", best)
    print("Best fitness:", score)
