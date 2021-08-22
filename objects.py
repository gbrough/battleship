#         ------ LEGEND ------
#
# (X) for placing a ship and hit battleship
# (' ') for available space
# (-) for missed shot


from random import randint
from os import system
from configparser import ConfigParser
from time import sleep


# vars
fullscreen = None


parser = ConfigParser()
parser.read('settings.cfg')

if parser.get('general', 'fullscreen') in ['False', 'false']:
    system('mode con: cols=40 lines=12')
    fullscreen = False


HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def print_board(board):
    print('  A B C D E F G H')
    print('  ----------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'

def get_ship_location():
    row = input('Please enter a ship row 1-8: ')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-8: ').upper()
    column = input('Please enter a ship column A-H: ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-H: ').upper()
    return int(row) - 1, letters_to_numbers[column]

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in board:
            if column == 'X':
                count += 1
    return count

create_ships(HIDDEN_BOARD)
turns = int(parser.get('general', 'turns'))

if parser.get('general', 'cheetsheet') in ['True', 'true']:
    cheetsheet = open('cheatsheet.txt', 'w+')
    for i in range(10):
        cheetsheet.write(str(HIDDEN_BOARD))
    cheetsheet.close()

while turns > 0:
    print('Welcome to Battleship')
    print(' ')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD [row][column] == '-':
        print('You\'ve already guessed that')
    elif HIDDEN_BOARD [row][column] == 'X':
        print('Congratuations. You have hit a battleship.')
        GUESS_BOARD [row][column] = 'X'
        turns -= 1
    else:
        print('Sorry, you\'ve missed.')
        GUESS_BOARD [row][column] = '-'
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print('Congratulations. You have sunk all the battleships!')
        break
    if fullscreen == False:
        timer = 5
        while True:
            sleep(1)
            print(
                """
      ###########################
      ###########################
      ###########################
      ###########################
      You have {} turns remaining
      ###########################
      ###########################
      ###########################
      ###########################
                """.format(turns)
            )
            timer -= 1
            if timer <= 0:
                break
    else:
        print('You have {} left'.format(turns))
    if turns == 0:
        print('Sorry, you have run out of turns, The game is over.')
        break