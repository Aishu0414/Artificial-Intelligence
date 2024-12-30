import itertools

def calculate_distance(route, dist_matrix):
    """
    Calculate the total distance for a given route.
    """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += dist_matrix[route[i]][route[i + 1]]
    total_distance += dist_matrix[route[-1]][route[0]]  # Return to the start city
    return total_distance

def traveling_salesman_bruteforce(dist_matrix):
    """
    Solve the TSP problem using brute force.
    dist_matrix: A 2D list where dist_matrix[i][j] is the distance from city i to city j.
    """
    n = len(dist_matrix)
    cities = list(range(n))  # List of cities (represented as integers)
    
    # Generate all possible routes (permutations)
    possible_routes = itertools.permutations(cities)
    
    # Initialize the minimum distance and best route
    min_distance = float('inf')
    best_route = None
    
    # Iterate through all possible routes and calculate the total distance
    for route in possible_routes:
        route_distance = calculate_distance(route, dist_matrix)
        if route_distance < min_distance:
            min_distance = route_distance
            best_route = route
    
    return best_route, min_distance

# Example usage
dist_matrix = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 5],
    [20, 25, 30, 0, 15],
    [25, 30, 5, 15, 0]
]

best_route, min_distance = traveling_salesman_bruteforce(dist_matrix)

print(f"Best route: {best_route}")
print(f"Minimum distance: {min_distance}")
