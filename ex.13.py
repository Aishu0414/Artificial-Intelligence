import math

# Evaluate function
def evaluate(state):
    """
    Evaluate the state of the game:
    - Return 1 if the maximizing player wins.
    - Return -1 if the minimizing player wins.
    - Return 0 if the game is a draw.
    - Return None if the game is not in a terminal state.
    """
    if sum(state) == 0:  # Terminal state: all numbers removed
        return 1 if sum(state) % 2 == 0 else -1
    return None  # Not a terminal state

# Generate moves function
def generate_moves(state, is_maximizing):
    """
    Generate all possible moves (next states) from the current state.
    - A move consists of removing one number (setting it to 0).
    """
    moves = []
    for i in range(len(state)):
        if state[i] != 0:  # If the number is not already removed
            new_state = state[:]
            new_state[i] = 0  # Simulate taking this number
            moves.append(new_state)
    return moves

# Minimax algorithm
def minimax(state, depth, is_maximizing, evaluate, generate_moves):
    """
    General Minimax algorithm for games.
    - state: The current game state (e.g., list of numbers).
    - depth: Current depth of the search tree.
    - is_maximizing: True if the current player is the maximizing player.
    - evaluate: A function to evaluate the score of the current state.
    - generate_moves: A function to generate all possible moves from the current state.
    """
    result = evaluate(state)
    if result is not None:  # If terminal state
        return result

    if is_maximizing:
        best_score = -math.inf
        for move in generate_moves(state, is_maximizing):
            score = minimax(move, depth + 1, False, evaluate, generate_moves)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in generate_moves(state, is_maximizing):
            score = minimax(move, depth + 1, True, evaluate, generate_moves)
            best_score = min(best_score, score)
        return best_score

# Main function to test the code
def main():
    # Input the initial state
    initial_state = list(map(int, input("Enter the initial state as space-separated numbers: ").split()))
    
    # Calculate the best score for the maximizing player
    best_score = minimax(initial_state, 0, True, evaluate, generate_moves)
    
    # Output the result
    print("Best score for the maximizing player:", best_score)

# Run the program
main()
