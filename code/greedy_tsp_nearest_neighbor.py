cities = ["A", "B", "C", "D"]

distance = {
    "A": {"A": 0, "B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "B": 0, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "C": 0, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30, "D": 0},
}


def nearest_neighbor(start):
    route = [start]
    unvisited = set(cities)
    unvisited.remove(start)
    total = 0
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance[current][city])
        step_cost = distance[current][next_city]
        print(f"From {current}, choose nearest city {next_city} with distance {step_cost}")

        route.append(next_city)
        unvisited.remove(next_city)
        total += step_cost
        current = next_city

    total += distance[current][start]
    route.append(start)
    print(f"Return from {current} to {start}, distance {distance[current][start]}")

    return route, total


if __name__ == "__main__":
    route, total = nearest_neighbor("A")
    print("\nGreedy TSP route:", route)
    print("Total distance:", total)
