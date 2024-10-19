from collections import deque

def bfs_search(graph, start, goal):
    """Perform BFS to find the shortest path from start to goal."""
    queue = deque([[start]])  # Queue stores paths
    visited = set()  # Track visited nodes

    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        node = path[-1]

        # If the goal is found, return the path
        if node == goal:
            return path

        # Explore neighbors if the node hasn't been visited
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = path + [neighbor]
                queue.append(new_path)

    return None  # Return None if no path is found

# Simple unweighted graph
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['G'],  # Goal reachable from D
    'E': [],
    'G': []  # Goal node
}

# Run BFS
path = bfs_search(graph, 'S', 'G')
print("BFS Search Path:", " -> ".join(path) if path else "No path found")
