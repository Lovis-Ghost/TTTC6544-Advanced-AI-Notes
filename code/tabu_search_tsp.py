cities = ["A", "B", "C", "D"]

distance = {
    "A": {"A": 0, "B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "B": 0, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "C": 0, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30, "D": 0},
}


def route_cost(route):
    return sum(distance[route[i]][route[(i + 1) % len(route)]] for i in range(len(route)))


def get_moves(route):
    moves = []
    for i in range(1, len(route) - 1):
        for j in range(i + 1, len(route)):
            new_route = route[:]
            new_route[i], new_route[j] = new_route[j], new_route[i]
            move = (route[i], route[j])
            moves.append((move, new_route))
    return moves


def tabu_search(start_route, tabu_size=3, steps=8):
    current = start_route
    best = start_route[:]
    best_cost = route_cost(best)
    tabu_list = []

    for step in range(steps):
        allowed_moves = []
        for move, route in get_moves(current):
            if move not in tabu_list:
                allowed_moves.append((move, route))

        if not allowed_moves:
            print("No allowed moves left")
            break

        move, chosen = min(allowed_moves, key=lambda item: route_cost(item[1]))
        chosen_cost = route_cost(chosen)

        print(
            f"Step {step + 1}: choose move {move}, route={chosen}, "
            f"cost={chosen_cost}, tabu={tabu_list}"
        )

        current = chosen
        tabu_list.append(move)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        if chosen_cost < best_cost:
            best = chosen[:]
            best_cost = chosen_cost

    return best, best_cost


if __name__ == "__main__":
    route, cost = tabu_search(["A", "B", "C", "D"])
    print("\nBest route found:", route)
    print("Best cost:", cost)
