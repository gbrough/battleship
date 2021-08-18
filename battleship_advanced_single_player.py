

from random import randint
#create board function
def create_board():
    
#Board for holding computer ship locations
computer_board = []
for x in range(1,9):
    computer_board.append([" "] * 8)

# Board for holding player ships
player_board = []
for x in range(1,9):
    player_board.append([" "] * 8)

# Create guess board to show player misses and hits agains computer
player_guess_board = []
for x in range(1,9):
    player_guess_board.append([" "] * 8)

#create a guess board for computer to check for hits and misses
computer_guess_board = []
for x in range(1,9):
    computer_guess_board.append([" "] * 8)

def print_board():
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
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678" or ValueError:
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH" or ValueError:
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]


#computer create 5 ships
def computer_create_ships():
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while computer_board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        computer_board[ship_row][ship_column] = "X"
#player creates 5 ships
def player_create_ships():
    for ship in range(5):
        ship_row, ship_column = get_ship_location()
        while player_board[ship_row][ship_column] == "X":
            print("That location is already taken, choose another")
            ship_row, ship_column = get_ship_location()
        player_board[ship_row][ship_column] = "X"

#check if all ships are hit
def count_hit_ships():
    computer_count = 0
    for row in computer_board:
        for column in row:
            if column == "X":
                computer_count += 1
    player_count = 0
    for row in player_board:
        for column in row:
            if column == "X":
                player_count += 1
    return computer_count, player_count

computer_create_ships()
player_create_ships()
while True:
    #player turn
    while True:
        print('Guess a battleship location')
        print_board(computer_board)
        row, column = get_ship_location()
        if computer_board[row][column] == "-":
            print("You guessed that one already.")
        elif computer_board[row][column] == "X":
            print("Hit")
            computer_board[row][column] = "X"  
            break 
        else:
            computer_board[row][column] == ' '
            print("MISS!")
            computer_board[row][column] = "-" 
            break     
    #computer turn
    while True:
        row, column = randint(1,9), randint(1,9)
        if player_board[row][column] == "-":
            row, column = get_ship_location()
        elif player_board[row][column] == "X":
            row, column = randint(1,9), randint(1,9)
        else:
            player_board[row][column] = 'X'
            break
    if count_hit_ships()[0] == 5:
        print("Computer win!")
        break
    elif count_hit_ships()[1] == 5:
        print("Player win!")
        break
