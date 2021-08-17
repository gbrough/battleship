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
    return letters_to_numbers[column], int(row) - 1

#Create 5 battleships
def create_battleships():
    print_board(board)
    for i in range(5):
        
        print('Where do you want your ' + str(i+1) + ' battleship?')
        column, row = get_ship_location()
        if board[column][row] == "X":
            print("That ship already exists")   
        else:
            board[column][row] = "X"
        print_board(board)
        
turns = 5
while turns > 0:
    create_battleships()
    print('Guess a battleship location')
    column, row = get_ship_location()
    print_board(guess_board)
    if guess_board[column][row] == "-":
        print("You guessed that one already.")
        continue
    elif guess_board[column][row] == ' ':
        print("MISS!")
        guess_board[column][row] = "-"
    else:
        board[column][row] = "X"
        print("Hit")
        guess_board[column][row] = "X"
    turns -= 1
    if turns == 0:
        print("You ran out of turns")

    











