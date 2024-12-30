# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (draw)
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic Tac Toe!")
    display_board(board)

    while True:
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn.")
        try:
            row, col = map(int, input("Enter row and column (0-2, space-separated): ").split())
            if board[row][col] == " ":
                board[row][col] = current_player
                display_board(board)
                
                if check_winner(board, current_player):
                    print(f"Player {current_player} wins!")
                    break
                elif is_draw(board):
                    print("It's a draw!")
                    break
                turn += 1
            else:
                print("That cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers between 0 and 2.")

tic_tac_toe()
