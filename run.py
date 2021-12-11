"""
Import randint from random module
"""

from random import randint

"""
Create board
"""

board = [["-"] * 6 for x in range(6)]


def print_board(board):
    """
    print_board function prints board and adds a pipe
    between each hyphen for clarity
    """
    for row in board:
        print(" | ".join(row))