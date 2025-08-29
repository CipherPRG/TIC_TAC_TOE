Tic-Tac-Toe in Python
A classic command-line implementation of the Tic-Tac-Toe game, built with Python. This project serves as a practical application of fundamental programming principles, including function design, list manipulation, and game loop logic.

Features
Interactive Gameplay: A two-player game where users can input their moves directly in the console.

Input Validation: The program robustly handles user input, ensuring that moves are within the valid range (0-8) and that players cannot select a spot that is already taken.

Win/Draw Detection: The game automatically checks for win conditions and draw conditions after every move.

How It Works
The game is built around a few core functions that each handle a single responsibility:

printboard(board): Takes the current board state (a list of 9 strings) and displays it in a clean, readable 3x3 grid for the players.

inputboardx(board) & inputboardo(board): These functions manage a single turn for Player X and Player O, respectively. They are responsible for prompting the user for a move, validating that the chosen position is valid (within range and not already taken), and updating the board.

check_win(board): This is the game's logic engine. After every move, it checks the board for all possible win conditions (all three rows, all three columns, and both diagonals). It also checks if the board is full, resulting in a draw.

Main Game Loop: An external while loop controls the flow of the game. It repeatedly calls the player turn functions and checks the game's status until the check_win function reports that the game has ended.

How to Run It
Make sure you have Python 3 installed on your system.

Download the .py file from this repository.

Open your terminal or command prompt, navigate to the folder where you saved the file, and run the following command:

python your_file_name.py
