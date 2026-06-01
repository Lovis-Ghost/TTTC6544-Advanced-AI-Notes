import random


random.seed(3)

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


def great_deluge(start_route, level=95, up=1.5, steps=15):
    current = start_route
    current_cost = route_cost(current)
    best = current[:]
    best_cost = current_cost

    for step in range(steps):
        candidate = random_neighbour(current)
        candidate_cost = route_cost(candidate)

        accept = candidate_cost <= level
        print(
            f"Step {step + 1}: level={level:.1f}, candidate={candidate}, "
            f"cost={candidate_cost}, accept={accept}"
        )

        if accept:
            current = candidate
            current_cost = candidate_cost

        if current_cost < best_cost:
            best = current[:]
            best_cost = current_cost

        level -= up

    return best, best_cost


if __name__ == "__main__":
    route, cost = great_deluge(["A", "B", "C", "D"])
    print("\nBest route found:", route)
    print("Best cost:", cost)
