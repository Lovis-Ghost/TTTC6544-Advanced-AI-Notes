cities = ["A", "B", "C", "D"]

distance = {
    "A": {"A": 0, "B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "B": 0, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "C": 0, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30, "D": 0},
}


def route_cost(route):
    total = 0
    for i in range(len(route)):
        total += distance[route[i]][route[(i + 1) % len(route)]]
    return total


def get_neighbours(route):
    neighbours = []
    for i in range(1, len(route) - 1):
        for j in range(i + 1, len(route)):
            new_route = route[:]
            new_route[i], new_route[j] = new_route[j], new_route[i]
            neighbours.append(new_route)
    return neighbours


def hill_climbing(start_route):
    current = start_route
    current_cost = route_cost(current)
    print(f"Start route: {current}, cost: {current_cost}")

    while True:
        neighbours = get_neighbours(current)
        best_neighbour = min(neighbours, key=route_cost)
        best_cost = route_cost(best_neighbour)

        print(f"Best neighbour: {best_neighbour}, cost: {best_cost}")

        if best_cost < current_cost:
            current = best_neighbour
            current_cost = best_cost
            print("Accept better route")
        else:
            print("No better neighbour, stop")
            break

    return current, current_cost


if __name__ == "__main__":
    route, cost = hill_climbing(["A", "B", "C", "D"])
    print("\nFinal route:", route)
    print("Final cost:", cost)
