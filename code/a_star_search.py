import heapq


graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("E", 1)],
    "D": [("G", 5)],
    "E": [("G", 3)],
    "G": [],
}

heuristic = {
    "A": 6,
    "B": 4,
    "C": 3,
    "D": 4,
    "E": 2,
    "G": 0,
}


def reconstruct_path(came_from, node):
    path = [node]
    while node in came_from:
        node = came_from[node]
        path.append(node)
    path.reverse()
    return path


def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    came_from = {}
    g_cost = {start: 0}

    while open_list:
        current_f, current = heapq.heappop(open_list)
        print(f"Checking {current}: g={g_cost[current]}, h={heuristic[current]}, f={current_f}")

        if current == goal:
            return reconstruct_path(came_from, goal), g_cost[goal]

        for neighbour, cost in graph[current]:
            new_g = g_cost[current] + cost

            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                came_from[neighbour] = current
                g_cost[neighbour] = new_g
                f_cost = new_g + heuristic[neighbour]
                print(f"  update {neighbour}: g={new_g}, h={heuristic[neighbour]}, f={f_cost}")
                heapq.heappush(open_list, (f_cost, neighbour))

    return None, None


if __name__ == "__main__":
    path, cost = a_star("A", "G")
    print("\nFinal path:", path)
    print("Total cost:", cost)
