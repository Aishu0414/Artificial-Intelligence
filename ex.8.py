def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set
    
    visited.add(node)  # Mark the current node as visited
    print(node, end=" ")  # Process the node (e.g., print it)
    
    # Recursively visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

start_node = 0
print("DFS traversal starting from node 0:")
dfs(graph, start_node)
