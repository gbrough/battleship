from random import randint
class Ship:
    def __init__(self, type, orientation, position_x, position_y):
        self.type = type
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def get_ship_type(self, type):
        type = {
            'Carrier': 5,
            'Battleship': 4,
            'Cruiser': 3,
            'Submarine': 3,
            'Destroyer': 2
        }
        return type[self.type]
    
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

#computer create 5 ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column, ship_orientation = randint(0,7), randint(0,7), randint(0,1)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

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

def get_ship_orientation():
    orientation = input("Enter the orientation of the ship (V or H): ").upper()
    if orientation == "V" or orientation == "H":
        return orientation
    else:
        while orientation != "V" and orientation != "H":
            orientation = input("Enter the orientation of the ship (V or H): ").upper()             

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

# check if orientation fits board
def check_orientation(ship_row, ship_column, orientation, board):
    if orientation == "horizontal":
        if ship_row + self.ShipObject.size < 8 and board[ship_row + 1][ship_column] == "X":
            return True
        else:
            return False
    elif orientation == "vertical":
        if ship_column + 1 < 8 and board[ship_row][ship_column + 1] == "X":
            return True
        else:
            return False

create_ships(HIDDEN_BOARD)
turns = 10
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
    if count_hit_ships(GUESS_BOARD) == 5:
        print("You win!")
        break
    print("You have " + str(turns) + " turns left")
    if turns == 0:
        print("You ran out of turns")