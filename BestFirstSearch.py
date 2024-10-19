import heapq
def best_first_search(graph, start, goal, heuristic):
    """Perform Best-First Search."""
    # Priority queue to store (heuristic value, path) tuples
    pq = [(heuristic[start], [start])]

    while pq:
        # Get the path with the lowest heuristic value
        _, path = heapq.heappop(pq)
        node = path[-1]

        # If the goal is reached, return the path
        if node == goal:
            return path

        # Explore neighbors
        for neighbor, _ in graph.get(node, []):  # Extract neighbors properly
            new_path = path + [neighbor]
            heapq.heappush(pq, (heuristic[neighbor], new_path))

    return None  # Return None if no path is found

# Graph with weighted edges
graph_weighted = {
    'S': [('A', 1), ('B', 2)],
    'A': [('D', 1)],
    'B': [('C', 2)],
    'C': [('G', 1)],
    'D': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'S': 3,  # Estimate from S to G
    'A': 2,  # Estimate from A to G
    'B': 4,  # Estimate from B to G
    'C': 1,  # Estimate from C to G
    'D': 1,  # Estimate from D to G
    'G': 0   # Goal node
}

# Run Best-First Search
path = best_first_search(graph_weighted, 'S', 'G', heuristic)
print("Best-First Search Path:", " -> ".join(path) if path else "No path found")
