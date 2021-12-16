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
        ship_row, ship_col = randint(0, 5), randint(0, 5)

        if board[ship_row][ship_col] != "O":
            board[ship_row][ship_col] = "O"
            ships += 1


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

    return row


def guess_col():
    """
    Player column guess
    """
    global col

    try:
        col = int(input("Please enter a column number:\n"))
        while col < 0 or col > 5:
            print("Oops, please choose a column between 0 and 5!")
            col = int(input("Please enter a column number:\n"))

    except ValueError:
        print("Please enter a valid number!")
        guess_col()

    return col


def guess_check():
    """
    Function to validate player guesses
    """
    row, col = guess_row(), guess_col()
    print(f"You chose the co-ordinates ({row}, {col})\n")

    if computer_board[row][col] == "#" or computer_board[row][col] == "X":
        print(f'''Oh {name}, you've already guessed those co-ordinates.
You've missed your turn!
        ''')
        return False

    elif hidden_computer_board[row][col] == "O":
        print("Congratulations, it's a direct hit!")
        computer_board[row][col] = "X"
        return True

    else:
        print("Sorry, you missed this time.\nPlease try again.")
        computer_board[row][col] = "#"
        return False


def computer_guess():
    """
    Function to generate random numbers for computer guess
    """
    guess_row, guess_col = randint(0, 5), randint(0, 5)
    return guess_row, guess_col


def computer_check():
    """
    Function to validate computer guess using recursion
    """
    row, col = computer_guess()

    if player_board[row][col] == "#" or player_board[row][col] == "X":
        return computer_check()

    elif player_board[row][col] == "O":
        print("\nComputer hit!\n")
        player_board[row][col] = "X"
        return True

    else:
        print("\nComputer missed!\n")
        player_board[row][col] = "#"
        return False


def start_game():
    """
    Start game function which calls the ship_placement function
    asks for name input, and calls welcome function
    """
    ship_placement(player_board)
    ship_placement(hidden_computer_board)
    print('''
__________.........__    __  .__               .__    .__ .............
\______   \_____ _/  |__/  |_|  |  ____   _____|  |__ |__|_____  ______
 |    |  _/\__  \\   __\   __\   |_/ __ \ /  ___/  |  \|  \____ \/  ___/
 |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   Y  \  |  |_> >___ \.
 |______  /(____  /__|  |__| |____/\___  >____  >___|  /__|   __/____  >
        \/      \/                     \/     \/     \/   |__|.......\/.
    ''')
    global name
    name = input("\n\nAhoy Matey!\n\nPlease enter your name to continue:\n\n")
    while len(name) == 0:
        name = input("Oops, you can't leave this section blank:\n\n")
    welcome(name)


def main():
    """
    This is the main function for starting the game
    """
    start_game()
    p_score = 0
    c_score = 0
    while p_score < 5 and c_score < 5:
        print(f"{name}'s score is {p_score}")
        print(f"Computer's score is {c_score}")
        print(f"\n\n{name}'s Board\n")
        print_board(player_board)
        print("\n\nComputer Board\n")
        print_board(computer_board)
        print("\n")
        print("Please choose co-ordinates between 0 and 5\n")

        if guess_check():
            p_score += 1

        if computer_check():
            c_score += 1
            
    if p_score == 5 and c_score == 5:
        print(f"\n\n{name}'s Board\n")
        print_board(player_board)
        print("\n\nComputer Board\n")
        print_board(computer_board)
        print("\n")
        print(f"{name}'s score is {p_score}")
        print(f"Computer's score is {c_score}")
        print("\nIt's a draw, how unlikely!\n")
        
    elif p_score == 5:
        print(f"\n\n{name}'s Board\n")
        print_board(player_board)
        print("\n\nComputer Board\n")
        print_board(computer_board)
        print("\n")
        print(f"{name}'s score is {p_score}")
        print(f"Computer's score is {c_score}")
        print(f"\nCongratulations {name}, you sunk all the battleships!\n")

    else:
        print(f"\n\n{name}'s Board\n")
        print_board(player_board)
        print("\n\nComputer Board\n")
        print_board(computer_board)
        print("\n")
        print(f"{name}'s score is {p_score}")
        print(f"Computer's score is {c_score}")
        print("\nOh no! The computer has won!\n")
    print("\nTHE END\n")


if __name__ == "__main__":
    main()
