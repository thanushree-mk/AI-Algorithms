def hill_climbing(graph, start, goal, heuristic):
    """Perform Hill Climbing using a heuristic."""
    current = start
    path = [current]

    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:
            return None  # Dead-end

        current = min(neighbors, key=lambda n: heuristic.get(n, float('inf')))
        path.append(current)

        if current == goal:
            return path

    return None

graph = {
    'S': ['A', 'B', 'C'],
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['G', 'D'],
    'D': ['G'],
    'G': []  
}

heuristic = {'S': 3, 'A': 2, 'B': 6, 'D': 1, 'G': 0}
path = hill_climbing(graph, 'S', 'G', heuristic)
print("Hill Climbing Path:", " -> ".join(path) if path else "No path found")
