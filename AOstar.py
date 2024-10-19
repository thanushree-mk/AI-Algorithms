def ao_star(graph, start, goal, heuristic):
    """Perform AO* search with weighted edges and heuristic values."""
    path = [start]  # Initialize path with the starting node
    current = start

    while current != goal:
        neighbors = graph.get(current, [])
        
        # Select the neighbor with the lowest heuristic value
        best_neighbor = min(neighbors, key=lambda n: heuristic[n[0]])[0]

        path.append(best_neighbor)
        current = best_neighbor

        if current == goal:
            return path

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

# Run AO* search
path = ao_star(graph_weighted, 'S', 'G', heuristic)
print("AO* Search Path:", " -> ".join(path) if path else "No path found")
