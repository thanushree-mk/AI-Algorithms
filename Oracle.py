def oracle_search(graph, start, goal, solution_path):
    """Use a pre-determined solution path."""
    if solution_path[0] == start and solution_path[-1] == goal:
        return solution_path
    return None

graph = {
    'S': ['A', 'B', 'C'],
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['G', 'D'],
    'D': ['G'],
    'G': []  
}
path = oracle_search(graph, 'S', 'G', ['S', 'A', 'D', 'G'])
print("Oracle Path:", " -> ".join(path) if path else "No path found")
