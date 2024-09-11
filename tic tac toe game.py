import os
import time

#constants for the players
player_X = 'X'
player_O = 'O'
EMPTY = ' '

# function to initialize the board
def initialize_board():
    ''' Initialize the board to start the game '''
    return [EMPTY] * 9
        # creates a list of 9 empty spaces

# function to display the board with a border around it
def display_board(board):
    '''Displays the Tic-Tac-Toe board.'''
    
    # visual representation of the board 
    print("\n" + "="*21)
    print(" Naughts and Crosses ")
    print("="*21 + "\n")
    
    for i in range(0, 9, 3):
        # print the rows of the board
        print("|", end="")
        
        for j in range(3):
            # print each cell in the row
            print(f" {board[i + j]} |", end="")
            
        if i < 6:
            # print row separators
            print("\n|---|---|---|")
    print()
    print("\n" + "="*21 + "\n")

# function to check for winner
def check_winner(board):
    '''check for a winner or draw'''
    '''check with all possible winning combinations'''

    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
        (0, 4, 8), (2, 4, 6)              # diagonal
    ]
    
    for a, b, c in winning_combinations:
        # check if any winning combination is met
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]  # return the winner ('X' or 'O')
        
    if EMPTY not in board:
        return 'Draw'  # if no empty spaces, it's a draw
    
    return None  # no winner and game is not a draw

# function to play a single game
def play_game():
    '''to play a single game of Tic-Tac-Toe '''
    
    board = initialize_board()  # start with an empty board
    current_player = player_X  # Player X always starts
    winner = None  # initialize winner variable

    while winner is None:
        display_board(board)  # show the current state of the board
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != EMPTY:
                # Invalid move if the space is not empty
                print("Invalid move. Try again.")
                continue
        except (ValueError, IndexError):
            
            '''ValueError - used to check if user input something that cannot be converted to an integer'''
            '''IndexError - used to check if a number is valid board position'''
            
            # Catch invalid input
            print("Invalid input. Enter a number between 1 and 9.")
            continue

        board[move] = current_player  # Place the player's move on the board
        winner = check_winner(board)  # Check if there's a winner or a draw
        current_player = player_O if current_player == player_X else player_X  # Switch player

        time.sleep(2)  # Adding a bit of suspense

    display_board(board)  # final display of the board
    if winner == 'Draw':
        print("It's a draw!")  # announce draw
    else:
        print(f"Player {winner} wins!")  # announce the winner
    return winner  # return the result

# function to save game result
def save_game_result(result):
    '''saves the result of the game to a text file'''
    
    with open("game_history.txt", "a") as file:
        file.write(result + "\n")  # Append the result to the history file

# function to read game history from file
def read_game_history():
    '''reads and returns the game history from a text file'''
    
    if not os.path.exists("game_history.txt"):
        return []  # Return empty list if no history file exists
    
    with open("game_history.txt", "r") as file: # read file content
        return file.readlines()  # Return the list of results

# function to display game history
def display_game_history():
    '''Displays the game history'''
    
    history = read_game_history()  # get the game history
    
    # count the number of wins for each player and draws
    x_wins = history.count(player_X + "\n")
    o_wins = history.count(player_O + "\n")
    draws = history.count("Draw\n")
    
    # display the counts
    print(f" Player X wins: {x_wins}")
    print(f" Player O wins: {o_wins}")
    print(f" Draws        : {draws}")

# function to generate HTML report of the game history
def generate_html_report():
    ''' Generates an HTML report of the game history '''
    
    history = read_game_history()  # Get the game history
    
    # Count the number of wins for each player and draws
    x_wins = history.count(player_X + "\n")
    o_wins = history.count(player_O + "\n")
    draws = history.count("Draw\n")

    # Create the HTML content with the counts
    html_content = f"""
    <html>
    <head>
        <title>Naughts and Crosses Game History</title>
    </head>
    <body>
        <h1>Naughts and Crosses Game History</h1>
        <p>Player X wins: {x_wins}</p>
        <p>Player O wins: {o_wins}</p>
        <p>Draws: {draws}</p>
    </body>
    </html>
    """

    with open("game_history.html", "w") as file:
        file.write(html_content)  # Write the HTML content to a file

    print("HTML report generated successfully.")  # confirm report generation

# main menu function
def main_menu():
    ''' Displays the main menu and handles user input.'''
    
    while True:
        # Display the menu options
        print("- - - Welcome to Naughts and Crosses! - - -")
        print("1. Play Game")
        print("2. View Game History")
        print("3. Generate HTML Report")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            result = play_game()  # Play a game
            save_game_result(result)  # Save the result
        elif choice == "2":
            display_game_history()  # Display the game history
        elif choice == "3":
            generate_html_report()  # Generate an HTML report
        elif choice == "4":
            print("- - - Thank you for playing Naughts and Crosses! - - -")  # Exit message
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")  # Invalid choice message
    
# Run the main menu
if __name__ == "__main__":
    main_menu()  # Start the main menu
    


        
    

       
