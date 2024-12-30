# Define the Vacuum Cleaner Problem

class VacuumCleaner:
    def __init__(self, grid_size=(2, 2)):
        self.grid_size = grid_size
        self.position = (0, 0)  # Start at the top-left corner
        self.grid = [['Dirty' for _ in range(grid_size[1])] for _ in range(grid_size[0])]
        self.moves = []  # Store the sequence of actions taken

    def clean(self):
        x, y = self.position
        if self.grid[x][y] == 'Dirty':
            self.grid[x][y] = 'Clean'
            self.moves.append(f"Cleaned cell ({x}, {y})")
    
    def move(self, direction):
        x, y = self.position
        if direction == "Left" and y > 0:
            self.position = (x, y - 1)
            self.moves.append(f"Moved Left to ({x}, {y - 1})")
        elif direction == "Right" and y < self.grid_size[1] - 1:
            self.position = (x, y + 1)
            self.moves.append(f"Moved Right to ({x}, {y + 1})")
        elif direction == "Up" and x > 0:
            self.position = (x - 1, y)
            self.moves.append(f"Moved Up to ({x - 1}, {y})")
        elif direction == "Down" and x < self.grid_size[0] - 1:
            self.position = (x + 1, y)
            self.moves.append(f"Moved Down to ({x + 1}, {y})")

    def print_grid(self):
        for row in self.grid:
            print(" ".join(row))

    def is_clean(self):
        return all(cell == 'Clean' for row in self.grid for cell in row)

# Initialize the VacuumCleaner
vacuum = VacuumCleaner(grid_size=(2, 2))  # 2x2 grid

# Simple cleaning strategy: clean all cells
while not vacuum.is_clean():
    vacuum.clean()
    if vacuum.position == (0, 0):  # If at top-left, move Right
        vacuum.move("Right")
    elif vacuum.position == (0, 1):  # If at top-right, move Down
        vacuum.move("Down")
    elif vacuum.position == (1, 1):  # If at bottom-right, move Left
        vacuum.move("Left")
    elif vacuum.position == (1, 0):  # If at bottom-left, move Up
        vacuum.move("Up")

# Display the final state of the grid and moves
vacuum.print_grid()
print("\nMoves:")
for move in vacuum.moves:
    print(move)
