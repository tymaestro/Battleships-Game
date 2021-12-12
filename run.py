"""
Import randint from random module
"""

from random import randint

"""
Create board
"""

def create_board():
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


# Collecting user input for name and printing opening message and board

def welcome(player):
    """
    welcome message for players
    """
    print(f"Welcome to Battleships {player}!")


def main():
    name = input("Ahoy Matey!\nPlease enter your name to continue:\n")
    welcome(name)
    print("Please choose co-ordinates between 0 and 5")
    print("\n\nPlayer Board\n")
    print_board(player_board)
    print("\n\nComputer Board\n")
    print_board(computer_board)
    print(player_guesses(player_board))


# generate random ship locations

def ship_location(board):
    """
    Generate random ship locations
    """
    for ship in range(6):
        ship_row, ship_column = randint(0, 5), randint(0, 5)
        board[ship_row][ship_column] = "X"

# player guesses

def player_guesses(player_board):
    """
    Player guesses
    """
    try:
        row = int(input("Please choose a row: "))
        if row < 0 or row > 6:
            row = int(input("Oops, please choose a row between 1 and 5! "))
    except Exception:
        print("Please enter a valid number")
        row = int(input("Please choose a row: "))
    column = input("Please choose a column: ")
    print(f"You chose the co-ordinates ({row}, {column})")


if __name__ == "__main__":
    main()