# Import randint from random module

from random import randint


def create_board():
    """
    Create board
    """
    board = [["-" for x in range(6)] for y in range(6)]
    return board


player_board = create_board()
computer_board = create_board()


def print_board(board):
    """
    print_board function prints board and adds a pipe
    between each hyphen for clarity
    """
    for row in board:
        print(" | ".join(row))


# Collecting user input for name and printing opening message

def welcome(player):
    """
    welcome message for players
    """
    print(f"Welcome to Battleships {player}!")


# generate random ship locations

def ship_placement(board):
    """
    Generate random ship locations
    """
    for ship in range(6):
        ship_row, ship_column = randint(0, 5), randint(0, 5)
        board[ship_row][ship_column] = "X"

# Player guesses


def player_guess():
    """
    Player guesses
    """
    # try:
    row = int(input("Please enter a row number: "))
    while row < 0 or row > 5:
        print("Oops, please choose a row between 0 and 5!")
        row = int(input("Please enter a row number: "))
    column = int(input("Please enter a column number: "))
    while column < 0 or column > 5:
        print("Oops, please choose a column between 0 and 5!")
        column = int(input("Please enter a column number: "))
    # except ValueError:
    #     print("Please enter a valid number!")
    #     row = int(input("Please enter a row number: "))
    print(f"You chose the co-ordinates ({row}, {column})")
    return int(row), int(column)


def guess_check():
    row, column = player_guess()
    if computer_board[row][column] == "#":
        print("Oops, you've already guessed those co-ordinates!")
    elif player_board[row][column] == "X":
        print("Congratulations, it's a direct hit!")
        computer_board[row][column] = "X"
    else:
        print("Sorry, you missed this time.\nPlease try again.")
        computer_board[row][column] = "#"


# Main start function for the game


def start_game():
    ship_placement(player_board)
    name = input("Ahoy Matey!\nPlease enter your name to continue: ")
    welcome(name)


def main():
    """
    This is the main function for starting the game
    """
    start_game()
    print("Please choose co-ordinates between 0 and 5")
    print("\n\nPlayer Board\n")
    print_board(player_board)
    print("\n\nComputer Board\n")
    print_board(computer_board)
    print("\n")
    guess_check()


if __name__ == "__main__":
    main()