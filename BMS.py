from itertools import permutations

def british_museum_search(graph, start, goal):
    """Try all possible paths until a solution is found."""
    nodes = list(graph.keys())
    for perm in permutations(nodes):
        if perm[0] == start and perm[-1] == goal:
            return perm
    return None

graph = {
    'S': ['A', 'B', 'C'],
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['G', 'D'],
    'D': ['G'],
    'G': []  # Goal node
}

path = british_museum_search(graph, 'S', 'G')
print("British Museum Search Path:", " -> ".join(path) if path else "No path found")
