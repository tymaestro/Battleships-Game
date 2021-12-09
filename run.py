"""Import from random module to generate random numbers"""

from random import randint

Class Board:
    """
    Board initialization. Creates new board including size, number of ships
    and position of ships
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = type