"""Import from random module to generate random numbers"""

from random import randint

# scores = {"computer": 0, "player": 0}

class Board:
    """
    Board initialization. Creates new board including size, number of ships
    and position of ships
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = type

size = 8
num_ships = 5

print(size)
print(num_ships)

# board = []

# def create_board(board):
#     for x in range(8)

# def new_game():
#     print("Ahoy Matey! Welcome to Battleships!")
#     size = 8
#     num_ships = 5
#     scores["computer"] = 0
#     scores["player"] = 0
#     player_name = input("Please enter your name")
#     print(new_game())


# new_game()
