import heapq
from copy import deepcopy

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def manhattan_distance(state, goal):
    return sum(abs(i - x) + abs(j - y) for i, row in enumerate(state) for j, val in enumerate(row) if val != 0 for x, y in [(divmod(goal.index(val), 3))])

def get_neighbors(state):
    moves = []
    x, y = find_blank(state)
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if is_valid(x + dx, y + dy):
            new_state = deepcopy(state)
            new_state[x][y], new_state[x + dx][y + dy] = new_state[x + dx][y + dy], new_state[x][y]
            moves.append(new_state)
    return moves

def solve_puzzle(start, goal):
    goal_flat = [n for row in goal for n in row]
    pq, visited = [(0, start, [])], {tuple(map(tuple, start))}
    while pq:
        cost, current, path = heapq.heappop(pq)
        if current == goal:
            return path + [current]
        for neighbor in get_neighbors(current):
            if (neighbor_tuple := tuple(map(tuple, neighbor))) not in visited:
                visited.add(neighbor_tuple)
                heapq.heappush(pq, (len(path) + 1 + manhattan_distance(neighbor, goal_flat), neighbor, path + [current]))
    return None

if __name__ == "__main__":
    start_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    solution = solve_puzzle(start_state, goal_state)
    if solution:
        print(f"Solution found in {len(solution) - 1} steps:")
        for step in solution:
            print('\n'.join(map(str, step)), "\n")
    else:
        print("No solution found!")
