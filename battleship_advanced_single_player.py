from random import randint

PLAYER_BOARD = [[" "] * 8 for i in range(1,9)]
COMPUTER_BOARD = [[" "] * 8 for i in range(1,9)]
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(1,9)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(1,9)]

def print_board(board): 
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

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
    row = input("Enter the row of the ship: ")
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ")
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

#computer create 5 ships
def computer_create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"
#player creates 5 ships
def player_create_ships(board):
    for ship in range(5):
        print_board(board)
        ship_row, ship_column = get_ship_location()
        while board[ship_row][ship_column] == "X":
            print("That location is already taken, choose another")
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

computer_create_ships(COMPUTER_BOARD)
print_board(COMPUTER_BOARD)
#player_create_ships(PLAYER_BOARD)
while True:
    #player turn
    while True:
        print('Guess a battleship location')
        print_board(PLAYER_GUESS_BOARD)
        row, column = get_ship_location()
        if PLAYER_GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif COMPUTER_BOARD[row][column] == "X":
            print("Hit")
            PLAYER_GUESS_BOARD[row][column] = "X"  
            break 
        else:
            print("MISS!")
            PLAYER_GUESS_BOARD[row][column] = "-" 
            break  
    if count_hit_ships(PLAYER_GUESS_BOARD) == 5:
        print("You win!")
        break   
    #computer turn
    while True:
        print_board(COMPUTER_GUESS_BOARD)
        row, column = randint(1,9), randint(1,9)
        if COMPUTER_GUESS_BOARD[row][column] == '-':
            row, column = randint(1,9), randint(1,9)
        elif PLAYER_BOARD[row][column] == "X":
            COMPUTER_GUESS_BOARD[row][column] = "X"
            break
        else:
            COMPUTER_GUESS_BOARD[row][column] = '-'
            break
    if count_hit_ships(COMPUTER_GUESS_BOARD) == 5:
        print("Sorry, the computer won.")
        break

