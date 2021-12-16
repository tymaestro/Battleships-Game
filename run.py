""" Import randint from random module """

from random import randint


def create_board():
    """
    Create board
    """
    board = [["-" for x in range(6)] for y in range(6)]
    return board


player_board = create_board()
computer_board = create_board()
hidden_computer_board = create_board()


def print_board(board):
    """
    print_board function prints board and adds a pipe
    between each hyphen for clarity
    """
    for row in board:
        print(" | ".join(row))


def welcome(player):
    """
    welcome message for players
    """
    print("-" * 35)
    print(f"Welcome to Battleships {player}!")
    print("-" * 35)


def ship_placement(board):
    """
    Generate random ship locations
    """
    ships = 0
    while ships < 5:
        ship_row, ship_column = randint(0, 5), randint(0, 5)

        if board[ship_row][ship_column] != "X":
            board[ship_row][ship_column] = "X"
            ships = ships+1


def guess_col():
    """
    Player column guess
    """
    global column

    try:
        column = int(input("Please enter a column number:\n"))
        while column < 0 or column > 5:
            print("Oops, please choose a column between 0 and 5!")
            column = int(input("Please enter a column number:\n"))

    except ValueError:
        print("Please enter a valid number!")
        guess_col()

    return column


def guess_row():
    """
    Player row guess
    """
    global row

    try:
        row = int(input("Please enter a row number:\n"))
        while row < 0 or row > 5:
            print("Oops, please choose a row between 0 and 5!")
            row = int(input("Please enter a row number:\n"))

    except ValueError:
        print("Please enter a valid number!")
        guess_row()

    col = guess_col()

    print(f"You chose the co-ordinates ({row}, {column})")
    return row, col


def guess_check():
    """
    Function to validate player guesses
    """
    row, column = guess_row()

    if computer_board[row][column] == "#":
        print("Oops, you've already guessed those co-ordinates!")

    elif hidden_computer_board[row][column] == "X":
        print("Congratulations, it's a direct hit!")
        computer_board[row][column] = "X"

    else:
        print("Sorry, you missed this time.\nPlease try again.")
        computer_board[row][column] = "#"


def computer_guess():
    """
    Function to generate random numbers for computer guess
    """
    guess_row, guess_column = randint(0, 5), randint(0, 5)
    return guess_row, guess_column


def computer_check():
    """
    Function to validate player guesses
    """
    row, column = computer_guess()

    if player_board[row][column] == "#":
        computer_guess()

    elif player_board[row][column] == "X":
        print("Computer hit!")
        # computer_board[row][column] = "X"

    else:
        print("Computer missed!")
        player_board[row][column] = "#"


# def increment_score(board):
#     """
#     Function to increment the score by 1 each time a ship is hit
#     """
#     player_score = 0
#     computer_score = 0
#     for row in board:
#         for column in row:
#             if column == "X":
#                 player_score += 1
#                 computer_score += 1
#     print(f"You've hit {player_score} out of 5 battleships")
#     print(f"Computer has hit {computer_score} battleships")
#     return player_score, computer_score


def start_game():
    """
    Start game function which calls the ship_placement function
    asks for name input, and calls welcome function
    """
    ship_placement(player_board)
    ship_placement(hidden_computer_board)
    print('''
__________.........__    __  .__                .__    .__ .............
\______   \_____ _/  |__/  |_|  |  ____   _____|  |__ |__|_____  ______
 |    |  _/\__  \\   __\   __\   |_/ __ \ /  ___/  |  \|  \____ \/  ___/
 |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   Y  \  |  |_> >___ \.
 |______  /(____  /__|  |__| |____/\___  >____  >___|  /__|   __/____  >
        \/      \/                     \/     \/     \/   |__|.......\/.
    ''')
    name = input("\n\nAhoy Matey!\n\nPlease enter your name to continue:\n")
    while len(name) == 0:
        name = input("\n\nOops, you can't leave this section blank:\n")
    welcome(name)


def main():
    """
    This is the main function for starting the game
    """
    start_game()
    score = 5
    while score < 6:
        print("Please choose co-ordinates between 0 and 5")
        print("\n\nPlayer Board\n")
        print_board(player_board)
        print("\n\nComputer Board\n")
        print_board(computer_board)
        print("\n")

        guess_check()
        computer_check()

        # if increment_score(computer_board) == 5:
        #     print("Congratulations! You sunk all the Battleships!")
        #     break
        # elif increment_score(player_board) == 5:
        #     print("Computer wins!")
        #     break


if __name__ == "__main__":
    main()
