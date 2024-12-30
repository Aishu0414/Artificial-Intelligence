import itertools

# Define the cryptarithmetic equation: SEND + MORE = MONEY
def is_valid_solution(perm):
    S, E, N, D, M, O, R, Y = perm
    
    # Ensure the digits of 'SEND' and 'MORE' do not start with 0 (no leading zeros)
    if S == 0 or M == 0:
        return False
    
    # Convert the letters to digits
    send = 1000 * S + 100 * E + 10 * N + D
    more = 1000 * M + 100 * O + 10 * R + E
    money = 10000 * M + 1000 * O + 100 * N + 10 * E + Y
    
    # Check if the equation SEND + MORE = MONEY holds
    return send + more == money

# Generate all permutations of digits 0-9 for the letters S, E, N, D, M, O, R, Y
digits = list(range(10))
letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

# Try all permutations of the digits for the letters
for perm in itertools.permutations(digits, len(letters)):
    if is_valid_solution(perm):
        solution = dict(zip(letters, perm))
        print("Solution found!")
        for letter, digit in solution.items():
            print(f"{letter}: {digit}")
        break
else:
    print("No solution found.")
