# initialising the grid
grid = [" "] * 9

# Function to print the 1D board
def print_board(board):
    # Loop from 0 to 8, jumping by 3 each time (0, 3, 6)
    for i in range(0, 9, 3):

        # Slice out 3 elements to create a row
        # When i=0, this grabs board[0:3]
        # When i=3, this grabs board[3:6], etc.
        row = board[i:i + 3]

        # Print the row with vertical dividers
        print(f" {row[0]} | {row[1]} | {row[2]} ")

        # Print a horizontal divider, but not after the last row
        if i < 6:
            print("---+---+---")

def is_board_filled(counter):
    if counter == len(grid):
        return True
    return False


def update_grid(place, current_player):
    grid[place-1] = current_player

if __name__ == "__main__":
    print("Test for the grid")
    print_board(grid)

def reset_grid():
    global grid
    grid = [" "] * 9