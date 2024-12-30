def is_safe(assignment, region, color, neighbors):
    """
    Check if assigning the given color to the region is safe.
    """
    for neighbor in neighbors[region]:
        if assignment.get(neighbor) == color:
            return False
    return True

def backtrack(assignment, regions, colors, neighbors):
    """
    Backtracking function to solve the map coloring problem.
    """
    # If all regions are assigned a color, return the assignment
    if len(assignment) == len(regions):
        return assignment
    
    # Select the next uncolored region
    for region in regions:
        if region not in assignment:
            break
    
    # Try assigning each color to the region
    for color in colors:
        if is_safe(assignment, region, color, neighbors):
            assignment[region] = color  # Assign the color
            result = backtrack(assignment, regions, colors, neighbors)
            if result:  # If successful, return the result
                return result
            assignment.pop(region)  # Undo the assignment if it fails
    
    return None  # No solution found

def map_coloring(regions, colors, neighbors):
    """
    Solve the map coloring problem using backtracking.
    regions: List of regions to color.
    colors: List of available colors.
    neighbors: Dictionary where the key is a region, and the value is a list of adjacent regions.
    """
    assignment = {}
    return backtrack(assignment, regions, colors, neighbors)

# Example usage:
regions = ["A", "B", "C", "D"]
colors = ["Red", "Green", "Blue"]
neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

solution = map_coloring(regions, colors, neighbors)
print("Solution:", solution)
