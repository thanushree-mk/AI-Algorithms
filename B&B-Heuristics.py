import heapq
def branch_and_bound_with_heuristics(graph, start, goal, heuristic):
    pq = [(0 + heuristic[start], [start])]

    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return path

        for neighbor, weight in graph.get(node, []):
            new_path = path + [neighbor]
            heapq.heappush(pq, (cost + weight + heuristic[neighbor], new_path))

    return None

graph_weighted = {
    'S': [('A', 1), ('B', 2)],
    'A': [('D', 1)],
    'B': [('C', 2)],
    'C': [('G', 1)],
    'D': [('G', 2)],
    'G': []
}

heuristic = {
    'S': 3,  # Estimate from S to G
    'A': 2,  # Estimate from A to G
    'B': 4,  # Estimate from B to G
    'C': 1,  # Estimate from C to G
    'D': 1,  # Estimate from D to G
    'G': 0   # Goal node, so the cost is 0
}

path = branch_and_bound_with_heuristics(graph_weighted, 'S', 'G', heuristic)
print("Branch and Bound with Heuristics Path:", " -> ".join(path) if path else "No path found")
