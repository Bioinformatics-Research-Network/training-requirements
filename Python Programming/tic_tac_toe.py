# 1. Import Modules
import random  # Import random module to generate random moves for the computer
import time  # Import time module to add delays for better user experience
import logging  # Import logging module to provide warning messages

# 2. Configure Logging
logging.basicConfig(level=logging.WARNING, format='%(message)s')

# 3. Define Custom Exception
class ExitGame(Exception):
    pass

# 4. Function to Print the Board
def print_board(board):
    print("~~~~~~~~~~~~~~~~~~~~~~~")  # Print top border of the board
    print("   1   2   3 ")  # Print column indices

    for idx, row in enumerate(board):
        print(f"{idx + 1}  {' | '.join(row)} ")  # Print row index and the row contents separated by '|'
        if idx < 2:
            print("  ---+---+---")  # Print row separator except after the last row

    print("~~~~~~~~~~~~~~~~~~~~~~~")  # Print bottom border of the board

# 5. Function to Check for a Winner
def check_winner(board, player):
    # Check rows for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True  # Player wins
    
    # Check columns for a win
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True  # Player wins
    
    # Check diagonals for a win
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True  # Player wins
    
    return False  # No win detected

# 6. Function to Get Empty Positions
def get_empty_positions(board):
    empty_positions = []  # Initialize an empty list to store empty positions
    for i in range(3):  # Iterate over each row
        for j in range(3):  # Iterate over each column
            if board[i][j] == " ":  # If the spot is empty
                empty_positions.append((i, j))  # Add the position to the list
    return empty_positions  # Return the list of empty positions

# 7. Function to Handle User Input
def get_input(prompt):
    user_input = input(prompt)  # Get input from the user
    if user_input.lower() == "exit":  # If the input is 'exit'
        raise ExitGame("Exiting the game. Goodbye!")  # Raise the ExitGame exception to exit the game
    return user_input  # Return the user input

# 8. Function to Handle Player's Move
def player_move(board, player):
    while True:  # Loop until a valid move is made
        try:
            row = get_input("What row? ")  # Get row input from the player
            col = get_input("What column? ")  # Get column input from the player
            row, col = int(row) - 1, int(col) - 1  # Convert input to zero-indexed integers
            
            if row not in [0, 1, 2] or col not in [0, 1, 2]:  # Validate row and column
                logging.warning("Invalid selection. Choose 1, 2, or 3 for row and column.")  # Print error message for invalid selection
                continue  # Continue the loop to get valid input
            
            if board[row][col] != " ":  # Check if the spot is already taken
                logging.warning("Invalid move. The spot is already taken.")  # Print error message for taken spot
                continue  # Continue the loop to get a valid move
            
            confirmation = get_input(f"Place '{player}' at row {row + 1}, column {col + 1}? [y/n] ").lower()  # Ask for confirmation
            if confirmation == 'y':  # If the move is confirmed
                board[row][col] = player  # Place the player's move on the board
                print("Move placed!")  # Print success message
                return  # Exit the function after a valid move
            else:
                print("Move not placed. Choose again.")  # Print message if the move is not confirmed
        except ValueError:  # Handle invalid input that cannot be converted to integers
            logging.warning("Invalid input. Please enter numbers for row and column.")  # Print error message for invalid input

# 9. Function to Handle Computer's Move
def computer_move(board, player):
    empty_positions = get_empty_positions(board)  # Get a list of all empty positions
    move = random.choice(empty_positions)  # Randomly choose one of the empty positions
    board[move[0]][move[1]] = player  # Place the computer's move on the board
    print(f"Computer move registered.")  # Print success message

# 10. Function to Check for a Draw
def check_draw(board):
    if all([all([spot != " " for spot in row]) for row in board]):  # Check if all spots are filled
        return True  # The game is a draw
    return False  # The game is not a draw

# 11. Main Function to Run the Tic-Tac-Toe Game
def tic_tac_toe():
    try:
        while True:  # Loop to allow replaying the game
            # Initialize a 3x3 board with empty spaces
            board = [[" " for _ in range(3)] for _ in range(3)]  
            print("Welcome to Tic-Tac-Toe!")  # Welcome message
            
            # Get the player's choice of symbol (X or O)
            player = get_input("X or O? ").upper()  
            while player not in ["X", "O"]:  # Validate the player's choice
                player = get_input("Invalid response. Choose X or O ").upper()  # Ask again if the choice is invalid

            # Assign the opposite symbol to the computer
            computer = "O" if player == "X" else "X"  
            
            # X always starts the game
            current_player = "X"  

            # Game loop for a maximum of 9 rounds (the board has 9 spots)
            for round_number in range(1, 10):  
                print("\n#######################")
                print(f"##### Round #{round_number} #####")  # Print the current round number
                print("#######################\n")
                print("Current board:")  # Print the current state of the board
                print_board(board)  # Call the function to print the board
                
                if current_player == player:  # Check if it's the player's turn
                    print(f"\nPlayer '{player}' turn:")  # Print the player's turn message
                    time.sleep(2)  # Add a 2-second delay for the player's turn
                    player_move(board, player)  # Call the function for the player's move
                else:
                    print(f"\nPlayer '{computer}' turn:")  # Print the computer's turn message
                    time.sleep(5)  # Add a 5-second delay for the computer's turn
                    computer_move(board, computer)  # Call the function for the computer's move
                
                print("Current board:")  # Print the current state of the board again
                print_board(board)  # Call the function to print the board

                if check_winner(board, current_player):  # Check if the current player has won
                    print_board(board)  # Print the final state of the board
                    if current_player == player:  # Check if the player has won
                        print(f"Player has won with {player}!")  # Print the player's win message
                    else:
                        print(f"Computer has won with {computer}!")  # Print the computer's win message
                    return  # Exit the game loop and end the game

                if check_draw(board):  # Check if the game is a draw
                    print_board(board)  # Print the final state of the board
                    print("It's a tie!")  # Print the tie message
                    return  # Exit the game loop and end the game

                # Switch turns
                current_player = computer if current_player == player else player  

    except ExitGame as e:  # Catch the custom exit game exception
        print(e)  # Print the exit message

# 12. Execute the Game
if __name__ == "__main__":
    tic_tac_toe()  # Call the main function to start the game
