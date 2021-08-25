import random
from random import randint

LENGTH_OF_SHIPS = [2,3,3,4,5]  
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
GUESS_BOARD = [[" "] * 8 for i in range(8)]

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

#check if ship fits in board
def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else:
            return True

#check each position for overlap
def ship_overlaps(board, row, column, orientation):
    if orientation == "H":
        for i in range(column, column + LENGTH_OF_SHIPS[0]):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + LENGTH_OF_SHIPS[0]):
            if board[i][column] == "X":
                return True
    return False

#place Ships
def place_ships(board):
    #loop through length of ships
    for ship_length in LENGTH_OF_SHIPS:
        #loop until ship fits
        while True:
            row, column = 0, random.randint(0,7)
            orientation = random.choice(["H", "V"])
            if check_ship_fit(ship_length, row, column, orientation):
                #check if ship overlaps
                    if ship_overlaps(board, row, column, orientation) == False:
                        #place ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break

def get_ship_location():
    while True:
        try: 
            row = input("Enter the row 1-8 of the ship: ")
            if row in '12345678':
                row = int(row) - 1
                break
        except ValueError:
            print('Enter a valid letter between 1-8')
    while True:
        try: 
            column = input("Enter the column of the ship: ").upper()
            if column in 'ABCDEFGH':
                column = letters_to_numbers[column]
                break
        except KeyError:
            print('Enter a valid letter between A-H')
    return row, column          

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

place_ships(HIDDEN_BOARD)
print_board(HIDDEN_BOARD)
turns = 100
while turns > 0:
    print('Guess a battleship location')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == "-":
        print("You guessed that one already.")
    elif HIDDEN_BOARD[row][column] == "X":
        print("Hit")
        GUESS_BOARD[row][column] = "X" 
        turns -= 1  
    else:
        print("MISS!")
        GUESS_BOARD[row][column] = "-"   
        turns -= 1     
    if count_hit_ships(GUESS_BOARD) == 17:
        print("You win!")
        break
    print("You have " + str(turns) + " turns left")
    if turns == 0:
        print("You ran out of turns")