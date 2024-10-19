import heapq

def beam_search(graph, start, goal, heuristic, beam_width=2):
    """Perform Beam Search with a fixed beam width."""
    # Priority queue to store (heuristic value, path) tuples
    pq = [(heuristic[start], [start])]
    
    while pq:
        # Keep only the top `beam_width` paths
        pq = heapq.nsmallest(beam_width, pq)

        next_level = []  # Store paths for the next level of exploration
        
        # Explore the current set of paths
        for _, path in pq:
            node = path[-1]

            # If the goal is reached, return the path
            if node == goal:
                return path

            # Explore neighbors
            for neighbor, _ in graph.get(node, []):
                new_path = path + [neighbor]
                heapq.heappush(next_level, (heuristic[neighbor], new_path))

        pq = next_level  # Move to the next level

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

# Run Beam Search with a beam width of 2
path = beam_search(graph_weighted, 'S', 'G', heuristic, beam_width=2)
print("Beam Search Path:", " -> ".join(path) if path else "No path found")
