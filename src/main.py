import board
import game_logic

counter = 1

# random player start --> yet to add
current_player = "X"

game_is_running = True

while game_is_running:
    # print grid
    board.print_board(board.grid)

    # Ask for input from current_player
    place = input(f"Player {current_player}, choose spot to play (1-9)")

    if game_logic.is_it_valid(place, board.grid):
        place = int(place)
        board.update_grid(place, current_player)

        #check if current player wins
        if game_logic.check_win(current_player, board.grid):
            # clears the screen
            game_logic.clear_screen()

            #print the board
            board.print_board(board.grid)

            print(f"\nPlayer {current_player} wins")

            if game_logic.restart_game():
                counter = 1
                continue
            else:   break



        # check if board is all filled
        if board.is_board_filled(counter):
            game_logic.clear_screen()
            print("\nDraw")
            if game_logic.restart_game():
                counter = 1
                continue
            else:
                break

        # Changing turns
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

        counter += 1

        # clears the screen
        game_logic.clear_screen()
    else:
        # clears the screen
        game_logic.clear_screen()
        print("Invalid Input\n")


