def dfs_search(graph, start, goal, path=None, visited=None):
    """Perform DFS to find a path from start to goal."""
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    if start == goal:
        return path

    visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs_search(graph, neighbor, goal, path + [neighbor], visited)
            if result:
                return result
    return None

graph = {
    'S': ['A', 'B', 'C'],
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['G', 'D'],
    'D': ['G'],
    'G': []  # Goal node
}
path = dfs_search(graph, 'S', 'G')
print("DFS Path:", " -> ".join(path) if path else "No path found")
