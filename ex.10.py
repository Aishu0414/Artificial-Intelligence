import heapq

def a_star(graph, start, goal, heuristic):
    """
    A* algorithm to find the shortest path in a graph.
    graph: A dictionary where the key is the node and the value is a list of tuples (neighbor, cost).
    start: The starting node.
    goal: The goal node.
    heuristic: A function that calculates the heuristic (estimated cost to reach the goal).
    """
    # Priority queue to store nodes to visit, starting with the start node
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), start))  # (f, node)
    
    # Dictionaries to track the cost and the parent of each node
    g_costs = {start: 0}
    parents = {start: None}
    
    while open_list:
        # Get the node with the lowest f value
        _, current = heapq.heappop(open_list)
        
        # If we reach the goal, reconstruct the path
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1]  # Reverse the path to get the correct order
        
        # Explore neighbors
        for neighbor, cost in graph[current]:
            tentative_g_cost = g_costs[current] + cost
            
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_cost, neighbor))
                parents[neighbor] = current
    
    return None  # No path found

# Example usage
def heuristic(node, goal):
    """Simple heuristic: Manhattan distance (assuming grid-based graph)."""
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# Graph (a grid with neighbors and their respective costs)
graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((1, 0), 1), ((0, 1), 1)]
}

start = (0, 0)
goal = (1, 1)

path = a_star(graph, start, goal, heuristic)
print("Path:", path)
