#Board for holding ship locations
board = []
for x in range(1,9):
    board.append([" "] * 8)

# Board for displaying hit/miss
guess_board = []
for x in range(1,9):
    guess_board.append([" "] * 8)

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number = row_number + 1

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}
def get_ship_location():
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    row = input("Enter the row of the ship: ").upper()
    while row not in "123456789":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

#Create 5 battleships
def create_battleships():
    ships = 5
    print_board(board)
    while ships > 0:
        row, column = get_ship_location()
        if board[row][column] == "X":
            print("You already have a ship there, try again")
            continue
        else:
            board[row][column] = "X"
            ships -= 1
            print_board(board)
            print('You have ' + str(ships) + ' ships left')

create_battleships()
turns = 5
while turns > 0:
    print('Guess a battleship location')
    print_board(guess_board)
    row, column = get_ship_location()
    print_board(guess_board)
    if guess_board[row][column] == "-":
        print("You guessed that one already.")
    elif guess_board[row][column] == ' ':
        print("MISS!")
        guess_board[row][column] = "-"
    else:
        board[row][column] = "X"
        print("Hit")
        guess_board[row][column] = "X"
    turns -= 1
    if turns == 0:
        print("You ran out of turns")

    











