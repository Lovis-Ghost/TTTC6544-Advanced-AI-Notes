import math
import random


random.seed(7)

cities = ["A", "B", "C", "D"]

distance = {
    "A": {"A": 0, "B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "B": 0, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "C": 0, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30, "D": 0},
}


def route_cost(route):
    return sum(distance[route[i]][route[(i + 1) % len(route)]] for i in range(len(route)))


def random_neighbour(route):
    new_route = route[:]
    i, j = random.sample(range(1, len(route)), 2)
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route


def simulated_annealing(start_route, temperature=50.0, cooling=0.85, steps=20):
    current = start_route
    current_cost = route_cost(current)
    best = current[:]
    best_cost = current_cost

    for step in range(steps):
        neighbour = random_neighbour(current)
        neighbour_cost = route_cost(neighbour)
        difference = neighbour_cost - current_cost

        if difference < 0:
            accept = True
            reason = "better"
        else:
            probability = math.exp(-difference / temperature)
            accept = random.random() < probability
            reason = f"worse, probability={probability:.3f}"

        print(
            f"Step {step + 1}: temp={temperature:.2f}, neighbour={neighbour}, "
            f"cost={neighbour_cost}, {reason}, accept={accept}"
        )

        if accept:
            current = neighbour
            current_cost = neighbour_cost

        if current_cost < best_cost:
            best = current[:]
            best_cost = current_cost

        temperature *= cooling

    return best, best_cost


if __name__ == "__main__":
    route, cost = simulated_annealing(["A", "B", "C", "D"])
    print("\nBest route found:", route)
    print("Best cost:", cost)
