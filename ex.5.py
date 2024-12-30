from collections import deque

# State is represented as a tuple (missionaries on left bank, cannibals on left bank, boat position)
def bfs():
    # Initialize the queue with the starting state
    initial_state = (3, 3, 'left')  # 3 missionaries, 3 cannibals, boat on left
    goal_state = (0, 0, 'right')  # Goal: all missionaries and cannibals on the right
    queue = deque([(initial_state, [])])  # Each element is a tuple (state, path taken)
    visited = set([initial_state])

    while queue:
        (m_left, c_left, boat), path = queue.popleft()

        # If we reached the goal state, return the solution path
        if (m_left, c_left, boat) == goal_state:
            return path

        # List of possible moves
        moves = [
            (1, 0),  # 1 missionary
            (0, 1),  # 1 cannibal
            (2, 0),  # 2 missionaries
            (0, 2),  # 2 cannibals
            (1, 1)   # 1 missionary and 1 cannibal
        ]
        
        # Generate next possible states
        for m, c in moves:
            if boat == 'left':
                new_m_left, new_c_left = m_left - m, c_left - c
                new_m_right, new_c_right = 3 - new_m_left, 3 - new_c_left
                new_boat = 'right'
            else:
                new_m_left, new_c_left = m_left + m, c_left + c
                new_m_right, new_c_right = 3 - new_m_left, 3 - new_c_left
                new_boat = 'left'

            # Check if the new state is valid (no more cannibals than missionaries on either side)
            if 0 <= new_m_left <= 3 and 0 <= new_c_left <= 3 and 0 <= new_m_right <= 3 and 0 <= new_c_right <= 3:
                if (new_m_left == 0 or new_m_left >= new_c_left) and (new_m_right == 0 or new_m_right >= new_c_right):
                    new_state = (new_m_left, new_c_left, new_boat)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [f"Move {m} missionaries and {c} cannibals to {new_boat}"]))

    return None  # If no solution found

# Call the BFS function to get the solution
solution = bfs()
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
