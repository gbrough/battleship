from random import randint

#Board for holding ship locations
board = []
for x in range(1,9):
    board.append([" "] * 8)

# Board for displaying hits and misses
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
    try:
        row = input("Enter the row of the ship: ").upper()
        while row not in "12345678":
            print('Not an appropriate choice, please select a valid row')
            row = input("Enter the row of the ship: ").upper()
        column = input("Enter the column of the ship: ").upper()
        while column not in "ABCDEFGH":
            print('Not an appropriate choice, please select a valid column')
            column = input("Enter the column of the ship: ").upper()
        return int(row) - 1, letters_to_numbers[column]
    except (ValueError, KeyError, IndexError, TypeError):
        print("Not an appropriate choice, please select a valid row and column")
        return get_ship_location()

#computer create 5 ships
def create_ships():
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

#check if all ships are hit
def count_hit_ships():
    count = 0
    for row in guess_board:
        for column in row:
            if column == "X":
                count += 1
    return count

create_ships()
turns = 10
while turns > 0:
    print('Guess a battleship location')
    print_board(guess_board)
    row, column = get_ship_location()
    if guess_board[row][column] == "-":
        print("You guessed that one already.")
    elif board[row][column] == "X":
        print("Hit")
        guess_board[row][column] = "X"   
    else:
        guess_board[row][column] == ' '
        print("MISS!")
        guess_board[row][column] = "-"   
        turns -= 1     
    if count_hit_ships() == 5:
        print("You win!")
        break
    print("You have " + str(turns) + " turns left")
    if turns == 0:
        print("You ran out of turns")
