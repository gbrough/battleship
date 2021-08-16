#initializing board
board = []
for x in range(1,9):
    board.append([" "] * 8)

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
}
def ship_column():
    ship_column = input("Enter the column of the ship A-H: ").upper()
    while ship_column not in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'):
        print("Not an appropriate choice.")
        ship_column = input("Enter the column of the ship A-H: ").upper()
    return letters_to_numbers[ship_column]

def ship_row():
    ship_row = input("Enter the row of the ship 1-8: ")
    while ship_row not in ('1', '2', '3', '4', '5', '6', '7', '8'):
        print("Not an appropriate choice.")
        ship_row = input("Enter the row of the ship 1-8: ")
    return int(ship_row) - 1

def guess_column(board):
    guess_column = input("Guess the column A-H: ").upper()
    while guess_column not in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'):
        print("Not an appropriate choice.")
        guess_column = input("Guess the column A-H: ").upper()
    return letters_to_numbers[guess_column]

def guess_row(board):
    guess_row = input("Guess the row 1-8: ")
    while guess_row not in ('1', '2', '3', '4', '5', '6', '7', '8'):
        print("Not an appropriate choice.")
        guess_row = input("Guess the row 1-8: ")
    return int(guess_row) - 1

def check_guess(board, ship_column, ship_row, guess_column, guess_row):
    if guess_row == ship_row and guess_column == ship_column:
        print("Congratulations! You sunk my battleship!")
        board[guess_row][guess_column] = "X"
        print_board(board)
        return True
    else:
        if board[guess_row][guess_column] == "X":
            print("You guessed that one already.")
            return False
        else:
            print("You missed my battleship!")
            board[guess_row][guess_column] = "-"
            print_board(board)
            return False
SHIP_COLUMN = ship_column()
SHIP_ROW = ship_row()
turns = 5
while turns > 0:
    print_board(board)
    print('You have ' + str(turns) + ' turns remaining.')
    GUESS_COLUMN = guess_column(board)
    GUESS_ROW = guess_row(board)
    check_guess(board, SHIP_COLUMN, SHIP_ROW, GUESS_COLUMN, GUESS_ROW)
    turns = turns - 1
    if turns == 0:
        print("Sorry, You ran out of turns. The game is over")

