import random
from random import randint

LENGTH_OF_SHIPS = [2,3,3,4,5]  
PLAYER_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]

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
def ship_overlaps(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False

#place Ships
def place_computer_ships(board):
    #loop through length of ships
    for ship_length in LENGTH_OF_SHIPS:
        #loop until ship fits and doesn't overlap
        while True:
            orientation = random.choice(["H", "V"])
            row = randint(0, 7)
            column = randint(0, 7)
            if check_ship_fit(ship_length, row, column, orientation):
                #check if ship overlaps
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        #place ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break

def place_user_ships(board):
    #loop through length of ships
    for ship_length in LENGTH_OF_SHIPS:
        print_board(PLAYER_BOARD)
        print('Place the ship with a length of ' + str(ship_length))
        #loop until ship fits and doesn't overlap
        while True:
            row = input("Enter the row 1-8 of the ship: ")
            column = input('Enter column of ship: ').upper()
            orientation = input("Enter orientation (H or V): ").upper()
            if check_ship_fit(ship_length, int(row), letters_to_numbers[column], orientation):
                #check if ship overlaps
                    if ship_overlaps(board, int(row), letters_to_numbers[column], orientation, ship_length) == False:
                        #place ship
                        if orientation == "H":
                            for i in range(letters_to_numbers[column], letters_to_numbers[column] + ship_length):
                                board[int(row)][i] = "X"
                        else:
                            for i in range(int(row), int(row) + ship_length):
                                board[i][letters_to_numbers[column]] = "X"
                        break    

def user_ship_input(row, column, orientation):
    while True:
        try: 
            orientation = input("Enter orientation (H or V): ").upper()
            if orientation == "H" or orientation == "V":
                break
        except TypeError:
            print('Enter a valid orientation H or V')
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
    return row, column, orientation 

def user_input_guess():
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

place_computer_ships(COMPUTER_BOARD)
place_user_ships(PLAYER_BOARD)
print(COMPUTER_BOARD)
print(PLAYER_BOARD)
        
while True:
    #player turn
    while True:
        print('Guess a battleship location')
        print_board(PLAYER_GUESS_BOARD)
        row, column = user_input_guess()
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
    if count_hit_ships(PLAYER_GUESS_BOARD) == 17:
        print("You win!")
        break   
    #computer turn
    while True:
        row, column = randint(0,7), randint(0,7)
        while COMPUTER_GUESS_BOARD[row][column] == "-":
            row, column = randint(0,7), randint(0,7)
        if PLAYER_BOARD[row][column] == "X":
            COMPUTER_GUESS_BOARD[row][column] = "X"
            break
        else:
            COMPUTER_GUESS_BOARD[row][column] = '-'
            print_board(COMPUTER_GUESS_BOARD)
            break
    if count_hit_ships(COMPUTER_GUESS_BOARD) == 17:
        print("Sorry, the computer won.")
        break