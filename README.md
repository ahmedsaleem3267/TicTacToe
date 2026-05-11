# Terminal Tic-Tac-Toe

A clean, modular, and fully functional Tic-Tac-Toe game built entirely in Python. Played right in the terminal, this project focuses on clean architecture, input validation, and a seamless user experience.

## Features
* **Modular Architecture:** Code is logically separated into distinct files (`main.py`, `board.py`, `game_logic.py`) for better readability and maintenance.
* **Smart Input Validation:** The game catches invalid inputs (letters, out-of-bounds numbers, and taken spots) without crashing.
* **Seamless UI:** Automatically clears the terminal screen between turns to create a static, locked-in game board.
* **Endless Play:** Features an outer game loop that asks players if they want to play again without restarting the script.

## Future Enhancements
* Add a Single-Player mode using the Minimax algorithm.
## Project Structure
* `main.py` - The game engine. Handles the main loops, user input, and turn switching.
* `board.py` - The visual engine. Handles storing the grid data, updating moves, and printing the UI.
* `game_logic.py` - The referee. Handles validating moves and checking for wins or draws.

## How to Play

### Prerequisites
You need Python 3 installed on your machine. 

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/ahmedsaleem3267/terminal-tic-tac-toe.git](https://github.com/YOUR-USERNAME/terminal-tic-tac-toe.git)