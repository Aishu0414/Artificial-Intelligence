# Function to evaluate the game state
def evaluate(state):
    """
    Evaluate the game state:
    - Return True if the game is over (state == 0).
    - Otherwise, return False.
    """
    return state == 0

# Function to generate all possible moves
def generate_moves(state):
    """
    Generate possible moves by removing 1, 2, or 3 stones from the pile.
    """
    moves = []
    for i in range(1, 4):
        if state - i >= 0:
            moves.append(i)
    return moves

# AI's turn: Greedy strategy
def ai_move(state):
    """
    AI's strategy to make the move:
    - Tries to leave the opponent with a number of stones where no winning move is possible.
    """
    # The greedy strategy: Try to remove enough stones to leave the opponent with a losing position
    for move in generate_moves(state):
        if (state - move) % 4 == 0:
            return move
    
    # If no optimal move is found, just remove a random valid number (1, 2, or 3 stones)
    return 1  # As a simple fallback, AI removes 1 stone

# Main game loop
def main():
    # Initialize the game with the number of stones
    state = int(input("Enter the number of stones in the pile: "))
    
    # Turn-based gameplay: AI vs Human
    while state > 0:
        # AI's turn
        print(f"\nCurrent pile size: {state}")
        print("AI is thinking...")
        ai_move_stones = ai_move(state)
        print(f"AI removes {ai_move_stones} stones.")
        state -= ai_move_stones
        
        # Check if the AI wins
        if evaluate(state):
            print("AI wins!")
            break
        
        # Human's turn
        print(f"\nCurrent pile size: {state}")
        move = int(input("Your turn! Enter the number of stones to remove (1, 2, or 3): "))
        
        if move not in [1, 2, 3] or move > state:
            print("Invalid move. Please enter a valid number of stones to remove.")
            continue
        
        # Apply the human's move
        state -= move
        
        # Check if the human wins
        if evaluate(state):
            print("You win!")
            break

# Run the game
main()
