from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    # Set to track visited states
    visited = set()

    # Queue to store states as (jug1, jug2)
    queue = deque([(0, 0)])

    while queue:
        jug1, jug2 = queue.popleft()

        # If we reach the target amount, return success
        if jug1 == target or jug2 == target or jug1 + jug2 == target:
            print(f"Solution found: Jug1 = {jug1}, Jug2 = {jug2}")
            return True

        # Skip already visited states
        if (jug1, jug2) in visited:
            continue

        # Mark the current state as visited
        visited.add((jug1, jug2))

        # Generate all possible moves
        possible_states = [
            (jug1_capacity, jug2),  # Fill Jug1
            (jug1, jug2_capacity),  # Fill Jug2
            (0, jug2),              # Empty Jug1
            (jug1, 0),              # Empty Jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  # Pour Jug1 -> Jug2
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))   # Pour Jug2 -> Jug1
        ]

        # Add all valid states to the queue
        for state in possible_states:
            if state not in visited:
                queue.append(state)

    print("No solution found.")
    return False

if __name__ == "__main__":
    jug1_capacity = 4  # Capacity of Jug1
    jug2_capacity = 3  # Capacity of Jug2
    target = 2         # Target amount of water

    water_jug_bfs(jug1_capacity, jug2_capacity, target)
