"""
Import randint from random module
"""

from random import randint

"""
Create board
"""

board = [["-" for x in range(6)] for y in range(6)]


def print_board(board):
    """
    print_board function prints board and adds a pipe
    between each hyphen for clarity
    """
    for row in board:
        print(" | ".join(row))


# Collecting user input for name and printing opening message and board


name = input("Ahoy Matey!\nPlease enter your name to continue:\n")
print(f"Welcome to Battleships {name}!")
print("Please choose co-ordinates between 0 and 5")
print_board(board)