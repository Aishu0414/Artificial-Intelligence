from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Queue initialized with the starting node

    while queue:
        node = queue.popleft()  # Dequeue a node from the front
        if node not in visited:
            print(node, end=" ")  # Process the node (e.g., print it)
            visited.add(node)  # Mark the node as visited

            # Enqueue all unvisited adjacent nodes
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

start_node = 0
print("BFS traversal starting from node 0:")
bfs(graph, start_node)
