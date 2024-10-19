import heapq

def branch_and_bound(graph, start, goal):
    pq = [(0, [start])]  

    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return path

        for neighbor, weight in graph.get(node, []):
            new_path = path + [neighbor]
            heapq.heappush(pq, (cost + weight, new_path))

    return None

graph_weighted = {
    'S': [('A', 1), ('B', 2)],
    'A': [('D', 1)],
    'B': [('C', 2)],
    'C': [('G', 1)],
    'D': [('G', 2)],
    'G': []
}
path = branch_and_bound(graph_weighted, 'S', 'G')
print("Branch and Bound Path:", " -> ".join(path) if path else "No path found")
