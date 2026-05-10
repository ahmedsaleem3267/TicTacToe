def is_it_valid(current_input, current_grid):

    if not current_input.isdigit():
        return False

    current_input = int(current_input)
    if not 0 < current_input < 10:
        return False

    if current_grid[current_input-1] != " ":
        return False

    return True

def check_win(symbol, grid):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # The 3 Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # The 3 Columns
        [0, 4, 8], [2, 4, 6]  # The 2 Diagonals
    ]

    # check if any combination has 3 in a row sequence
    for comb in win_combinations:
        if (grid[comb[0]] == symbol and
                grid[comb[1]] == symbol  and
                grid[comb[2]] == symbol):
            return True



