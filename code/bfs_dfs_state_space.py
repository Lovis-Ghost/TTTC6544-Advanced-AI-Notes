from collections import deque


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": ["G"],
    "G": [],
}


def bfs(start):
    visited = set()
    order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue

        print(f"BFS visiting: {node}")
        visited.add(node)
        order.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return order


def dfs(start):
    visited = set()
    order = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        print(f"DFS visiting: {node}")
        visited.add(node)
        order.append(node)

        # Reverse so the left-side neighbour is visited first.
        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return order


if __name__ == "__main__":
    print("Graph:", graph)
    print("\nBreadth First Search")
    bfs_order = bfs("A")
    print("BFS order:", bfs_order)

    print("\nDepth First Search")
    dfs_order = dfs("A")
    print("DFS order:", dfs_order)
